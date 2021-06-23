from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

#os.system('/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="~/ChromeProfile"')

usernamelist = []
passwordlist = []

options = webdriver.ChromeOptions()
options.add_argument('User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36')
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")


driver = webdriver.Chrome('크롬 드라이버 주소', options=options)
driver.implicitly_wait(1)

driver.delete_all_cookies()
driver.get('https://www.nike.com/kr/ko_kr/login?successUrl=/account/theDrawList')

for i in range(len(usernamelist)-1):
    time.sleep(1)
    driver.execute_script('window.open("https://www.nike.com/kr/ko_kr/login?successUrl=/account/theDrawList");')

driver.implicitly_wait(3)

for i in range(len(usernamelist)):
    driver.switch_to_window(driver.window_handles[i])
    elem = driver.find_element_by_id("j_username")
    elem.send_keys(usernamelist[i])
    elem = driver.find_element_by_id("j_password")
    elem.send_keys(passwordlist[i])
    driver.find_element_by_xpath("//button[@type='submit']").click()
    

    c_xpath = "/html/body/section/section/article[2]/div/div[2]/div/div[1]/div[1]/div/a[1]/span"
    c = driver.find_element_by_xpath(c_xpath)
    k = int(c.text)
    if k >= 8:
        k = 8
    else:
        k = k 

    name_list = [] 
    for p in range(1,k+1):
        name_xpath = "/html/body/section/section/article[2]/div/div[2]/div/div[2]/div["+str(p)+"]/div[2]/div[1]/div[2]/span[2]"
        name = driver.find_element_by_xpath(name_xpath)
        name_list.append(name.text)

    result_list = []
    for p in range(1,k+1):
        result_xpath = "/html/body/section/section/article[2]/div/div[2]/div/div[2]/div["+str(p)+"]/div[1]/span[2]"
        result = driver.find_element_by_xpath(result_xpath)
        result_list.append(result.text)
    
    driver.implicitly_wait(0.3)

    total = driver.find_element_by_xpath("/html/body/section/section/article[2]/div/div[2]/div/div[1]/div[1]/div/a[1]/span")
    processing = driver.find_element_by_xpath("/html/body/section/section/article[2]/div/div[2]/div/div[1]/div[1]/div/a[2]/span")
    Win = driver.find_element_by_xpath("/html/body/section/section/article[2]/div/div[2]/div/div[1]/div[1]/div/a[3]/span")
    Lose = driver.find_element_by_xpath("/html/body/section/section/article[2]/div/div[2]/div/div[1]/div[1]/div/a[4]/span")

    print(str(i+1)+str('.')+str(' ')+usernamelist[i])
    print(str(' [전체: ')+total.text+str('개 | ')+str('진행중: ')+processing.text+str('개 | ')+str('당첨: ')+Win.text+str('개 | ')+str('미당첨: ')+Lose.text+str('개]'))
    print('제품명:',name_list)
    print('당첨 여부:',result_list,'\n')
   
for i in range(len(usernamelist)-1):
    time.sleep(0.3)
    driver.switch_to.window(driver.window_handles[-1])
    driver.close()

driver.switch_to.window(driver.window_handles[-1])
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #스크롤
posting = driver.find_element_by_xpath('/html/body/footer/div/div[1]/div/div/p[5]/a') #로그아웃
posting.click()


driver.quit()
print("Done!")