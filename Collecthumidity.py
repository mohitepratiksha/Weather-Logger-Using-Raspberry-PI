from sense_hat import * 
from time import sleep 
sense = SenseHat() 
while True: 
myfile = open('humidity.txt', 'a') 
myfile.write(sense.humidity) 
myfile.write('\n') 
myfile.close() 
sleep(5) 
collectpressure.py 
from sense_hat import * 
from time import sleep 
sense = SenseHat() 
while True: 
myfile = open('atmpressure.txt', 'a') 
myfile.write(sense.pressure) 
myfile.write('\n') 
myfile.close() 
sleep(5) 
display.py 
import pygal
temp = [] 
humid=[] 
pressure=[] 
file = open('weather.txt', 'r') 
file1 = open('humidity.txt','r') 
file2 = open('atmpressure.txt','r') 
for line in file.read().splitlines(): 
if line: 
temp.append( float(line) ) 
file.close() 
for line in file1.read().splitlines(): 
if line: 
humid.append( float(line) ) 
file1.close() 
for line in file2.read().splitlines(): 
if line: 
pressure.append( float(line) ) 
file2.close() 
weatherchart = pygal.Bar() 
weatherchart.title = 'Weather' 
weatherchart.x_labels = range(1, len(temp) + 1) 
weatherchart.add('temp', temp)
weatherchart.add('humid',humid) 
weatherchart.add('pressure',pressure) 
weatherchart.render() 
