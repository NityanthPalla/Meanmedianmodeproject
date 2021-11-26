
import csv
with open("SOCR-HeightWeight.csv",newline="")as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
weight=[]
for i in file_data:
    num= i[2]
    weight.append(float(num)) 
n=len(weight)
weight.sort()
if n % 2== 0:
    m1=float(weight[n//2])
    m2=float(weight[n//2-1])
    median=(m1+m2)//2
else:
    median=float(weight[n//2-1])
print(median)