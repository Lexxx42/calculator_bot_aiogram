a = "-2.0 - -"
b = a.split()

try:
    number1 = float(b[0])
    number2 = float(b[2])
except ValueError:
    print("Input data is incorrect")
print("hehe")


