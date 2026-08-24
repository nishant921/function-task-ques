# Problem-10:Write a python program that receives a list of strings and performs bag of word operation on those strings  

# The bag-of-words (BoW) model is a model of text which uses an unordered collection (a "bag") of words. It is used in natural language processing and information retrieval (IR). It disregards word order (and thus most of syntax or grammar) but captures multiplicity.

# The bag-of-words model is commonly used in methods of document classification where, for example, the (frequency of) occurrence of each word is used as a feature for training a classifier.[1] It has also been used for computer vision.

# ["John","likes","to","watch","movies","Mary","likes","movies","too"]
# BoW1 = {"John":1,"likes":2,"to":1,"watch":1,"movies":2,"Mary":1,"too":1}

def bag_of_word(l):
    d={}
    for word in l:
        if word not in d:
            d[word]=1
        else:
            d[word]=d[word]+1

    return d
# def bag_of_word(words):
#     d = {}

#     for word in words:
#         d[word] = d.get(word, 0) + 1

#     return d

words=input("Enter string: ").split()
print(bag_of_word(words))


