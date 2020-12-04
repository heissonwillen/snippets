import requests
from math import sqrt
from statistics import median, mean, stdev, mode

MA_CONFIRMED = 'https://www.corona.ma.gov.br/public/api/casos/confirmados.json'
MA_DEATHS = 'https://www.corona.ma.gov.br/public/api/casos/obitos.json'

PI_CONFIRMED = 'http://coronavirus.pi.gov.br/public/api/casos/confirmados.json'
PI_DEATHS = 'http://coronavirus.pi.gov.br/public/api/casos/obitos.json'

def describe(endpoint):
    data = requests.get(endpoint)
    data_list = data.json()

    for i in range(len(data_list)):
        data_list[i]['quantidade'] = int(data_list[i]['quantidade'])
        if i == 0:
            data_list[i]['novos'] = 0
        else:
            data_list[i]['novos'] = int(data_list[i]['quantidade']) - int(data_list[i-1]['quantidade'])

    new = [x['novos'] for x in data_list]

    print(f'median: {median(new)}')
    print(f'mean: {mean(new)}')
    print(f'stdev: {stdev(new)}')
    print(f'mode: {mode(new)}')
    print(f'max: {max(new)}, {data_list[new.index(max(new))]["data"].split("T")[0] }')
    print(f'min: {min(new)}, {data_list[new.index(min(new))]["data"].split("T")[0] }')
    print()

if __name__ == '__main__':
    describe(MA_CONFIRMED)
    describe(MA_DEATHS)
    describe(PI_CONFIRMED)
    describe(PI_DEATHS)
