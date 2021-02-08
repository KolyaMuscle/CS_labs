from collections import Counter
from math import log2
import os
file = open("C:/Users/nik-v/Desktop/3.txt",encoding='utf8')
words = file.read()
#clear_words = sorted(''.join(e for e in words if e.isalnum()))
numbers_of_char = len(words)
uniqchar = sorted(set(words))
quantity = Counter(words)
average_entropy = 0
print(uniqchar)
#Вывод Символа и количества его повторений
for i in uniqchar:
    frequency = quantity[i] / int(numbers_of_char)
    entropy = frequency * log2(1 / frequency)
    print("--------------------------------------------------------")
    print(" Частота для символа " + "'" + i + "'" + " = " + str(frequency))
    print("--------------------------------------------------------")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(" Entropy for " + "'" + i + "'" + " = " + str(entropy))
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    average_entropy +=entropy      
#Количество уникальных символов в тексте
print("Number of uniq char",len(set(words)))
file_stats = os.stat("C:/Users/nik-v/Desktop/3.txt")
print("Average entropy = " + str(average_entropy) + " bytes " + " File size = " + str(file_stats.st_size) + " bytes ")
information = (average_entropy * numbers_of_char) / 8 
print(" Information  = " + str(information) + " bytes ")