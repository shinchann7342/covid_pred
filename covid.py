import pandas as pd #importing packages
import matplotlib.pyplot as plt
csv_file='data.csv'  #initialize the csv file
data = pd.read_csv(csv_file)    #reads the csv file
Date = data["date"]     #lists for storing the elements of the csv file
New = data["daily new"] #
x=[]    
y=[] 
x=list(Date)
y=list(New)
temp=[] #temproary list for processing the data of last 10 days
i=len(y)-10
while(i<len(y)):
    temp.append(y[i]/(y[i-1])) #mathematical equation for growth rate (current value/previous value)
    i=i+1
growth=sum(temp)/len(temp) #average growth rate
print("Growth rate:",growth)
dd=float(input("Enter the number of days:")) #getting the input of number of days we want to predict
last=y[-1]
pred=last*(growth)**dd #equation for prediction(last known value)X(growth rate)^number of days
pred=int(pred) #converting the float value to int value
print("As of the given number of days the count will be:",pred)
plt.plot(x,y) #code for plotting of the existing data
plt.xlabel('Date')
plt.ylabel('new cases')
plt.title('covid data')
plt.show()