print("(a){:10s}(b){:10s}(c){:19s}(d)".format(" ", " ", " "))
for i in range(20):
    for _ in range(i//2 + 1):
        print("*", end="")
    for _ in range(10 - (i//2 + 1)):
        print(" ", end="")

    print("  ", end="")

    for _ in range(10 - (i // 2)):
        if i % 2 == 0:
            print("*", end="")
        else:
            print(" ", end="")
    for _ in range(i // 2 + 1):
        print(" ", end="")

    print("  ", end="")

    for _ in range((i // 2) + 1):
        print(" ", end="")

    for _ in range(10 - (i//2)):
        if i % 2 == 0:
            print("*", end="")
        else:
            print(" ", end="")

    print("  ", end="")

    for _ in range(10 - (i // 2)):
        print(" ", end="")
    for _ in range((i // 2 + 1)):
        print("*", end="")
    print()
