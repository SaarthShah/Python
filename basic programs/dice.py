import random
class dice:
    def roll(self):
         n1= random.randint(1,6)
         n2= random.randint(1,6)
         return n1,n2
    
dice1= dice()
print(dice1.roll())