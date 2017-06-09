#opens audit log and inputs data
#reads and prints data of audit log
# source https://docs.python.org/3/howto/urllib2.html#urllib-howto

import urllib.request
import urllib.parse
import time
import datetime
from datetime  import date
import re
import Parser
import OpenUrl
from bs4 import BeautifulSoup

'''
req = urllib.request.Request('http://beta.cp.contigo.com')
with urllib.request.urlopen(req) as response:
   the_page = response.read()
print(the_page)

'''
'''
local_filename, header = urllib.request.urlretrieve('http://beta.cp.contigo.com')
html = open(local_filename)
print(html.read())
'''

class AuditLog():
    

   
    #myurl = 'http://localhost:8013/developer/misc/audit_log/gprs_extract.php'
    def auditLogDate(year, month, day, yesterday):
    
        bid = '69391'
        url = 'http://localhost:8013/developer/misc/audit_log/gprs_extract.php'
        values = {'bid':bid,
                  'esn':'359486060202403',
                  'serial_no':'000036001261',
                  'fyr':year,
                  'fmth':month,
                  'fday':yesterday,
                  'fhr':'00',
                  'fmin':'59',
                  'tyr':year,
                  'tmth':month,
                  'tday':day,
                  'thr':'00',
                  'tmin':'59'}
                  
        data = urllib.parse.urlencode(values)
        data = data.encode('ascii')
        req = urllib.request.Request(url,data)
        with urllib.request.urlopen(req) as response:
            the_page=response.read()
            return the_page
    
    def mSearch(page):
        mySearch = re.findall('DIAG HOS', page, re.M)
        soup = BeautifulSoup(page, 'html.parser')
        #print(soup.get_text())
        
        #print(soup.prettify())   #BeautifulSoup is not working.....
        print("found hos.......", soup.find_all(string="HOS:"))
        print("found from html.......", soup.html.find_all('<td>HOS:'))
        
        if mySearch:

            print('found the term', mySearch)
            #print('next to it is ', soup.find_next_sibilings(mySearch))
        else:
            print('couldnot find it')

    
    
    month = time.strftime('%m')
    year = time.strftime('%Y')
    day = time.strftime('%d')
    print(day)
    currentMiniute = str(time.strftime('%M'))

    yesterday = (str(int(day)-1))
    print(yesterday)

    #htmlPage = auditLogDate(year,month,day, yesterday)
    page = str(auditLogDate(year,month,day, yesterday))
    mSearch(page)

    print(str(time.strftime('%Y:%M:%H:%M')))
    parser = Parser.MyHTMLParser() #instantiating Parser class
    parser.feed(page) #parses through the html data and printout
    print(parser.handle_starttag())
    print(type(page))
   # a = OpenUrl()
    #a.logIn('http://beta.cp.contigo.com','qatest','test')


    

def mSearch(page):
    mySearch = re.search('HOS:', page)
    if mySearch:
        print('found the term HOS')
    else:
        print('couldnot find it')


myAudit = AuditLog() #calling the Audit log class

        

