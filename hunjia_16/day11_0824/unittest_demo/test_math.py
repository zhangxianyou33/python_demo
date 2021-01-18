from  unitest_demo import Math

import unittest

class Testmath(unittest.TestCase): #继承testcase父类
    @classmethod
    def setUpClass(self):
        print("【=======全部测试开始=====】")
    @classmethod
    def tearDownclass(self):
        print("【=======全部测试结束=====】")
    def setUp(self) -> None:
        print("{}：测试开始".format(self.id()))
    def tearDown(self) -> None:
        print("{}：测试结束".format(self.id()))

    def test_add(self):
        self.assertEqual(Math().add(1,2),3)

    # 不需要测试的功能，使用装饰器进行装饰
    @unittest.skip("Math.sub方法，功能暂不需要测试。")
    def test_sub(self):
        self.assertEqual(Math().sub(3,2),1)
if __name__ == '__main__':
    unittest.main()
