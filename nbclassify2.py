import sys,pickle,operator
from stemming.stemming.porter2 import stem


def classify_song(song) :
   song = song.replace('\n',' ')
   
   # hardcode the path of model file
   inputfile = 'model'
   main_dict={}
   map_dict={}
   mood_rank_dict = {}
   finame=open(inputfile,'rb')
   main_dict=pickle.load(finame)
   map_dict=pickle.load(finame)
   stop_word_list = ['a','an','and','are','as','at','be','but','by','for','if','in','into','is','it','of','on','or','s','such','t','that','the','their','then','there','these','they','this','to','was','will','with']
   punc_list = ['.','?','!','@','\"','\,','*','#','$','(',')','-',':',';','[',']']
   num_list = []
   num_list = [0,1,2,3,4,5,6,7,8,9]

   list1=song.split()
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
   mood_rank_list = sorted(dict1.items(), key=operator.itemgetter(1), reverse=True) 
   i = 1
   
  
   for j in range (0,len(mood_rank_list)):
       mood_rank_dict[mood_rank_list[j][0]] = i 
       i += 1
   
   finame.close()
   return mood_rank_dict

if __name__ == "__main__" :
      dict1 = {}
      song = "Imagine if we could go back Actually talk to the motherfuckers that persevered (hehehe) I mean the first motherfuckers that came in the slave ships (Hey, excuse me, excuse me) Y'know? (Look) (2Pac) We back for everything you owe, no longer oppressed Cause now we overthrow those that placed us in this rotten mess But let's agree on strategy and pick out enemies right Who stands accused of the abuse my own, kind do right Pardon, not disregardin what you thinkin but you musta been the ship Cause once I rip your whole shit is sinkin Supreme ideology, you claim to hold Claimin that we all drug dealers with empty souls That used to tempt me to roll, commit to violence In the midst of an act of war, witnesses left silent Shatter, black talon style, thoughts I throw It remains in your brain then of course it grows Maybe, even your babies can produce and rise Picture a life where black babies can survive past five But we must have hope, quotin the reverand from the pulpit Refuse to turn the other cheek we must defeat the evil culprit Lace me with words of destruction and I'll explode But supply me with the will to survive, and watch the world grow This ain't bout talkin bout problems, I bring solutions Where's the restitution, stipulated through the constitution You violated, now I'm back to haunt your nights Listen to the screams, of the lives you sacrificed And in case you don't know, ghetto born black seeds still grow We comin back, for everything you owe (Chorus: sung) I'm comin collectin the shit that belong to me Motherfuckers are runnin and duckin I'm a crazy nigga on a mission wit a bad mentality Armed with missiles guns grenades Pull out the pin, free I'm comin (2Pac over Chorus) How do you plead Mr. Shakur, how do you plead? How do I plead? Yes sir, how do you plead? Shit, you know how I plead C'mon!! Psssh (2Pac) Not guilty on the grounds of insanity it was them or me Bustin at my innocent family, say they lookin for ki's I was home alone, blind to the prelude Bust in, talkin bout, Where is the quaaludes? What you say fool? Where in the hell is the search warrant? No feedback is what he uttered, before he screamed Nigga motherfucker Dropped me to my knees I proceed to bleed Sufferin a rain of blows to my hands and knees Will I survive, is God watchin? I grab his gat and bust in self - defense, my only option, God damn Now they got me goin to the county jail And my family can't pay this outrageous bail Try to offer me a deal, they told me if I squeal Move me, and my people, to a mansion in Brazil Not me, so this is how it ends, no friends I'll be stressed and they just, reposessed my Benz Told the judge it was self - defense, he won't listen So I'm bumpin this in federal prison, givin everything I owe (Chorus - 2X) "
      
      dict1 = classify_song(song2)
      print(dict1)

