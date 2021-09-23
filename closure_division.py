def make_divisionby(n: int):
    def division(integer) -> float:
        assert type(integer) == int, "Solo puedes ingresar números enteros"
        return integer / n
    return division

def run():
    division_by3 = make_divisionby(3)
    print(division_by3(18))
    division_by5 = make_divisionby(5)
    print(division_by5(100))
    division_by18 = make_divisionby(18)
    print(division_by18(54))
    

if __name__ == '__main__':
    run()