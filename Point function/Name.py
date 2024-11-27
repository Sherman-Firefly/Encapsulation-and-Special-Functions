class person:
    def __init__(self, name, age):
        self.__name=name
        self.age=age
        
    def aged(self):
        return self.__name
    def newname(self, newname):
        self.__name=newname

n=person("Bob", 22)
print(n.aged())
n.newname("Will")
print(n.newname("Dave"))