from bpy import *


class OrbitProperties(types.PropertyGroup):
    orbit_index: props.IntProperty(name="轨道索引")  # type: ignore
    electron_group_count: props.IntProperty(
        name="Electron Group Count", default=1, min=1, max=1000
    )  # type: ignore
    electrons_per_group: props.IntProperty(name="Electron Per Group", default=1, min=1, max=1000)  # type: ignore


class AtomModelProperties(types.PropertyGroup):

    proton_count: props.IntProperty(
        name="Proton Count", default=1, min=1, max=500
    )  # type: ignore
    neutron_count: props.IntProperty(name="Neutron Count", default=1, min=0, max=500)  # type: ignore
    proton_neutron_radius: props.FloatProperty(
        name="Proton Neutron Radius", default=0.5, min=0, max=20
    )  # type: ignore

    orbits: props.CollectionProperty(type=OrbitProperties)  # type: ignore
    active_orbit_index: props.IntProperty(name="Active Orbit Index", default=0)  # type: ignore

    orbit_radius_multiplier: props.FloatProperty(
        name="Orbit Radius Multiplier", default=1, min=0, max=20
    )  # type: ignore
    electron_radius: props.FloatProperty(
        name="Electron Radius", default=0.5, min=0, max=20
    )  # type: ignore

    atom_name: props.StringProperty(name="Atom Name", default="atom")  # type: ignore
