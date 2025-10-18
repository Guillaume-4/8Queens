import random

''' CONSTANT '''

    # Parametters
nb_pop = 25
select_hcount = 5
select_lcount = 5
BOARD_SIZE= 8

    # /!\ Don't touch this /!\
list_pop = []
list_all_solution = []
nb_gen = 1
RDM_SELECT = select_lcount + select_hcount -1


''' FUNCTION '''

def fillPop(pop: list[object] ,count: int):
    """
        Refills `pop` with random Individuals while length of `pop` < `count`
    """
    while(len(pop) <= count):
        pop.append(Individual(random.sample(range(BOARD_SIZE),BOARD_SIZE)))

def create_random_pop(count: int):
    """
        Creates a new random population with `count` Individual
    """
    for _ in range(count):
        list_pop.append(Individual(random.sample(range(BOARD_SIZE),BOARD_SIZE)))

def evaluate(pop: list[object]):
    """
        Sorts the `pop` with each `nbconflict`
    """
    pop.sort(key=lambda individu: individu.nbconflict)

def selection(pop: list[object], hcount: int, lcount: int):
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

def checkSolution(allSolution : list[object], solutionToCheck: object):
    """
        Checks if a `solutionToCheck` is in `allSolution` list
    """
    for i in allSolution:
        if(i.list == solutionToCheck.list):
            return True
    return False



def findSolution(messages: bool):
    """
        Found a solution for the 8 queens problems with the `pop`
    """
    global nb_gen, nb_pop, list_pop
    list_pop.clear()
    create_random_pop(nb_pop)
    while(True):
        if messages:
            print(f"Attempt#{nb_gen}")
        evaluate(list_pop)
        if(list_pop[0].nbconflict == 0):
            if messages:
                print(f"{list_pop[0]} \nIn {nb_gen} generation(s)")
            return list_pop[0]
        else:
            selection(list_pop,select_hcount,select_lcount)
            new_generation(list_pop[random.randint(0,RDM_SELECT)], list_pop[random.randint(0,RDM_SELECT)])
            mutation(list_pop[random.randint(0,RDM_SELECT)])
            fillPop(list_pop, nb_pop)
        nb_gen += 1


def findAllSolution():
    """
        Looking for all solution of 8 queens problems 
    """
    global list_all_solution, nb_pop
    while(True):
        print(f"Numbers of solutions find : {len(list_all_solution)}")
        temp_solution = findSolution(False)
        if not checkSolution(list_all_solution, temp_solution):
            list_all_solution.append(temp_solution)

''' CLASSE '''

class Individual:
    """
        Represents each configuration of the chessboard.
        For each column, indicate the row where the queen is located.
    """
    
    def __init__(self, lst: list[int]):
        """
            Constructor of the `Individu` class
        """
        self.list = lst
        self.nbconflict = self.fitness()
        

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

"""
    If you want to have all solutions for the 8 queens problems,
    just write : 
        findAllSolution()

    If you need just one write : 
        findSolution(True) 
"""

findAllSolution()
#findSolution(True)