#F to C temperature
#Formula c = 5*(f-32)/9

def C_to_F(f):
    # formule is used
    c=5*(f-32)/9
    return c

user_input_in_F = int(input('Enter tempetature in F :'))
results = C_to_F(user_input_in_F)
# round(value,rounded_digit) is used to round off
print(f'The temperature in {user_input_in_F} F to C is {round(results,2)} C.')