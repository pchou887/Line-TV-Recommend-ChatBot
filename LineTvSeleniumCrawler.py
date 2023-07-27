from bs4 import BeautifulSoup
from selenium import webdriver as wd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By as by
from selenium.common.exceptions import NoSuchElementException
from openpyxl import Workbook
from time import sleep

option = wd.ChromeOptions()
prefs = {"profile.default_content_setting_values":{"notifications":2}}
option.add_experimental_option("prefs", prefs)

 
driver = wd.Chrome("C:\\Users\\user\\Desktop\\chromedriver.exe", options = option)
driver.get("https://www.linetv.tw/")
#連續劇

def change_page():
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    try :
        wdw(driver, 3).until(ec.element_to_be_clickable((by.CSS_SELECTOR, 'a[class="Pagination-nextLink"][aria-disabled="false"]'))).click()
    except (ElementClickInterceptedException, TimeoutException, NoSuchElementException):
        return False
    return True

lang_t = 8
lkyu = []
url = []
while lang_t < 10:
    kind_t = 2
    #語言
    wdw(driver, 5).until(ec.element_to_be_clickable((by.XPATH, '//*[@id="root"]/div/div/div/div/nav/div/div[1]/div[2]/a['+str(lang_t)+']'))).click()
    sleep(1)
    #類別
    while True:
        year_t = 2
        try :
            wdw(driver, 5).until(ec.element_to_be_clickable((by.XPATH, '//*[@id="root"]/div/div/div/div/nav/div/div[2]/div[2]/a['+str(kind_t)+']'))).click()
        except (TimeoutException, NoSuchElementException):
            break
        sleep(1)
        #年份
        while True:
            url_temp = 1
            url_total = 1
            try :
                wdw(driver, 5).until(ec.element_to_be_clickable((by.XPATH, '//*[@id="root"]/div/div/div/div/nav/div/div[3]/div[2]/a['+str(year_t)+']'))).click()
            except (TimeoutException, NoSuchElementException):
                print("going to next kind")
                break
            sleep(3)
            #抓網頁
            while True:
                try :
                    url.append(driver.find_element(by.XPATH, '//*[@id="root"]/div/div/div/div/section/div[2]/a['+ str(url_temp) +']').get_attribute("href"))
                except NoSuchElementException:
                    if change_page():
                        print("going to next page.")
                        url_temp = 0
                        url_total -= 1
                        sleep(3)
                    else :
                        print(url_total)
                        driver.execute_script("window.scrollTo(0,0)")
                        print("going to next year.")
                        lkyu.append([lang_t - 1, kind_t - 1, year_t - 1, url_total - 1])
                        break
                sleep(0.5)
                url_temp += 1
                url_total += 1
            year_t += 1
        kind_t += 1
    print("going to next language")
    lang_t += 1
    import requests as req

def driver_get(dri, u, u_t):
    try:
        dri.get(u[u_t])
    except TimeoutException:
        print("get error")
        driver_get(dri, u, u_t)
        
def ban_18(dri):
    sleep(2)
    if len(dri.find_elements(by.CSS_SELECTOR, 'div[class="ReactModalPortal"]')) == 4:
        wdw(dri, 3).until(ec.element_to_be_clickable((by.XPATH, '/html/body/div[4]/div/div/div/div/button[2]'))).click()

def roll_down(dri):
    try :
        dri.execute_script("window.scrollTo(0,1080)")
    except :
        print("roll error")
        driver.refresh()
        ban_18(dri)
        roll_down(dri)
    sleep(1)

def in_c(s,sc):
    try :
        temp_c = round(float(s.find('script').text[(sc.text).find('"rating_avg":') + 13:(sc.text).find('"rating_avg":') + 17]), 1)
    except ValueError:
        temp_c = 0
    return temp_c

def in_d(dri):
    try :
        temp_d = wdw(driver, 3).until(ec.element_to_be_clickable((by.XPATH, '//*[@id="react-tabs-0"]'))).text
    except (TimeoutException, NoSuchElementException):
        driver.refresh()
        ban_18(dri)
        roll_down(dri)
        return in_d(dri)
    temp_d = int(temp_d[temp_d.find("(") + 1:temp_d.find(")")])
    return temp_d


def in_e(sc):
    if "普遍級" in sc.text:
        temp_e = "普遍級"
    elif "保護級" in sc.text:
        temp_e = "保護級"
    elif "輔導十二歲級" in sc.text:
        temp_e = "輔導十二歲級"
    elif "限制級" in sc.text:
        temp_e = "限制級"
    else :
        temp_e = "None"
    return temp_e

def in_f(s):
    try :
        temp_f = s.find("div", class_="flex-none text-brand-black bg-brand-yellow-400 text-12 font-500 px-2").text
    except AttributeError:
        temp_f = False
    if not temp_f:
        temp_f = 0
    else :
        temp_f = 1
    return temp_f

wb = Workbook()
ws = wb.active
ws.append(["語言", "種類", "年份", "類型與集數", "標題", "評分", "留言數", "分級", "VIP"])
print(len(url), len(lkyu))
url_intimes = 0

for i in lkyu:
    print(i)
    temp = []
    if i[0] == 1:
        temp.append("日本")
    elif i[0] == 2:
        temp.append("其他地區")
#     elif i[0] == 3:
#         temp.append("大陸")
#     elif i[0] == 4:
#         temp.append("日本")
#     elif i[0] == 5:
#         temp.append("新加坡")
#     elif i[0] == 6:
#         temp.append("泰國")
#     elif i[0] == 7:
#         temp.append("香港")
#     elif i[0] == 8:
#         temp.append("其他地區")

    if i[1] == 1:
        temp.append("Ani-One專區")
    elif i[1] == 2:
        temp.append("熱血")
    elif i[1] == 3:
        temp.append("王道")
    elif i[1] == 4:
        temp.append("懸疑")
    elif i[1] == 5:
        temp.append("勵志")
    elif i[1] == 6:
        temp.append("科幻")
    elif i[1] == 7:
        temp.append("青春")
    elif i[1] == 8:
        temp.append("幽默")
    elif i[1] == 9:
        temp.append("校園")
    elif i[1] == 10:
        temp.append("料理")
    elif i[1] == 11:
        temp.append("格鬥")
    elif i[1] == 12:
        temp.append("家庭")
    elif i[1] == 13:
        temp.append("友情")
    elif i[1] == 14:
        temp.append("愛情")
    elif i[1] == 15:
        temp.append("運動")
    elif i[1] == 16:
        temp.append("妖怪")
    elif i[1] == 17:
        temp.append("恐怖")
    elif i[1] == 18:
        temp.append("職人")
    elif i[1] == 19:
        temp.append("耽美")

    if i[2] == 1:
        temp.append("2023")
    elif i[2] == 2:
        temp.append("2022")
    elif i[2] == 3:
        temp.append("2021")
    elif i[2] == 4:
        temp.append("2020")
    elif i[2] == 5:
        temp.append("2019")
    elif i[2] == 6:
        temp.append("2018")
    elif i[2] == 7:
        temp.append("2017")
    elif i[2] == 8:
        temp.append("2016")
    elif i[2] == 9:
        temp.append("2011-2015")
    elif i[2] == 10:
        temp.append("2000-2010")
    elif i[2] == 11:
        temp.append("2000年以前")

    if i[3] == 0:
        continue
    else :
        for t in range(i[3]):
            res = req.get(url[url_intimes])
            soup = BeautifulSoup(res.text)
            driver_get(driver, url, url_intimes)
            print("connect success", t+1)
            ban_18(driver)
            roll_down(driver)
            url_intimes += 1
            scripts = soup.find('script')
            a = soup.find("div", class_ = "flex items-end mt-2").text
            b = soup.find("h1", class_ = "sr-only").text
            c = in_c(soup, scripts)
            d = in_d(driver)
            e = in_e(scripts)
            f = in_f(soup)
            temp.append(a) #類型與集數
            temp.append(b) #標題
            temp.append(c) #評分
            temp.append(d) #留言數
            temp.append(e) #分級(普遍...)
            temp.append(f) #VIP
            ws.append(temp)
            for pop in range(6):
                temp.pop()
    wb.save("anime_3.xlsx")