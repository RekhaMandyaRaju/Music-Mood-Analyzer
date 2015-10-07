import os,glob,sys
inputdir= sys.argv[1]
outputfile= sys.argv[2]
angry_count = 0
relax_count = 0
happy_count = 0
romantic_count = 0
sad_count = 0
try:
   foname=open(outputfile,'w')
   for root, dirs, files in os.walk(inputdir):
       files.sort()
       for file in files:
        # if glob.fnmatch.fnmatch(file, '*'):
            name=file.split('_')
            if name[0] == 'angry':
                angry_count += 1
            if name[0] == 'relax':
                relax_count += 1
            if name[0] == 'happy':
                happy_count += 1
            if name[0] == 'sad':
                sad_count += 1
            if name[0] == 'romantic':
                romantic_count += 1                        
            foname.write(name[0])
            foname.write(' ')
            try:
             inputfile=os.path.join(root,file)
             finame=open(inputfile,'r',encoding='UTF-8',errors='ignore')
             for line in iter(finame):
                foname.write(line.lower().rstrip('\n'))
                foname.write(' ')
             foname.write('\n')
            except IOError:
             print ('Error while reading from file') 
            finally:
             finame.close()
   print(angry_count)
   print(happy_count)
   print(relax_count)
   print(romantic_count)
   print(sad_count) 
               
except IOError:
     print ('Error while writing into file') 
finally:
 foname.close()
 
