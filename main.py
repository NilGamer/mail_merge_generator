PLACEHOLDER = "[name]"

# get the starting letter
with open('input/Letters/starting_letter.txt') as file:
    letter = file.read()

# get all the names
with open('input/Names/invited_names.txt') as file:
    names = file.readlines()
    allname = []

    # get individual name from names
    for name in names:
        allname.append(name.strip())

    # create letter for each name
    for name in allname:
        with open(f'Output/ReadyToSend/{name}_mail', mode='w') as file:
            file.write(letter.replace(PLACEHOLDER,name))
