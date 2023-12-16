import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt


# Лингвистические переменные
attendance = ctrl.Antecedent(np.arange(0, 17, 1), 'Посещаемость')
performance = ctrl.Antecedent(np.arange(0, 9, 1), 'Результативность')
assessment = ctrl.Consequent(np.arange(2, 5.1, 0.1), 'Оценка')

# Термы
# Посещаемость
attendance['Хорошая'] = fuzz.smf(attendance.universe, 5, 16)
attendance['Плохая'] = fuzz.zmf(attendance.universe, 0, 7)

# Результативность
performance['Высокая'] = fuzz.smf(performance.universe, 6, 7)
performance['Средняя'] = fuzz.pimf(performance.universe, 1, 3, 5, 7)
performance['Низкая'] = fuzz.zmf(performance.universe, 0, 3)

# Оценка
assessment['Отличная'] = fuzz.smf(assessment.universe, 4, 4.9)
assessment['Нормальная'] = fuzz.pimf(assessment.universe, 2.7, 3.5, 3.7, 4.3)
assessment['Ужасная'] = fuzz.zmf(assessment.universe, 2, 3.4)

attendance.view()
performance.view()
assessment.view()

# Правила
# rule1 = ctrl.Rule(performance['Высокая'] & ~attendance['Плохая'], assessment['Отличная'])
# rule2 = ctrl.Rule(performance['Низкая'], assessment['Ужасная'])
# rule3 = ctrl.Rule(performance['Средняя'], assessment['Нормальная'])
# rule4 = ctrl.Rule(performance['Высокая'] & attendance['Плохая'], assessment['Нормальная'])

# control_system = ctrl.ControlSystem([rule1, rule2, rule3, rule4])

rule1 = ctrl.Rule(attendance['Хорошая'] & performance['Высокая'], assessment['Отличная'])
rule2 = ctrl.Rule(attendance['Плохая'] & performance['Высокая'], assessment['Нормальная'])
rule3 = ctrl.Rule(attendance['Хорошая'] & performance['Средняя'], assessment['Нормальная'])
rule4 = ctrl.Rule(attendance['Плохая'] & performance['Средняя'], assessment['Ужасная'])
rule5 = ctrl.Rule(attendance['Хорошая'] & performance['Низкая'], assessment['Ужасная'])
rule6 = ctrl.Rule(attendance['Плохая'] & performance['Низкая'], assessment['Ужасная'])

control_system = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6])

control_system_simulation = ctrl.ControlSystemSimulation(control_system)

control_system_simulation.input['Посещаемость'] = 16  # Сколько пар посетил студент
control_system_simulation.input['Результативность'] = 8  # Сколько лаб сдал студент

control_system_simulation.compute()

print(control_system_simulation.output['Оценка'])

assessment.view(sim=control_system_simulation)

resultiveness_values = np.arange(0, 9, 1)
attendance_values = np.arange(0, 17, 1)

resultiveness_mesh, attendance_mesh = np.meshgrid(resultiveness_values, attendance_values)

assessment_values = np.zeros_like(resultiveness_mesh)
for i in range(len(resultiveness_values)):
    for j in range(len(attendance_values)):
        control_system_simulation.input['Посещаемость'] = attendance_values[j]
        control_system_simulation.input['Результативность'] = resultiveness_values[i]
        control_system_simulation.compute()
        assessment_values[j, i] = control_system_simulation.output['Оценка']

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

surface = ax.plot_surface(resultiveness_mesh, attendance_mesh, assessment_values, cmap='viridis')

ax.set_xlabel('Результативность')
ax.set_ylabel('Посещаемость')
ax.set_zlabel('Оценка')

fig.colorbar(surface, ax=ax, shrink=0.5, aspect=10)

plt.show()
