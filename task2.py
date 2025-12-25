import math
def cal(number):
    square_root = math.sqrt(number)
    natural_log = math.log(number)
    sine_value = math.sin(number)
    return square_root, natural_log, sine_value
num = int(input("Enter a number: "))
result = cal(num)
print(f"Square root : {result[0]}")
print(f"Natural log : {result[1]}")
print(f"Sine value : {result[2]}")