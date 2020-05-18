# Viết một chương trình tìm tất cả các số trong đoạn 1000 và 3000 (tính cả 2 số này)
# sao cho tất cả các chữ số trong số đó là số chẵn.
# In các số tìm được thành chuỗi cách nhau bởi dấu phẩy, trên một dòng.

values = []
def EvenNumber(value):
    if not int(i) % 2:
        return True
    else:
        return False
for i in range(1000,3001):
    s = str(i)
    if EvenNumber(s[0]) and EvenNumber(s[1]) and EvenNumber(s[2]) and EvenNumber(s[3]):
        values.append(str(i))

print(','.join(values))