import datetime

# course 30 Days of Python https://www.codingforentrepreneurs.com/projects/30-days-python/ 
# Day 6 | String Formatting, Substitution & more Functions:

default_names = ["Justin", "john", "Emilee", "Jim", "Ron", "Sandra", "veronica", "Whitney"]
default_amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]

unf_message = """Hi {name}! 
Thank you for the purchase on {date}. 
We hope you are exicted about using it. Just as a
reminder the purcase total was ${total}.
Have a great one!
Team CFE
"""

# My solution:
names_amounts = dict(zip(default_names, default_amounts)) # join two list and convert a dict key value
today = datetime.date.today()
date_text = f'{today.day}/{today.month}/{today.year}' # use new style fstring python 3.6

for key, value in names_amounts.items():
    print(unf_message.format(name=key, date=date_text, total=value))


# CFE Solution https://github.com/codingforentrepreneurs/30-Days-of-Python/blob/master/Day%206
# def make_messages(names, amounts):
#     messages = []
#     if len(names) == len(amounts):
#         i = 0
#         today = datetime.date.today()
#         text = '{today.month}/{today.day}/{today.year}'.format(today=today)
#         for name in names:
#             """
#             Here's a simple solution to capitalize 
#             everyone's name prior to sending
#             """
#             name = name[0].upper() + name[1:].lower() 

#             """
#             Did you get the bonus??
#             """
            
#             new_amount = "%.2f" %(amounts[i])
#             new_msg = unf_message.format(
#                     name=name,
#                     date=text,
#                     total=new_amount
#                 )
#             i += 1
#             print(new_msg)



# make_messages(default_names, default_amounts)