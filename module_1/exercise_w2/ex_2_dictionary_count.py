""" function tra ve mot dictionary dem so luong
chu xuat hien trong mot tu,
voi key la chu cai va value la so lan xuat hien """


def character_count(user_list):
    no_space = [char for char in user_list if char != " "]
    no_space.sort()
    times = {}
    for i in no_space:
        if i not in times:
            times[i] = 1
        else:
            times[i] += 1
    return times


print(character_count("smiles"))
