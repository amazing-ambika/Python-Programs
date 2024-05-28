# program to convert temperatures to and from Centigrade to Fahrenheit
F = float(input("Enter Temperature in Fahrenheit: "))
C = (F - 32) * 5.0/9.0
print("Temperature :", F, "Fahrenheit = ", C, " C")
C = float(input("Enter a temperature in Celsius: "))
F = 9.0/5.0 * C + 32
print("Temperature :", C, "Celsius = ", F, " F")
