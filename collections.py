from collections import Counter, namedtuple, OrderedDict, defaultdict

#counter 
text = "aaaabbbbbbcccccc"
counter = Counter(text) #returns dict with the number of chars in str
print(counter.items())

