class SingleTon:
    def __new__(self):
        if not hasattr(self,'instance'):
            self.instance = super().__new__(self)
        return self.instance
    





instance1 = SingleTon()
instance2 = SingleTon()


print('THIS FILE REPRESENTS SINGLETON PATTERN')
print(id(instance1))
print(id(instance2))