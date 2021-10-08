import selenium
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

def Clicker(target_url, pw):
    driver.get(target_url)
    time.sleep(1)

    box_password = driver.find_element_by_id('password')
    box_password.send_keys(pw)
    box_password.send_keys(Keys.ENTER)
    time.sleep(1)

    menu = 'k'
    x = 70
    y = 935
    x_start = 70.0
    x_one = float(4794 / (1350 - 70))
    print(x_one)
    while menu:
        menu = input()
        timeRangeCurrent = driver.find_element_by_class_name('vjs-time-range-current').text
        minute = int(timeRangeCurrent[3]) * 10 + int(timeRangeCurrent[4])
        second = int(timeRangeCurrent[6]) * 10 + int(timeRangeCurrent[7])
        second += minute * 60.0
        if menu == 'e':
            break
        elif menu == 'j':
            x = (x_start + (second - 10) / x_one + 3)  # +3은 그냥 수동 보정
            pyautogui.moveTo(x, y)
            pyautogui.click()
        elif menu == 'l':
            x = (x_start + (second + 10) / x_one + 3)
            pyautogui.moveTo(x, y)
            pyautogui.click()

    '''
    print(pyautogui.position())
    
    pyautogui.moveTo(70, 935)
    pyautogui.click()
    point_start = tooltip.text
    print(point_start)

    pyautogui.moveTo(1350, 935)
    pyautogui.click()
    point_end = tooltip.text
    print(point_end)

    # 1(x)에 3.8(초), 소수는 안 됨
    # 3.8초의 원리: 영상 길이 / 바 길이 = 4794(초) / 1280(X) = 3.745
     영상과 프로그레스 바 길이 사이의 비율 관계를 이용해 현재 재생 시각 10초 전후의 X 좌표를 계산해서 이동하는 방식
    '''

    # driver.close()


options = Options()
options.add_argument('incognito')  # 시크릿 모드 실행
options.add_argument("--start-maximized")  # 최대화
# options.add_argument('--start-fullscreen') # F11
driver = Chrome("chromedriver_win32\chromedriver", options=options)

Clicker(
    'https://···.zoom.us/rec/play/···',
    '···')
