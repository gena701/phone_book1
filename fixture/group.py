
class GroupHelper:

     def __init__(self, app):
        self.app = app


     def return_to_groups(self):
        # return to groups page
        wd = self.app.wd # ссылка на вебдрайвер
        wd.find_element_by_link_text("group page").click()

     def create(self, group):
        # initialisation of new group (sozdanie novoi gryppi)
        wd = self.app.wd # ссылка на вебдрайвер
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
        wd = self.app.wd # ссылка на вебдрайвер
        wd.find_element_by_link_text("groups").click()

     def delete_first_group(self):
        wd = self.app.wd # ссылка на вебдрайвер
        self.open_groups_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # confirm deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups()
