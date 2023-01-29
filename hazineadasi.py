print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Hazine Adasına Hoşgeldiniz!")
print("Göreviniz gizli hazineyi bulmak.") 

yon=input("Yol ayrımına geldiniz. Ne tarafa gitmek istiyorsun?(sag veya sol)")
if yon=="sol":
    eylem=input("\nSol taraf güvenli gibi duruyor. Biraz ilerledikten sonra karşına büyük bir su birikintisi çıktı. Derinliğinin ne kadar olduğunu kestiremiyorsun.Ne yapıcaksın?(yuz veya bekle)")
    if eylem=="bekle":
        kapi=input("\nHadi biraz bekleyelim. Beklerken etrafına bakınıp farklı bir yol arıyorsun. O da ne? Suyun içinde devasa bir alabalık var. Beklemek doğru bir seçimmiş anlaşılan. Duvarların birinde bir halat buldun. Yukarı doğru gidiyor. Şansını deneyip halata tırmanmaya başladın. Biraz zorlayıcı olsa da tırmanmayı başardın. Karşına 3 adet kapı çıktı. Mavi, Kırmızı ve Sarı renkte. Hangi kapıdan girmek istersin?(mavi,kirmizi,sari)")
        if kapi=="mavi":
            print("\nMavi kapıyı seçtin. İçeri girdikten sonra kapı kapandı. İçerisi çok karanlık etrafı göremiyorsun. Neyseki yanında el feneri var. El fenerini yakıyorsun. Sanırım bu yanlış kapıydı. Karşında bir grup timsah sürüsü var ve sana doğru yavaşça yaklaşıyor.\nTimsahlar seni canlı canlı yedi ve öldün.\n Oyun bitti! :(")
        if kapi=="sari":
            print("\nSarı kapıyı seçtin. İçerisi biraz karanlık. Ama uzaktan bir şey ışık saçıyor. O yöne doğru ilerliyorsun. NE! HAZİNE! Bu kadar kolay olmamalıydı. Umarım başımız belaya girmez.:)\nTebrikler! Kazandınız.")
        if kapi=="kirmizi":
            print("\nKırmızı kapıyı seçtin. İçerisi biraz aydınlık. Önümüzü rahat görüyoruz. Ama bir tuhaflık var. Fazla sıcak. Olamaz! Üstümüze doğru bir lav yığını geliyor. Kaçacak yerimiz yok ve kapı açılmıyor.\nLavın içinde cayır cayır yandın.\nOyun Bitti! :(")
    else:
        print("\nYüzmeyi tercih ettin. Birikintinin ortasına kadar geldin ve ayağına bir şeyler takılmaya başladı.Bu DA NE?! DEVASA BİR ALABALIK! Sana saldırmaya başladı. Göğüs Kafesine sert bir darbe vurdu. Sanırım kemiklerin kırılmış olabilir. İç kanama geçiyorsun ve yavaşça bilincin kayboluyor.\n Malesef Öldün. Oyun bitti! :(")
else:
    print("\nSağ tarafa doğru ilerlerken ayağınla bir taşa takıldın. Sanırım bu tuzağa etkin hale getirdi. Bir çukur açıldı ve içine düştün.\nOyun Bitti! :( ")