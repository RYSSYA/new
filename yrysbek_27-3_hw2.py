month = int(input("ВВЕДИТЕ МЕСЯЦ ВАШЕГО РОЖДЕНИЯ "))
day = int(input("ВВЕДИТЕ ЧИСЛО ВАШЕГО РОЖДЕНИЯ "))
if(day>=21 and day<=31 and month==3) or(month==4 and day>=1 and day<=19):
    print(" ОВЕН ")
elif(day>=21 and day<=30 and  month==4) or ( month==5 and day>=1 and day<= 21):
    print(" ТЕЛЕЦ ")
elif(day>=22 and day<=30 and month==5) or (month==6 and day>=1 and day<= 21):
    print(" БЛИЗНЕЦЫ ")
elif(day>=22 and day<=31 and month==6) or ( month==7 and day>=1 and day<=22):
    print(" РАК")
elif(day>=23 and day<=31 and month==7) or (month==8 and day>=1 and day<=21):
    print(" ЛЕВ ")
elif(day>=22 and day<=31 and month==8) or (month==9 and day>=1 and day<=23):
    print(" ДЕВА ")
elif(day>=24 and day<=30 and month==9) or (month==10 and day>=1 and day<=23):
    print(" ВЕСЫ")
elif(day>=24 and day<=30 and month==10) or (month==11 and day>1 and day<=22):
    print(" СКОРПИОН")
elif(day>=23 and day<=30 and month==11) or (month==12 and day>=1 and day<=21):
    print(" СТРЕЛЕЦ ")
elif(day>=22 and day<=31 and month==12) or (month==1 and day>=1 and day<=20):
    print(" КОЗЕРОГ")
elif(day>=21 and day<30 and month==1) or (month==2 and day>=18 and day<=18):
    print(" ВОДОЛЕЙ ")
elif(day>=19 and day<=30 and month==2) or (month==3 and day>=1 and day<=20):
    print(" РЫБА ") 
else: print(" ВВЕДИТЕ ПРАВИЛЬНЫЕ ДАННЫЕ ") 







