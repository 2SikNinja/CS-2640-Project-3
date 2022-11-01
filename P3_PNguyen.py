#Authors: Peter Nguyen
#Assignment: Project #3
#Completed (or last revision): 11/01/2022

# from wordcloud import WordCloud, STOPWORDS
# import matplotlib.pyplot as plt
# userInputOpenFile = input("Please enter the file you would like to open to make a word cloud: ")
# #task 1
# try:
#      file = open(userInputOpenFile, 'r')
#      text = [word.replace(",", "").replace(".", "") for line in file for word in line.lower().split()]
#      print(text)
#      freq = {}
#      def CountFrequency(my_list,freq):
 
#           freq = freq
#           for item in my_list:
#                if (item in freq):
#                     freq[item] += 1
#                else:
#                     freq[item] = 1

#           for key, value in freq.items():
#                print((key, value))
#           return freq
#      CountFrequency(text,freq)
#      # MyData= {u'arbeid': 0.0006715695865686539,
#      #  u'banen': 0.00066821988636323406,
#      #  u'begrotingsherstel': 0.00071106447864468028,
#      #  u'belastingplan': 0.00064287666559415511,
#      #  u'bestuursakkoord': 0.00085938678272561703,
#      #  u'duurzame': 0.00086622249359887991,
#      #  u'energie': 0.00071735256545447078,
#      #  u'energievoorziening': 0.00091959448177479836,
#      #  u'europa': 0.00077342364155819174,
#      #  u'inkomens': 0.00086651160197001511,
#      #  u'kabinet': 0.0012281373248267241,
#      #  u'pakket': 0.00078934462283374919,}
     
     
#      # # generate wordcloud
#      # wcloud = WordCloud().generate_from_frequencies(MyData)

#      # # make figure to plot
#      # plt.figure()
#      # # plot words
#      # plt.imshow(wcloud, interpolation="bilinear")
#      # # remove axes
#      # plt.axis("off")
#      # # show the result
#      # plt.show()


# except FileNotFoundError:
#      print("The file does not exist.")




#Task 2
R1 = []
R2 = []
R3 = []
L1 = []
L2 = []
bool = False
k=2
count = 1
while(count <= 100):
     if k > 1:
          for i in range(2, k):
               if (k % i) == 0:
                    bool = True
                    break
     if bool:
          pass
     else:
          L1.append(k)
          count+=1
     bool=False
     k+=1
print("This is L1", L1)

# Fibonacci list maker
n1, n2 = 0, 1
count = 0
while count < 100:
     L2.append(n1)
     nth = n1 + n2
     n1 = n2
     n2 = nth
     count += 1

print("This is L2", L2)

S1 = [x for x in L1]
print("This is S1", S1)

S2 = [x for x in L2]
print("This is S2", S2)

for i in L1:
     R1.append(L1)
for i in L2:
     R1.append(L2)
print("The length of R1 is ", len(R1))

for i in range(len(L2)):
     for k in range(len(L1)):
          if L2[i] == L1[k]:
               R2.append(L2[i])       
print("The length of R2 is ", len(R2))

for i in L1[:]:
     if i in L2:
          L1.remove(i)   
for i in range(len(L1)):
     R3.append(L1[i])
print("The length of R3 is ", len(R3))