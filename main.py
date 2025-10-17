import random

''' CONSTANTES '''
liste_individu = []
solution_trouver = False
nb_gen = 0

''' FUNCTION '''

def create_rand_pop(count: int):
    for _ in range(count):
        liste_individu.append(Individu([random.randint(0, 7) for _ in range(8)]))

def evaluate(pop: list):
    pop.sort(key=lambda individu: individu.fitness())

def selection(pop: list, hcount: int, lcount: int):
    del pop[hcount:len(pop)-lcount]

def croisement(ind1: object, ind2: object):
    temp1 = ind1.liste.copy()
    temp2 = ind2.liste.copy()

    for i in range(4):
        temp1[i], temp2[i] = temp2[i], temp1[i]
    
    ind1.liste = temp1.copy()
    ind2.liste = temp2.copy()

def mutation(ind: object):
    index_rdm = random.randint(0,7)
    nb_rdm = random.randint(0,7)
    ind.liste[index_rdm] = nb_rdm


''' DEBUG FUNCTION '''

def printAllFitness(pop: list):
    for i in pop:
        print(i.fitness())

def printListInd(ind):
    print(ind.liste)

''' CLASSE '''

class Individu:
    """
        Représente chaque configuration de l'échiquier.
        Pour chaque colonne on indique la ligne où se trouve la reine.

        liste: Représente la position Y des reines dans l'échiquier.
        nbconflict: Représente le nombre de conflits de la configuration.
    """
    
    #Constructeur
    def __init__(self, lst: list):
        self.liste = lst
        self.nbconflict = 0
        

    #Afficher la configuration
    #def __str__(self):
    #    return 0

    # Vérifier si 2 reines se menacent
    def conflict(self, col1: int, col2: int):
        lig1 = self.liste[col1]
        lig2 = self.liste[col2]
        if (abs(col1 - col2) == abs(lig1 - lig2) or lig1 == lig2):
            return True
        else:
            return False
        
    #Retourne le nombre de conflits
    def fitness(self):
        self.nbconflict = 0
        for i in range(len(self.liste)):
            for j in range(i+1, len(self.liste)):
                if self.conflict(i, j):
                    self.nbconflict += 1
        return self.nbconflict  


''' MAIN PROGRAMME '''   

create_rand_pop(25)


while(solution_trouver == False):
    print(f"Nous sommes à la génération : {nb_gen}")
    evaluate(liste_individu)
    if(liste_individu[0].nbconflict == 0):
        solution_trouver = True
        print(f"Un individu de Fitness 0 à été trouvé : {liste_individu[0].liste}, {liste_individu[0].nbconflict} \nEn {nb_gen} génération(s)")
    else:
        selection(liste_individu,10,5)
        croisement(liste_individu[random.randint(0,14)], liste_individu[random.randint(0,14)])
        mutation(liste_individu[random.randint(0,14)])
    nb_gen += 1
        
    