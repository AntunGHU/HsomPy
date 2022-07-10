# 2'46

# Kombinacija for i else na istoj uvlaci znaci da ce se else odraditi samo ako for ne odradi ni u jednoj iteraciji

successful = False
for number in range(3):
    print("Attempt...")
    if successful:
        print("Successful!")
        break
else:
    print("Attempted 3 times and failed:")