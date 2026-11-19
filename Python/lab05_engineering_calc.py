import math

print("ENGINEERING CALCULATION TOOL")
val = float(input("Enter a numerical value: "))
exp = float(input("Enter an exponent: "))
dec = float(input("Enter a decimal measurement: "))

print("\nResults")
print(f"Value : {val}")
print(f"Exponent : {exp}")
print(f"Power (pow) : {math.pow(val, exp)}")
print(f"Square Root (sqrt) : {math.sqrt(val):.4f}")
print(f"Decimal Value : {dec}")
print(f"Ceil Value : {math.ceil(dec)}")
print(f"Floor Value : {math.floor(dec)}")
