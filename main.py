import os

import selenium
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

# 채팅 있을 때
# x_start: 62~74 -> 70
# x_end: 1348 ~ 1361 -> 1350

# 채팅 없을 때
# x_start: 178~191 -> 190
# x_end: 1719~1731 -> 1720
def OpenZoom(target_url, pw, lecture_name):
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

def CrawlTimeline(lecture_name):
    try:
        f = open(lecture_name + '.txt', 'r', encoding='UTF-8')
    except FileNotFoundError:
        print("타임라인 스캔을 시작합니다. 반드시 마우스를 움직이지 말고 기다려주세요.")
        time.sleep("3")
    else:
        return 0

    try:
        y = 930
        x_start = 70
        x_end = 1350
        driver.find_element_by_class_name("transcript-wrapper")
    except selenium.common.exceptions.NoSuchElementException:
        x_start = 190
        x_end = 1720
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
        tooltips += tooltip + "\n"

    f = open(lecture_name+'.txt', 'w', encoding='UTF-8')
    f.write(tooltips)
    f.close()
    print("타임라인 스캔을 종료합니다.")

def Clicker(lecture_name):
    f = open(lecture_name+'.txt', 'r', encoding='UTF-8')
    tooltips = f.readlines()
    f.close()

    try:
        y = 930
        x_start = 70
        x_end = 1350
        driver.find_element_by_class_name("transcript-wrapper")
    except selenium.common.exceptions.NoSuchElementException:
        x_start = 190
        x_end = 1720

    menu = '0'
    btn_play = driver.find_element_by_xpath('//*[@id="vjs_video_3"]/div[4]/button')
    while menu != 'e':
        menu = input('명령어를 입력하세요: ')
        pyautogui.moveTo(x_start, y)
        time.sleep(1)
        timeRangeCurrent = driver.find_element_by_class_name('vjs-time-range-current').text
        cur_hour = int(timeRangeCurrent[1])
        cur_minute = int(timeRangeCurrent[3]) * 10 + int(timeRangeCurrent[4])
        cur_second = int(timeRangeCurrent[6]) * 10 + int(timeRangeCurrent[7])
        tooltips_len = len(tooltips)
        if len(menu) == 0:
            continue
        if menu[0] == '5':
            btn_play.click()
            continue
        elif menu[0] == '4':
            i = tooltips_len
            while i >= 0:
                i -= 1
                print(tooltips[i])
                if len(tooltips[0]) == 6:
                    tip_hour = 0
                    tip_minute = int(tooltips[i][0]) * 10 + int(tooltips[i][1])
                    tip_second = int(tooltips[i][3]) * 10 + int(tooltips[i][4])
                else:
                    tip_hour = int(tooltips[i][0])
                    tip_minute = int(tooltips[i][2]) * 10 + int(tooltips[i][3])
                    tip_second = int(tooltips[i][5]) * 10 + int(tooltips[i][6])

                if ((cur_hour == tip_hour and cur_minute == tip_minute and cur_second - 10 <= tip_second <= cur_second - 5)
                    or (cur_hour == tip_hour and cur_minute - 1 == tip_minute and 50 <= tip_second <= 59)
                    or (cur_hour - 1 == tip_hour and cur_minute == 00 and 50 <= tip_second <= 59)):
                    pyautogui.moveTo(x_start + i - (len(menu) - 1), y) # 문자 여러 개 입력한 만큼 더 ㄱㄱ
                    break
        elif menu[0] == '6':
            i = 0
            while i < tooltips_len:
                i += 1
                print(tooltips[i])
                if len(tooltips[0]) == 6:
                    tip_hour = 0
                    tip_minute = int(tooltips[i][0]) * 10 + int(tooltips[i][1])
                    tip_second = int(tooltips[i][3]) * 10 + int(tooltips[i][4])
                else:
                    tip_hour = int(tooltips[i][0])
                    tip_minute = int(tooltips[i][2]) * 10 + int(tooltips[i][3])
                    tip_second = int(tooltips[i][5]) * 10 + int(tooltips[i][6])

                if ((cur_hour == tip_hour and cur_minute == tip_minute and cur_second + 5 <= tip_second <= cur_second + 10)
                    or (cur_hour == tip_hour and cur_minute + 1 == tip_minute and 0 <= tip_second <= 10)
                    or (cur_hour + 1 == tip_hour and cur_minute == 59 and 0 <= tip_second <= 10)):
                    pyautogui.moveTo(x_start + i + (len(menu) - 1) + 2, y) # 2는 수동 보정. 왜냐하면 이거 하는 사이에 영상이 계속 재생되니까. 그리고 보통 영상 넘길 땐 팍팍 넘기니까
                    break
        else:
            continue
        pyautogui.click()
        time.sleep(1)
        me.activate() # 다시 이 프로그램(ZoomClicker) 창 맨 앞으로 띄우기
        pyautogui.moveTo(x_end, y) # 그냥 내가 타임 테이블 계속 보고 싶어서

    driver.close()
    return 0


#'''
me = pyautogui.getActiveWindow()

options = Options()
options.add_argument('incognito')  # 시크릿 모드 실행
options.add_argument("--start-maximized")  # 최대화
# options.add_argument('--start-fullscreen') # F11
options.add_experimental_option('excludeSwitches', ['enable-logging']) # https://stackoverflow.com/questions/69370457/google-chrome-always-crashes-after-opening-a-page
driver = Chrome("chromedriver_win32\chromedriver", options=options)

target_url = input("Zoom Video의 링크를 입력하세요: ")
password = input("Zoom Video의 암호를 입력하세요: ")
lecture_name = input("Zoom Video의 이름을 입력하세요(웬만하면 영어로 짧게): ")
OpenZoom(target_url, password, lecture_name)
CrawlTimeline(lecture_name)
Clicker(lecture_name)
#'''