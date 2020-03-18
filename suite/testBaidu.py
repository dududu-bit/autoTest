import time
import unittest

from selenium import webdriver

from util.Properties import Properties


class BaiDu(unittest.TestCase):
    def setUp(self):
        properties = Properties('../testBaidu.properties')
        self.url = properties.getProperties().get('url')
        self.key = properties.getProperties().get('key')
        # 加载chrome驱动
        self.driver = webdriver.Chrome()
        # 配置窗口尺寸
        # driver.set_window_size("400", "600")
        self.driver.maximize_window()
        # 设置等待时长
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_01(self):
        # 配置url
        # url = "http://baidu.com"
        # 执行url访问
        self.driver.get(self.url)
        # 获取输入框元素
        elem = self.driver.find_element_by_id('kw')
        # elem = driver.find_elements_by_css_selector('#index-kw')
        # 在输入框中输入 java
        elem.send_keys(self.key)
        # 等待是为了方便查看浏览器效果
        time.sleep(5)
        # 点击搜索按钮
        click = self.driver.find_element_by_id('su')
        # 点百度一下
        click.click()
