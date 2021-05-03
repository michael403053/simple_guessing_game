

correct_answer = 20
a = int(input("First Number:"))
print()
b = int(input("Second Number:"))
print()


def multiply(a, b):
    return a * b

# print(multiply(a, b))

if multiply(a,b) == correct_answer:
    print("Winner Winner Chicken Dinner")
else:
    print("Wrong! Try 2 numbers between 1 and 5")
