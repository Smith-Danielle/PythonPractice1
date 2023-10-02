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


def autocomplete(input_, dictionary):
    check = ""
    for x in input_:
        if x.lower() in "abcdefghijklmnopqrstuvwxyz":
            check += x
    length = len(check)
    return [x for x in dictionary if x[0:length].lower() == check.lower()][:5]

def solve(arr):
    ascend_check = []
    for x in range(len(arr) - 1):
        ascend_check += [arr[x] < arr[x + 1]]
    if len([x for x in ascend_check if x == True]) == len(arr) - 1:
        return "A"
    if len([x for x in ascend_check if x == False]) == len(arr) - 1:
        return "D"
    if len([x for x in ascend_check if x == True]) > len([x for x in ascend_check if x == False]):
        return "RA"
    if len([x for x in ascend_check if x == True]) == len([x for x in ascend_check if x == False]):
        if ascend_check[0] == True:
            return "RD"
        else:
            return "RA"
    return "RD"

def smile(text):
    for x in range(len(text)):
        if text[x] == ":" or text[x] == ";" or text[x] == "=":
            if x != len(text) - 1:
                if text[x + 1] == "(":
                    text = text[0: x + 1] + ")" + text[x + 2:]
                if text[x + 1] == "[":
                    text = text[0: x + 1] + "]" + text[x + 2:]
                if text[x + 1] == "-" or text[x + 1] == "~":
                    if x != len(text) - 2:
                        if text[x + 2] == "(":
                            text = text[0: x + 2] + ")" + text[x + 3:]
                        if text[x + 2] == "[":
                            text = text[0: x + 2] + "]" + text[x + 3:]
    return text

def one_down(txt):
    if type(txt) != str:
        return "Input is not a string"
    decoded = ""
    letters = "abcdefghijklmnopqrstuvwxyz"
    for x in txt:
        if x.lower() in letters:
            temp_letter = ""
            if letters.index(x.lower()) == 0:
                temp_letter = "z"
            else:
                temp_letter = letters[letters.index(x.lower()) - 1]
            if not x.islower():
                temp_letter = temp_letter.upper()
            decoded += temp_letter
        else:
            decoded += x
    return decoded

def solution(s):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    sliced = ""
    temp = ""
    for x in s:
        if len(temp) == 0:
            temp += x
        else:
            temp += x
            if temp not in alpha:
                sliced += temp[:-1][::-1]
                temp = temp[len(temp) - 1]
    if len(temp) > 0:
        sliced += temp[::-1]
    return sliced

def check_vin(number):
    if len(number) != 17 or "I" in number or "O" in number or "Q" in number:
        return False

    conversion = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "J": 1, "K": 2,
                  "L": 3, "M": 4, "N": 5, "P": 7, "R": 9, "S": 2, "T": 3, "U": 4, "V": 5, "W": 6,
                  "X": 7, "Y": 8, "Z": 9}
    weights = [8,7,6,5,4,3,2,10,0,9,8,7,6,5,4,3,2]
    converted = 0

    for x in range(len(number)):
        if number[x].isalpha() and number[x].islower():
            return False
        if number[x].isnumeric():
            converted += int(number[x]) * weights[x]
        else:
            converted += conversion[number[x]] * weights[x]

    if number[8].isnumeric() and converted % 11 == int(number[8]):
        return True
    if converted % 11 == 10 and number[8] == "X":
        return True
    return False

def find_children(dancing_brigade):
    together = ""
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for x in alpha:
        if x.upper() in dancing_brigade:
            together += x.upper()
        if x in dancing_brigade:
            while x in dancing_brigade:
                together += x
                dancing_brigade = dancing_brigade.replace(x, "", 1)
    return together

def hungry_foxes(farm):
    fox_chick = ""
    temp = ""
    fox_outside = False
    cage = False
    for x in farm:
        if cage:
            if x == ']':
                cage = False
                if 'F' in temp:
                    fox_chick += temp.replace('C', '.')
                else:
                    fox_chick += temp
                fox_chick += x
                temp = ""
            else:
                temp += x
        else:
            if x == '[':
                cage = True
                if len(temp) > 0 and 'F' in temp:
                    fox_chick += temp.replace('C', '.')
                    fox_outside = True
                elif len(temp) > 0:
                    fox_chick += temp
                fox_chick += x
                temp = ""
            else:
                temp += x

    if len(temp) > 0:
        if 'F' in temp:
            fox_chick += temp.replace('C', '.')
            fox_outside = True
        else:
            fox_chick += temp
        temp = ""
        cage = False

    fox_check = ""
    if fox_outside and '[' in farm:
        for x in fox_chick:
            if cage:
                if x == ']':
                    cage = False
                    fox_check += temp
                    fox_check += x
                    temp = ""
                else:
                    temp += x
            else:
                if x == '[':
                    cage = True
                    if len(temp) > 0:
                        fox_check += temp.replace('C', '.')
                    fox_check += x
                    temp = ""
                else:
                    temp += x
        if len(temp) > 0:
                fox_check += temp.replace('C', '.')
        fox_chick = fox_check
        
    return fox_chick

def encrypter(strng):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    answer = ""
    for x in strng:
        if x in alpha:
            index_1 = alpha.index(x) + 13
            if index_1 > 25:
                index_1 = index_1 - 26
            answer += alpha[abs(index_1 - 25)]
        else:
            answer += x
    return answer

def string_suffix(str_):
    words = [str_]
    count = len(str_)
    for x in range(len(str_) - 1):
        words += [words[-1][1:]]
    words = words[1:]
    for x in range(len(words)):
        loop = 0
        if len(str_) > len(words[x]):
            loop = len(words[x])
        else:
            loop = len(str_)
        for y in range(loop):
            if str_[y] == words[x][y]:
                count += 1
            else:
                break
    return count

def autocorrect(input):
    words = input.split(" ")
    sentence = []
    for x in words:
        if x.lower() == "u" or x.lower() == "you":
            sentence += ["your sister"]
        elif "youu" in x.lower() and x.lower().index("youu") == 0:
            sentence += ["your sister"]
        elif "you" in x.lower() and x.lower().index("you") == 0 and not x.lower()[3].isalnum():
            sentence += [x.replace("you", "your sister")]
        else:
            sentence += [x]
    return " ".join(sentence)

def sequence(phrase):
    phone = {"1":"1", "2":"ABC2", "3":"DEF3", "4":"GHI4", "5":"JKL5", "6":"MNO6", "7":"PQRS7", "8":"TUV8", "9":"WXYZ9", "*":"*", "0":" 0", "#":"#"}
    keypad = ""
    for x in phrase:
        values = [y for y in phone.values() if x.upper() in y][0]
        button = list(phone.keys())[list(phone.values()).index(values)]
        temp = ""
        count = values.index(x.upper()) + 1
        temp = ""
        for z in range(count):
            temp += button
        if len(keypad) > 0 and keypad[-1] == button:
            keypad += "p"
        keypad += temp
    return keypad

def yes_no(arr):
    order = []
    start_first = True
    while len(arr) > 0:
        for x in range(len(arr)):
            if start_first:
                if x % 2 == 0:
                    order += [arr[x]]
                    arr[x] = '0'
            else:
                if x % 2 != 0:
                    order += [arr[x]]
                    arr[x] = '0'
        if arr[-1] == '0':
            start_first = False
        else:
            start_first = True
        arr = [i for i in arr if i != '0']
    return order

def solveit(s):
    alpha = "abcdefghijklmnopqrstuvwxyz";
    vowels = list(sorted([x for x in s if x in "aeiou"]))
    cons = list(sorted([x for x in s if x not in "aeiou"]))
    v_length = len(vowels)
    c_length = len(cons)
    lexi = ""
    if v_length + 1 == c_length or v_length - 1 == c_length or v_length == c_length:
        if v_length > c_length or v_length == c_length:
            for x in range(c_length):
                lexi += vowels[x]
                lexi += cons[x]
            if v_length > c_length:
                lexi += vowels[-1]
        else:
            for x in range(v_length):
                lexi += cons[x]
                lexi += vowels[x]
            lexi += cons[-1]
    if lexi == "":
        return "failed"
    return lexi

print(solveit("oruder"))



