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
    x_start = 70
    x_end = 1350
    y = 935
    while menu != 'e':
        menu = input()
        i = x_end
        timeRangeCurrent = driver.find_element_by_class_name('vjs-time-range-current').text
        print(timeRangeCurrent)
        cur_minute = int(timeRangeCurrent[3]) * 10 + int(timeRangeCurrent[4])
        cur_second = int(timeRangeCurrent[6]) * 10 + int(timeRangeCurrent[7])
        if menu == 'j':
            while i <= x_end:
                pyautogui.moveTo(i, y)
                tooltip = driver.find_element_by_xpath('//*[@id="vjs_video_3"]/div[4]/div[1]/div[1]/div[2]/div').text
                tip_minute = int(tooltip[2]) * 10 + int(tooltip[3])
                tip_second = int(tooltip[5]) * 10 + int(tooltip[6])
                print("cur: ", timeRangeCurrent)
                print("tip: ", tooltip)
                if tip_minute == cur_minute and cur_second - 15 <= tip_second < cur_second - 5:
                    break
                elif cur_second <= 15 and tip_minute == cur_minute - 1 and 45 <= tip_second <= 55:
                    break

                i -= 1
                if (int(tooltip[0]) == 1 and cur_minute <= 55) or tip_minute - cur_minute >= 3:
                    i -= 30
        elif menu == 'l':
            while i <= x_end:
                pyautogui.moveTo(i, y)
                tooltip = driver.find_element_by_xpath('//*[@id="vjs_video_3"]/div[4]/div[1]/div[1]/div[2]/div').text
                tip_minute = int(tooltip[2]) * 10 + int(tooltip[3])
                tip_second = int(tooltip[5]) * 10 + int(tooltip[6])
                print("cur: ", timeRangeCurrent)
                print("tip: ", tooltip)
                if tip_minute == cur_minute and cur_second + 5 < tip_second <= cur_second + 15:
                    break
                elif cur_second <= 15 and tip_minute == cur_minute + 1 and 5 <= tip_second <= 15:
                    break

                i -= 1
                if (int(tooltip[0]) == 1 and cur_minute <= 55) or tip_minute - cur_minute >= 3:
                    i -= 30
        pyautogui.click()

    # driver.close()


options = Options()
options.add_argument('incognito')  # 시크릿 모드 실행
options.add_argument("--start-maximized")  # 최대화
# options.add_argument('--start-fullscreen') # F11
driver = Chrome("chromedriver_win32\chromedriver", options=options)

Clicker(
    'https://···.zoom.us/rec/play/···',
    '···')
