'''otam={

     "ismi":"Shuhrat",
     "familiyasi":"Hamidullayev"
     "yoshi":44,
      }

onam={     
     "ismi":"Gulchehra"
     "familiyasi":"Hamidullayev"
     "yoshi":43
     }

print(f"otam otam["ismi"]familiyasi otam["familiyasi"].Otamning yoshi otam[yoshi] da".)
print(f"onam onam["ismi"]familiyasi oanm["familiyasi"].Onamning yoshi onam [yoshi] da")


for x in range(1,6):
    for y in range(5,x,-1):
        print("",end="")
    for z in range(0,x):
        print("*",end="")
    print()
      

for i in range(1,6):
    for j in range(5,0,1):
     if i>j:
         print("*",end="")
    else:
        print(" ",end="")
    print()


for i in range(1,6):
   for j in range(5,0,-1):
    if i>=j:
        print("*",end="")
    else:
        print(" ",end="")
    print(end="")
    for j in range(1,i):
        print("*",end="")
    print()
for i in range(1,6):
    for j in range(5,0,-1):
        if i>=j:
            print("*",end="")
   else:
       
              print(" ",end="")
        print(end="")
        for j in range(1,i):
             print("*",end="")'''




Friends={
   'Ismoil':"pubg",
   'Shamsi':"contr",
   'Dimir':"contr",
   'Dilshod':"pubg"
   }
for kalit, qiymat in friends.items():
   print(f"mening dostim {kalit} yoqtirgan oyini {qiymat}")
