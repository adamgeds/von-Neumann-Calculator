emptySet = []
set = [emptySet]

for i in range(1000):
    emptySet = emptySet + [emptySet]
    set.append(emptySet)

def addition(x, y):
    if x in y:
        return addition(y, x) # n1 > n2
    if y == []:
        return x
    x = x + [x]
    y = y[-1]
    return addition(x, y)

def subtraction(x, y):
    if x in y:
        return subtraction(y,x)
    elif y == []:
        return x
    else:
        for i in range(len(y)):
            x.pop()
        return x

def multiplication(x, y):
    if x in y:
        return multiplication(y, x)
    if y == []:
        return []
    hold = []
    if len(y) == 0: return []
    elif len(y) == 1: return x
    else:
        for i in range(len(y)):
            hold = addition(hold, x)
        return hold

def main():
    sol = []

    print("Here are the operations you can choose from:\n")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")

    operation = input("Which operation would you like?\n")

    a = int(input("Enter a number: "))
    b = int(input("Enter a second number: "))

    if "1" in operation:
        sol = addition(set[a], set[b])
        print(sol)
        print(len(sol))
    elif "2" in operation:
        sol = subtraction(set[a], set[b])
        print(sol)
        print(len(sol))
    elif "3" in operation:
        sol = multiplication(set[a], set[b])
        print(sol)
        print(len(sol))
    else:
        print("Invalid entry. Try again.\n")
        continue

    print("Thank you for using the von Neumann Calculator!")

main()
