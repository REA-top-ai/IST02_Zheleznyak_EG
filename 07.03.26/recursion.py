#Задание 1
def factorial(n: int):
    if n == 1:
        return 1
    return n*factorial(n-1)
print(factorial(int(input())))
def factorial2(n: int):
    ck = 1
    for i in range(1, n+1):
        ck *= i
    return ck
print(factorial2(int(input())))


#Задание 2
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def kv(arr):
    new_arr = []
    for i in arr:
        new_arr.append(i**2)
    return new_arr
print(kv(arr))