my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
tochka = 0
while tochka < len(my_list):
    chisla = my_list[tochka]
    tochka = tochka + 1
    if chisla == 0:
        continue
    elif chisla < 0:
        break
    elif chisla == len(my_list):
        break
    else:
        print(chisla)
