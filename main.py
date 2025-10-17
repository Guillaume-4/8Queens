import random

''' CONSTANT '''
list_pop = []
solution = False
nb_gen = 0

''' FUNCTION '''

def create_random_pop(count: int):
    """
        Creates a new random population with `count` Individual
    """
    for _ in range(count):
        list_pop.append(Individual([random.randint(0, 7) for _ in range(8)]))

def evaluate(pop: list):
    """
        Sorts the `pop` with each `nbconflict`
    """
    pop.sort(key=lambda individu: individu.fitness())

def selection(pop: list, hcount: int, lcount: int):
    """
        Keeps `hcount` best Individuals of the `pop` list and the `lcount` worst
    """
    del pop[hcount:len(pop)-lcount]

def new_generation(ind1: object, ind2: object):
    """
        Switches the 4th first numbers on `ind1` with `ind2
    """
    temp1 = ind1.list.copy()
    temp2 = ind2.list.copy()

    for i in range(4):
        temp1[i], temp2[i] = temp2[i], temp1[i]
    
    ind1.list = temp1.copy()
    ind2.list = temp2.copy()

def mutation(ind: object):
    """
        Changes a random number on the list of `ind`
    """
    index_rdm = random.randint(0,7)
    nb_rdm = random.randint(0,7)
    ind.list[index_rdm] = nb_rdm


''' CLASSE '''

class Individual:
    """
        Represents each configuration of the chessboard.
        For each column, indicate the row where the queen is located.
    """
    
    def __init__(self, lst: list):
        """
            Constructor of the `Individu` class
        """
        self.list = lst
        self.nbconflict = 0
        

    def __str__(self):
        return f"There is {self.nbconflict} conflict on this configuration : {self.list}"

    def conflict(self, queen1: int, queen2: int):
        """
            Check if `queen1` and `queen2` are in conflict, 
            Conflict: 
                -Same Lines
                -Same diagonal 
        """
        lig1 = self.list[queen1]
        lig2 = self.list[queen2]
        if (abs(queen1 - queen2) == abs(lig1 - lig2) or lig1 == lig2):
            return True
        else:
            return False
        
    #Retourne le nombre de conflits
    def fitness(self):
        """
            Returns the number of conflicts in a configuration of Individual
        """
        self.nbconflict = 0
        for i in range(len(self.list)):
            for j in range(i+1, len(self.list)):
                if self.conflict(i, j):
                    self.nbconflict += 1
        return self.nbconflict  


''' MAIN PROGRAM '''   

create_random_pop(25)


while(solution == False):
    print(f"Attempt#{nb_gen}")
    evaluate(list_pop)
    if(list_pop[0].nbconflict == 0):
        solution = True
        print(f"{list_pop[0]} \nIn {nb_gen} generation(s)")
    else:
        selection(list_pop,10,5)
        new_generation(list_pop[random.randint(0,14)], list_pop[random.randint(0,14)])
        mutation(list_pop[random.randint(0,14)])
    nb_gen += 1
        
    