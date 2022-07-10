# 3'08

print(type(5))   # <class 'int'> uz bool, float, string itd primjeri "primitive types" 
print(type(range(5)))   # <class 'range'> primjer "complex types" uz list, dict itd, "iterable" kao i strings itd tj u for-loopu uvjek daju drugaciju vrijednost!!!

for x in range(5) :
    print(x)

for x in"Python" :
    print(x)
    
for x in [1,2,3,4,5] :
    print(x)