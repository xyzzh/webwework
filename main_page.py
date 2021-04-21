from selenium import webdriver
from selenium.webdriver.common.by import By

from add_member import AddMemberPage
from basepage import BasePage


class MainPage(BasePage):
    def goto_add_member(self):
        # 添加成员
        self.find((By.CSS_SELECTOR, ".ww_indexImg_AddMember")).click()

        return AddMemberPage(self.driver)

    def goto_contact(self):
        # 通讯录添加部门
        self.driver.find_element_by_css_selector("[id='menu_contacts'] span").click()
        self.driver.find_element_by_css_selector(".member_colLeft_top_addBtn.member_colLeft_top_addBtn").click()
        self.driver.find_element_by_css_selector(".js_create_party").click()

        return AddMemberPage(self.driver)

    def goto_address_book(self):
        # 导入通讯录
        self.driver.find_element_by_css_selector(".ww_indexImg.ww_indexImg_Import").click()
        return AddMemberPage(self.driver)



