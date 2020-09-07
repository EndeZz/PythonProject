import random as rnd

from people.Human import Human


class Woman(Human):

    def __init__(self, name='Noname'):
        super().__init__(name)
        self.hairColor = 'blond'

    def shopping(self, man):
        # super().say(1)
        if isinstance(man, Human):
            if man.money > 0:
                print(self.name + ' say: Пора шопиться')
            else:
                print(self.name + ' say: Нету денег!!!')

    @staticmethod
    def sex(father, mother, name='НЕ выбрали'):
        # проверить, чтобы папа был папой, а мама - мамой
        # возвращать человека СЛУЧАЙНОГО пола и со случайный именем
        if isinstance(father, Human) and isinstance(mother, Woman):
            genders = ('МУЖЧИНА', 'девка')
            gender = rnd.choice(genders)
            if gender == 'МУЖЧИНА':
                first_names = ('Володя', 'Сергей', 'Ванос', 'Бубулкин', 'Андрей', 'Семен Семеныч', 'Гном Гномыч')
            else:
                first_names = ('Света', 'Оля', 'Аня', 'Ванярита', 'Даша', 'ЛЮДА', 'Натаха')
            name = rnd.choice(first_names)
            print('Пол: ' + gender)
        return [Human(name), gender]
