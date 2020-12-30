#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest


class TestStringMethods(unittest.TestCase):
    # setup和teardown方法是在每条测试用例前后调用
    def setUp(self) -> None:
        print('setup')

    def tearDown(self) -> None:
        print('teardoem\n')

    # setupclass和teardownclass方法是在所有测试用例的前后调用
    @classmethod
    def setUpClass(cls) -> None:
        print('setup class\n')

    @classmethod
    def tearDownClass(cls) -> None:
        print('teardown class')

    def test_upper(self):
        print('\ttest upper')
        self.assertEqual('foo'.upper(), 'FOO')

    # unittest.skip跳过测试
    @unittest.skip
    def test_isupper(self):
        print('\ttest is upper')
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print('\ttest split')
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    # 方法一：执行当前文件所有的测试用例
    # unittest.main()

    # 方法二：执行指定的测试用例，创建一个测试套件，只执行添加的测试用例
    # suite = unittest.TestSuite()
    # suite.addTest(TestStringMethods("test_split"))
    # unittest.TextTestRunner().run(suite)

    # 方法三：执行某个测试类，将测试类添加到测试套件里
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    suite = unittest.TestSuite([suite1])
    unittest.TextTestRunner(verbosity=2).run(suite)
