#Authors: Peter Nguyen
#Assignment: Project #3
#Completed (or last revision): 11/01/2022

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
userInputOpenFile = input("Please enter the file you would like to open to make a word cloud: ")
#task 1
try:
     file = open(userInputOpenFile, 'r')
     text = [word.replace(",", "").replace(".", "") for line in file for word in line.lower().split()]
     print(text)
     freq = {}
     def CountFrequency(my_list,freq):
 
          freq = freq
          for item in my_list:
               if (item in freq):
                    freq[item] += 1
               else:
                    freq[item] = 1

          for key, value in freq.items():
               print((key, value))
          return freq
     CountFrequency(text,freq)
     # MyData= {u'arbeid': 0.0006715695865686539,
     #  u'banen': 0.00066821988636323406,
     #  u'begrotingsherstel': 0.00071106447864468028,
     #  u'belastingplan': 0.00064287666559415511,
     #  u'bestuursakkoord': 0.00085938678272561703,
     #  u'duurzame': 0.00086622249359887991,
     #  u'energie': 0.00071735256545447078,
     #  u'energievoorziening': 0.00091959448177479836,
     #  u'europa': 0.00077342364155819174,
     #  u'inkomens': 0.00086651160197001511,
     #  u'kabinet': 0.0012281373248267241,
     #  u'pakket': 0.00078934462283374919,}
     
     
     # # generate wordcloud
     # wcloud = WordCloud().generate_from_frequencies(MyData)

     # # make figure to plot
     # plt.figure()
     # # plot words
     # plt.imshow(wcloud, interpolation="bilinear")
     # # remove axes
     # plt.axis("off")
     # # show the result
     # plt.show()


except FileNotFoundError:
     print("The file does not exist.")