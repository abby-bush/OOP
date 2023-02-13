import insectclass as i


def main():
    mosquito = i.Insect("mosquito", 2, 4)
    housefly = i.Insect("housefly", 2, 4)
    my_insect = i.Insect("my insect", 2, 4)

    mosquito.flight_len()
    housefly.flight_len()
    my_insect.flight_len()

    print(f"The {mosquito.get_name()} can fly up to {mosquito.get_miles()} miles")
    print(f"The {housefly.get_name()} can fly up to {housefly.get_miles()} miles")
    print(f"{my_insect.get_name()} can fly up to {my_insect.get_miles()} miles")


main()
