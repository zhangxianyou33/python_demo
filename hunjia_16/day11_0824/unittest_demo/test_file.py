# 测试文件，都保存在某个目录下，可以集中测试

import os
import unittest

class RunAllTest(unittest.TestCase):
    def test_run(self):
        case_path = os.getcwd() # 获取测试文件目录
        discover = unittest.defaultTestLoader.discover(case_path, pattern="test_ma*.py")

        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(discover)
if __name__ == '__main__':
    unittest.main()
