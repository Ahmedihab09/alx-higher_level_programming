import marshal
import types

def print_names():
    with open('hidden_4.pyc', 'rb') as file:
        code_object = marshal.load(file)

    # Extract names
    names = set()
    for name, value in code_object.co_names.items():
        if not name.startswith('__'):
            names.add(name)

    # Print names in alphabetical order
    for name in sorted(names):
        print(name)

if __name__ == "__main__":
    print_names()

