houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]


def without_recursion(houses):
    for house in houses:
        print(house)


def with_recursion(houses: list) -> None:
    if len(houses) == 1:
        house = houses[0]
        print(f"The house is {house}")

    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]
        with_recursion(first_half)
        with_recursion(second_half)


if __name__ == '__main__':
    with_recursion(houses)