vocale="AaEeIiOoUu"
x=0
with open("C:/Users/User/Desktop/xx.txt", 'r') as f:
    a=f.read()
with open('xy.txt', 'w') as f:
    for i in a:
        if i in vocale:
            f.write(i)
            x+=1
print('vocalele', x)