import time
print("Welcome to Wconfig! (Word Configuration)")
word = input("Word here:\n")
choose = input("What do you want?\n 1. Invert (Hi -> Ih) 2. Jump (Pumpkin -> Pmkn) 3. Count (Apple -> 2 p's)\n").capitalize()
if choose == "1" or choose == "invert".capitalize():
    print(word[::-1])
    time.sleep(1.5)
    input("Close the program")
elif choose == "2" or choose == "jump".capitalize():
    print(word[::2])
    time.sleep(1.5)
    input("Close the program")
elif choose == "3" or choose == "count".capitalize():
    countword = input("what do you want to count?\n")
    print(f"This word have {word.count(countword)} {countword}'s")
    time.sleep(1.5)
    input("Close the program")
else:
    print(f"Error! You typed this: {choose}, but if ths is a bug, please, tell to me!\n Repository link:\n")