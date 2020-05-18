# Viết một chương trình chấp nhận chuỗi là các dòng được nhập vào,
# chuyển các dòng này thành chữ in hoa và in ra màn hình.
# Giả sử đầu vào là:
#
# Hello world
# Practice makes perfect
#
# Thì đầu ra sẽ là:
#
# HELLO WORLD
# PRACTICE MAKES PERFECT

# input_str = [x for x in input("KEY:").split(',')]
# arr = []
# for c in input_str:
#     arr.append(c.upper())
# print(''.join(arr))

lines = []
while True:
   s = input()
   if s:
      lines.append(s.upper())
   else:
      break;
# Bài Python 12, Code by Quantrimang.com
for sentence in lines:
    print (sentence)