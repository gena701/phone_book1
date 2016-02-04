
class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        # login
        wd = self.app.wd # ссылка на вебдрайвер
        self.app.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def logout(self):
        # logout
        wd = self.app.wd # ссылка на вебдрайвер
        wd.find_element_by_link_text("Logout").click()
