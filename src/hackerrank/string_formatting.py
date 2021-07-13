number = 17
width = len(bin(number)[2:])
for x in range(1, 18):
    binary_representation = bin(x)[2:]
    octal_representation = oct(x)[2:]
    hex_representation = hex(x)[2:]
    print(f"{x:>{width}d} {octal_representation:>{width}s} {hex_representation:>{width}s} {binary_representation:>{width}s}")
