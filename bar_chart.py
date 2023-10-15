list = []
for i in range(9):
    inp = input(f"enter value {i+1}: ")
    if 0 < int(inp) < 9: 
        list.append(int(inp))
    else: 
        print("invalid input")
        inp = input(f"enter value {i+1}: ")
print(list)

maxValue = 9
for j in range(9):
    # range(start, end, increment)
    reverse = maxValue - j
    output = f"{reverse} | "
    for idx in range(9):
        number = list[idx]
        if number == reverse:
            output += " * "
            list[idx] = number - 1 
        else:
            output += "   "
    print(output)

print("   ---------------------------")
print("    1  2  3  4  5  6  7  8  9")