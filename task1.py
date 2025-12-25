def fac(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * fac(number - 1)
