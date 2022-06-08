from hashlib import new
from importlib.resources import path
import numbers
from this import d
from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# put here the email of your account
email ="your_email"  
# put here the password of your account
password="your_passowd"
#put in the get the link of the groupp  your want to scrap
the_linked="https://free.facebook.com/groups/466350787195322/"
# how many page you want scrap
number_of_pages =2

path="/home/maxime/webdriver/chromedriver" # here the path of chromedriver that you have to download

driver = webdriver.Chrome(path)
driver.get("https://free.facebook.com/")
print(driver.title)
login = driver.find_element_by_name("login")
username= driver.find_element_by_name("email")
password= driver.find_element_by_name("pass")
username.send_keys(email)
password.send_keys(password)

login.click()

confirm = driver.find_element(by=By.LINK_TEXT,value= "Plus tard")
confirm.click()

driver.get(the_linked)
tab_posts=[]
number=0

for i  in range(number_of_pages):
 
    links = driver.find_elements(by=By.LINK_TEXT,value="Actualité intégrale")
    
    
    print(len(links) )
    tab_links = [lk.get_attribute("href") for lk in links]
    for link in tab_links:
        driver.get(link)
        
        
        text= driver.find_element(by=By.CLASS_NAME,value="cj").text
        if text not in tab_posts:
            tab_posts.append(text)
            with open("group.txt",'a+') as f:
                f.write(text + "\n\n\n ...new_post...  \n\n")
        else:
            number+=number
    
        print("before go back")
        driver.back()
        print("after go back")
        driver.refresh()
            
    print("everything is good, you scalability is high",i)
    driver.find_element(by = By.LINK_TEXT,value="Afficher plus de publications").click()
        
    

print("\n\n-------------------------------- End of scraping --------------------------------",number)   


