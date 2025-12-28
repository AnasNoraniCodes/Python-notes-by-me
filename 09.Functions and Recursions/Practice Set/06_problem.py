#Inch to cm

def inch_to_cm(inch):
    #formula
    results = inch * 2.54
    return results

user_input = int(input('Enter value is inches :'))
results = inch_to_cm(user_input)
print(f"The value of {user_input} inches in cm is {results}cm.")