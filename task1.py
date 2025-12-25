def fac(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * fac(number - 1)

num = int(input("Enter a number: "))
print(f"The Factorial of {num} is : {fac(num)}")