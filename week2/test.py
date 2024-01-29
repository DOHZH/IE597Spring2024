f = open("./week2/data/F-n135-k7.vrp", "r")

dimension = 0
capacity = 0
depot_index = []
coordinate_section = False
demand_section = False
depot_section = False
route_type = ""

coodinates = []
demand_list = []

for l in f.readlines():
    if "CAPACITY :" in l:
        capacity = int(l.split("CAPACITY :")[-1])
        continue
    elif "DIMENSION :" in l:
        dimension = int(l.split("DIMENSION :")[-1])
        continue

    elif l == "NODE_COORD_SECTION\n":
        coordinate_section = True
        demand_section = False
        depot_section = False
        continue

    elif l == "DEMAND_SECTION\n":
        coordinate_section = False
        demand_section = True
        depot_section = False
        continue

    elif l == "DEPOT_SECTION\n":
        coordinate_section = False
        demand_section = False
        depot_section = True
        continue

    elif l == "EOF\n":
        break

    
    if coordinate_section:
        coordinate = l.split()[1:]
        coordinate = [float(_) for _ in coordinate]
        coodinates.append(coordinate)
        continue
    
    if demand_section:
        demand = [int(l.split()[-1])]
        demand_list.append(demand)
        continue

    if depot_section:
        number = int(l.split()[-1])
        if number != -1:
            depot_index.append(number)