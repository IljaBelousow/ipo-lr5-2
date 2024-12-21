stroka1 = input("Введите слово 1: ")
stroka2 = input("Введите слово 2: ")

stroka1 = stroka1.lower()
stroka2 = stroka2.lower()

anagram = all(i in stroka2 for i in stroka1)

if anagram:
    print("они анаграммы.")
else:
    print("они не анаграммы.")
