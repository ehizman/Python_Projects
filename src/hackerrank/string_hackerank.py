string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
counter = 4
start = 0
stop = 25
result = ""
while start < stop:
    result = result + string[start:start + counter] + "\n"
    start += counter

print(result)
