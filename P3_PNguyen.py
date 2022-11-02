#Authors: Peter Nguyen
#Assignment: Project #3
#Completed (or last revision): 11/01/2022

# from wordcloud import WordCloud, STOPWORDS
# import matplotlib.pyplot as plt
# userInputOpenFile = input("Please enter the file you would like to open to make a word cloud: ")
# #task 1

#Authors: Peter Nguyen
#Assignment: Project #3
#Completed (or last revision): 11/01/2022

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

#task 1
userInput = input("Enter the name of the file you wish to open: ")
try: 
     freq = []
     words = []
     wordList = []
     file = open(userInput, 'r')
     text = [word.replace(",", "").replace(".", "") for line in file for word in line.lower().split()]
     frequency = {}
     for word in text:
          if word in frequency:
               frequency[word] += 1
          else:
               frequency[word] = 1
     sortedFrequencyList = sorted(frequency,key = frequency.get, reverse = True)
     for i in range(10):
          print("The",str(10-i)+"th", "most frequent word is",'"'+ sortedFrequencyList[i]+'":', frequency[sortedFrequencyList[i]] )
          words.append(sortedFrequencyList[i])
          freq.append(frequency[sortedFrequencyList[i]])
     dictionary = {}
     for key in words:
          for value in freq:
               dictionary[key] = value
               freq.remove(value)
               break
     # generate wordcloud
     wcloud = WordCloud().generate_from_frequencies(dictionary)
     # make figure to plot
     plt.figure()
     # plot words
     plt.imshow(wcloud, interpolation="bilinear")
     # remove axes
     plt.axis("off")
     # show the result
     plt.show()
except FileNotFoundError:
     print("The file does not exist.")

#Task 1 Output:
# Enter the name of the file you wish to open: text.txt
# The 10th most frequent word is "the": 9
# The 9th most frequent word is "pumpkin": 4
# The 8th most frequent word is "patch": 4
# The 7th most frequent word is "to": 3
# The 6th most frequent word is "can": 2
# The 5th most frequent word is "of": 2
# The 4th most frequent word is "corn": 2
# The 3th most frequent word is "farm": 2
# The 2th most frequent word is "moo": 2
# The 1th most frequent word is "childrenâ€™s": 2


# Enter the name of the file you wish to open: article.txt
# The 10th most frequent word is "the": 7
# The 9th most frequent word is "south": 6
# The 8th most frequent word is "and": 5
# The 7th most frequent word is "of": 4
# The 6th most frequent word is "in": 4
# The 5th most frequent word is "to": 4
# The 4th most frequent word is "north": 4
# The 3th most frequent word is "had": 4
# The 2th most frequent word is "on": 3
# The 1th most frequent word is "fired": 3



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


#Task 2 Output
# This is L1 [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]
# This is L2 [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 
# 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025, 20365011074, 32951280099, 53316291173, 86267571272, 139583862445, 225851433717, 365435296162, 591286729879, 956722026041, 1548008755920, 2504730781961, 4052739537881, 6557470319842, 10610209857723, 17167680177565, 27777890035288, 44945570212853, 72723460248141, 117669030460994, 190392490709135, 308061521170129, 498454011879264, 806515533049393, 1304969544928657, 2111485077978050, 3416454622906707, 5527939700884757, 8944394323791464, 14472334024676221, 23416728348467685, 37889062373143906, 61305790721611591, 99194853094755497, 160500643816367088, 259695496911122585, 420196140727489673, 679891637638612258, 1100087778366101931, 1779979416004714189, 2880067194370816120, 4660046610375530309, 7540113804746346429, 12200160415121876738, 19740274219868223167, 31940434634990099905, 51680708854858323072, 83621143489848422977, 135301852344706746049, 218922995834555169026]
# This is S1 [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]
# This is S2 [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 
# 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025, 20365011074, 32951280099, 53316291173, 86267571272, 139583862445, 225851433717, 365435296162, 591286729879, 956722026041, 1548008755920, 2504730781961, 4052739537881, 6557470319842, 10610209857723, 17167680177565, 27777890035288, 44945570212853, 72723460248141, 117669030460994, 190392490709135, 308061521170129, 498454011879264, 806515533049393, 1304969544928657, 2111485077978050, 3416454622906707, 5527939700884757, 8944394323791464, 14472334024676221, 23416728348467685, 37889062373143906, 61305790721611591, 99194853094755497, 160500643816367088, 259695496911122585, 420196140727489673, 679891637638612258, 1100087778366101931, 1779979416004714189, 2880067194370816120, 4660046610375530309, 7540113804746346429, 12200160415121876738, 19740274219868223167, 31940434634990099905, 51680708854858323072, 83621143489848422977, 135301852344706746049, 218922995834555169026]
# The length of R1 is  200
# The length of R2 is  6
# The length of R3 is  94