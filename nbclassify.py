import sys,math,pickle,operator
from stemming.stemming.porter2 import stem

inputfile= sys.argv[1]
testfile= sys.argv[2]

main_dict={}
map_dict={}

#try:
finame=open(inputfile,'rb')
fintest=open(testfile,'r',encoding='utf-8',errors='ignore')
foname=open("output.txt",'w',encoding='utf-8',errors='ignore')
main_dict=pickle.load(finame)
map_dict=pickle.load(finame)
stop_word_list = ['a','an','and','are','as','at','be','but','by','for','if','in','into','is','it','of','on','or','s','such','t','that','the','their','then','there','these','they','this','to','was','will','with']
punc_list = ['.','?','!','@','\"','\,','*','#','$','(',')','-',':',';','[',']']
num_list = []
num_list = [0,1,2,3,4,5,6,7,8,9]

for line in fintest:
  list1=line.split()
  dict1={}
  for key,value in map_dict.items():
     val=main_dict[key]['PROB']
     for i in range(1,len(list1)):
      if list1[i] not in punc_list and stop_word_list and len(list1[i]) > 3 and list1[i] not in num_list :
        list1[i] = stem(list1[i]) 
        if list1[i] in main_dict[key]['WD']:
          val+=main_dict[key]['WD'][list1[i]]
        else:
          val+=main_dict[key]['NEW']
     dict1[key]=val
  maxValue=max(dict1.items(), key=operator.itemgetter(1))[1]
  
  for k,v in dict1.items():
    
    if v==maxValue:
      foname.write(k)
      print(k)
      foname.write('\n')  
            
#except:
 #   print ("Error in reading or writing file")
#finally:
finame.close()
fintest.close()
