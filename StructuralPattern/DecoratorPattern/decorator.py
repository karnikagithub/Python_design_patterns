class Class:
    def __init__(self):
        pass

    def something_print(self,string):
        return string
    

class Decorator:
    def __init__(self,wrapped):
        self._wrapped=wrapped

    def withUnderscores(self,string):
        return "_".join(string.split(" "))

    def __getattr__(self,name):
        return getattr(self._wrapped,name)
    


#### this is the instance of a class

ins = Class()
print(ins.something_print("THIS IS THE DECORATOR PATTERN CONCEPT"))
# output: THIS IS THE DECORATOR PATTERN CONCEPT


#### this is the instance of decorator class
# here im passing "INS" as an argument to the DECAORATOR class
obj = Decorator(ins)
print(obj.withUnderscores("THIS IS THE DECORATOR PATTERN CONCEPT"))
# output: "THIS_IS_THE_DECORATOR_PATTERN_CONCEPT"

print(obj.something_print("THIS IS THE DECORATOR PATTERN CONCEPT"))
# output: THIS IS THE DECORATOR PATTERN CONCEPT
