""""
Depriciated file
"""

import os 
import pickle
os.system("clear")
#makes a Files class
class Files:
    def __init__(self,name):
        #creates an attripute for the path
        self.path = f"{name}.dat"
    #method to write data
    def write(self,data):
        pickle.dump(data,open(self.path,'wb'))
    #method to read data
    def read(self):
        return pickle.load(open(self.path,'rb'))








    
    

