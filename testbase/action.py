'''

선택, 입력 등 동작 함수 코드

'''

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from retrying import retry

from testbase.slack_connect import send_slack_msg

class action:
    def __init__(self, driver):
        self.driver = driver

    # 클릭
    @retry(stop_max_attempt_number=2, wait_fixed=2000)            
    def tap(self, element):
        try:
            wait = WebDriverWait(self.driver, 5)
            if element.startswith('(') or element.startswith('//'):
                button = wait.until(EC.element_to_be_clickable((By.XPATH, element)))
                button.click()
                    
            else:
                button = wait.until(EC.element_to_be_clickable((By.ID, element)))
                button.cilck()
                    
        except Exception:
            raise AssertionError()        

    # 노출 체크
    @retry(stop_max_attempt_number=2, wait_fixed=2000)
    def visible_check(self, element):
        try:
            wait = WebDriverWait(self.driver, 7)
            if element.startswith('(') or element.startswith('//'):
                search_result = wait.until(EC.presence_of_element_located((By.XPATH, element)))
                if search_result.is_displayed():
                    pass
            
            else:
                search_result = wait.until(EC.presence_of_element_located((By.ID, element)))
                if search_result.is_displayed():
                    pass

        except Exception:
            raise AssertionError()

    # 입력박스 입력
    @retry(stop_max_attempt_number=2, wait_fixed=2000)
    def keyword_input(self, element, keyword):
        try:
            wait = WebDriverWait(self.driver, 5)
            if element.startswith('(') or element.startswith('//'):
                input_box = wait.until(EC.element_to_be_clickable((By.XPATH, element)))
                input_box.send_keys(keyword)
                    
            else:
                input_box = wait.until(EC.element_to_be_clickable((By.ID, element)))
                input_box.send_keys(keyword)
                    
        except Exception:
            raise AssertionError()

    
            