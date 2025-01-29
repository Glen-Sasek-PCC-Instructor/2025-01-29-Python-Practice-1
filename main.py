




# RESTAURANT NEAR ME PREFERENCES
# Vegetarian  [y/n] y
# Vegan       [y/n] N
# Gluten-Free [y/n] y

# RESTAURANTS WITH YOUR PREFERENCES:
# Bamboo Sushi 
# Grassa
# Oven and Shaker

glutenFree = False # Boolean
vegetarian = False # Boolean
vegan      = False # Boolean

bambooSushi = "Bamboo Sushi"
grassa = "Grassa"
ovenAndShaker = "Oven and Shaker"
screenDoor = "Screen Door"
verdeCocina = "Verde Cocina"

# MESSAGE "RESTAURANT NEAR ME PREFERENCES"
print("RESTAURANT NEAR ME PREFERENCES")

# PROMPT  "Vegetarian  [y/n] y"
# INPUT    vegetarian
vegetarian = input('Vegetarian  [y/n]  ').lower() == 'y'

# PROMPT  "Vegan  [y/n] y"
# INPUT    vegan
vegan = input('Vegan  [y/n]  ').lower() == 'y'

# PROMPT  "Gluten-Free  [y/n] y"
# INPUT    glutenFree
glutenFree = input('Gluten-Free  [y/n]  ').lower() == 'y'

# FILTER by matching property table SEE CALCULATIONS
#                     Vegetarian  Vegan   Gluten-Free
# Bamboo Sushi        Yes         Yes     Yes 
# Grassa              Yes         No      Yes
# Oven and Shaker     Yes         Yes     Yes
# Screen Door         No          No      No
# Verde Cocina        Yes         No      No

print(bambooSushi)

if(not vegan):
    print(grassa)

print(ovenAndShaker)

if(not (vegan or vegetarian or glutenFree)):
    print(screenDoor)

if(not vegetarian):
    print(verdeCocina)

# Display results, see sample run.
