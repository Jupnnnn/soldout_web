'''

자동화 실행 코드

'''

import unittest
import HtmlTestRunner
from datetime import datetime


from testcase import login

if __name__ == '__main__':
    test_suite = unittest.TestSuite()

    # 테스트 진행할 코드 추가
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(login.Login))

    

# ==========================================================================================

    # 보고서 생성 시점 기록 및 보고서명 기록
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_name = f"Report_{current_time}"

    # html 보고서 저장
    HtmlTestRunner.HTMLTestRunner(
        output="Reports",
        report_name="Report",
        report_title="Test Results",
        combine_reports=True
    ).run(test_suite)
    
    report_filename = f"{report_name}.html"

    # 보고서명 .txt 파일에 저장
    with open('report_filename.txt', 'w') as f:
        f.write(report_filename)    

