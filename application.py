from selenium.webdriver.firefox.webdriver import WebDriver

class Application:
     def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

     def logout(self):
        # logout
        wd = self.wd # ссылка на вебдрайвер
        wd.find_element_by_link_text("Logout").click()

     def return_to_groups(self):
        # return to groups page
        wd = self.wd # ссылка на вебдрайвер
        wd.find_element_by_link_text("group page").click()

     def create_group(self, group):
        # initialisation of new group (sozdanie novoi gryppi)
        wd = self.wd # ссылка на вебдрайвер
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups()

     def open_groups_page(self):
        # open groups page
        wd = self.wd # ссылка на вебдрайвер
        wd.find_element_by_link_text("groups").click()

     def login(self, username, password):
        # login
        wd = self.wd # ссылка на вебдрайвер
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

     def open_home_page(self):
        # open home page
        wd = self.wd # ссылка на вебдрайвер
        wd.get("http://localhost/addressbook/?group=Group1")

     def destroy(self):
        self.wd.quit()