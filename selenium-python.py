'''
Loads the beta page and logs in
NOT WORKING
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from myPy import myFile

class mypage(object):

      
    def __init__(self, page, pname,uname,pword):

        self.page = page
        self.pname = pname
        self.uname = uname
        self.pword = pword
 
    def openUrl(page):
        browz = webdriver.Firefox()
        openPage = browz.get(page)

               


 '''

import unittest
from selenium import webdriver




def openUrl(page):   
    driver = webdriver.Firefox()
    openPage = driver.get(page)



def login(pname,uname,pword):
    
    '''inputElement = browser.find_element_by_name('pname')
    inputElement.send_keys(pname)
    inputElement = browser.find_element_by_name('uname')
    inputElement.send_keys(uname)
    inputElement = browser.find_element_by_name('pword')
    inputElement.send_keys(pword)
    inputElement.send_keys(Keys.RETURN)

'''    
openUrl("http://beta.cp.contigo.com")












    
    def loadpage(p,pname,uname,pword):

        #browz = webdriver.Firefox()
        
        myinput = browz.find_element_by_name('pname')
        myinput.send_keys(pname)
        myinput = browz.find_element_by_name('uname')
        myinput.send_keys(uname)
        myinput = browz.find_element_by_name('pword')
        myinput.send_keys(pword)
        myinput.send_keys(Keys.RETURN)
                




m = mypage("http://beta.cp.contigo.com", "beta","qatest","test")
mypage.loadpage(m.page, m.pname, m.uname, m.pword)
               
 '''

#m = mypage("http://beta.cp.contigo.com", "beta","qatest","test")
   
