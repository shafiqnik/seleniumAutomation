from selenium import webdriver


class myPage(object):

	farm = 'staging'

	def __init__(self,url,pname,uname,pword):
		self.url = url
		self.pname = pname
		self.uname = uname
		self.pword = pword
		
		browser=webdriver.Firefox()
		browser.get(url)	
	
        
t1 = myPage('beta.cp.contigo.com','','','')
