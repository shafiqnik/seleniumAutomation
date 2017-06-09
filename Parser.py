from html.parser import HTMLParser
import re

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    #def handle_starttag(self, tag, attrs):
       # print ("Encountered a start tag:", tag)

    #def handle_endtag(self, tag):
        #print ("Encountered an end tag :", tag)

    def handle_data(self, data):

        search = re.match('HOS', data)
        if(search):
            print(HTMLParser.get_starttag_text(self))
            print ("Encountered some data  :", data)
        

# instantiate the parser and fed it some HTML
#parser = MyHTMLParser()
#parser.feed('<html><head><title>Test</title></head>'
            #'<body><h1>Parse me!</h1></body></html>')
