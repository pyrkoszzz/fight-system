from random import randint
import time

class gnom:
    name = "gnom"
    hp = 100
    atak = 10

class mag:
    name = "mag"
    hp = 30
    atak = 50

def status(self):
    print("%s HP: %d ATAK: %d" %(self.name, self.hp, self.atak))

def walka(glad1, glad2):

        def restore_health(glad1, glad2): #restores class health 
            glad1.hp = glad1.temp[0]
            glad2.hp = glad2.temp[0]
            
        def restore_atak(glad1, glad2): #restores class attack
            glad1.atak = glad1.temp[1]
            glad2.atak = glad2.temp[1]
            
        glad1.temp = [glad1.hp, glad1.atak]
        glad2.temp = [glad2.hp, glad2.atak]

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
                glad1.atak = randint(glad1.atak-10, glad1.atak+10) 
                glad2.hp -= glad1.atak  
                status(glad1)
                restore_atak(glad1,glad2)

            while glad1.hp > 0 or glad2.hp > 0:
                punch(glad1, glad2)
                if glad2.hp <=0:
                    restore_health(glad1, glad2)
                    return print("Zwyciezyl %s" %(glad1.name))
                time.sleep(1)
                punch(glad2, glad1)
                if glad1.hp <=0:
                    restore_health(glad1, glad2)
                    return print("Zwyciezyl %s" %(glad2.name))
                time.sleep(1)

        los(glad1, glad2)
        

merino = gnom()
merino.name = "Merino"
status(merino)

doritos = gnom()
doritos.name = "Doritos"
status(doritos)

merlin = mag()
merlin.name = "Merlin"
status(merlin)

walka(merino, doritos)
walka(merino, merlin)