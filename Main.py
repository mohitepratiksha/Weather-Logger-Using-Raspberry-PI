print("Welcome to Weather Logger") 
print("--------------------------") 
print("Choose Your Option\n1:Collect Temperature Data\n2:Collect Humidity Data\n3:Collect Atmospheric Pressure Data\n4:Display all Data\n") 
x=int(input()) 
if x==1: 
import collectweather 
elif x==2: 
import collecthumidity 
elif x==3: 
import collectpressure 
elif x==4: 
import display 
else: 
print("Wrong Option!!") 
