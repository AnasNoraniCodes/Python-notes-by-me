#Adding fav places and friends names in dict
#dict created
initial_dict = {}
#{} is syntax of dict
friend_name = input('Enter name :')
fav_place   = input('Enter place name :')

#syntax of updating dict is dict.update({name:value})
initial_dict.update({friend_name:fav_place})

friend_name = input('Enter name :')
fav_place   = input('Enter place name :')
initial_dict.update({friend_name:fav_place})

friend_name = input('Enter name :')
fav_place   = input('Enter place name :')
initial_dict.update({friend_name:fav_place})

friend_name = input('Enter name :')
fav_place   = input('Enter place name :')
initial_dict.update({friend_name:fav_place})

#printing dict
print(initial_dict)

#key points...values same ho sakti hain but update method se keys same
# nahi rehti balky wo update ho jati hain 