import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from info import info
from testpage.home_data import Home
from testbase.action import action
from testbase.slack_connect import send_slack_msg

class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        send_slack_msg("테스트 시작..")
        cls.service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=cls.service)
        cls.driver.get(info.test_url)

        cls.home = Home(cls.driver)
        cls.action = action(cls.driver)

    # 로그인 버튼 선택
    def test01_login_btn_tap(self):
        self.action.tap(self.home.login_btn)

    # 아이디 입력박스 > 아이디 입력
    def test02_id_input(self):
        self.action.keyword_input(self.home.id_inputbox, 'wkdsj92')

    # 비밀번호 입력박스 > 비밀번호 입력
    def test03_pw_input(self):
        self.action.keyword_input(self.home.pw_inputbox, 'qatest1!')

    # 로그인 버튼 선택
    def test04_login_confirm_btn_tap(self):
        self.action.tap(self.home.login_confirm_btn)

    # 로그인 완료 여부 체크
    def test05_login_check(self):
        self.action.visible_check(self.home.logout_btn)
        

    @classmethod
    def tearDownClass(cls):
        send_slack_msg("테스트 종료..")
        cls.driver.quit()