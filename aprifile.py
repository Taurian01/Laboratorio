import datetime
a = open('shampoo_sales.csv','r')
b = []
for line in a:
    x = line.split(',')
    if x[1] != 'Val\n':
        c=float(x[1])
        b.append(c)
print(b)
a.close()