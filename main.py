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

def block_print(string):
    alpha = {' ': ['     ', '     ', '     ', '     ', '     ', '     ', '     '], 'a': [' AAA ', 'A   A', 'A   A', 'AAAAA', 'A   A', 'A   A', 'A   A'], 'b': ['BBBB ', 'B   B', 'B   B', 'BBBB ', 'B   B', 'B   B', 'BBBB '], 'c': [' CCC ', 'C   C', 'C    ', 'C    ', 'C    ', 'C   C', ' CCC '], 'd': ['DDDD ', 'D   D', 'D   D', 'D   D', 'D   D', 'D   D', 'DDDD '], 'e': ['EEEEE', 'E    ', 'E    ', 'EEEEE', 'E    ', 'E    ', 'EEEEE'], 'f': ['FFFFF', 'F    ', 'F    ', 'FFFFF', 'F    ', 'F    ', 'F    '], 'g': [' GGG ', 'G   G', 'G    ', 'G GGG', 'G   G', 'G   G', ' GGG '], 'h': ['H   H', 'H   H', 'H   H', 'HHHHH', 'H   H', 'H   H', 'H   H'], 'i': ['IIIII', '  I  ', '  I  ', '  I  ', '  I  ', '  I  ', 'IIIII'], 'j': ['JJJJJ', '    J', '    J', '    J', '    J', '    J', 'JJJJ '], 'k': ['K   K', 'K  K ', 'K K  ', 'KK   ', 'K K  ', 'K  K ', 'K   K'], 'l': ['L    ', 'L    ', 'L    ', 'L    ', 'L    ', 'L    ', 'LLLLL'], 'm': ['M   M', 'MM MM', 'M M M', 'M   M', 'M   M', 'M   M', 'M   M'], 'n': ['N   N', 'NN  N', 'N   N', 'N N N', 'N   N', 'N  NN', 'N   N'], 'o': [' OOO ', 'O   O', 'O   O', 'O   O', 'O   O', 'O   O', ' OOO '], 'p': ['PPPP ', 'P   P', 'P   P', 'PPPP ', 'P    ', 'P    ', 'P    '], 'q': [' QQQ ', 'Q   Q', 'Q   Q', 'Q   Q', 'Q Q Q', 'Q  QQ', ' QQQQ'], 'r': ['RRRR ', 'R   R', 'R   R', 'RRRR ', 'R R  ', 'R  R ', 'R   R'], 's': [' SSS ', 'S   S', 'S    ', ' SSS ', '    S', 'S   S', ' SSS '], 't': ['TTTTT', '  T  ', '  T  ', '  T  ', '  T  ', '  T  ', '  T  '], 'u': ['U   U', 'U   U', 'U   U', 'U   U', 'U   U', 'U   U', ' UUU '], 'v': ['V   V', 'V   V', 'V   V', 'V   V', 'V   V', ' V V ', '  V  '], 'w': ['W   W', 'W   W', 'W   W', 'W W W', 'W W W', 'W W W', ' W W '], 'x': ['X   X', 'X   X', ' X X ', '  X  ', ' X X ', 'X   X', 'X   X'], 'y': ['Y   Y', 'Y   Y', ' Y Y ', '  Y  ', '  Y  ', '  Y  ', '  Y  '], 'z': ['ZZZZZ', '    Z', '   Z ', '  Z  ', ' Z   ', 'Z    ', 'ZZZZZ']}
    blocked = ""
    string = string.strip()
    if len(string) == 0:
        return ''
    for x in range(7):
        for y in string:
            blocked += alpha[y.lower()][x] + ' '
        while blocked[len(blocked) - 1] == " ":
            blocked = blocked[:-1]
        blocked += "\n"
    return blocked[:-1]

def max_sum(arr,ranges):
    max_values = []
    for x in ranges:
        index = x[0]
        temp_max = 0
        while index <= x[1]:
            temp_max += arr[index]
            index += 1
        max_values += [temp_max]
    return max(max_values)


def alan_annoying_kid(sentence):
    action = sentence[sentence.index('I') + 2:]
    didnt = "didn't" in sentence
    response = "I don't think you " + action[:-1] + " today, I think you "
    if didnt:
        verb = action[7:]
        verb = verb[0:verb.index(" ")]
        response += "did " + verb + " it!"
    else:
        verb = action[0:action.index(" ") - 2]
        response += "didn't " + verb + " at all!"
    return response

def added_char(s1, s2):
    for x in s1:
        s2 = s2.replace(x, '', 1)
    return s2[0]

def ascend_descend(length, minimum, maximum):
    word = ""
    if maximum < minimum or length == 0:
        return word
    current = minimum
    increase = True
    while len(word) < length:
        word += str(current)
        if current == maximum:
            increase = False
        if current == minimum:
            increase = True
        if maximum == minimum:
            continue
        elif increase:
            current += 1
        else:
            current -= 1
    while len(word) > length:
        word = word[:-1]
    return word
