import allure


@allure.feature("百度搜索测试")
class TestAllureReport:

    @allure.story("原神关键字搜索测试")
    def test_yuanshen_search(self):
        with allure.step("打开浏览器"):
            print("1.打开浏览器")
        with allure.step("输入被测网站的url"):
            print("2.输入被测网站的url：https://www.baidu.com")
        with allure.step("找到搜索框"):
            print("3.找到搜索框")
        with allure.step("在搜索框中输入原神"):
            print("4.在搜索框中输入原神")
        with allure.step("点击搜索按钮"):
            print("5.点击搜索按钮")
            allure.attach(open("data/yuanshen.txt", encoding="utf-8").read(), name="文本数据",
                          attachment_type=allure.attachment_type.TEXT)
        with allure.step("断言测试结果"):
            print("6.搜索页面的标题包含原神")
            allure.attach(r"data/yuanshen.png", name="图片数据",
                          attachment_type=allure.attachment_type.PNG)
            title = "原神_百度搜索"
            assert "原神" in title

    @allure.story("王者荣耀关键字搜索测试")
    def test_wangzhe_search(self):
        with allure.step("打开浏览器"):
            print("1.打开浏览器")
        with allure.step("输入被测网站的url"):
            print("2.输入被测网站的url：https://www.baidu.com")
        with allure.step("找到搜索框"):
            print("3.找到搜索框")
        with allure.step("在搜索框中输入王者荣耀"):
            print("4.在搜索框中输入王者荣耀")
        with allure.step("点击搜索按钮"):
            print("5.点击搜索按钮")
        with allure.step("断言测试结果"):
            print("6.搜索页面的标题包含王者荣耀")
            title = "王者荣耀_百度搜索"
            assert "王者荣耀" in title
