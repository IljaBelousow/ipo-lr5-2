stroka1 = input("Введите слово 1: ")
stroka2 = input("Введите слово 2: ")

stroka1 = stroka1.lower()
stroka2 = stroka2.lower()

is_anagram = all(char in stroka2 for char in stroka1)

if is_anagram:
    print("Да, они анаграммы.")
else:
    print("Нет, они не анаграммы.")
