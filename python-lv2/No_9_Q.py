# Viết chương trình và in giá trị theo công thức cho trước:
# Q = √([(2 * C * D)/H]) (bằng chữ: Q bằng căn bậc hai của [(2 nhân C nhân D) chia H].
# Với giá trị cố định của C là 50, H là 30. D là dãy giá trị tùy biến
# , được nhập vào từ giao diện người dùng
# , các giá trị của D được phân cách bằng dấu phẩy.
#
# Ví dụ: Giả sử chuỗi giá trị của D nhập vào là 100,150,180 thì đầu ra sẽ là 18,22,24.
import math

#seft
# mInput = input("Key value D:")
# C,H = 50,30
# arr = []
# def calcQ(D):
#     q = math.sqrt((2*C*D)/H)
#     return q
#
# def slipInput(value):
#     arr = value.split(",")
#     return arr
#
# item = slipInput(mInput)
# print(slipInput(mInput))
#
# s=[]
# for i in item:
#     s.append(str(round(calcQ(float(i)))))
#
# print(",".join(s))

#gg
c=50
h=30
value = []
items = [x for x in input("Nhập giá trị:").split(",")]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d) /h )))))

print(",".join(value))

