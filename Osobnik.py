import random
from numpy import array, hstack


class Osobnik:

    szansa_mutacji = 0.003
    wartosc = 0

    def __init__(self, n_tasks, szansa_mutacji, chromosom=None):
        if chromosom is None:
            self.chromosom = array([random.choice([0, 1]) for _ in range(n_tasks)])
        else:
            self.chromosom = chromosom

        self.n_tasks = n_tasks
        self.szansa_mutacji = szansa_mutacji

    def __str__(self):
        return str(self.chromosom)

    def krzyzowanie(self, drugi: 'Osobnik') -> 'Osobnik':

        punkt_przedzialu = random.randint(0, self.n_tasks)
        return Osobnik(n_tasks=self.n_tasks, szansa_mutacji=self.szansa_mutacji,
                       chromosom=hstack((self.chromosom[:punkt_przedzialu], drugi.chromosom[punkt_przedzialu:])))

    def mutacja(self):

        if self.szansa_mutacji >= random.random():
            mutation = random.randint(0, self.n_tasks - 1)

            if self.chromosom[mutation]:
                self.chromosom[mutation] = 0
            else:
                self.chromosom[mutation] = 1
