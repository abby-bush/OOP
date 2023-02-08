import insectclass as i


def main():
    my_insect = i.Insect()

    my_insect.create_flight_len()

    print(f"My insect can fly {my_insect.get_flight_len()} miles")


main()
