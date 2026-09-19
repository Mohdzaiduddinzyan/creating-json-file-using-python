import json

n= int(input("Enter number of objects: "))
f= int(input("enter number of fields: "))
l=[]

for i in range(n):
  d={}
  for j in range(f):
    k = input("Enter key: ")
    v= input("Enter value: ")
    d[k]=v
  d.append(d)
with open("sample.json","w") as f:
  json.dump(d,f)
