class String:
    def __init__(self, originalstring):
        self.originalstring=originalstring

    def display(self):
        print(f"Original string: {self.originalstring}")

class Rstring(String):
    def reverse(self):
        reversedstring=self.originalstring[::-1]
        return reversedstring

inputstring="racecar"
string=Rstring(inputstring)

string.display()
reversedstr=string.reverse()
print(f"Reverse string: {reversedstr}")

