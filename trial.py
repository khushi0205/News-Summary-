from selenium import webdriver
import time
links= ['https://www.moneycontrol.com/news/business/', 'https://www.moneycontrol.com/news/business/economy/','https://www.livemint.com/latest-news','https://www.livemint.com/market','https://www.business-standard.com/economy-policy','https://www.business-standard.com/finance','https://www.thehindubusinessline.com/']
driver = webdriver.Edge(r'C:\Users\khushi\Downloads\edgedriver_win32 (1)\msedgedriver.exe')

t = 120

for i in links:
    driver.get(i)
    driver.implicitly_wait(20)
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    
