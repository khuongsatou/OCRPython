# Viết một chương trình chấp nhận đầu vào là chuỗi các số nhị phân 4 chữ số, phân tách bởi dấu phẩy,
# kiểm tra xem chúng có chia hết cho 5 không.
# Sau đó in các số chia hết cho 5 thành dãy phân tách bởi dấu phẩy.
#
# Ví dụ đầu vào là: 0100,0011,1010,1001
#
# Đầu ra sẽ là: 1010

value = []
items = [x for x in input("Nhập các số nhị phận:").split(",")]
for i in items:
    print(i)
    intp = int(i,2)
    print(intp)
    if not intp %5:
        value.append(i)

print(','.join(value))