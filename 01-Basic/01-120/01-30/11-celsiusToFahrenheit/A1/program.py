# Celsius to Fahrenheit
# f = (c * 1.8) + 32
def CelsiusToFahrenheit(Celsius):
    Result = Celsius * 1.8
    return Result + 32

print(CelsiusToFahrenheit(0))

# c =  (f - 32) / 1.8
def FahToCel(Fa):
    Result = Fa - 32
    return Result / 1.8

print(FahToCel(0))