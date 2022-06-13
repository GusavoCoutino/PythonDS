import random
dict = {}
def random_num():
    for i in range(30):
        n = random.randint(1, 53)
        if n in dict.keys():
            while n in dict.keys():
                 n = random.randint(1, 53)
                 
            print(i+1,n)
        elif n not in dict.keys():
            dict[n] = 1
            print(i+1,n)

random_num()
        
