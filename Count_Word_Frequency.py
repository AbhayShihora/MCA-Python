import string
para="Dynamic tracking logic is A programming technique in which a program continuously monitors and updates the value or state of data whenever new input or changes occur during execution.".lower()

freq={}
for word in para.strip(string.punctuation).split(" "):
    if word in freq: freq[word]+=1
    else: freq[word]=1
print(freq)