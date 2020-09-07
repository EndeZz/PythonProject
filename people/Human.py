import math
import random as rnd


class Human:

    def __init__(self, name='Noname'):
        self.name = name
        self.satiety = math.ceil(rnd.random() * 99)
        self.money = math.ceil(rnd.random() * 99)
        self.happiness = math.ceil(rnd.random() * 99)
        # print('Йа родилсо!')

    '''
    def __del__(self):
        print('Йа убилсо!')
    '''
    def say(self, count=1):
        for i in range(count):
            print(self.name + ' say: AAAAAAAA!!!')

    def work(self):
        self.satiety -= math.ceil(rnd.random() * 99)
        self.money += math.ceil(rnd.random() * 99)
        self.happiness -= math.ceil(rnd.random() * 99)
        if self.satiety <= 0:
            self.eat()
        if self.happiness <= 0:
            print('Да пошло оно все, пойду на рыбалку!')
            self.fishing()
        return [self.satiety, self.money, self.happiness]

    def eat(self):
        if self.money <= 0:
            print('БОМЖАРА')
        else:
            self.satiety += math.ceil(rnd.random() * 99)
            self.money -= math.ceil(rnd.random() * 99)
            self.happiness += math.ceil(rnd.random() * 99)
        return [self.satiety, self.money, self.happiness]

    # Рыбалка
    def fishing(self):
        self.happiness += math.ceil(rnd.random() * 99)
        self.money -= math.ceil(rnd.random() * 99)
        if self.money < 0:
            print('Я КАМЕНЩИК ПОРА ИДТИ РАБОТАТЬ')
        return [self.money, self.happiness]
