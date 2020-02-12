def fibonacci(seq,size):
    for i in range(size):
        seq.append(seq[-1] + seq[-2])
    return seq

def fibonacci2(a,b,size):
    f = [a,b]
    for i in range(size):
        f.append(f[-1] + f[-2])
    return f

# calling
print(fibonacci([13,5], 6))

res = fibonacci2(0,1,10)
print(res)

res = fibonacci2(a=4,b=6,size=10)
print(res)
