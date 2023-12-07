import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Лингвистические переменные
attendance = ctrl.Antecedent(np.arange(0, 17, 1), 'Посещаемость')
performance = ctrl.Antecedent(np.arange(0, 9, 1), 'Результативность')
assessment = ctrl.Consequent(np.arange(2, 5.1, 0.1), 'Оценка')

# Термы
# Посещаемость
attendance['Хорошая'] = fuzz.smf(attendance.universe, 5, 16)
attendance['Плохая'] = fuzz.zmf(attendance.universe, 0, 7)

# Результативность
performance['Высокая'] = fuzz.smf(performance.universe, 3, 7)
performance['Средняя'] = fuzz.pimf(performance.universe, 1, 3, 4, 5)
performance['Низкая'] = fuzz.zmf(performance.universe, 0, 3)

# Оценка
assessment['Отличная'] = fuzz.smf(assessment.universe, 4, 4.9)
assessment['Нормальная'] = fuzz.pimf(assessment.universe, 2.7, 3.5, 3.7, 4.3)
assessment['Ужасная'] = fuzz.zmf(assessment.universe, 2, 3.4)

attendance.view()
performance.view()
assessment.view()
# assessment['Отличная'].view()

# Правила
rule1 = ctrl.Rule(performance['Высокая'] & ~attendance['Плохая'], assessment['Отличная'])
rule2 = ctrl.Rule(performance['Низкая'], assessment['Ужасная'])
rule3 = ctrl.Rule(performance['Средняя'], assessment['Нормальная'])
rule4 = ctrl.Rule(performance['Высокая'] & attendance['Плохая'], assessment['Нормальная'])

control_system = ctrl.ControlSystem([rule1, rule2, rule3, rule4])

control_system_simulation = ctrl.ControlSystemSimulation(control_system)

control_system_simulation.input['Посещаемость'] = 8  # Сколько пар посетил студент
control_system_simulation.input['Результативность'] = 4  # Сколько лаб сдал студент

control_system_simulation.compute()

print(control_system_simulation.output['Оценка'])

assessment.view(sim=control_system_simulation)

# Генерация значений для построения поверхности
resultiveness_values = np.arange(0, 9, 1)
attendance_values = np.arange(0, 17, 1)

# Создание сетки для значений Результативность и Посещаемость
resultiveness_mesh, attendance_mesh = np.meshgrid(resultiveness_values, attendance_values)

# Вычисление значений для Оценки с использованием выделенной нечеткой системы
assessment_values = np.zeros_like(resultiveness_mesh)
for i in range(len(resultiveness_values)):
    for j in range(len(attendance_values)):
        control_system_simulation.input['Посещаемость'] = attendance_values[j]
        control_system_simulation.input['Результативность'] = resultiveness_values[i]
        control_system_simulation.compute()
        # Используйте i и j в обратном порядке при присвоении значений
        assessment_values[j, i] = control_system_simulation.output['Оценка']

# Построение 3D графика
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Построение поверхности
surface = ax.plot_surface(resultiveness_mesh, attendance_mesh, assessment_values, cmap='viridis')

# Добавление подписей осей
ax.set_xlabel('Результативность')
ax.set_ylabel('Посещаемость')
ax.set_zlabel('Оценка')

# Добавление цветовой шкалы
fig.colorbar(surface, ax=ax, shrink=0.5, aspect=10)

plt.show()
