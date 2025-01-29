




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
temp = input('Vegetarian  [y/n]  ').lower() or "n"
vegetarian = temp[0] == 'y'

# PROMPT  "Vegan  [y/n] y"
# INPUT    vegan
try:
    vegan = input('Vegan  [y/n]  ').lower()[0] == 'y'
except Exception as e:
    vegan = False

# PROMPT  "Gluten-Free  [y/n] y"
# INPUT    glutenFree
temp = input('Vegetarian  [y/n]  ').lower() 
glutenFree = len(temp) >= 1 and temp[0] == 'y'

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
