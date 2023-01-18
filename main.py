
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time
import secret
driver = webdriver.Chrome()


# 로그인
url = 'https://www.letskorail.com/korail/com/login.do'
driver.get(url)
#id 입력
driver.find_element(By.ID, "txtMember").send_keys(secret.id)
time.sleep(0.5)
#password 입력
driver.find_element(By.ID, "txtPwd").send_keys(secret.password)
time.sleep(0.5)
driver.find_element(By.CLASS_NAME, "btn_login").click()
time.sleep(2)

driver.switch_to.window(driver.window_handles[1])
driver.close()
time.sleep(1)

driver.switch_to.window(driver.window_handles[0])    
time.sleep(1)

#승차표 검색
url = 'https://www.letskorail.com/ebizprd/EbizPrdTicketpr21100W_pr21110.do'
driver.get(url)
time.sleep(2)
driver.find_element(By.ID, "start").clear()
driver.find_element(By.ID, "start").send_keys("광명\n")

driver.find_element(By.ID, "get").clear()
driver.find_element(By.ID, "get").send_keys("울산(통도사)\n")

driver.find_element(By.ID, "s_day").send_keys("20")
time.sleep(0.5)

driver.find_element(By.ID, "s_hour").send_keys("15")
time.sleep(0.5)

driver.find_element(By.CLASS_NAME, "btn_inq").click()
time.sleep(1)

#팝업 닫기
driver.switch_to.window(driver.window_handles[1])
driver.close()
time.sleep(1)

driver.switch_to.window(driver.window_handles[0])    
time.sleep(2)

flag = False
while 1:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "tableResult"))
    )
    for i in range(6, 1, -1):
        if len(driver.find_elements(By.XPATH, '//*[@id="tableResult"]/tbody/tr['+str(i)+']/td[6]/a[1]/img')):
            driver.find_elements(By.XPATH, '//*[@id="tableResult"]/tbody/tr['+str(i)+']/td[6]/a[1]/img')[0].click()
            flag = True
        elif len(driver.find_elements(By.XPATH, '//*[@id="tableResult"]/tbody/tr['+str(i)+']/td[10]/a[1]/img')):
            driver.find_elements(By.XPATH, '//*[@id="tableResult"]/tbody/tr['+str(i)+']/td[10]/a[1]/img')[0].click()
            flag = True
        elif len(driver.find_elements(By.XPATH, '//*[@id="tableResult"]/tbody/tr['+str(i)+']/td[8]/a[1]/img')):
            driver.find_elements(By.XPATH, '//*[@id="tableResult"]/tbody/tr['+str(i)+']/td[8]/a[1]/img')[0].click()
            flag = True
        elif len(driver.find_elements(By.XPATH, '//*[@id="tableResult"]/tbody/tr['+str(i)+']/td[6]/a/img')):
            driver.find_elements(By.XPATH, '//*[@id="tableResult"]/tbody/tr['+str(i)+']/td[6]/a/img')[0].click()
            flag = True
            
    if flag:
        break
    driver.refresh()
    
while(True):
    	pass
# #move to pop-up
# driver.switch_to.window(driver.window_handles[1])
# time.sleep(1)

# xpath2 = '//span[@id="d20230120"]'
# driver.find_element_by_xpath(xpath2).click()
# time.sleep(1)

# #move to main-window again
# driver.switch_to.window(driver.window_handles[0])
# time.sleep(1)

# xpath3 = '//select[@id="time"]'
# driver.find_element_by_xpath(xpath3).click()
# driver.find_element_by_xpath(xpath3).send_keys("15")
# time.sleep(1) 

# xpath4 = '//img[@alt="조회하기"]'
# driver.find_element_by_xpath(xpath4).click()
# time.sleep(1)

# while True :
#     if select_btn == "예약하기" :
#         driver.find_element_by_xpath(xpath6).click()
#         break
#     else : 
#         print(select_btn)
#         time.sleep(0.5)
#         driver.refresh()