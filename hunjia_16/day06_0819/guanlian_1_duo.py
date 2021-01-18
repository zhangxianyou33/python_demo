class Dept:
    def __init__(self, **kwargs):
        self.__dname = kwargs.get("dname")
        self.__loc = kwargs.get("loc")
        self.__emps = []   #雇员信息

    def get_emps(self):   # 获取全部雇员信息
        return self.__emps
    def get_info(self):
        return "Depy类:{}{}".format(self.__dname, self.__loc)
class Emp:  # 雇员信息
    def __init__(self, **kwargs):
        self.__name = kwargs.get("name")
        self.__sal = kwargs.get("sal")

    def set_dept(self, dept):  # 设置雇员和部门的关系
        self.__dept = dept
    def set_mgr(self, mgr):  #设置全部领导信息
        self.__mgr = mgr

    def get_mgr(self):       # 获取雇员信息
        if "emp_mgr" in dir(self):  # 给定的对象有mgr，才返回
            return self.__mgr
        else:
            return None

    def get_info(self):
        return "Emp类：{}{}".format(self.__name, self.__sal)
if __name__ == '__main__':
    d = Dept(dname="教学部", loc="北京")
    e_a = Emp(name="张显友", sal=3000)
    e_b = Emp(name="南毛毛", sal=4000)
    e_c = Emp(name="总经理", sal=5000)
    e_a.set_dept(d)  #设置部门和雇员的关系
    e_b.set_dept(d)
    e_c.set_dept(d)
    e_b.set_mgr(e_a) #设置领导关系
    e_a.set_mgr(e_c)
    d.get_emps().append(e_a) # 设置部门和员工的关系
    d.get_emps().append(e_b) # 设置部门和员工的关系
    d.get_emps().append(e_c) # 设置部门和员工的关系
    # 设置部门和员工的关系
    for i in d.get_emps():
        print(i.get_info())
        if i.get_mgr() != None:
            print(i.get_mgr().get_info())