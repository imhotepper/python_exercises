def convert_to_farenheight(degrees_celsius):
    return degrees_celsius * (9/5) + 32

def convert_to_celsius(degrees_farenheight):
    return (degrees_farenheight - 32) * 5/9 

print("0 Celsius to Farenheight is:", convert_to_celsius(0))
assert convert_to_celsius(0) ==-17.77777777777778
print("180 Celsius to Farenheight is:", convert_to_celsius(180))
assert convert_to_celsius(180) == 82.22222222222223

print("0 Farenheight to Celsius is:",convert_to_farenheight(0))
assert convert_to_farenheight(0) == 32
print("180 Farenheight to Celsius is:",convert_to_farenheight(180))
assert convert_to_farenheight(100) == 212
