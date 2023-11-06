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

def reverse(st):
    reversal = ""
    last = ""
    for x in st:
        if len(last) == 0 or x == last[-1]:
            last += x
        else:
            if len(last) > 1:
                if last.islower():
                    reversal += last.upper()
                else:
                    reversal += last.lower()
            else:
                reversal += last
            last = x
    if len(last) != 0:
        if len(last) > 1:
            if last.islower():
                reversal += last.upper()
            else:
                reversal += last.lower()
        else:
            reversal += last
    return reversal

def change_case(identifier, target_case):
    if identifier == "":
        return identifier

    if target_case not in ["snake", "camel", "kebab"]:
        return None

    hasCaps = len([i for i in identifier if i.isupper()]) > 0
    hasDash = len([i for i in identifier if i == "-"]) > 0
    hasUnder = len([i for i in identifier if i == "_"]) > 0

    if len([i for i in [hasCaps, hasDash, hasUnder] if i == True]) > 1:
        return None

    words = []

    if hasCaps:
        temp = ""
        for x in identifier:
            if x.isupper():
                words += [temp.lower()]
                temp = x
            else:
                temp += x
        words += [temp.lower()]

    if hasDash:
        words = identifier.split("-")

    if hasUnder:
        words = identifier.split("_")

    if target_case == "snake":
        return "_".join(words)

    if target_case == "camel":
        group = []
        for x in range(len(words)):
            if x == 0:
                group += [words[x]]
            else:
                group += [words[x].capitalize()]
        return "".join(group)

    return "-".join(words)

def flesch_kincaid(text):
    sentences = []
    temp = ""
    for x in text:
        temp += x
        if x == "." or x == "?" or x == "!":
            sentences += [temp.strip()]
            temp = ""
    words_count = [len(x.split(" ")) for x in sentences]
    words_per_sentence = sum(words_count) / len(sentences)

    all_words = text.split(" ")
    remove_letters = [x.replace("a", " ") for x in all_words]
    remove_letters = [x.replace("A", " ") for x in remove_letters]
    remove_letters = [x.replace("e", " ") for x in remove_letters]
    remove_letters = [x.replace("E", " ") for x in remove_letters]
    remove_letters = [x.replace("i", " ") for x in remove_letters]
    remove_letters = [x.replace("I", " ") for x in remove_letters]
    remove_letters = [x.replace("o", " ") for x in remove_letters]
    remove_letters = [x.replace("O", " ") for x in remove_letters]
    remove_letters = [x.replace("u", " ") for x in remove_letters]
    remove_letters = [x.replace("U", " ") for x in remove_letters]
    remove_letters = [x.replace("  ", " ") for x in remove_letters]
    remove_letters = [len([i for i in x if i == " "]) for x in remove_letters]
    syllables_per_word = sum(remove_letters) / len(all_words)

    return round((0.39 * words_per_sentence) + (11.8 * syllables_per_word) - 15.59, 2)

def do_math(s) :
    parts = s.split(" ")
    nums = []
    letters = []
    for x in parts:
        nums += [int("".join([i for i in x if i.isnumeric()]))]
        letters += [i for i in x if i.isalpha()]
    alpha = "abcdefghijklmnopqrstuvwxyz"
    place = []
    for x in range(len(letters)):
        if len(place) > 0 and letters[x] in letters[0 : x]:
            place += [max([i for i in place[0 : x] if i >= alpha.find(letters[x]) and i <= alpha.find(letters[x]) + .99]) + .01]
        else:
            place += [alpha.find(letters[x])]
    dictionary = {place[x] : nums[x] for x in range(len(nums))}
    sorted_dictionary = dict(sorted(dictionary.items()))
    sorted_nums = sorted_dictionary.values()
    operator = "+"
    math = ""
    for x in sorted_nums:
        if math == "":
            math = int(x)
        elif operator == "+":
            operator = "-"
            math += x
        elif operator == "-":
            operator = "*"
            math -= x
        elif operator == "*":
            operator = "/"
            math *= x
        else:
            operator = "+"
            math /= x
    return round(math)

def fruit_pack(orders):
    shop = []
    for x in orders:
        bag = ""
        box = ""
        pallet = ""
        number = ""
        for y in x:
            if y.isnumeric():
                number += y
            else:
                num = int(number)
                while num >= 50:
                    pallet += "[" + y + "]"
                    num -= 50
                while num >= 10:
                    box += "{" + y + "}"
                    num -= 10
                if num > 0:
                    bag += "("
                    while num > 0:
                        bag += y
                        num -= 1
                    bag += ")"
                number = ""
        lengths = [len(bag), len(box), len(pallet)]
        max_length = max(lengths)
        while len(bag) < max_length:
            bag = "-" + bag
        while len(box) < max_length:
            box = "-" + box
        while len(pallet) < max_length:
            pallet = "-" + pallet
        shop += [[bag, box, pallet]]
    return shop

def one_two_three(n):
    first = "0"
    second = "0"
    if n < 10:
        first = str(n)
    else:
        num = str(n)
        sum = 0
        for x in num:
            sum += int(x)
        nines = int(num[:-1])
        temp = ""
        for y in range(nines):
            temp += '9'
        if nines >= 10:
            temp_nine = int(str(nines)[:-1])
            for z in range(temp_nine):
                temp += '9'
        if sum >= 10:
            sum -= 9
            temp += '9'
        first = temp + str(sum)
    for x in range(n):
        second += '1'
    return [int(first), int(second)]

# d = direction, v = values array, c = number to search
# return None in case of value not found
def cycle(d, v, c):
    if c in v:
        index = v.index(c)
        index += d
        if index < 0:
            index = len(v) - 1
        if index > len(v) - 1:
            index = 0
        return v[index]
    return None

def pop_blocks(lst):
    change_made = True
    popped = []
    while change_made:
        match = ""
        match_found = False
        for x in range(len(lst)):
            if not match_found:
                if x != len(lst) - 1:
                    if lst[x] != lst[x + 1]:
                        if lst[x] != match:
                            popped += [lst[x]]
                        if match != "":
                            match_found = True
                        match = ""
                    else:
                        match = lst[x]
                else:
                    if lst[x] != match:
                        popped += [lst[x]]
            else:
                popped += [lst[x]]
        if lst == popped:
            change_made = False
        else:
            change_made = True
            lst = popped
            popped = []
    return popped

def range_parser(s):
    nums = []
    s += ','
    s = [x for x in s.split(',') if x != ""]
    for x in s:
        step = 0
        first = 0
        last = 0
        divide = ""
        if '-' in x:
            divide = x.split('-')
            first = int(divide[0].strip())
            if ':' in divide[1]:
                temp = divide[1].split(':')
                last = int(temp[0].strip())
                step = int(temp[1].strip())
            else:
                last = int(divide[1].strip())
        if step > 0:
            while first <= last:
                nums += [first]
                first += step
        elif first > 0 and last > 0:
            while first <= last:
                nums += [first]
                first += 1
        else:
            nums += [int(x.strip())]
    return nums

print(range_parser('5-10'))



