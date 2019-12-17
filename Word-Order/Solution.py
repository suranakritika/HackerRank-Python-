# Code

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter
n=input()
out=[]
s=""
for i in range(int(n)):
    word=input()
    out.append(word)
d=dict(Counter(out))
print(len(d))
for key, val in d.items():
    s+=str(val)+" "
print(s)
