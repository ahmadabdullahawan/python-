def even(x):
    if x % 2 == 0:
        return "it's an even number"
    else:
        return "it's an odd number"

number = int(input("How many numbers do you want to check? "))
i = 1
while i <= number:
    z = int(input("Enter the number you want to check: "))
    result = even(z)
    print("Your result for this number is:", result)
    i += 1
