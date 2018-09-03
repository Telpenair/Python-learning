from random import shuffle

#в итоге нам нужно получить процент успеха
#для начала считаем количество успешных попыток за одну итерацию
#игры с вложенными атрибутами для вложенных классов уже начались
class prisoner:
    def __init__ (self,quan_prisoner,quan_tries,listlabels):
        self.quan_tries = quan_tries
        self.quan_prisoner = quan_prisoner
        self.listlabels = listlabels

    def tries (self):
        quan_success = 0
        for k in range(self.quan_prisoner):
            n = k
            i = 0
            while i <= self.quan_tries:
                bln = box(self.listlabels, n)
                if  bln.label_number() == k :
                    quan_success += 1
                    i = self.quan_tries
                n = bln.label_number()
                i += 1         
        return quan_success == self.quan_prisoner

#здесь получилось уж очень много входных данных переданных от вложенных классов
#наверняка можно сделать проще
class percent_counter:
    def __init__(self,quan_global_tries,quan_prisoner,quan_tries,nob):
        self.quan_global_tries = quan_global_tries
        self.quan_prisoner = quan_prisoner
        self.quan_tries = quan_tries
        self.nob = nob

    def percent(self):
        quan_success_run = 0
        for i in range(self.quan_global_tries):
            listlabels = generator(self.nob)
            llg = listlabels.generate()
            pt = prisoner(self.quan_prisoner,self.quan_tries,llg)
            quan_success_run += pt.tries()
        return quan_success_run
