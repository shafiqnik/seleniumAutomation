import os
import Car

class myFile(object):
    
  

    def __init__(self):

        d = os.getcwd()
        #print(d)
        x = os.chdir('c:\\')
        print(os.path.getsize(d))
        gnx = open('C:\\Users\\sahmad\\Desktop\\9.9.0\\gnx6.txt')
        myfile = gnx.readlines()
        sound = Car.mustang
        
        print(myfile)
#help(dir(os))

m=myFile()
print(' first part of the file ',type(m))
