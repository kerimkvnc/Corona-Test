def start1():
 print("QUIT FOR -Q- / START FOR -ENTER-")

def start():
  print(""" 
 SEÇENEKLER
  +Bazen = 1
  +Sık = 2
  +Şiddetli = 3
  """)

 
while True:
    start1()
    test = input("Q:")
    if test == "Q" or test == "q":
       print("TEST KAPANIYOR...")
       break
    else:
      start()
      break 

ates = input("ATEŞ SIKLIĞI:")
yorgunluk = input("YORGUNLUK SIKLIĞI:")
oksuruk = input("KURU ÖKSÜRÜK SIKLIĞI:")
solunum = input("SOLUNUM ZORLUĞU SIKLIĞI:")
agrı = input("AĞRI SIKLIĞI:")
akıntı = input("BURUN AKINTISI SIKLIĞI:")
bogaz = input("BOĞAZ AĞRISI SIKLIĞI:")
ıshal = input("İSHAL SIKLIĞI:")   
            
if ates == "2" and yorgunluk == "2" and oksuruk == "2" and solunum == "3" and agrı == "1" and akıntı == "1" and bogaz == "1" and ıshal == "1":        
    print("*****CORONA TANISI KONULDU.***** \n *****ACİLEN HASTANEYE GİTMEN GEREK!*****")        
else:
    print("CORONA TANISI KONULMADI.")
        

    



    
 


