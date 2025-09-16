apple = "apple"
answer = [x for x in apple if x not in "aeiou"]

print(answer)

squares = [i**2 for i in range(1, int(20**0.5) + 1)]

print(squares)


def quality(x):
    if x > 3 and x % 2 == 0:
        return True
    else:
        return 7


ans = [x for x in range(2, 26) if quality(x) == True]

print(ans)


# Use your function to remove vowels from an input string

# use your function to remove vowels from a list of strings:


array4 = [[[row, col] for row in range(4)] for col in range(4)]

print(array4)


s = "Apple"
print("Answer")
ans = s[::1]

print(ans)


def main():
    print("Hello from lists!")


if __name__ == "__main__":
    main()
