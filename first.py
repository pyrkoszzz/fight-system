from random import randint
import time

class gnom:
    name = "gnom"
    hp = 100
    atak = 10

def walka(glad1, glad2):

        def los(glad1, glad2):
            glad1.los = randint(0,9)
            glad2.los = randint(0,9)

            print(glad1.name, glad1.los, glad2.name, glad2.los)

            if glad1.los > glad2.los:
                start(glad1,glad2)
            elif glad1.los < glad2.los:
                start(glad2,glad1)
            else:
                los(glad1, glad2)

        def start(glad1,glad2):

            def punch(glad1, glad2): 
                x = glad1.atak
                glad1.atak = randint(glad1.atak-10, glad1.atak+10) 
                glad2.hp -= glad1.atak  
                print("%s HP: %d ATAK: %d" %(glad1.name, glad1.hp, glad1.atak))
                glad1.atak = x

            while glad1.hp > 0 or glad2.hp > 0:
                punch(glad1, glad2)
                if glad2.hp <=0:
                    return print("Zwyciezyl %s" %(glad1.name))
                time.sleep(1)
                punch(glad2, glad1)
                if glad1.hp <=0:
                    return print("Zwyciezyl %s" %(glad2.name))
                time.sleep(1)

        los(glad1, glad2)


merino = gnom()
merino.name = "Merino"
print("%s HP: %d ATAK: %d" %(merino.name, merino.hp, merino.atak))

doritos = gnom()
doritos.name = "Doritos"
print("%s HP: %d ATAK: %d" %(doritos.name, doritos.hp, doritos.atak))

walka(merino, doritos)
