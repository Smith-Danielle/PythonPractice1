# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"""
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""

def sortme(words):
    dictionary = {}
    for x in range(len(words)):
        dictionary.update({x: words[x].lower()})
    from operator import itemgetter
    ordered = sorted(dictionary.items(), key=itemgetter(1))
    originalValues = [words[x[0]] for x in ordered]
    return originalValues


def max_and_min(arr1,arr2):
    longest = []
    shortest = []
    values = []
    if len(arr1) > len(arr2):
        longest = arr1
        shortest = arr2
    else:
        longest = arr2
        shortest = arr1
    for x in longest:
        for y in shortest:
            dif = abs(x - y)
            if dif not in values:
                values += [dif]
    return [max(values), min(values)]


def recoverSecret(triplets):
    letters = []
    for x in triplets:
        for y in x:
            if y not in letters:
                letters += [y]
    if len(letters) > 10:
        letters.sort()
    for z in triplets:
        for i in range(len(z)):
            if i != len(z) - 1:
                if letters.index(z[i]) > letters.index(z[i + 1]):
                    letters.remove(z[i])
                    letters.insert(letters.index(z[i + 1]), z[i])
    return ''.join(letters)


