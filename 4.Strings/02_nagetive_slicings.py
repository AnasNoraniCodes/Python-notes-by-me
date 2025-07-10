#Nagetive slicings

name = 'Anas'
print(name[-4:-1]) #Always ,first index is included and second is not included
#output : Ana

print(name[1:-1]) #Easy solution is to convert it into positive index first...
print(name[1:3])  #output will be same...

#Always remember that start_index (included) : end_index(not included)

# Skip values

a = '123456789'
print(a[0:-1])     # start index and end index added using both -,+
print(a[0:-1:4])   # added skip feature and its value is 2

print(a[:5]) # means that start index is 0
print(a[0:])  # means that end index is -1 or total length

print(a[:]) # means that start index is 0 and end index is total length