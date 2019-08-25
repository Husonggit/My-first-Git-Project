sandwich_olders = ['Xiaochaorou', 'Dapanji', 'Zhouzi', 'Hongshaoyu']

finished_sandwich = []

while sandwich_olders:
    sandwich = sandwich_olders.pop()
    print("I made your " + sandwich + " sandwich! ")

    finished_sandwich.append(sandwich)

for finish in finished_sandwich:
    print("The " + finish + " has finished! ")