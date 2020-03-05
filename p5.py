import csv
import math

def mean(numbers):
	return sum(numbers)/float(len(numbers))

def stdev(numbers):
	avg=mean(numbers)
	variance=sum([pow(avg-x,2) for x in numbers])/float(len(numbers)-1)
	return math.sqrt(variance)

def summarize(dataset):
	summaries = [(mean(attribute), stdev(attribute)) for attribute in zip(*dataset)]
	del summaries[-1]
	return summaries

def calcprob(summary,item):
	prob=1
	for i in range(len(summary)):
		x=item[i]
		mean,stdev=summary[i]
		exponent=math.exp(-math.pow(x-mean,2)/(2*math.pow(stdev,2)))
		final=exponent/(math.sqrt(2*math.pi)*stdev)
		prob*=final
	return prob	

yes=[]
no=[]

with open('ConceptLearning.csv') as csvfile:
	data=[line for line in csv.reader(csvfile)]
for i in range(len(data)):
	data[i]=[float(x) for x in data[i]]

train=[]
test=[]
split=int(0.60*len(data))
train=data[:split]
test=data[split:]
print("{} input rows is split into {} training and {} testing datasets".format(len(data), len(train), len(test)))
print("\nThe values assumed for the concept learning attributes are\n")
print("OUTLOOK=> Sunny=1 Overcast=2 Rain=3\nTEMPERATURE=> Hot=1 Mild=2 Cool=3\nHUMIDITY=> High=1 Normal=2\nWIND=> Weak=1 Strong=2")
print("TARGET CONCEPT:PLAY TENNIS=> Yes=10 No=5")
print("\nThe Training set are:")
for x in train:
	print(x)
print("\nThe Test data set are:")
for x in test:
	print(x)

for i in range(len(train)):
	if data[i][-1] == 5.0:
		no.append(data[i])
	else:
		yes.append(data[i])
yes=summarize(yes)
no=summarize(no)
predictions=[]
for item in test:
	noprob=calcprob(no,item)
	yesprob=calcprob(yes,item)
	predictions.append(5.0 if noprob>yesprob else 10.0)
print("actual prob=")
for i in test:
	print(i[-1])
print("predicted prob=")
for i in predictions:
	print(i)
correct=0
for i in range(len(test)):
	if test[i][-1]==predictions[i]:
		correct+=1
print("accuracy={}%".format(float(correct/float(len(test)/100))))
