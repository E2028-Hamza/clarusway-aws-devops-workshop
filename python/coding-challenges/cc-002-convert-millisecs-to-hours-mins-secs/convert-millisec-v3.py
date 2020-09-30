def hesap(milisaniye):
    # burada normal saniye dakika ve saat değerlerini alıyoruz
    saniye = int(milisaniye/1000)
    dakika = int(saniye/60) 
    saat = int(dakika/60)
    # burada gerçek saniye ve dakika değerlerini bulmak için bir işlem yapıyoruz. Mesela Normalde 3661011 milisaniye [saat:  1, dakika:  61, saniye:  3661] değerini verir ama 61 dakikanın 60 dakikası aslında 1 saat olarak saat yerinde belirtiliyor
    saniye = saniye -dakika*60
    dakika = dakika -saat*60
    #burada 0 olan değer yazdırılacak texten çıkarılıyor
    if saniye > 0 : 
        santext = "{} second/s".format(saniye)
    elif dakika == 0 and saat == 0: 
        santext = "just {} milisecond/s".format(milisaniye)
    else: santext = ""
    if dakika > 0 : 
        daktext = "{} minute/s".format(dakika)
    else: daktext = ""
    if saat > 0 : 
        saattext = "{} hour/s".format(saat)
    else: saattext = ""
    #burada nihai sonuç yazdırılıyor
    print(saattext, daktext, santext)   

milisaniye = input("Please enter the milliseconds (should be written in numbers and greater than zero): ")
if milisaniye == "exit":
    print ("Exiting the program... Good Bye")    
elif (not milisaniye.isdigit()) or int(milisaniye) <= 0 : # Burada girilen değer exit dışında bir text mi veya o 'dan küçük bir değer mi o kontrol ediliyor
    print ("Not Valid Input !!!. Please enter the milliseconds (should be written in numbers and greater than zero):")
else:        
    milisaniye = int(milisaniye)
    hesap(milisaniye)