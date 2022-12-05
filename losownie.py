import random

class Lottery:
    def __init__(self):
        self.dict = {0: "Marczak", 1: "Adrian", 2:"Karo", 3:"Korek", 4: "P", 5: "Markos", 6:"Jagoda"}
        self.table = []
        self.pula = [0, 1, 2, 3, 4, 5, 6]
    def has_value(self, value):
        for i in self.table:
            if value == i:
                return True
    def append_table(self, value):
        self.table.append(value) 
    def return_table(self):
        return self.table
    def last_element(self):
        last_element = 0
        for i in range(len(self.table)):
            last_element= self.table[i]
        return last_element
    def drew_itself(self, value,i):
        if self.pula[i] == value:
            return True
    def drew_its_lover(self, value, i):
        if value%2==0:
            if value == i-1:
                return True
        if value%2==1:
            if value == i+1:
                return True

lottery = Lottery()

for i in range(0,7):
    value = random.randint(0,6)
    while lottery.has_value(value) == True or lottery.drew_itself(value,i)== True or lottery.drew_its_lover(value, i):
        value = random.randint(0,6)
    lottery.append_table(value)
    table = lottery.return_table()
    print(lottery.dict[i]," kupuje prezent dla ", lottery.dict[lottery.last_element()])