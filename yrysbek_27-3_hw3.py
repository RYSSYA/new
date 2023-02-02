print("напишите- стоп для остановки цикла")
glas = "aeiouаяуюоеёиыAEIOUАЯУЮОЕИЫ"
soglas = "БВГДЖЗЙКЛМНПРСТФХЦЧШЩбвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwzyxBCDFGHJKLMNPQRSTVWXYZ"

while True:
    slovo = input("ВВЕДИТЕ СЛОВО: ")
    if slovo == "стоп":
        break

    glas1 = 0
    soglas1 = 0
    for i in slovo:
        if i in glas:
            glas1 += 1
        elif i in soglas:
            soglas1 += 1

    print("Количество букв:", len(slovo))
    print("Согласных букв:", soglas1)
    print("Гласных букв:", glas1)
    print("Гласные/Согласные: {:.2f}% / {:.2f}%".format(glas1 / len(slovo) * 100, soglas1 / len(slovo) * 100))

