x = "\t \t \n i hear that \n cats \r are really interesting \t creatures ! \n"

print(x)
print("--------------------")
new_x = x.strip()
print(new_x)

print(x.split())


file = open("input.txt", "r")

lines = file.readlines()

print(lines)

for line in file:
    print(line)
    line = line.strip()
    y = line.split("%%")

    print(y)

    if not line:
        continue

    name = y[0]
    age = y[1]
    school = y[2]

    print(f"name is {name}  age is {age}, and school is , {school}")


x = ""
print(x and True)

x = 10
x
