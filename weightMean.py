import pandas
import csv
with open("SOCR-HeightWeight.csv",newline="")as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
weight=[]
for i in file_data:
    num= i[2]
    weight.append(float(num)) 
totalnum=len(weight)
sum=0
for x in weight:
    sum = sum+x
mean = sum/totalnum
print(mean)    