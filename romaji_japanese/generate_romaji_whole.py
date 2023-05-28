def generate_romaji_50():
    lst = []
    vowels = ['a','i','u','e','o']
    b = ['','k','s','t','n', 'h','m', 'y','r','w']
    for e in b:
        front = e
        for v in vowels:
            second = v

            word = front + second
            lst.append(word)
    lst[11] = "shi"
    lst[16] = "chi"
    lst[17] = "tsu"
    lst[27] = 'fu'
    del lst[36]
    del lst[37]
    del lst[44]
    del lst[44]
    del lst[44]
    lst.append('n')
    return lst

def generate_rest(): 
    lst =  []
    vowels = ['a','i','u','e','o']
    b = ['g','z','d','b','p']
    for e in b:
        front = e
        for v in vowels:
            second = v
            if (front == 'z' or front == 'd'):
                if second == 'i':
                    word = 'j' + second
                elif second == 'u':
                    word = 'z' + second
                else:
                    word = front + second
                    
            else:
                word = front + second
            lst.append(word)
    return lst

def generate_poly():
    lst = []

    front = ['g','b','p','k','n','h','m','r']
    back = ['ya','yu','yo']
    for e in front:
        first = e
        for b in back:
            second = b
            word = first + second
            lst.append(word)
    return lst

def generate_special_poly():
    lst = []
    front = ['j','sh','ch']
    back = ['a','u','o']

    for e in front:
        first = e
        for b in back:
            second = b
            word = first + second
            lst.append(word)
    return lst


def generate_whole():
    lst = generate_romaji_50() + generate_rest() + generate_poly() + generate_special_poly()
    lst[44] = "(w)o"
    return lst
            
    
    
