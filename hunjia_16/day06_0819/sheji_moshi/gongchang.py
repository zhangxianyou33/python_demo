# 设计模式，在面向对象设计与开发过程中，形成的开发结构，利用这种结构，可以避免耦合问题
#

class Food:
    def eat(self):
        pass
class Bread(Food):
    def eat(self):
        print("Bread:吃面包")
class Milk(Food):
    def eat(self):
        print("Milk：喝牛奶")
def get_food(cls):
    if cls == "bread":
        return Bread()
    elif cls == "milk":
        return Milk()
    else:
        return None

if __name__ == '__main__':
    food = get_food("bread")
    if food != None:
        food.eat()