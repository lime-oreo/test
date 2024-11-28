import random

class Dice:
    def __init__(self):
        self.numbers = []

    def playDice(self):
        self.numbers.append(random.randint(1, 6));

    def getNumbers(self):
        return self.numbers

    def getSum(self):
        return sum(self.numbers)

def sortNumbers(*numbers):
    list = sorted(numbers)
    list.sort(reverse = True)
    return list
    

gamer1Dice = Dice()
gamer2Dice = Dice()
gamer3Dice = Dice()

for i in range(5):
    gamer1Dice.playDice()
    gamer2Dice.playDice()
    gamer3Dice.playDice()

print('Gamer1 :', gamer1Dice.getNumbers())
print('Sum of Gamer1 :', gamer1Dice.getSum())
print('-'*25)

print('Gamer2 :', gamer2Dice.getNumbers())
print('Sum of Gamer2 :', gamer2Dice.getSum())
print('-'*25)

print('Gamer3 :', gamer3Dice.getNumbers())
print('Sum of Gamer3 :', gamer3Dice.getSum())
print('-'*25)

sortedNumbers = sortNumbers(gamer1Dice.getSum(), gamer2Dice.getSum(), gamer3Dice.getSum())
print('='*25)
print('1등 :', sortedNumbers[0], '점 \tWIN!!')
print('2등 :', sortedNumbers[1], '점')
print('3등 :', sortedNumbers[2], '점')
print('='*25)
