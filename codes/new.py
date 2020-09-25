#参数前面加一个*，表示是可变参数
def add(*args): 
    total=0
    for val in args:
        total += val
    return total

print(add())
print(add(1,))
print(add(5,4))
print(add(5,4,9,10,11))