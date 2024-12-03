stroka1 = str(input("vvedite slovo "))
stroka2 = str(input("vvedite slovo2 "))
index = 0
for i in stroka1:#i проходит по первой строке
    if i in stroka2:#если i есть во второй строке
        index += 1
if index == len(stroka1): #если index равен длине stroka1
    print("да они амнкраш")
else:
    print("нет они не амнкраш")
                