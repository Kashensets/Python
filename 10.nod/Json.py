import requests
import json
from collections import Counter
import matplotlib.pyplot as plt

# Fetch recipes from the API
url = "https://dummyjson.com/recipes"
response = requests.get(url)
recipes = response.json()['recipes']

# 1a. Extract 5 recipes containing potatoes
potato_recipes = [recipe for recipe in recipes if 'potato' in recipe['ingredients'].lower()]
potato_recipes = potato_recipes[:5]

# Save to JSON file
with open('potato_recipes.json', 'w') as file:
    json.dump(potato_recipes, file, indent=4)

# 1b. Extract all soup recipes
soup_recipes = [recipe for recipe in recipes if recipe['mealType'] == 'soup']

# Save to JSON file
with open('soup_recipes.json', 'w') as file:
    json.dump(soup_recipes, file, indent=4)

# 1c. Create a list of all ingredients
all_ingredients = []
for recipe in recipes:
    all_ingredients.extend(recipe['ingredients'].split(','))

# 1d. Find the most used ingredients
ingredient_counter = Counter(all_ingredients)
top_5_ingredients = ingredient_counter.most_common(5)

# Print top 5 ingredients
print("Top 5 ingredients:")
for ingredient, count in top_5_ingredients:
    print(f"{ingredient.strip()}: {count}")

# 1e. Plot a histogram of the top 10 ingredients
top_10_ingredients = ingredient_counter.most_common(10)
ingredients, counts = zip(*top_10_ingredients)

plt.bar(ingredients, counts, color='blue')
plt.xlabel('Ingredients')
plt.ylabel('Count')
plt.title('Top 10 Ingredients in Recipes')
plt.xticks(rotation=45, ha='right')
plt.show()
