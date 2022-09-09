# from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class TestBrowser(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = webdriver.Chrome(
            executable_path='/home/vikornienko/PycharmProjects/learningDjango/DjangoCRMProject002/other_files/forwebdrivers/chromedriver',
            service_log_path='/home/vikornienko/PycharmProjects/learningDjango/DjangoCRMProject002/other_files/forwebdrivers/chromedriver.log'
        )
        cls.browser.implicitly_wait(30)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.quit()
        super().tearDownClass()

    def setUp(self) -> None:
        super(TestBrowser, self).setUp()


class TestAdminEnter(TestBrowser):

    def test_super_user_authentication(self):
        pass
        # self.browser.get(self.live_server_url)
        # WebDriverWait(self.browser, 10)
        # self.assertEqual(self.browser.title, "The install worked successfully! Congratulations!")
