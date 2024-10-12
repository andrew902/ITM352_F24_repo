#Debugging exercise # 5

def fibonacci(n):
    fibo_list = [0, 1]
    for i in range(2, n):
        fibo_list.append(fibo_list[-1] + fibo_list[-2])
    return fibo_list

n = 5
print(fibonacci(n))
