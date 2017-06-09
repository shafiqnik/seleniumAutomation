import unittest
from selenium import webdriver
'''
Opens Audit log on Proudction
Changes the day to 15
Closes the browser.
'''

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re
import urllib.request


class PythonOrgSearch(unittest.TestCase):

    
    def setUp(self):
        self.driver = webdriver.Firefox()

     
        
    def test_search_in_python_org(self):
        
        driver = self.driver
        
        url = "http://localhost:8013/support/tools/model/?model=genxhspa6"
        openPage = driver.get(url)
        self.assertIn("Guardian Administration", driver.title)
        elem = driver.find_element_by_name("beacon_id")
        elem.send_keys("69391")

        #wp = urllib.request.urlopen(url)
        #pw = wp.read()
        #print(pw)
        
       '''  
        day = driver.find_element_by_name("fday")
        
        if(day):
            
            print('day is ', format(day.get_attribute('value')))
            day.clear()
            day.send_keys('15')
           
        else:
            print('didnt find fyr')
       '''     
        #elem.send_keys(Keys.RETURN)
        ##assert "No results found." not in driver.page_source
        
  
        #def mySearch(self, readPage):
        #web.read()
        '''
        print('inside mysearch method', web.read())
        searchit = re.search('first_fix', str(web.read()))
        if searchit:
            print('found the key word')
        else:
            print('couldnot find the keywork')     
        '''

'''
#the Search Function is not working, not sure why

    def Search(url,term):

        print(url)
    #driver.get(url)
    #wp = urllib.request.urlopen(url)
    #pw = wp.read()
    
    

        mySearch = re.search(term, url)#, re.M|re.I)
        if mySearch:
            print('found it')
        #print(str(pw))
       # print(getattr(pw))
        else:
            print('didnnot find it')
            
        #print(len(pw))
'''        
        
    def tearDown(self):
        #mySearch(web)
        print('it is working')
        #self.driver.close()
        


    
if __name__ == "__main__":
    unittest.main()
    

