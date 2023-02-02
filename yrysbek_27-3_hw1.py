print("НАПИШИТЕ ТЕМПЕРАТУРУ ПО ОБЛАСТЯМ: ")

chui = int(input("чуйская область: "))
talas = int(input("таласская область: "))
naryn = int(input("нарынская область: "))
issykkol = int(input("иссык-кульская область: "))
osh = int(input("ошская область: "))
batken = int(input("баткенская область: "))
djal = int(input("джалал-абадская область: "))


summ_temp = (chui + talas + naryn + issykkol + osh + batken + djal) / 7

summ_temp = round(summ_temp, 1 )
print("СРЕДНЯЯ ТЕМПРЕАТУРА ПО КР: " + str(summ_temp) + ("°"))
print( "С НАСТУПАЮЩИМ ! " )
