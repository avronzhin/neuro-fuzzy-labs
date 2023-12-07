import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

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

control_system = ctrl.ControlSystem([rule1, rule2, rule3])

control_system_simulation = ctrl.ControlSystemSimulation(control_system)

control_system_simulation.input['Посещаемость'] = 8  # Сколько пар посетил студент
control_system_simulation.input['Результативность'] = 4  # Сколько лаб сдал студент

control_system_simulation.compute()

print(control_system_simulation.output['Оценка'])

assessment.view(sim=control_system_simulation)