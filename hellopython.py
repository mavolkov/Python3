from pylab import *
from matplotlib import *

x = linspace(0, 5, 10)
y = x**2
print(x)
print(y)
'''
# способ построение графика 1
# %matplotlib inline #не сработало(должно построить прям в консоле?)
figure()
plot(x, y, 'black')
xlabel('x')
ylabel('y')
title('title')
show()
'''

'''
# способ построения графика 2
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

axes.plot(x, y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title1')  # чтобы не отображалась строка <matplotlib.text.Text at ...> в конце можно
show()
'''

'''
# строим 2 графика сразу
fig = plt.figure()

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # main axes
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])  # inset доп axes

# main figure
axes1.plot(x, y, 'r')
axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title('title')

# insert
axes2.plot(y, x, 'g')
axes2.set_xlabel('x')
axes2.set_ylabel('y')
axes2.set_title('insert title');

show()  # показываем все
'''

'''
# строим 2 графика отдельно 
fig, axes = plt.subplot(nrows=1, ncols=2)  # не заработало...
for ax in axes:
    ax.plot(x, y, 'r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('title')
fig.tight_layout()
'''

'''
# с регулировкой размера 
fig = plt.subplot(figsize=(12, 3))  # не заработало..
axes = plt.subplot(figsize=(12, 3))
axes.plot(x, y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title')
# show()
'''




