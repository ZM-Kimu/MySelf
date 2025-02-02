from bpy import *

from .operators import AddOrbitOperator, GenerateAtomModelOperator, RemoveOrbitOperator
from .properties import AtomModelProperties, OrbitProperties
from .ui import AtomPannel, ORBIT_UL_List

bl_info = {
    "name": "Atom_generator",
    "author": "kimu",
    "description": "Easy way to generate atom.",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "location": "",
    "warning": "",
    "category": "Generic",
}


def register():
    utils.register_class(OrbitProperties)
    utils.register_class(ORBIT_UL_List)
    utils.register_class(AddOrbitOperator)
    utils.register_class(RemoveOrbitOperator)
    utils.register_class(AtomModelProperties)
    utils.register_class(GenerateAtomModelOperator)
    utils.register_class(AtomPannel)
    types.Scene.atom_model_properties = props.PointerProperty(type=AtomModelProperties)


def unregister():
    utils.unregister_class(AtomModelProperties)
    utils.unregister_class(GenerateAtomModelOperator)
    utils.unregister_class(AtomPannel)
    utils.unregister_class(OrbitProperties)
    utils.unregister_class(ORBIT_UL_List)
    utils.unregister_class(AddOrbitOperator)
    utils.unregister_class(RemoveOrbitOperator)

    del types.Scene.atom_model_properties


if __name__ == "__main__":
    register()
