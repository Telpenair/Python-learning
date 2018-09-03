#готовимся тасовать колоду
from random import shuffle
#from b_classes import generator
#from b_classes import box
from b_classes import prisoner
from b_classes import percent_counter

#следим за временем
import time
start_time = time.time()

nob = 100
quan_prisoner = nob

quan_tries = int(nob/2)
quan_global_tries = nob * 10
print("Количество попыток: %d" % quan_global_tries)

class generator:
    def __init__(self,nob):
        self.nob = nob
        
    def generate(self):
        label_list = list(range(self.nob))
        shuffle(label_list)
        return label_list
    
class box:

    def __init__ (self,listlabels,nb):
        #тасованый список бумажек
        self.listlabels = listlabels
        #номер коробки
        self.nb = nb
        
    #возвращаем по номеру коробки номер бумажки
    def label_number(self):
        return self.listlabels[self.nb]


percent_counter_1 = percent_counter(quan_global_tries,quan_prisoner,quan_tries,nob)
a = percent_counter_1.percent()
print ('Кол-во успешных попыток ', a, ((a/quan_global_tries)*100), '%%')

print("Вермя выполнения расчётов %s ms" % ((time.time() - start_time)*1000))
