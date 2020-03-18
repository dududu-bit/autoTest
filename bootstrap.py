import os

from excep.myException import *
from suite.testBaidu import *
from util.HTMLTestRunner import *
from util.Properties import Properties

properties = Properties('../config.properties')
reportPath = properties.getProperties().get('report_path')
if not os.path.exists(reportPath):
    raise MyException('config exception', '配置文件中指定的报告路径不存在')
else:
    pass
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
HtmlFile = reportPath + now + ".html"
current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
testUnit = unittest.TestSuite()  # 构建测试套件
testUnit.addTest(BaiDu("test_01"))
fp = open(reportPath + current_time + ".html", "wb")
runner = HTMLTestRunner(stream=fp, verbosity=2, title=u"自动化测试报告", description="自动化测试演示报告", tester='lvhong')
runner.run(testUnit)
fp.close()
