import csv
from statistics import median, mean, stdev, mode, variance

with open('datasets/obitos-sp.csv', 'r') as data_file:
    reader = csv.reader(data_file, delimiter=';')
    new_cases = []
    new_deaths = []

    for row in reader:
        try:
            new_cases.append(int(row[2]))
        except ValueError:
            new_cases.append(int(0))

        try:
            new_deaths.append(int(row[3]))
        except ValueError:
            new_deaths.append(int(0))

print(f'median: {median(new_cases)}')
print(f'mean: {mean(new_cases)}')
print(f'stdev: {stdev(new_cases)}')
print(f'variance: {variance(new_cases)}')
print(f'mode: {mode(new_cases)}')
print(f'max: {max(new_cases)}')