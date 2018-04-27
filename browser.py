from nltk.corpus import reuters
from nltk.stem import *

#print(reuters.categories()) # display categories
#print(reuters.fileids('income')[:10]) # from displayed categories


words = reuters.words('test/16318')
words = [word.lower() for word in words]
stemmer = PorterStemmer()

print(' '.join(words)) # from displayed files

singles = [stemmer.stem(word) for word in words] #data preprocessing - stemming

print(' '.join((singles)))

index = 0
dict= {}
dict_index_r = {}
dict_freq = {}
for i in singles:
    if(i not in dict):
        dict[i] = index
        dict_index_r[index] = i
        index+=1
        dict_freq[i] = 1
    else:
        dict_freq[i]+=1
print(dict)
print(dict_index_r)
print(dict_freq)






