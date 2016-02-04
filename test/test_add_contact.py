# -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="R_first name", middlename="R_middle name", lastname="R_last name", nickname="R_nickname", homephone="054586611",
                               mobilephone="0549452145"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", homephone="",
                               mobilephone=""))
    app.session.logout()
