def run():
    my_set1 = {"pera","manzana", "uva", "fresa", "melon","guayaba"}
    my_set2 = {"sandia","mango","manzana","platano","uva","frambuesa"}

    union = my_set1 | my_set2
    intersection = my_set1 & my_set2
    diference = my_set2 - my_set1
    simetric_diference = my_set1 ^ my_set2

    print(union)
    print(intersection)
    print(diference)
    print(simetric_diference)

if __name__ == '__main__':
    run()