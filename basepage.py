from selenium import webdriver


class BasePage:
    def __init__(self, base_driver=None):
        if base_driver is not None:
            self.driver = base_driver
        else:
            chrome_arg = webdriver.ChromeOptions()
            chrome_arg.debugger_address = '127.0.0.1:9222'  # 本机浏览器服用命令：google-chrome --remote-debugging-port=9222
            self.driver = webdriver.Chrome(options=chrome_arg)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            self.driver.implicitly_wait(3)

    def find(self, locator):
        return self.driver.find_element(*locator)

