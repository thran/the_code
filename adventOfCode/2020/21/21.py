# start 8:23, 1. 8:45, 2. 8:55
from collections import defaultdict
from pathlib import Path

from parse import parse


all_ingredients = set()
all_allergens = set()
ingredients_list = []
with Path('input.txt').open() as file:
    for line in file:
        results = parse('{ingredients} (contains {allergens})', line.strip())
        allergens = set(results['allergens'].split(', '))
        ingredients = set(results['ingredients'].split())
        ingredients_list.append((ingredients, allergens))
        all_allergens |= allergens
        all_ingredients |= ingredients
possible_mapping = {ing: set(all_allergens) for ing in all_ingredients}


for ings, als in ingredients_list:
    for ing in all_ingredients - ings:
        possible_mapping[ing] -= als

good_ingredients = {ing for ing, als in possible_mapping.items() if len(als) == 0}
print(sum(1 for ings, _ in ingredients_list for ing in ings if ing in good_ingredients))


bad_ingredients = {ing: als for ing, als in possible_mapping.items() if als}
resolved = {}
while bad_ingredients:
    for ing, als in bad_ingredients.items():
        if len(als) == 1:
            resolved[next(iter(als))] = ing
            del bad_ingredients[ing]
            for aas in bad_ingredients.values():
                aas -= als
            break

print(','.join(ing for _, ing in sorted(resolved.items())))
