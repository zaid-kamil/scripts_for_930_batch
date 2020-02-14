from reader import read_file
import matplotlib.pyplot as plt

def visualize(file):
    vowels= 'aeiou'
    data = read_file(file).lower()

    results = {} # empty dict
    for v in vowels:
        size = data.count(v)
        results[v] = size

    x = list(results.keys())
    h = list(results.values())
    colors= ['red','blue','green','#ff8800','#9090ff']
    plt.bar(x,h,color=colors)
    plt.savefig('images/vowels_bar.png', bbox_inches='tight')

visualize('data/Richardson_Clarissa.txt')