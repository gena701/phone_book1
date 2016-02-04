# -*- coding: utf-8 -*-

import pytest
from fixture.app_for_contact import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_new_contact(Contact(firstname="R_first name", middlename="R_middle name", lastname="R_last name", nickname="R_nickname", homephone="054586611",
                                mobilephone="0549452145"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_new_contact(Contact(firstname="", middlename="", lastname="", nickname="", homephone="",
                                mobilephone=""))
    app.session.logout()
