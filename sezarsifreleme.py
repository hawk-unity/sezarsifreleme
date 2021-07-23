print("""
+++++++++++++++++++++++++++
   Sezar Şifreleme aracı
   CODED : H4WK OFCX 
   instagram : hawkofcx
   youtube : HAWK DEFACER 
+++++++++++++++++++++++++++
1-İfade Şifrele =>
2-Şifrelenen İfadeyi çöz
+++++++++++++++++++++++++++
(eğer çözemiyorsanız 'chr(ord(k) - 5)' kodundaki 5'i ,
1'den başlayıp tek tek deneyiniz, çünkü öteleme hareketi ile şifreleniyor
mesela P harfini öteleyelim önce ascii karşılığına bakalım 
sonuç ney 80 şimdi bunu 5'e öteleylim yani 80+5 yapalım peki 85'in 
ötelenmeş hali ney onuda söylim büyük U harfi bunu anlatmamamın sebebi 
anlamanız ve mantığı çözmeniz için isterseniz 'chr(ord(k) - 5)' burayı 6,7,8
yapın yine aynı şekilde şifrelenir sadece değişen tek şey öteleme farkı ,sonuç olarak 
bu bir şifreleme ve çözme aracı)
+++++++++++++++++++++++++++
""")
veri = input("Şifrele yada çöz seç birini => ")
if veri =="1":
    metin = input("şifrelencek string ifadeyi lütfen giriniz => ")
    sifre=""
    for k in metin:
        print(ord(k))
        print(k, "=>", chr(ord(k) +5 ))
        sifre = sifre + chr(ord(k) + 5)
    print("şifrelenen yer => ", metin)
    print(metin, "=> ", sifre)
     
if veri == "2":
    metin = input("çözülecek ifade gir => ")
    sifre = ""
    for k in metin : 
        print(ord(k))
        print(k, "=>", chr(ord(k) - 5))
        sifre = sifre + chr(ord(k) - 5)
    print("Çözülen hal => ", sifre)
    print(metin, "=>",sifre)
