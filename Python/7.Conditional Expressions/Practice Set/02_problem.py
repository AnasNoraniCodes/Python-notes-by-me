#Marks calculations

#user input of marks
mark_in_english = int(input('Enter your marks of English :'))
mark_in_maths = int(input('Enter your marks of Maths :'))
mark_in_urdu = int(input('Enter your marks of Urdu :'))

total_persentage = (100*(mark_in_english+mark_in_maths+mark_in_urdu))/300


#conditional statements


if( total_persentage >100 or total_persentage <0 ):
    
    print('Enter correct marks from 1 to 100 .')
elif( total_persentage >= 40 and mark_in_english >= 33 and mark_in_maths >= 33 and mark_in_urdu >= 33):
    print('You total persentage is :',total_persentage)
    print('You are passed...Congratulations')

else:
    print('You total persentage is :',total_persentage)
    print('Oh...You failed')    


#use of "in" keyword in if conditions
spam_keyword1 ='order now' 
spam_keyword2 ='click this' 

user_comment = input('Enter comment...')
if ( spam_keyword1 in user_comment or spam_keyword2 in user_comment ):
    print('This comment is spam...')
else:
    print('Good comment...')    

# use "in" keyword in if statement that is helpful...    