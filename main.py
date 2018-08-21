from fightsystem import status 
from fightsystem import walka

class gnom:
    name = "gnom"
    hp = 100
    atak = 10

class mag:
    name = "mag"
    hp = 30
    atak = 50

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