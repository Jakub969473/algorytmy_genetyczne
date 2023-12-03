import numpy as np
import matplotlib.pyplot as plt
from Osobnik import Osobnik
from Populacja import Populacja


class Problem:
    n_tasks = 30
    populacja = 100
    pokolenia = 200
    szansa_mutacji = 0.007
    n_procent_najlepszych = 15

    def __init__(self):
        #self.lista_zadan = np.random.randint(10, 20, size=[1, self.n_tasks])[0]
        self.lista_zadan = np.array([10, 17, 17, 10, 14, 19, 11, 16, 11, 19, 19, 12, 16, 18, 13, 12, 19, 11, 11, 15])
        self.suma_taskow = sum(self.lista_zadan)
        print(sum(self.lista_zadan))

    def solve_problem(self):

        test = Populacja(self.populacja, self.n_tasks, self.lista_zadan, self.szansa_mutacji, self.n_procent_najlepszych)

        test.stworz_populacje()
        najlepsi = []
        for _ in range(self.pokolenia):
            test.krzyzowanie()
            najlepsi.append(test.najlepszy())

        print(f'Początkowe przystowanie: {najlepsi[0]}')
        print(f'Końcowe przystowanie: {najlepsi[-1]}')

        '''pop = self.stworz_populacje()

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
        print(sum(self.lista_zadan))'''
