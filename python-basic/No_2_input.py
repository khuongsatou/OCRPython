# Viết một chương trình có thể tính giai thừa của một số cho trước.
# Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy.
# Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.

mInput =int(input("(Example: (n+1)!= n!*(n+1)  condition: n > 0 )Input key:"));

def fact(x):
    if x==0 :
        return 1
    return x * fact(x-1)

print("Result:"+str(fact(mInput)))