from random import randint


print("\== Chào mừng bạn đến với hiệp sĩ mộng mơ ==/")
qs = input("bạn đã sẵn sàng chưa [y/n] : ")
if qs.lower() == 'y':
  
    hiep_si = 100
    boss    = 100
    while True:
        print( f" máu hiệp sĩ = {hiep_si} \n máu quái vật = {boss}" )
        print(" chọn 1 : tấn công | chọn 2 : hồi máu ")
        player = int(input("bạn chọn : "))
        if player == 1 : 
            damme = randint(10,25)
            boss -= damme
        elif player == 2 :
            hp = randint (10,20)
            if hiep_si == 100:
               print(" hp has max ")
            else :
                hiep_si += hp
                if hiep_si > 100:
                    hiep_si == 100

        else :
            print(" error ! ")
        
        if boss == 0:
            print ("boss đã chết 🎉 , công chúa đã được cứu 😍 ")
            print (" nhưng công chúa về lấy hoàng từ 💑, còn bạn chỉ là lốp xe 🗿 ")
        else :
            damme = randint(10,25)
            hiep_si -= damme
            if hiep_si <= 0 :
                print ( "hiệp sĩ đã xanh cỏ ☠️")
              print("hello thang nhoc")
         

       
       
            


