
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import smtplib
from email.message import EmailMessage
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
driver.find_element(By.ID, "start").send_keys("울산(통도사)\n")

driver.find_element(By.ID, "get").clear()
driver.find_element(By.ID, "get").send_keys("광명\n")

driver.find_element(By.ID, "s_day").send_keys("24")
time.sleep(0.5)

driver.find_element(By.ID, "s_hour").send_keys("17")
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
    #조회 된 승차권들 중에 6번째부터 4번째 승차권 순서대로
    for i in range(6, 3, -1):
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
        print("break")
        try:
            WebDriverWait(driver, 3).until(EC.alert_is_present())
            alert = driver.switch_to.alert

            # 확인하기
            alert.accept()
        except:
            print("no alert")
            flag=False
            driver.find_elements(By.CLASS_NAME, 'btn_blue_ang')[0].click()
        break
    if flag == False:
        driver.refresh()
    
    


# 1. SMTP 서버 연결
smtp_gmail  = smtplib.SMTP('smtp.gmail.com', 587)

# 2. SMTP 서버에 로그인
smtp_gmail.ehlo()
 
# 연결을 암호화
smtp_gmail.starttls()
 
#로그인
smtp_gmail.login(secret.EMAIL_ADDR_FROM, secret.EMAIL_PASSWORD)

# 3. MIME 형태의 이메일 메세지 작성
message = EmailMessage()
message.set_content('코레일 예약 완료!')
message["Subject"] = "코레일 예약 완료!"
message["From"] = secret.EMAIL_ADDR_FROM  #보내는 사람의 이메일 계정
message["To"] = secret.EMAIL_ADDR_TO

# 4. 서버로 메일 보내기
smtp_gmail.send_message(message)
print("sended mail")
# 5. 메일을 보내면 서버와의 연결 끊기
smtp_gmail.quit()

while True:
    pass
