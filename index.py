from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
import json
from selenium.webdriver.common.alert import Alert
import time
import datetime
import requests
import pyautogui as pag

option = Options()
option.add_argument("disable-infobars")
option.add_argument("disable-extensions")
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17 "
option.add_argument('user-agent=' + user_agent)
option.add_argument('disable-gpu')
option.add_argument('incognito')
option.add_argument('headless')

# Selenium 4.0 - load webdriver
s = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=s, options=option)

# Move to URL
browser.get('https://eclass.daejin.ac.kr/login.php?sso=ok')

stdid = "ID"
stdpw = "PW"

browser.find_element(By.NAME, "username").send_keys(stdid)
browser.find_element(By.NAME, "password").send_keys(stdpw)
browser.find_element(By.CLASS_NAME, "main_login_btn").click()

def post_message(channel, text):
    SLACK_BOT_TOKEN = "xoxb-4530833576885-4936667113093-TUDfVoLqstue6c13QrO6gRYV" # 발급받은 토큰 입력
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + SLACK_BOT_TOKEN
    }
    payload = {
        'channel': channel,
        'text': text
    }
    r = requests.post('https://slack.com/api/chat.postMessage', headers=headers, data=json.dumps(payload))

vide = 16224
video = vide+1
for u in range(16152, video, 1):
    print("U is",u)
    key = str(u)
    ketnas = "https://eclass.daejin.ac.kr/mod/xncommons/viewer.php?i="+key
    ati = 'window.open("domain");'
    tji = ati.replace("domain", ketnas)
    print(tji)
    luci = "실행 중인 영상 번호 : "+key
    post_message("#insc", luci)
    post_message("#insc", "------------------------------")
    browser.execute_script(tji)
    url = "https://eclass.daejin.ac.kr/mod/xncommons/viewer.php?i=16151"
    browser.switch_to.window(browser.window_handles[1])
    count = u
    # if count == 16151:
    #     browser.get(url)
    print(ketnas)
    settime = 1800
    browser.switch_to.frame(0)
    browser.switch_to.frame('ViewerFrame')
    time.sleep(1.8)
    browser.find_element(By.CLASS_NAME, "vc-front-screen-play-btn").click()
    # pag.click(x=661, y=606, clicks=1, button='left', interval=0.5)
    # browser.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div[1]/div")
    print("재생 실행..")
    post_message("#insc", "재생 실행..")
    for iu in range(settime, 0, -1):
        logss = datetime.datetime.now()
        lopia = str(logss)
        print("남은 시간 (s)", iu)
        printia = lopia+": [LOG-000000][OK] 영상 남은 시간 (S)_"+str(iu)
        prit = printia.replace("000000", key)
        post_message("#log", prit)
        if iu == 1800:
            tils = luci+" 번호 영상에 대한 남은 시간은 30분 입니다"
            print(tils)
            post_message("#insc", "------------------------------")
            post_message("#insc", tils)
        if iu == 1200:
            print(tils.replace("30", "20"))
            post_message("#insc", tils.replace("30", "20"))
            post_message("#insc", "------------------------------")
        if iu == 600:
            print(tils.replace("30", "10"))
            post_message("#insc", tils.replace("30", "10"))
            post_message("#insc", "------------------------------")
        time.sleep(1)
        if iu == 1:
            post_message("#insc", "다음 영상으로 넘어갔어요!")
            post_message("#insc", "------------------------------")
            print("log :","다음 영상 수행")
            browser.close()  #링크 이동 후 탭 닫기
            da = Alert(browser)
            print("----------------------")
            print(da.text)
            da.accept()
            browser.switch_to.window(browser.window_handles[0])
    # settime = 5
    # for iu in range(settime, 0, -1):
    #     print("남은 시간 (s)", iu)
    #     time.sleep(1)
    #     if iu == 1:
    #         print("log :","다음 영상 수행")
post_message("#insc", "실행 종료에요!")
post_message("#insc", "------------------------------")
while True:
    pass
