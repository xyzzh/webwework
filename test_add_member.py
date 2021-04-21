import pytest

from main_page import MainPage
class TestAddMember:
    @pytest.mark.parametrize('name', ["火枪手"])
    def test_add_member(self, name):
        self.main = MainPage()
        # self.main.goto_add_member().add_member(name).get_list()
        self.main.goto_add_member().add_member(name)
        # assert name in res

    @pytest.mark.parametrize('name', ["研发部"])
    def test_add_party(self, name):
        # 添加部门
        self.main = MainPage()
        self.main.goto_contact().add_party(name)

    def test_address_book(self):
        # 导入通讯录
        self.main = MainPage()
        self.main.goto_address_book().add_address_book()


