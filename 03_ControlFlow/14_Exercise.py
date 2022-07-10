# 2'05

count=0
for number in range(102):
    if number % 2 == 0:
        print(number)
        count+=1
print(f"We got {count} even numbers!")