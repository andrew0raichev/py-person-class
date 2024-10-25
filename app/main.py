class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people_list: list):
    person_objects = []

    for data in people_list:
        person = Person(data["name"], data["age"])
        person_objects.append(person)

    for data in people_list:
        person = Person.people[data["name"]]

        if "wife" in data and data["wife"] is not None:
            person.wife = Person.people[data["wife"]]

        if "husband" in data and data["husband"] is not None:
            person.husband = Person.people[data["husband"]]

    return person_objects
