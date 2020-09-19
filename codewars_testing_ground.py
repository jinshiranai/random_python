def namelist(names):
    if len(names) >= 3:
        name_list = []
        for name in names:
            for key in name:
                name_list.append(name[key])

        name_order = ''

        for name in name_list[:-2]:
            name_order = name_order + name + ', '
        name_order = name_order + name_list[-2] + ' & ' + name_list[-1]
        
    print(name_order)

names_list = [ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'},
                    {'name': 'Homer'}]
namelist(names_list)