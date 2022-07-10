# 4'59

number = 100
while number > 0:
    print(number)
    number //= 2     # augmenting assigning operator sa integer division "//"
    
# malo se rabacivao komandama "ECHO" itd u REPL-u 

command=""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)  # ECHO asds, ECHO quit i izasao!