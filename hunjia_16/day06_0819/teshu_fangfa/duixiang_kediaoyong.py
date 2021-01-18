class Message:
    pass
class Me:
    def __call__(self, *args, **kwargs):
        return "name:{},age:{}".format(kwargs.get("name"), kwargs.get("age"))


if __name__ == '__main__':
    m = Message()
    print("默认方法：",callable(m))
    m2 = Me()
    print("覆写了call方法演示：",callable(m2))
    print(m2())
    print(m2(name="tom", age=22))
