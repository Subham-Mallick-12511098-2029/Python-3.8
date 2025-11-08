mountains=["Himalayas","K2","Kanchenjunga","Mount Everest","Nanda Devi","Nanga Parvat"]
rivers=["Ganges","Brahmaputra","Yamuna","Indus","Godavari","Narmada","Sabarmati","Krishna"]
countries=["India","China","North America","South America","Russia","South Korea","Japan","Israel"]
cities=["Delhi","Mumbai","Kolkata","Bengaluru","Gujurat"]

print("Accessing Elements-------------------")

print(mountains[3])
print(rivers[0])
print(countries[0])

print("Modifying Elements  in list------------")

print(cities)
cities[1]="Rajasthan"
print(cities)

print("Adding elements to a list--------------")

print(mountains)
mountains.append("Katwa")
print(mountains)

print("Inserting elements in a list----------------")

print(cities)
cities.insert(0,"Kerela")
print(cities)

print("Sorting a list ------------------------------")
print(mountains)
print(sorted(mountains))

print("Finding a length of list ------------------")

print(mountains)
print("Length os list is ", len(mountains))


