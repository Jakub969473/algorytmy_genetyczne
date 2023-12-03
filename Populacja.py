from Osobnik import Osobnik
import numpy as np


class Populacja:

    def __init__(self, populacja, n_tasks, lista_zadan, szansa_mutacji, n_procent_najlepszych):
        self.populacja = populacja
        self.n_tasks = n_tasks
        self.lista_zadan = lista_zadan
        self.suma_taskow = sum(lista_zadan)
        self.pop = []
        self.szansa_mutacji = szansa_mutacji
        self.n_procent_najlepszych = n_procent_najlepszych

    def ocen(self, chromoson: np.array):

        wartosc = 0

        for gen, task in zip(chromoson, self.lista_zadan):

            if gen:
                wartosc += task
            else:
                wartosc -= task

        return self.suma_taskow - abs(wartosc)

    def stworz_populacje(self):

        for _ in range(self.populacja):
            temp = Osobnik(self.n_tasks, self.szansa_mutacji)
            temp.wartosc = self.ocen(temp.chromosom)
            self.pop.append(temp)

    def krzyzowanie(self):

        good_ones = []

        for j in range(int(self.n_procent_najlepszych / self.n_tasks)):
            max = self.pop[0]
            n_max = 0
            for k, i in enumerate(self.pop):
                if i.wartosc < max.wartosc:
                    max = i
                    n_max = k
            good_ones.append(self.pop.pop(n_max))

        wartosc_calk = sum([i.wartosc for i in self.pop])
        prob = np.array([i.wartosc / wartosc_calk for i in self.pop])

        pop_do_krzy = np.random.choice(self.pop, size=len(self.pop), p=prob)

        '''for i, j in zip(pop, prob):
            print(i.wartosc, '', j)'''

        pop2 = []

        for i, j in zip(pop_do_krzy, reversed(pop_do_krzy)):
            temp = i.krzyzowanie(j)

            temp.mutacja()

            temp.wartosc = self.ocen(temp.chromosom)

            pop2.append(temp)

        self.pop = pop2 + good_ones

    def wybierz_najlepszych(self):

        good_ones = []

        for j in range(int(self.n_tasks / 10)):
            max = self.pop[0]
            for j, i in enumerate(self.pop):
                if i.wartosc < max.wartosc:
                    max = i
            good_ones.append(self.pop.pop(j))

        return good_ones

    def najlepszy(self):

        max = self.pop[0]
        for i in self.pop:
            if max.wartosc > i.wartosc:
                max = i

        return max.wartosc
