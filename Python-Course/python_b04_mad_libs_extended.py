#Topic: Getting an input from the user. Mad Libs game.

# You are the sun that shines brightly throughout my day.
# You are the gravity that holds me down in every way.
# You are the moon that shimmers throughout my night.
# You are stars that glimmer oh so bright.

# Source: https://www.familyfriendpoems.com/poem/forever-and-always-poem

action_01 = input('Enter an action in third person: ')
body_part_01 = input('Enter a body part: ')
noun_01 = input('Enter a singular noun: ')
action_02 = input('Enter another action in third person: ')
noun_02 = input('Enter an animal: ')
body_part_02 = input('Enter a body part: ')
celebrity = input('Enter a celebrity: ')
adjective = input('Enter an adjective: ')

print('You are the sun that ' + action_01 + ' throughout my ' + body_part_01 + ',')
print('you are the ' + noun_01 + ' that ' + action_02 +' in every way,')
print('you are the ' + noun_02 + ' that shimmers throughout my ' + body_part_02 + ',')
print('You are ' + celebrity + ' that glimmer oh so ' + adjective+ '.')