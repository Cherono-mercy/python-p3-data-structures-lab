spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]
'''
Define a function get_names() that takes a list of spicy_foods 
and returns a list of strings with the names of each spicy food.
'''
def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

'''
Define a function get_spiciest_foods() that takes a list of spicy_foods 
and returns a list of dictionaries where the heat level of the food is greater than 5.
'''
def get_spiciest_foods(spicy_foods):
     return [food for food in spicy_foods if food["heat_level"] > 5]

'''
Define a function print_spicy_foods() that takes a list of spicy_foods 
and output to the terminal each spicy food in the following format using print():
 Buffalo Wings (American) | Heat Level: 🌶🌶🌶.

HINT: you can use times (*) with a stringLinks to an external site. to produce the correct number of "🌶" emojis.
'''
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level_emojis = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")

'''
Define a function get_spicy_food_by_cuisine() that takes a list of spicy_foods and a string representing a cuisine,
 and returns a single dictionary for the spicy food whose cuisine matches the cuisine being passed to the method.
 '''
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"].lower() == cuisine.lower():
            return food
    return None

'''
Define a function print_spiciest_foods() that takes a list of spicy_foods 
and outputs to the terminal ONLY the spicy foods that have a heat level greater than 5, in the following format:

Buffalo Wings (American) | Heat Level: 🌶🌶🌶.

Try to use functions you've already written to solve this!
'''
def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    if spiciest_foods:
        print_spicy_foods(spiciest_foods)
    else:
         print("No spiciest foods found.")    

'''
Define a function average_heat_level() that takes a list of spicy_foods 
and returns an integer representing the average heat level of all the spicy foods in the array. 
Recall that to derive the average of a collection, you need to calculate the total 
and divide number of elements in the collection.
'''
def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0  # Return 0 for an empty list to avoid division by zero
     
         
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    average_heat = total_heat / len(spicy_foods)
    return int(average_heat)  # Return the average as an integer

'''
 A function create_spicy_food that returns original list of spicy_foods with new spicy_food added
'''
def create_spicy_food(spicy_foods, spicy_food):
    return spicy_foods + [spicy_food]
