#keyword detection in post

user_post = input('Enter your post :')
if 'scam' in user_post.lower():
    print('post hided')
else:
    print('Good post')    

'''
    We learn that we can detect the keyword ]
    by using .lower() in post...
'''    