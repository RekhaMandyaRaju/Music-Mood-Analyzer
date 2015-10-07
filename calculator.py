import sys
import os

actfilelist = open(sys.argv[1],"r").read().split("\n")
predfilelist = open(sys.argv[2],"r").read().split("\n")
count = {}
counter = 0

for i in range(len(actfilelist)-1):
	namea = actfilelist[i]
	namep = predfilelist[i]
	
	if namea:

		if namea not in count:
			count[namea] = {}
			count[namea]["correctly_counted"]=0
			count[namea]["classified_as"]=0
			count[namea]["belongs_to"]= 0
		count[namea]["belongs_to"]= count[namea]["belongs_to"] + 1

		if namep not in count:
			count[namep] = {}
			count[namep]["correctly_counted"]=0
			count[namep]["classified_as"]=0
			count[namep]["belongs_to"]=0   
		count[namep]["classified_as"] = count[namep]["classified_as"] + 1

		if actfilelist[i] == predfilelist[i]:
			#count = count + 1
			count[namea]["correctly_counted"] = count[namea]["correctly_counted"] + 1

#print(count/len(predfilelist));

for i in count:
	
	print("correctly counted = "+str(count[i]["correctly_counted"]))
	print("belongs to = "+str(count[i]["belongs_to"]))
	print("classified as = "+str(count[i]["classified_as"])+"\n")
	prec=(count[i]["correctly_counted"]/count[i]["classified_as"])
	print("precision = "+str(prec)+"\n")
	recall=(count[i]["correctly_counted"]/count[i]["belongs_to"])
	print("recall = "+str(recall)+"\n")
	fscore=(2* prec *recall)/(prec+recall);
	print("fscore = "+str(fscore)+"\n")

