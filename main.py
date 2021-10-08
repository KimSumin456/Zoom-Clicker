import selenium
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import pyautogui


# x_start: 62~74
# x_end: 1348 ~ 1361
def OpenZoom(target_url, pw):
    driver.get(target_url)
    time.sleep(1)

    box_password = driver.find_element_by_id('password')
    box_password.send_keys(pw)
    box_password.send_keys(Keys.ENTER)
    time.sleep(1)

    btn_play = driver.find_element_by_xpath('//*[@id="vjs_video_3"]/div[4]/button')
    btn_play.click()

    btn_mute = driver.find_element_by_xpath('//*[@id="vjs_video_3"]/div[4]/div[3]/button')
    btn_mute.click()

def CrawlTimeline():
    x_start = 70
    x_end = 1350
    y = 930
    tooltips = ""
    for i in range(x_start, x_end):
        i += 2
        pyautogui.moveTo(i, y)

        '''
        timeRangeCurrent = driver.find_element_by_class_name('vjs-time-range-current').text
        cur_minute = int(timeRangeCurrent[3]) * 10 + int(timeRangeCurrent[4])
        cur_second = int(timeRangeCurrent[6]) * 10 + int(timeRangeCurrent[7])
        print(timeRangeCurrent)

        tooltip = driver.find_element_by_xpath('//*[@id="vjs_video_3"]/div[4]/div[1]/div[1]/div[2]/div').text
        tip_minute = int(tooltip[2]) * 10 + int(tooltip[3])
        tip_second = int(tooltip[5]) * 10 + int(tooltip[6])
        print(tooltip)
        '''

        tooltip = driver.find_element_by_xpath('//*[@id="vjs_video_3"]/div[4]/div[1]/div[1]/div[2]/div').text
        tooltips += tooltip

    f = open('tooltips.txt', 'w', encoding='UTF-8')
    f.write(tooltips)
    f.close()

def Clicker():
    tooltips = ""
    f = open('tooltips.txt', 'r', encoding='UTF-8')
    tooltips = f.readlines()
    f.close()

    x_start = 70
    x_end = 1350
    y = 930
    menu = 'k'
    while menu != 'e':
        menu = input('명령어를 입력하세요: ')
        pyautogui.moveTo(x_start, y)
        timeRangeCurrent = driver.find_element_by_class_name('vjs-time-range-current').text
        cur_hour = int(timeRangeCurrent[1])
        cur_minute = int(timeRangeCurrent[3]) * 10 + int(timeRangeCurrent[4])
        cur_second = int(timeRangeCurrent[6]) * 10 + int(timeRangeCurrent[7])
        i = len(tooltips)
        if menu == 'j':
            while i >= 0:
                i -= 1
                print(tooltips[i])
                tip_hour = int(tooltips[i][0])
                tip_minute = int(tooltips[i][2]) * 10 + int(tooltips[i][3])
                tip_second = int(tooltips[i][5]) * 10 + int(tooltips[i][6])
                if ((
                        cur_hour == tip_hour and cur_minute == tip_minute and cur_second - 10 <= tip_second <= cur_second - 5)
                        or (cur_hour == tip_hour and cur_minute - 1 == tip_minute and 50 <= tip_second <= 59)
                        or (cur_hour - 1 == tip_hour and cur_minute == 00 and 50 <= tip_second <= 59)):
                    pyautogui.moveTo(x_start + i, y)
                    break
        elif menu == 'l':
            while i >= 0:
                i -= 1
                tip_minute = int(tooltips[i][2]) * 10 + int(tooltips[i][3])
                tip_second = int(tooltips[i][5]) * 10 + int(tooltips[i][6])
                if ((cur_minute == tip_minute and cur_second + 5 <= tip_second <= cur_second + 10)
                        or (cur_hour == tip_hour and cur_minute + 1 == tip_minute and 0 <= tip_second <= 10)
                        or (cur_hour + 1 == tip_hour and cur_minute == 59 and 0 <= tip_second <= 10)):
                    pyautogui.moveTo(x_start + i, y)
                    break
        pyautogui.click()


options = Options()
options.add_argument('incognito')  # 시크릿 모드 실행
options.add_argument("--start-maximized")  # 최대화
# options.add_argument('--start-fullscreen') # F11
driver = Chrome("chromedriver_win32\chromedriver", options=options)

OpenZoom(
    'https://···.zoom.us/rec/play/···',
    '···')

# CrawlTimeline()

Clicker()