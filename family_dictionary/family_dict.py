# Define a dictionary that contains information about several members of your family. Use the following example as a template.

my_family = {
    'mother': {
        'name': 'Karen',
        'age': 63
    },
    'father': {
        'name': 'Mike',
        'age': 63
    },
    'brother': {
        'name': 'Colin',
        'age': 36
    },
    'sister': {
        'name': 'Emily',
        'age': 23
    }
}


# Using dictionary comprehension, produce output

for key, value in my_family.items():
    print(key, value["name"], value["age"])


family_string = {"My " + key + " named " + value["name"] + " is " + str(value["age"]) + " years old" for (key,value) in my_family.items()}

print(family_string)


