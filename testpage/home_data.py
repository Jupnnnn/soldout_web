'''

페이지 별 Xpath, ID 값

'''

class Home:
    def __init__(self, driver):
        self.driver = driver

    # 홈_로그인 버튼
    login_btn = '//*[@id="__layout"]/div/div[1]/header/div/ul/li[1]/a[text()="로그인"]'

    # 아이디 입력박스
    id_inputbox = '//*[@id="__layout"]/div/div[2]/div/form/div[1]/div/input'

    # 비밀번호 입력박스
    pw_inputbox = '//*[@id="__layout"]/div/div[2]/div/form/div[2]/div/input'

    # 로그인화면_로그인 버튼
    login_confirm_btn = '//*[@id="__layout"]/div/div[2]/div/form/button'

    # 마이페이지 버튼
    mypage = '//*[@id="__layout"]/div/div[1]/header/div/ul/li[2]/a'

    # 홈_로그아웃 버튼
    logout_btn = '//*[@id="__layout"]/div/div[1]/header/div/ul/li[1][text()="로그아웃"]'


    