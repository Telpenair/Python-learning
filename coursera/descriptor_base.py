# this exercise made me crazy
# need more accuracy with obj in __set__ input

class Value:
    def __init__(self, commission):
        self.commission = commission
        self.amount = None
        
        # print(self.amount)
        # print(self.commission)
    
    def __get__(self, obj, obj_type):
        return self.amount
    
        # print(self.commission)
        # print(self.amount)
    
    def __set__(self, obj, value):
        self.amount = value - value * self.commission
        
        # print(self.amount)

if __name__ == "__main__": 

    class Account:
        amount = Value()
        
        def __init__(self, commission):
            self.commission = commission

    new_account = Account(0.1)
    new_account.amount = 100

    print(new_account.amount)

