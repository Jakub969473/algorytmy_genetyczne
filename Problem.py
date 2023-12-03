import numpy as np
import matplotlib.pyplot as plt
from Osobnik import Osobnik


class Problem:
    n_tasks = 30
    populacja = 100
    pokolenia = 200
    szansa_mutacji = 0.003
    n_procent_najlepszych = 10

    def __init__(self):
        self.lista_zadan = np.random.randint(10, 20, size=[1, self.n_tasks])[0]
        self.suma_taskow = sum(self.lista_zadan)
        print(sum(self.lista_zadan))

    def ocen(self, chromoson: np.array):

        wartosc = 0

        for gen, task in zip(chromoson, self.lista_zadan):

            if gen:
                wartosc += task
            else:
                wartosc -= task

        return self.suma_taskow - abs(wartosc) #TODO

    def stworz_populacje(self):

        pop = []

        for _ in range(self.populacja):
            temp = Osobnik(self.n_tasks)
            temp.wartosc = self.ocen(temp.chromosom)
            pop.append(temp)

        return pop

    def krzyzowanie(self, pop):

        good_ones = []

        for j in range(int(self.n_procent_najlepszych/self.n_tasks)):
            max = pop[0]
            n_max = 0
            for k, i in enumerate(pop):
                if i.wartosc < max.wartosc:
                    max = i
                    n_max = k
            good_ones.append(pop.pop(n_max))

        wartosc_calk = sum([i.wartosc for i in pop])
        prob = np.array([i.wartosc / wartosc_calk for i in pop]) #TODO złe liczeie prawdopodobienstwa

        pop_do_krzy = np.random.choice(pop, size=len(pop), p=prob)

        '''for i, j in zip(pop, prob):
            print(i.wartosc, '', j)'''

        pop2 = []

        for i, j in zip(pop_do_krzy, reversed(pop_do_krzy)):
            temp = i.krzyzowanie(j)

            temp.mutacja()

            temp.wartosc = self.ocen(temp.chromosom)

            pop2.append(temp)

        return pop2 + good_ones

    def solve_problem(self):

        pop = self.stworz_populacje()

        x = []
        y = []

        for j in range(self.pokolenia):

            max = pop[0].wartosc
            debesiak = pop[0]
            avg = 0
            for i in pop:
                if i.wartosc < max:
                    max = i.wartosc
                    debesiak = i
                avg += i.wartosc

            print()
            print(f'Różnica między procesamai: {avg / self.populacja} {max} osobnik: {debesiak}')

            x.append(j)
            y.append(max)

            pop = self.krzyzowanie(pop)


        plt.plot(x, y)
        plt.xlabel('Pokolenia')
        plt.ylabel('Średnia wartość')
        plt.title('Algorytm genetyczny')
        plt.show()
        print(sum(self.lista_zadan))
