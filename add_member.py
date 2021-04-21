from selenium import webdriver
from time import sleep
from basepage import BasePage
from contact_page import ContactPage


class AddMemberPage(BasePage):
    def add_member(self, name):
        self.driver.find_element_by_id("username").send_keys(name)
        self.driver.find_element_by_id("memberAdd_english_name").send_keys("xixi")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("002")
        self.driver.find_element_by_id("memberAdd_phone").send_keys("13693147526")
        self.driver.find_element_by_css_selector(".qui_btn.ww_btn.js_btn_save").click()
        ele_list1 = self.driver.find_elements_by_css_selector(".ww_inputWithTips_tips")
        ele_name1 = [i.text for i in ele_list1]
        if ele_name1 != '':
            print(ele_name1)

        return ContactPage(self.driver)


    def add_party(self, name):
        # 添加部门页面
        self.driver.find_element_by_css_selector("[name=name]").send_keys(name)
        self.driver.find_element_by_css_selector(".js_parent_party_name").click()
        self.driver.find_element_by_css_selector(".qui_dialog_body.ww_dialog_body [id='1688849984108183_anchor']").click()
        self.driver.find_element_by_css_selector(".qui_dialog_foot.ww_dialog_foot a:nth-child(1)").click()

    def add_address_book(self):
        # 导入通讯录上传文件
        self.driver.find_element_by_id("js_upload_file_input").send_keys("/data/mydata.xlsx")
        assert "mydata.xlsx" == self.driver.find_element_by_id("upload_file_name").text
        sleep(3)
        self.driver.find_element_by_id("submit_csv").click()






