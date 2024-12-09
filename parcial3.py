a=25000000
b=18900000
año = 2022
while (a>b):
    a = ((a*0.02)+a)
    
    b = ((b*0.03)+b)
    año =año+1
print ("La poblacion B superara a la A en el año:",año)