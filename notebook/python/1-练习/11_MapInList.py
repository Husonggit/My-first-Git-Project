
# pizza = {
#     'crust' : 'thick',
#     'toppings' : ['mushrooms', 'extra cheese'],
# }

# print("crust = " + pizza['crust'])

# print(pizza['toppings'])

# for topping in pizza['toppings']:
#     print("topping = " + topping)

favorite_languages = {
    'jen' : ['python', 'ruby', 'java'],
    'sarah' : ['c', 'c++'],
    'edward' : ['ruby'],
    'phil' : ['python', 'haskell'],
}

for name,languages in favorite_languages.items():
    if len(languages) >= 2:
        print("\n" + name.title() + "s favorite languages are :")
        for language in languages:
            print("\t" + language.title())
    else:
        # print()
        # print(type(languages))
        print("\n" + name.title() + "s favorite languages are : " + str(languages[0].title()))


            

    

