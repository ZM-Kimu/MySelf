import random
from math import cos, pi, radians, sin

import bpy
from bpy import *

from .properties import AtomModelProperties
from .utils import parse_yaml


class AtomOperators:
    def __init__(self, context, atom_props) -> None:
        self.context: types.Context = context
        self.atom_props: AtomModelProperties = atom_props

    # 创建原子核
    def create_nucleus(self, proton_count: int, neutron_count: int):
        particles = []
        particle_radius = self.atom_props.proton_neutron_radius
        nucleus = {"proton": proton_count, "neutron": neutron_count}
        for particle_type in nucleus:
            for _ in range(nucleus[particle_type]):
                if particles:
                    # 在已有的粒子中选取随机粒子做出偏移
                    ref_particle = random.choice(particles)
                    ref_location = ref_particle.location
                    location = [
                        random.uniform(-1, 1) * particle_radius * 1.5
                        + ref_location[vec]
                        for vec in range(3)
                    ]
                else:
                    # 随机创建第一个粒子
                    location = [
                        random.uniform(-particle_radius, particle_radius)
                        for _ in range(3)
                    ]

                # location = [coord * 2 for coord in location]
                particles.append(self.create_proton_neutron(particle_type, location))
        # 合并中子与质子
        self.join_particles(particles)

        return particles

    # 创建中子或质子
    def create_proton_neutron(self, particle_type: str, location: types.Sequence):
        ops.mesh.primitive_uv_sphere_add(
            radius=self.atom_props.proton_neutron_radius, location=location
        )
        obj = self.context.object
        obj.name = particle_type.capitalize()
        # 取得材质
        material_name = f"{particle_type}_material"
        self.add_material(material_name, obj)

        return obj

    def join_particles(self, particles: list[types.Object]):
        ops.object.select_all(action="DESELECT")
        for particle in particles:
            particle.select_set(True)
        self.context.view_layer.objects.active = particles[0]

        ops.object.join()
        ops.object.origin_set(type="ORIGIN_GEOMETRY", center="BOUNDS")
        self.context.object.location = (0, 0, 0)

    def create_orbit(self, radius: float):
        ops.curve.primitive_bezier_circle_add(radius=radius)
        orbit = self.context.object
        orbit.data.fill_mode = "FULL"
        orbit.data.bevel_depth = 0.2
        orbit.name = "Orbit"
        self.add_material("orbit_material", orbit)
        return orbit

    def create_electron(self, location: types.Sequence):
        ops.mesh.primitive_uv_sphere_add(
            radius=self.atom_props.electron_radius, location=location
        )
        electron = self.context.object
        electron.name = "Electron"
        self.add_material("electron_material", electron)
        return electron

    def create_orbits_and_electrons(
        self,
        orbit_index: int,
        orbit_radius_multiplier: float,
        electron_group_count: int,
        electrons_per_group: int,
    ):
        orbit_radius = 2 * (orbit_index + 1) * orbit_radius_multiplier
        self.create_orbit(orbit_radius)

        group_spacing = (2 * pi) / electron_group_count
        electron_on_orbit = []
        for group_num in range(electron_group_count):
            group_angle = group_num * group_spacing
            for electron in range(electrons_per_group):
                electron_spacing = (
                    self.atom_props.proton_neutron_radius / 2 * orbit_radius_multiplier
                )
                angle = group_angle + electron * electron_spacing
                x = orbit_radius * cos(angle)
                y = orbit_radius * sin(angle)
                electron_on_orbit.append(self.create_electron((x, y, 0)))

        self.animate_electrons(electron_on_orbit)

    def animate_electrons(self, electrons: list[types.Object]):
        initial_rotation = random.uniform(0, 2 * pi)
        final_rotation = initial_rotation + random.randint(3, 8) * 2 * pi
        for electron in electrons:
            ops.object.select_all(action="DESELECT")
            electron.select_set(True)
            self.context.view_layer.objects.active = electron
            self.context.scene.cursor.location = (0, 0, 0)
            ops.object.origin_set(type="ORIGIN_CURSOR", center="BOUNDS")
            # self.context.view_layer.objects.active = electron

            electron.rotation_euler = (0, 0, initial_rotation)
            electron.keyframe_insert(data_path="rotation_euler", frame=0)
            electron.rotation_euler = (0, 0, final_rotation)
            electron.keyframe_insert(data_path="rotation_euler", frame=200)

            fcurves = electron.animation_data.action.fcurves
            for fcurve in fcurves:
                if fcurve.data_path == "rotation_euler" and fcurve.array_index == 2:
                    for keyframe in fcurve.keyframe_points:
                        keyframe.interpolation = "LINEAR"
                    fcurve.modifiers.new(type="CYCLES")

    def add_material(self, material_name: str, object: types.Object):
        # 取得材质
        material = bpy.data.materials.get(material_name)
        # 为粒子添加材质
        if material:
            object.data.materials.append(material)
        else:
            print(f"Material {material_name} not found.")

    def add_atom_name(self, atom_name: str, nucleus_size: float):
        ops.object.text_add()
        text_obj = self.context.object
        text_obj.data.body = atom_name
        text_obj.name = "AtomName"
        ops.object.origin_set(type="ORIGIN_GEOMETRY", center="BOUNDS")
        text_obj.location = (0, -(nucleus_size + 0.5), 0)
        text_obj.rotation_euler = (radians(60), 0, 0)
        self.add_material("text_material", text_obj)

    def apply_smooth_shading_to_all(self):
        for obj in self.context.scene.objects:
            if obj.type == "MESH":
                self.context.view_layer.objects.active = obj
                obj.select_set(True)
                ops.object.mode_set(mode="EDIT")
                ops.mesh.select_all(action="SELECT")
                ops.mesh.faces_shade_smooth()
                ops.object.mode_set(mode="OBJECT")
                obj.select_set(False)

    def clear_scene(self):
        ops.object.select_all(action="DESELECT")
        # 遍历场景中的所有对象
        for obj in self.context.scene.objects:
            animation = obj.animation_data
            if animation is not None:
                while animation.nla_tracks:  # 清除NLA Tracks
                    animation.nla_tracks.remove(animation.nla_tracks[0])
                obj.animation_data_clear()  # 清除动画数据
            obj.select_set(True)
        ops.object.delete()
        # 清除动作
        for action in bpy.data.actions:
            bpy.data.actions.remove(action)
        # 清除所有子集合
        for collection in self.context.scene.collection.children:
            bpy.data.collections.remove(collection)
        # 清除孤立数据块
        for block in bpy.data.materials:
            if block.users == 0:
                bpy.data.materials.remove(block)
        for block in bpy.data.textures:
            if block.users == 0:
                bpy.data.textures.remove(block)
        for block in bpy.data.images:
            if block.users == 0:
                bpy.data.images.remove(block)
        ops.outliner.orphans_purge(
            do_local_ids=True,
            do_linked_ids=True,
            do_recursive=False,  # 不要递归，以免清除材质
        )


class GenerateAtomModelOperator(types.Operator):
    bl_idname = "wm.generate_atom_model"
    bl_label = "Generate Atom Model"

    def execute(self, context: types.Context):
        scene = context.scene
        atom_props: AtomModelProperties = scene.atom_model_properties

        ops = AtomOperators(context, atom_props)
        ops.clear_scene()
        ops.create_nucleus(atom_props.proton_count, atom_props.neutron_count)
        for orbit in atom_props.orbits:
            ops.create_orbits_and_electrons(
                orbit.orbit_index,
                atom_props.orbit_radius_multiplier,
                orbit.electron_group_count,
                orbit.electrons_per_group,
            )
        # ops.animate_electrons(
        #    atom_props.orbit_count, atom_props.orbit_radius_multiplier
        # )
        ops.add_atom_name(atom_props.atom_name, 2)
        ops.apply_smooth_shading_to_all()
        return {"FINISHED"}


class GenerateAndExportAtomModelOperator(types.Operator):
    bl_idname = "wm.generate_and_export_atom_model"
    bl_label = "Generate and Export Atom Model"

    def execute(self, context: types.Context):
        scene = context.scene
        atom_props: AtomModelProperties = scene.atom_model_properties

        # 读取 YAML 文件内容
        yaml_path = "path_to_your_yaml_file.yaml"
        with open(yaml_path, "r", encoding="utf8") as file:
            yaml_content = file.read()

        atoms = parse_yaml(yaml_content)

        for atom_name, atom_data in atoms.items():
            ops = AtomOperators(context, atom_props)
            ops.clear_scene()
            ops.create_nucleus(atom_data["Proton"], atom_data["Neutron"])
            for electron_config in atom_data["Electron"]:
                ops.create_orbits_and_electrons(
                    electron_config["orbit"] - 1,
                    atom_props.orbit_radius_multiplier,
                    electron_config["group_count"],
                    electron_config["electrons_per_group"],
                )
            ops.add_atom_name(atom_name, 2)
            ops.apply_smooth_shading_to_all()

            # 导出为 FBX
            fbx_path = f"{atom_name}.fbx"
            bpy.ops.export_scene.fbx(filepath=fbx_path, use_selection=True)

        return {"FINISHED"}


class AddOrbitOperator(types.Operator):
    bl_idname = "atom.add_orbit"
    bl_label = "Add Orbit"

    def execute(self, context: types.Context):
        atom_props = context.scene.atom_model_properties
        orbit = atom_props.orbits.add()
        orbit.orbit_index = len(atom_props.orbits)
        return {"FINISHED"}


class RemoveOrbitOperator(types.Operator):
    bl_idname = "atom.remove_orbit"
    bl_label = "Remove Orbit"

    def execute(self, context: types.Context):
        atom_props = context.scene.atom_model_properties
        if len(atom_props.orbits) > 0:
            atom_props.orbits.remove(atom_props.active_orbit_index)
        return {"FINISHED"}
