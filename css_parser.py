import random
import cssutils

favorite_colour = ['#782727', '#277872', '#632778', '#46198d', '#8d1954']

new_colour = random.choice(favorite_colour)

# Parse the stylesheet, replace color
parser = cssutils.parseFile('style.css')
for replace in parser.cssRules:
    if replace.selectorText == '#dev':
        replace.style.backgroundColor = f'{new_colour}'  # Replace background

# Write to a new file
with open('style.css', 'wb') as file:
    file.write(parser.cssText)
