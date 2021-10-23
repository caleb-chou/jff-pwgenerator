import random
import math

class Password:

    # Defining character sets
    ALPHA   = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    NUMBERS = '1234567890'
    SYMBOLS = '!@#$%^&*()-_=+,<.>/?;:\'"[{]}\|'

    '''
    Creating pool for characters
    User can decide what character sets they want to use
    Pool is list of dictionaries, each dictionary has a character set
    and weight, weight is used to guarantee that the specified characters will 
    be present in the password
    '''
    POOL = [
        {
            'chars': ALPHA.lower(),
            'weight': 0.,
        },
    ]

    # Constructor, will create password based on args
    def __init__(self, length: int=8, upper: bool=True, num: bool=True, sym: bool=False, extra: str='') -> None:
        if upper:
            self.POOL.append({
                'chars': self.ALPHA,
                'weight': 0.,
            })
        if num:
            self.POOL.append({
                'chars': self.NUMBERS,
                'weight': 0.,
            })
        if sym:
            self.POOL.append({
                'chars': self.SYMBOLS,
                'weight': 0.,
            })

        # Set initial weights
        for i in self.POOL:
            i['weight'] = 1. / len(self.POOL)
        self.generate(length)
    
    # toString method, returns password
    def __str__(self) -> str:
        return self.password

    # Generate method
    def generate(self,length) -> None:
        self.password = ''

        # Generates password of <length>
        for i in range(length):

            # Random roll to determine what character is used
            roll = random.random()

            # Iterate over pool, once the roll is less than 0, picks char set
            for s in range(len(self.POOL)):

                # Decrease roll until < 0
                roll -= self.POOL[s]['weight']

                # Once choice is made, pick a character from the char set
                if roll < 0:
                    self.password += random.choice(self.POOL[s]['chars'])

                    # Calculate weight difference, rounded to make sure there are no edge cases with weird rounding
                    weight_diff = math.ceil(10000 * self.POOL[s]['weight'] / (length - i - len(self.POOL) + 1)) / 10000

                    # Decrease current char set weight
                    self.POOL[s]['weight'] -= weight_diff

                    # If the weight is 0, remove from the pool
                    if self.POOL[s]['weight'] <=0:
                        self.POOL.pop(s)

                        # Update weights
                        for o in self.POOL:
                            o['weight'] += weight_diff / (len(self.POOL))
                    
                    # If weight is not 0, just update weights of others
                    else:
                        for o in self.POOL:
                            if not o == self.POOL[s]:
                                o['weight'] += weight_diff / (len(self.POOL) - 1)
                    break

p = Password(3,True,True,False)
print(p)