#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

"""Module to test functionally user login"""

import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from users.models import User


class MySeleniumTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()
        cls.selenium.implicitly_wait(10)


    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        User.objects.create_user(
            username='myuser@gmail.com',
            first_name='test',
            password='connectme1234')
        self.selenium.get('%s%s' % (self.live_server_url, '/users/login'))
        time.sleep(3)
        username_input = self.selenium.find_element(By.ID, "id_username")
        username_input.send_keys('myuser@gmail.com')
        time.sleep(1)
        password_input = self.selenium.find_element(By.ID, "id_password")
        password_input.send_keys('connectme1234')
        time.sleep(1)
        self.selenium.find_element(
            By.ID, "button-addon2").click()
        time.sleep(1)
        message = WebDriverWait(
            self.selenium, timeout=10).until(
            EC.presence_of_element_located(
                (By.ID, "alert_message")))
        assert "Vous êtes désoramais connectés." in message.text
