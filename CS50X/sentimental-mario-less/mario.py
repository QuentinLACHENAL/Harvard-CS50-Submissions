from cs50 import get_int

height = 0
while height < 1 or height > 8:
    height = get_int("Height: ")

counter = 0
while counter < height:
    spaces = height - counter - 1
    s_counter = 0
    while s_counter < spaces:
        print(" ", end="")
        s_counter += 1
    hashs = counter + 1
    h_counter = 0
    while h_counter < hashs:
        print("#", end="")
        h_counter += 1
    print()
    counter += 1
