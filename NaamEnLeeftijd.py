from time import sleep
Vraag = True
def greet():
    print('Hallo, '+ name +', je bent '+ str(age) +' jaar.')

while Vraag == True:
    print('Type \'stop\' bij \'naam\' en \'1\' bij \'leeftijd\' wanneer je wilt stoppen')
    name = input('Wat is jouw naam? ')
    if name == 'stop':
        break
    age = int(input('Hoe oud ben jij? '))
    if age < 2:
        Vraag = False
    else:
        greet()
