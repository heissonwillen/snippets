import requests
from math import sqrt
from statistics import median, mean, stdev, mode, variance

urls = [
    'https://www.corona.ma.gov.br/public/api/casos/confirmados.json',
    'https://www.corona.ma.gov.br/public/api/casos/obitos.json',
    'http://coronavirus.pi.gov.br/public/api/casos/confirmados.json',
    'http://coronavirus.pi.gov.br/public/api/casos/obitos.json',
]

def describe(url):
    data = requests.get(url)
    cases = data.json()
    cases[0]['novos'] = 0
    new_cases = [0]
    
    for i in range(1, len(cases)):
        cases[i]['quantidade'] = int(cases[i]['quantidade'])
        new_cases.append(int(cases[i]['quantidade']) - int(cases[i-1]['quantidade']))

    print(f'median: {median(new_cases)}')
    print(f'mean: {mean(new_cases)}')
    print(f'stdev: {stdev(new_cases)}')
    print(f'variance: {variance(new_cases)}')
    print(f'mode: {mode(new_cases)}')
    print(f'max: {max(new_cases)}, {cases[new_cases.index(max(new_cases))]["data"].split("T")[0] }')
    print(f'min: {min(new_cases)}, {cases[new_cases.index(min(new_cases))]["data"].split("T")[0] }\n')

if __name__ == '__main__':
    for url in urls:
        print(url)
        describe(url)