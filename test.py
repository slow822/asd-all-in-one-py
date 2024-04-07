
def kt(a,x):
    for k in range(x,a+1):
        j = 'co'
        for i in range(2,k):
            if k%i == 0:
                j='ko'
        if j == 'co':        
            print(k)
m = int(input(""))
n = int(input(""))
d = kt(n,m)
if 1<m<n:
  print(d)
else:
    print('loi')