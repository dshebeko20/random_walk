import matplotlib.pyplot as plt

from random_walk import Randomwalk

# Создание случайного блуждания.
rw = Randomwalk()
rw.fill_walk()

# Нанесение точек на диаграмму.
plt.style.use('classic')

fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
ax.set_aspect('equal')
plt.show()