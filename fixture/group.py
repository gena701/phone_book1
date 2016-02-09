
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
        # click "New Group" button
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups()

     def fill_group_form(self, group):
        wd = self.app.wd # ссылка на вебдрайвер
        # fill group form
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

     def change_field_value(self, field_name, text):
        wd = self.app.wd # ссылка на вебдрайвер
        if text is not None:
           wd.find_element_by_name(field_name).click()
           wd.find_element_by_name(field_name).clear()
           wd.find_element_by_name(field_name).send_keys(text)

     def open_groups_page(self):
        # open groups page
        wd = self.app.wd # ссылка на вебдрайвер
        wd.find_element_by_link_text("groups").click()

     def delete_first_group(self):
        wd = self.app.wd # ссылка на вебдрайвер
        self.open_groups_page()
        self.select_first_group()
        # confirm deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups()

     def select_first_group(self):
        wd = self.app.wd # ссылка на вебдрайвер
        # select first group
        wd.find_element_by_name("selected[]").click()

     def modify_first_group(self, new_group_date):
        wd = self.app.wd # ссылка на вебдрайвер
        self.open_groups_page()
        self.select_first_group()
        # open modification form
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(new_group_date)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_groups()
