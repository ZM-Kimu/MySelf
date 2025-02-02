from bpy import *

from .properties import AtomModelProperties


class ORBIT_UL_List(types.UIList):
    def draw_item(
        self,
        context,
        layout: types.UILayout,
        data,
        item,
        icon,
        active_data,
        active_propname,
        index,
    ):
        col = layout.column()
        col.label(text=f"轨道 {index + 1}", icon="MESH_CIRCLE")
        box = col.box()
        split = box.split(factor=0.25)
        split.label(text="电子组数")
        split.prop(item, "electron_group_count", slider=True)
        split = box.split(factor=0.25)
        split.label(text="每组电子数")
        split.prop(item, "electrons_per_group", slider=True)


class AtomPannel(types.Panel):
    bl_label = "原子生成器(Atom Model Generator)"
    bl_idname = "OBJECT_PT_atom_generator"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Atom Tool"

    def draw(self, context: types.Context):
        layout = self.layout
        scene = context.scene
        atom_props: AtomModelProperties = getattr(scene, "atom_model_properties")

        box = layout.box()
        box.label(text="原子核(Nucleus)", icon="META_BALL")
        split = box.split(factor=0.25)
        split.label(text="质子数")
        split.prop(atom_props, "proton_count", slider=True)
        split = box.split(factor=0.25)
        split.label(text="中子数")
        split.prop(atom_props, "neutron_count", slider=True)
        split = box.split(factor=0.25)
        split.label(text="粒子半径")
        split.prop(atom_props, "proton_neutron_radius", slider=True)

        # 轨道列表
        box = layout.box()
        box.label(text="轨道与电子(Orbit&Electron)", icon="CURVE_NCIRCLE")

        # 添加/删除按钮
        col = box.row(align=False)
        col.operator("atom.add_orbit", icon="ADD", text="")
        col.operator("atom.remove_orbit", icon="REMOVE", text="")

        row = box.row()
        row.template_list(
            "ORBIT_UL_List", "", atom_props, "orbits", atom_props, "active_orbit_index"
        )

        split = box.split(factor=0.25)
        split.label(text="半径缩放系数")
        split.prop(atom_props, "orbit_radius_multiplier", slider=True)
        split = box.split(factor=0.25)
        split.label(text="电子半径")
        split.prop(atom_props, "electron_radius", slider=True)

        layout.separator(type="LINE")
        box = layout.box()
        split = box.split(factor=0.3)
        split.label(text="文字(Text)")
        split.prop(atom_props, "atom_name", text="")
        box.operator("wm.generate_atom_model", text="生成(Generate)")
        box.operator(
            "wm.generate_and_export_atom_model", text="加载配置并导出(Load & Export)"
        )
