omelet_ingredients = {}
omelet_ingredients["egg"] = 2
omelet_ingredients["mushroom"] = 5
omelet_ingredients["pepper"] = 1
omelet_ingredients["cheese"] = 1
omelet_ingredients["milk"] = 1

print "Omelet Ingredients and their quantities are \n%s" %omelet_ingredients
print "Ingredients are \n%s" %omelet_ingredients.keys()
print "Values \n%s" %omelet_ingredients.values()

ingredients = omelet_ingredients.keys()
print "Ingredients again are \n%s" %ingredients

while len(ingredients) > 0:
	current_ingredient = ingredients.pop()
	print "Adding %d %s to the mix." %(omelet_ingredients[current_ingredient],current_ingredient)


