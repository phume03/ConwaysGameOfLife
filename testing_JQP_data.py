from pprint import pprint

def initial_transform(data):
    """
    Flatten nested dicts
    """
    for item in list(data):
        if type(item) is dict:
            print("item is dict!")
            pprint(item)
            for key in item:
                data[key] = item[key]
                
    outside_module.do_something()
    return data


def final_transform(transformed_data):
    """
    Transform address structures into a single structure
    """
    transformed_data['address'] = str.format(
        "{0}\n{1}, {2} {3}", transformed_data['street'], 
        transformed_data['state'], transformed_data['city'], 
        transformed_data['zip'])

    return transformed_data


def print_person(person_data):
    parents = "and".join(person_data['parents'])
    siblings = "and".join(person_data['siblings'])
    person_string = str.format(
        "Hello, my name is {0}, my siblings are {1}, "
        "my parents are {2}, and my mailing"
        "address is: \n{3}", person_data['name'], 
        parents, siblings, person_data['address'])
    print(person_string)


john_data = {
    'name': 'John Q. Public',
    'street': '123 Main St.',
    'city': 'Anytown',
    'state': 'FL',
    'zip': 99999,
    'relationships': {
        'siblings': ['Michael R. Public', 'Suzy Q. Public'],
        'parents': ['John Q. Public Sr.', 'Mary S. Public'],
    }
}

suzy_data = {
    'name': 'Suzy Q. Public',
    'street': '456 Broadway',
    'apt': '333',
    'city': 'Miami',
    'state': 'FL',
    'zip': 33333,
    'relationships': {
        'siblings': ['John Q. Public', 'Michael R. Public', 
                    'Thomas Z. Public'],
        'parents': ['John Q. Public Sr.', 'Mary S. Public'],
    }
}

inputs = [john_data, suzy_data]

for input_structure in inputs:
    initial_transformed = initial_transform(input_structure)
    final_transformed = final_transform(initial_transformed)
    pprint(final_transformed)
    #print_person(final_transformed)

