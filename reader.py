
def read_file(path):
    f = open(path) 
    d = f.read()
    f.close()
    return d

def count_word_in_file(word,path):
    data = read_file(path).lower()
    return data.count(word)



# data = read_file('data/Richardson_Clarissa.txt')
# print(data[:1000].split()) # 200 chars only, we dont need to see the whole file

# print("Clarissa = ",count_word_in_file('clarissa',file))
# print(count_word_in_file('the',file))
# print(count_word_in_file('hello',file))

def count_vowels(file):
    data = read_file(file).lower()
    vowels = 'aeiou'
    total_vowels = 0 
    for v in vowels:
        total_vowels+= data.count(v)
    return total_vowels


# file ='data/Richardson_Clarissa.txt'
# vowels = count_vowels(file)
# print('total vowels == ',vowels)