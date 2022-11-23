"""
contains the order class and other related functions
"""

class Order:
    #each Product
    def __init__(self,customer_name, customer_address, customer_phone,status,contents,courier):
        self.name = customer_name
        self.address = customer_address
        self.phone = customer_phone
        self._status = status
        self._contents = contents
        self._courier = courier
        self.dic = vars(self).copy()
        self.status_options = ['preparing','prepared', 'delivering', 'delivered']
        
    
    
    
    
    
  #Making status a property  
    @property 
    def status(self):
        print('Getting status')
        return self._status
    
    @status.setter
    def status(self,value):
        print('setting value')
        if value not in self.status_options:
            print('not a valid status')
        self._status = value
    

    


