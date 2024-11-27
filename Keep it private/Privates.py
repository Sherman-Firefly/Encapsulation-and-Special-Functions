class myclass:

    __myclass= 'hi'
    def __privatemethod(self):
        print("This is a private class.")
    def intro(self):
        print("Private variables being used: ", myclass.__myclass)

p=myclass()
p.intro()
p.__privatemethod()