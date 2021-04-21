from basepage import BasePage


class ContactPage(BasePage):
    def goto_add_member(self):
        pass

    def get_list(self):
        ele_list = self.driver.find_elements_by_css_selector(".member_colRight_memberTable_td:nth-child(2)")
        name_list = [i.text for i in ele_list]
        print(name_list)
        return name_list




