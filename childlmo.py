from OopsDemo import Calculator

class childlmp(Calculator):
    num2=200

    def __init__(self):
        super().__init__(10,20)
    def getComplateData(self):
        return self.num2 + self.num+ self.Sum()
    


obj = childlmp()
print(obj.getComplateData())