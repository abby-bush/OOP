import CoinClass as c

# this import is the name of the file, not the name of the class
# it doesn't recognize the .py, etc., so don't add it


# The main function.
def main():
    # Create an object from the Coin class.
    # this is important--how we create an instance
    my_coin = (
        c.Coin()
    )  # this creates an instance called 'my_coin' of the class 'Coin()'

    # Display the side of the coin that is facing up.
    print(
        "This side is up:", my_coin.get_sideup()
    )  # notice you do not have to supply the argument/parameter

    # Toss the coin.
    print("I am going to toss the coin ten times:")
    for count in range(10):
        my_coin.toss()
        # hacking - my_coin.sideup = "Heads"

        # even my_coin.__sideup() = "Heads" doesn't work
        # the only way to alter the attribute is to go through a method
        # going forward, always hide your attributes!

        # Display the side of the coin that is facing up.
        print("This side is up:", my_coin.get_sideup())


# Call the main function.

main()
