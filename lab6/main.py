import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

food = ctrl.Antecedent(np.arange(0, 11, 1), 'Ужин')
service = ctrl.Antecedent(np.arange(0, 11, 1), 'Обслуживание')

tip = ctrl.Consequent(np.arange(0, 31, 1), 'Чаевые')

food['подгоревший'] = fuzz.trapmf(food.universe, [0, 0, 1, 3])
food['превосходный'] = fuzz.trapmf(food.universe, [7, 9, 10, 10])

service['плохое'] = fuzz.gaussmf(service.universe, 0, 1.5)
service['хорошее'] = fuzz.gaussmf(service.universe, 5, 1.5)
service['отличное'] = fuzz.gaussmf(service.universe, 10, 1.5)

tip['малые'] = fuzz.trimf(tip.universe, [0, 5, 10])
tip['средние'] = fuzz.trimf(tip.universe, [10, 15, 20])
tip['щедрые'] = fuzz.trimf(tip.universe, [20, 25, 30])

food.view()

service.view()

tip['щедрые'].view()

rule1 = ctrl.Rule(service['плохое'] | food['подгоревший'], tip['малые'])
rule2 = ctrl.Rule(service['хорошее'], tip['средние'])
rule3 = ctrl.Rule(service['отличное'] | food['превосходный'], tip['щедрые'])

tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

tipping.input['Ужин'] = 2.45
tipping.input['Обслуживание'] = 6.9

tipping.compute()

print(tipping.output['Чаевые'])

tip.view(sim=tipping)

unsampled = np.arange(0, 11, 1)

x, y = np.meshgrid(unsampled, unsampled)

z = np.zeros_like(x)
for i in range(11):
    for j in range(11):
        tipping.input['Ужин'] = x[i, j]
        tipping.input['Обслуживание'] = y[i, j]
        tipping.compute()
        z[i, j] = tipping.output['Чаевые']

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='viridis', linewidth=0.4, antialiased=True)

cset = ax.contourf(x, y, z, zdir='z', offset=-2.5, cmap='viridis', alpha=0.5)
cset = ax.contourf(x, y, z, zdir='x', offset=30, cmap='viridis', alpha=0.5)
cset = ax.contourf(x, y, z, zdir='y', offset=30, cmap='viridis', alpha=0.5)

ax.view_init(50, 200)
plt.show()