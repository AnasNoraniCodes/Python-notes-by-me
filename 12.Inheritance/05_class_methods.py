#Class decorater

class decorater_check:
    a = 3

    def checking( cls ):
        print('Class decorater...',cls.a)


results = decorater_check()
results.a = 13 #instance attributes added
results.checking()

#using classmethods 

#Class decorater

class decorater_check:
    a = 3
    @classmethod
    def checking( cls ):
        print('Class decorater...',cls.a)


results = decorater_check()
results.a = 13 #instance attributes added
results.checking()
