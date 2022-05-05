from ssl import ALERT_DESCRIPTION_ACCESS_DENIED


person = ["Deepak", "Thakur", "Ktm", "kamalpokahri"]
# print(person[0] + " " + person[1])
# print(len(person))
# animal = ["lion", "tiger"]
# print(animal)
# print(len(animal))
print(person[-1])
print(person[:3])
print(person[2:])
print(person[-4:-1])
person.insert(4,"ram")
person.append("shyam")
newPerson=["Mohan","Sita", "Gita"]
person.extend(newPerson)
print(person)
person.remove("Gita")
print(person)
# person.pop(1)
print(person)
person.pop()
print(person)
person.pop()
print(person)
person.clear()
print(person)
