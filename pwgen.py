import random

class password_gen:

    def __init__(self, upper, number, symbol, length):
        
        UPPER = char_set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        NUM = char_set('0123456789')
        SYMBOLS = char_set('!@#$%^&*()-=_+,.<>/?')
    
        self.pool = [char_set(UPPER.getSet().lower())]

        if upper:
            self.pool.append(UPPER)
        if number:
            self.pool.append(NUM)
        if symbol:
            self.pool.append(SYMBOLS)
        for k in self.pool:
            k.updateData(1.0/len(self.pool))
        
        self.length = length
        self.password = ''

    def __str__(self):
        return self.password

    def generate(self):
        self.password = ''
        if(self.length >= len(self.pool)):
            while len(self.password) < self.length:
                threshold = random.random()
                z = self.count_zero()
                val = 0
                cs = None
                for k in self.pool:
                    val += k.getData()
                    if val > threshold:
                        cs = k
                        self.password += cs.getSet()[random.randint(0,len(k.getSet())-1)]
                        break
                new_weight = cs.getData() * (1.0/(self.length-len(self.pool)+1))
                for k in self.pool:
                    if k == cs:
                        k.updateData(k.getData()-new_weight)
                    else:
                        if(not k.getData() == 0.0):
                            k.updateData(k.getData()+(new_weight/(len(self.pool)-z-1)))
            return True
        else:
            return False
    
    def count_zero(self):
        count = 0
        for k in self.pool:
            if k.getData() == 0.0:
                count += 1
        return count

class char_set:
    
    def __init__(self, cs, data = 0.0):
        self.key = cs
        self.info = {self.key:data}
    
    def __str__(self):
        return str(self.info)
    
    def getData(self):
        return self.info.get(self.key)
    
    def getSet(self):
        return self.key
    
    def updateData(self,data):
        self.info[self.key] = data

p = password_gen(True,True,True,12)

try:
    num_pw = int(input('How many passwords to generate? '))
except Exception:
    num_pw = 999
for i in range(num_pw):
    
    p.generate()
    print (p)
    
    something = input('Type \'q\' or \'quit\' to exit')
    if something == 'quit' or something == 'q':
        break