with open("fichero.log", "r") as f:
    lines = f.readlines()

# rest = [] -> usa append
rest = set() # usa add

for i, line in enumerate(lines):
    _line = line.replace("\n", "")

    if i % 2 == 0:
        # parsed = _line.split(" ")
        _, b, c = _line.split(" ", maxsplit=2)
        # _, b, *_ = _line.split(" ") # Python v2
        # print(c)

        rest.add(b)

with open("salida.txt", "w") as f:
    f.writelines(rest)

# print(rest)