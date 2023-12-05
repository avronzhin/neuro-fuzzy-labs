import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

attendance = ctrl.Antecedent(np.arange(0, 17, 1), 'Посещаемость')
performance = ctrl.Antecedent(np.arange(0, 9, 1), 'Результативность')
assessment = ctrl.Consequent(np.arange(2, 6, 1), 'Оценка')

attendance['Хорошая'] = fuzz.trapmf(attendance.universe, [12, 16, 16, 16])
attendance['Плохая'] = fuzz.trapmf(attendance.universe, [0, 0, 1, 4])

# Задать нормальные функции принадлежности
performance['Высокая'] = fuzz.gaussmf(performance.universe, 0, 1.5)
performance['Средняя'] = fuzz.trapmf(performance.universe, [3, 4, 5, 6])
performance['Низкая'] = fuzz.gaussmf(performance.universe, 5, 1.5)

assessment['Отличная'] = fuzz.trimf(assessment.universe, [4, 5, 5])
assessment['Нормальная'] = fuzz.trimf(assessment.universe, [3, 4, 4])
assessment['Ужасная'] = fuzz.trimf(assessment.universe, [2, 2, 3])

attendance.view()
performance.view()
assessment.view()

# assessment['Отличная'].view()

# Нет возможности задавать всес правила
rule1 = ctrl.Rule(performance['Низкая'] & ~attendance['Хорошая'], assessment['Ужасная'])
rule2 = ctrl.Rule(performance['Высокая'], assessment['Отличная'])
rule3 = ctrl.Rule(performance['Средняя'] | attendance['Хорошая'], assessment['Нормальная'])

control_system = ctrl.ControlSystem([rule1, rule2, rule3])

control_system_simulation = ctrl.ControlSystemSimulation(control_system)

control_system_simulation.input['Посещаемость'] = 16 # Сколько пар посетил студент
control_system_simulation.input['Результативность'] = 8 # Сколько лаб сдал студент

control_system_simulation.compute()

print(control_system_simulation.output['Оценка'])

assessment.view(sim=control_system_simulation)

unsampled1 = np.arange(0, 9, 1)
unsampled2 = np.arange(0, 17, 1)

x, y = np.meshgrid(unsampled1, unsampled2)

z = np.zeros_like(x)
for i in range(17):
    for j in range(9):
        control_system_simulation.input['Посещаемость'] = x[i, j]
        control_system_simulation.input['Результативность'] = y[i, j]
        control_system_simulation.compute()
        z[i, j] = control_system_simulation.output['Оценка']

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='viridis', linewidth=0.4, antialiased=True)

cset = ax.contourf(x, y, z, zdir='z', offset=-2.5, cmap='viridis', alpha=0.5)
cset = ax.contourf(x, y, z, zdir='x', offset=30, cmap='viridis', alpha=0.5)
cset = ax.contourf(x, y, z, zdir='y', offset=30, cmap='viridis', alpha=0.5)

ax.view_init(50, 200)
plt.show()