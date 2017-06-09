from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

class OpenUrl():
    
    driver = webdriver.Firefox()
    
    def __init__(self):
        
        
        print('opening a webpage')
        return None

    def logIn(self, url, loginname, password):
        driver = self.driver
        driver.get(url)
        
        uname = self.driver.find_element_by_name('uname')
        uname.send_keys(loginname)
        pword = self.driver.find_element_by_name('pword')
        pword.send_keys(password)
        pword.send_keys(Keys.RETURN)
        print('logIn')

a = OpenUrl()
a.logIn('http://beta.cp.contigo.com','qatest','test')


    
