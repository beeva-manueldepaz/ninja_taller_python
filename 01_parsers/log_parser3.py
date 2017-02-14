with open("fichero.log", "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    _line = line.replace("\n", "")

    if i % 2 == 0:
        # parsed = _line.split(" ")
        _, b, c = _line.split(" ", maxsplit=2)
        # _, b, *_ = _line.split(" ") # Python v2
        print(c)