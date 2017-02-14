with open("fichero.log", "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    _line = line.replace("\n", "")


    if i % 2 == 0:
        print(i)        # imprimo pares
