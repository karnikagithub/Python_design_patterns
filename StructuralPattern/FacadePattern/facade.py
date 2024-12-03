class CPU:
    def freeze(self): pass
    def jump(self,position): pass
    def execute(self): pass

class Memory:
    def load(self,position,data): pass

class HardDrive:
    def read(self,lba,size): pass


## FACADE CLASS TO IMPLEMENT ABOVE ALL SUB-SYSTEMS INTO A SIMPLIFIED WAY

class Facade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hd = HardDrive()


    def start_computer(self):
        self.cpu.freeze()
        self.memory.load(0, self.hd.read(0,1024))
        self.cpu.jump(10)
        self.cpu.execute()



c1 = Facade()
c1.start_computer()