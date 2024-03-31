
m = float(input("nhap: "))
kg = float(input("nhap: "))

bmi = kg/(m*m)
if bmi < 16:
    print('gay cap 3')
elif bmi <17:
    print('gay cap 2')
elif bmi <18.5:
    print('gay cap 1') 
elif bmi <25:
    print('binh thuong') 
elif bmi <30:
    print('thua can') 
elif bmi <35:
    print('beo cap 1') 
elif bmi <40:
    print('beo cap 2') 
else:
    print('beo cap 3') 
    