Getal = int(input('Van welk getal wilt u de tafel zien? Type alleen het cijfer in '))

def Tafel_Som(Getal:int):
   for x in  range(1,11):
        Antwoord = x * Getal
        print(str(x)+' x '+str(Getal)+' = '+ str(Antwoord)) 

Tafel_Som(Getal)