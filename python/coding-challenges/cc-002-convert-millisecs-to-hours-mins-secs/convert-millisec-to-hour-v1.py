def hesap(milisaniye):
    # burada normal saniye dakika ve saat deðerlerini alýyoruz
    saniye = int(milisaniye/1000)
    dakika = int(saniye/60) 
    saat = int(dakika/60)
    # burada gerçek saniye ve dakika deðerlerini bulmak için bir iþlem yapýyoruz. Mesela Normalde 3661011 milisaniye [saat:  1, dakika:  61, saniye:  3661] deðerini verir ama 61 dakikanýn 60 dakikasý aslýnda 1 saat olarak saat yerinde belirtiliyor
    saniye = saniye -dakika*60
    dakika = dakika -saat*60
    #burada 0 olan deðer yazdýrýlacak texten çýkarýlýyor
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
    #burada nihai sonuç yazdýrýlýyor
    print(saattext, daktext, santext)   

milisaniye = input("Please enter the milliseconds (should be written in numbers and greater than zero): ")
if milisaniye == "exit":
    print ("Exiting the program... Good Bye")    
elif (not milisaniye.isdigit()) or int(milisaniye) <= 0 : # Burada girilen deðer exit dýþýnda bir text mi veya o 'dan küçük bir deðer mi o kontrol ediliyor
    print ("Not Valid Input !!!. Please enter the milliseconds (should be written in numbers and greater than zero):")
else:        
    milisaniye = int(milisaniye)
    hesap(milisaniye)