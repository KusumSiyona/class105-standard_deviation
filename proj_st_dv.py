import csv
import math

with open("prij_data.csv", newline = "") as f:
    reader = csv.reader(f)
    file_data = list(reader)

data= file_data[0]
print(data)

def mean(data):
    n = len(data)
    total = 0
    for x in data :
        total = total + int(x)

    mean = total/n
    return mean

squared_list  = []
for num in data:
    a = int(num) - mean(data)
    a = a**2
    squared_list.append(a)

sum = 0
for sum in squared_list:
    sum = sum + a

result = sum/(len(data)-1)

st_dv = math.sqrt(result)
print(st_dv)





