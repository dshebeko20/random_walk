import matplotlib.pyplot as plt

from random_walk import Randomwalk

# Новые блуждания создаются до тех пор, пока программа остаётся активной.
while True:
    # Создание случайного блуждания.
    rw = Randomwalk()
    rw.fill_walk()

    # Нанесение точек на диаграмму.
    plt.style.use('classic')

    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)
    ax.set_aspect('equal')
    plt.show()

    keep_running = input("Make another walk? (y/n):")
    if keep_running == 'n':
        break