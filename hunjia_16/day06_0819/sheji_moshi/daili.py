# 正向代理：找A，A找B，B干活去了
# 反向代理：我要找B干活，谁去干，咋去无所谓


class Food:
    def eat(self):
        pass
class Food_real(Food):
    def eat(self):
        print("Foodreal：享用丰盛的美食@")

class Food_Proxy(Food):
    def __init__(self, food):
        self.__food = food

    def prepare(self):
        print("【餐厅在：】准备做饭的食材.")
    def clear(self):
        print("【餐厅在：】收拾碗筷，打扫卫生。")

    def eat(self):
        self.prepare()
        self.__food.eat()
        self.clear()
def get_instance():
    return Food_Proxy(Food_real())
if __name__ == '__main__':
    food = get_instance()
    if food != None:
        food.eat()

    # 代理设计模式，实现辅助的实现


