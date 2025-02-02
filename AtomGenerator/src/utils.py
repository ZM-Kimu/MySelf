def parse_yaml(yaml_content):
    atoms = {}
    lines = yaml_content.splitlines()
    current_atom = None

    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            key, value = key.strip(), value.strip()
            if not value:  # New atom definition
                current_atom = key
                atoms[current_atom] = {"Proton": 0, "Neutron": 0, "Electron": []}
            else:
                if key == "Proton":
                    atoms[current_atom]["Proton"] = int(value)
                elif key == "Neutron":
                    atoms[current_atom]["Neutron"] = int(value)
        elif "*" in line and current_atom:
            orbit, group_info = line.split("*")
            group_count, electrons_per_group = map(int, group_info.split("g"))
            atoms[current_atom]["Electron"].append(
                {
                    "orbit": int(orbit),
                    "group_count": group_count,
                    "electrons_per_group": electrons_per_group,
                }
            )

    return atoms
