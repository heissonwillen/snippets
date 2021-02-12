import matplotlib.pyplot as plt

names = ['2016', '2017', '2018']
values_list = [
    [55.0, 63.8, 64.2],
    [58.6, 63.6, 65.0],
    [65.3, 64.1, 57.8],
    [61.0, 54.3, 52.5],
    [60.0, 56.3, 52.3],
]

for index, values in enumerate(values_list):
    plt.plot(names, values, label=str(index+1))

plt.legend(loc='lower left')
# plt.show()
plt.savefig('plot.png')
