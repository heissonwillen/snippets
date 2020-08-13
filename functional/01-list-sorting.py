people = [
    {
        "name": "vito",
        "age": 20
    },
    {
        "name": "joshua",
        "age": 18
    },
    {
        "name": "laura",
        "age": 18
    }
]

people.sort(key=lambda person : person['age'])

for person in people:
    print(person['name'])
