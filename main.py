from people.Human import Human
from people.Woman import Woman

man = Human('Andrey')
man.say(1)
man = Human('Vasya')
man.say(1)
woman = Woman('Masha')
print(man.work())
woman.shopping(man)
some = Woman.sex(man, woman)
some[0].say()
