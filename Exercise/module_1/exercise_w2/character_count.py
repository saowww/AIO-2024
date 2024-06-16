""" function tra ve mot dictionary dem so luong
chu xuat hien trong mot tu,
voi key la chu cai va value la so lan xuat hien """


def character_count(word):
    character_statistic = {}
    for c in word:
        character_statistic[c] = character_statistic.get(c, 0)+1
    return character_statistic


if __name__ == "__main__":
    print(character_count("smiles"))
