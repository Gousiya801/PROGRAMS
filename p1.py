import csv
with open('trainingexamples.csv') as csvfile:
	data=[line for line in csv.reader(csvfile) if line[-1]=="Y"]
print("positive examples are {}".format(data))
S=['$']*len(data[0])
print("after every step value={}".format(S))
for example in data:
	i=0
	for feature in example:
		S[i]=feature if S[i]=='$' or S[i]==feature else '?'
		i+=1
	print(S)