# coding:utf-8
import time
import unittest

from ddt import ddt, data, unpack
from selenium import webdriver


def readFile():
    params = []
    fl = open('../testBaidu.properties', 'r')
    for line in fl.readlines():
        params.append(line.strip('\n').split(','))
    return params


@ddt
class autoTestHtml(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com')

    def tearDown(self):
        time.sleep(10)
        self.driver.quit()

    @data(*readFile())
    @unpack
    def test_1(self, txt1, text1):
        self.driver.find_element_by_id('kw').send_keys(txt1)
        self.driver.find_element_by_id('kw').send_keys(text1)
        self.driver.find_element_by_id('su').click()


if __name__ == '__main__':
    unittest.main(verbosity=2)
