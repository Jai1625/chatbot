# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
    import json

    # Opening JSON file
    f = open('/Users/jayakumar/Downloads/TemplateStore.json')

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    count = 1
    lis = ['Tp4hCWjZXbAK', 'Tp4VocgmVjxO', 'Tl3xeLVXjiaFU', 'TlzCeLVRWTF__', 'TlI3WGzFWOoFg', 'TlkVWGzFWd2wM', 'TlAuWGzFcUjB_'
           'TliNWGzFCPfHJ', 'TlH6WGzF0LjBi', 'TlrlWGzF5E0kI', 'Tl9ljvPoLJWux','Tl9kRd1LTy0jL','Tl8NzZaKG6ZWI', 'Tl7IwXhMpI1px',
           'Tl7B_iggrfZup', 'Tl6SKMtAAzNNV', 'Tl5DVLhhTUFs2', 'Tl4DnSxxjfKtb', 'Tl3TRJvDAtlT1', 'Tl0gRd1uOa7cq', 'Tl0TVLhdFCcpE'
           'Tl0G7zLH92n7_', 'Tl0DuWqbpYKFN', 'TlzGeLVRarxam', 'TlEfWGzFFRLx7', 'TlbeWGzF2McGB', 'Tl1DWGzFjI8Dy', 'TlVtWGzFvAapB',
           'TlrRWGzF6F7Sz', 'TlyIWGzFryYQc', 'TlwhWGzFgq0Rh']
    for i in data['values']:
        if i.get('FlowType') == 'Process' and i.get('_id') not in lis:
            json_object = json.dumps(i, indent=4)
            count += 1
            file_name = "process" + str(count) + i.get('FlowType') +".json"
            with open(file_name, "x") as outfile:
                outfile.write(json_object)

            print(i)