import random
import cssutils

favorite_color = ['#782727', '#277872', '#632778', '#46198d', '#8d1954']

# random choice one favourite hex color
new_colour = random.choice(favorite_color)

# Parse the stylesheet
parser = cssutils.parseFile('style.css')

# Replace background color
for replace in parser.cssRules:
    if replace.selectorText == '#dev':
        replace.style.backgroundColor = f'{new_colour}'

# Write to a new file
with open('style.css', 'wb') as file:
    file.write(parser.cssText)
