CPU = "one2"

match CPU:
    case "one":
        print("Cpu is One")
    case "i3":
        print("Cpu is i3")
    case _:
        print("WTF")

# match with dict
data = {"one": "One", "two": "Two"}

print(data.get(CPU, "WTF"))