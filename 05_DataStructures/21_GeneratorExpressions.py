# 3'51

# Na videu naslov samo "Generators"
# ponekad loopanje sa LC nije memorijski povoljno recimo da idemo do bilion

from sys import getsizeof
values = [x*2 for x in range(10)]
for x in values:
    print(x)        # 0; 2; ...;18

# u takvim slucajevima <generator object <genexpr> at 0x7ff9e5c64890>
# oni ne drze sve valuese u mem nego samo 1 u 1 trenutku! dobiju se samo zamjenom [] sa ()
values = (x*2 for x in range(10))
print(values)   # <generator object <genexpr> at 0x7ff9e5c64890>
for x in values:
    print(x)        # 0; 2; ...;18


# malo demoa o stedljivosti gen.objecta:

values = (x*2 for x in range(1000))
print("Gen:", getsizeof(values))   # Gen: 112 i za 1000 i za 100000

values = [x*2 for x in range(1000)]
print("Lst:", getsizeof(values))    # Lst: 9016

# za kraj nam pokazuje sto dobijemo ako hocemo len od generatora
values = (x*2 for x in range(1000))
print(len(values))  # TypeError: object of type 'generator' has no len()
