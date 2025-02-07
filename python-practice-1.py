# Task 1
"""
Complete the function that accepts a string parameter,
and reverses each word in the string. All spaces in the
string should be retained.
"""


def reverse_words(text):
    ls_reverse = [i[::-1] for i in text.split()]
    ls_reverse = "".join(ls_reverse)
    result = ""
    n = 0
    for i, val in enumerate(text):
        if val != " ":
            result += ls_reverse[n]
            n += 1
        else:
            result += text[i]
    return result


# Task 2
"""
Write a function that when given a URL as a string, parses out
just the domain name and returns it as a string.
"""


def domain_name(url):
    url = url.replace("www.", "")
    string_ls = url.split(".")
    if "/" in string_ls[0]:
        return string_ls[0].split("//")[1]
    return string_ls[0]


# Task 3
"""
Write an algorithm that takes an array and moves all of the zeros
to the end, preserving the order of the other elements.
"""


def move_zeros(lst):
    nums, zeroz = [], []
    for i in lst:
        if i == 0:
            zeroz.append(i)
        else:
            nums.append(i)
    return nums + zeroz


# Task 4
"""
Given a list and a number, create a new list that contains each number
of list at most N times, without reordering. For example if the input
number is 2, and the input list is [1,2,3,1,2,1,2,3], you take
[1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2
being in the result 3 times, and then take 3, which leads to
[1,2,3,1,2,3]. With list [20,37,20,21] and number 1, the result would
be [20,37,21].
"""


def delete_nth(order, max_e):
    result = []
    count = {}
    print(order, max_e)

    for i in order:
        if not count.get(i):
            count[i] = 1
        else:
            if count.get(i) < max_e:
                count[i] += 1
    print(count)
    for j in order:
        if count.get(j) > 0:
            result.append(j)
            count[j] -= 1

    return result


# Task 5
"""
Convert a string to a new string where each character in the new string
is "(" if that character appears only once in the original string, or
")" if that character appears more than once in the original string.
Ignore capitalization when determining if a character is a duplicate.
"""


def duplicate_encode(word):
    word = word.lower()
    result = ""
    for i in word:
        if word.count(i) > 1:
            result += ")"
        else:
            result += "("
    return result


# Task 6
"""
Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this task (but not y)
"""


def get_count(sentence):
    count = 0
    for i in "aeiou":
        if i in sentence:
            count += sentence.count(i)
    return count


# Task 7
"""
You are going to be given an array of integers. Your job is to take
that array and find an index N where the sum of the integers to the
left of N is equal to the sum of the integers to the right of N.
If there is no index that would make this happen, return -1.
"""


def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i + 1:]):
            return i
    return -1


# Task 8
"""
Build a function that returns an array of integers
from n to 1 where n>0.
"""


def reverse_seq(n):
    return [i for i in range(1, n + 1)][::-1]


# Task 9
"""
Make a program that filters a list of strings and returns a list
with only your friends name in it. If a name has exactly 4 letters in it,
you can be sure that it has to be a friend of yours! Otherwise,
you can be sure he's not.
"""


def friend(x):
    return [i for i in x if len(i) == 4]


# Task 10
"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain
anything but exactly 4 digits or exactly 6 digits. If the function is
passed a valid PIN string, return true, else return false.
"""


def validate_pin(pin):
    # return len(pin) in (4, 6) and pin.isdigit()
    for i in pin:
        if not i.isdigit():
            return False
    return True if len(pin) == 4 or len(pin) == 6 else False


# Task 11
"""
Given an array of integers, return a new array with each value doubled.
"""


def maps(a):
    # return map(lambda x: 2 * x, a)
    return [i * 2 for i in a]


# Task 12
"""
A hero is on his way to the castle to complete his mission. However, he's
been told that the castle is surrounded with a couple of powerful dragons!
each dragon takes 2 bullets to be defeated, our hero has no idea how many
bullets he should carry.. Assuming he's gonna grab a specific given number
of bullets and move forward to fight another specific given number of dragons,
will he survive? Return true if yes, false otherwise
"""


def hero(bullets, dragons):
    return bullets / 2 >= dragons


# Task 13
"""
Given a non-negative integer, 3 for example, return a string with a murmur:
"1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no
negative integers.
"""


def count_sheep(n):
    result = ""
    for i in range(1, n + 1):
        result += f"{i} sheep..."
    return result


# Task 14
"""
Code as fast as you can! You need to double the integer and return it.
"""


def double(n):
    return n * 2


# Task 15
"""
The first century spans from the year 1 up to and including the year 100,
the second century - from the year 101 up to and including the year 200, etc.
Given a year, return the century it is in.
"""


def century(year):
    return year // 100 if year % 100 == 0 else year // 100 + 1


# Task 16
"""
You probably know the "like" system from Facebook and other pages. People
can "like" blog posts, pictures or other items. We want to create the text that
should be displayed next to such an item. Implement the function which takes
an array containing the names of people that like an item.
"""


def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"


# Task 17
"""
Create a function that takes an integer as an argument and returns "Even" for
even numbers or "Odd" for odd numbers.
"""


def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"


# Task 18
"""
Write a function that takes an array of words and smashes them together
into a sentence and returns the sentence. You can ignore any need to sanitize
words or add punctuation, but you should add spaces between each word.
Be careful, there shouldn't be a space at the beginning or the end
of the sentence!
"""


def smash(words):
    return " ".join(words)


# Task 19
"""
Write a function, persistence, that takes in a positive parameter num and
returns its multiplicative persistence, which is the number of times you must
multiply the digits in num until you reach a single digit.
"""


def persistence(n):
    mult = 0
    while n > 9:
        n = eval("*".join(str(n)))
        mult += 1
    return mult


# Task 20
"""
Take 2 strings s1 and s2 including only letters from a to z. Return a new
sorted string (alphabetical ascending), the longest possible, containing
distinct letters - each taken only once - coming from s1 or s2.
"""


def longest(a1, a2):
    # return "".join(sorted(set(s1).union(s2)))
    # return "".join(sorted(set(a1 | a2)))
    return "".join(sorted(set(a1 + a2)))


# Task 21
"""
Implement a function which convert the given boolean value into its string
representation.
"""


def boolean_to_string(b):
    # return str(b)
    # return f"{b}"
    # return "True" if b else "False"
    return ("False", "True")[b]


# Task 22
"""
Your task is to sort a given string. Each word in the string will contain a
single number. This number is the position the word should have in the result.
Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
If the input string is empty, return an empty string.
"""


def order(sentence):
    result = []
    for i in range(1, 10):
        for j in sentence.split():
            if str(i) in j:
                result.append(j)
    return " ".join(result)


# Task 23

def solution(text, ending):
    return text.endswith(ending)


# Task 24
"""
Complete the method that takes a boolean value and return a "Yes" string for
true, or a "No" string for false.
"""


def bool_to_word(boolean):
    return "Yes" if boolean else "No"


# Task 25
"""
In a small town the population is p0 = 1000 at the beginning of a year. The
population regularly increases by 2 percent per year and moreover 50 new
inhabitants per year come to live in the town. How many years does the town
need to see its population greater than or equal to p = 1200 inhabitants?
"""


def nb_year(p0, percent, aug, p):
    count = 0
    while p0 < p:
        print(p0)
        p0 += int(p0 * percent / 100) + aug
        count += 1
    return count


# Task 26
"""
You are going to be given a non-empty string. Your job is to return the middle
character(s) of the string.
If the string's length is odd, return the middle character.
If the string's length is even, return the middle 2 characters.
"""


def get_middle(s):
    if len(s) % 2 == 0:
        return s[len(s) // 2 - 1:len(s) // 2 + 1]
    return s[len(s) // 2]


# Task 27
"""
Build a pyramid-shaped tower, as an array/list of strings, given a positive
integer number of floors. A tower block is represented with "*" character.
"""


def tower_builder(n_floors):
    tower = []
    space = [i for i in range(n_floors)[::-1]]
    for j in range(n_floors):
        stars = "*" * (j + 1) + "*" * j
        tower.append(" " * space[j] + stars + " " * space[j])
    return tower


# Tsk 28
"""
An isogram is a word that has no repeating letters, consecutive or
non-consecutive. Implement a function that determines whether a string that
contains only letters is an isogram. Assume the empty string is an isogram.
Ignore letter case.
"""


def is_isogram(string):
    return len(string.lower()) == len(set(string.lower()))


# Task 29
"""
Write a function which takes a list of strings and returns each line prepended
by the correct number.
"""


def number(lines):
    return [f"{i + 1}: {val}" for i, val in enumerate(lines)]


# Task 30
"""
Complete the solution so that the function will break up camel casing,
using a space between words.
"""


def solution1(s):
    result = [i if i.islower() else i + " " for i in s[::-1]]
    return "".join(result)[::-1]


# Task 31
"""
Given a random non-negative number, you have to return the digits
of this number within an array in reverse order.
"""


def digitize(n):
    n = [int(i) for i in list(str(n))]
    return n[::-1]


# Task 32


def accum(st):
    result = []
    for i, val in enumerate(st):
        result.append(val.capitalize() + val.lower() * i)
    return "-".join(result)


# Task 33
"""
Given an array (arr) as an argument complete the function countSmileys
that should return the total number of smiling faces.
"""


def count_smileys(arr):
    count = 0
    for i in arr:
        if i[-1] in "D)" and i[-2] in "-~:;":
            count += 1
    return count


# Task 34
"""
Given a month as an integer from 1 to 12, return to which quarter of the
year it belongs as an integer number.
"""


def quarter_of(month):
    for i, val in enumerate([3, 6, 9, 12]):
        if month <= val:
            return i + 1


# Task 35
"""
Create a function with two arguments that will return an array of the
first n multiples of x.
"""


def count_by(x, n):
    return [x * i for i in range(1, n + 1)]


# Task 36
"""
It's pretty straightforward. Your goal is to create a function that
removes the first and last characters of a string. You're given one
parameter, the original string.
"""


def remove_char(s):
    return s[1:-1]


# Task 37
"""
Your task is to create a function that does four basic mathematical
operations.
"""


def basic_op(operator, value1, value2):
    return eval(f"{value1} {operator} {value2}")


# Task 38
"""
Create a function that gives a personalized greeting.
This function takes two parameters: name and owner.
"""


def greet(name, owner):
    return "Hello " + ("boss" if name == owner else "guest")


# Task 39
"""
Timmy & Sarah think they are in love, but around where they live, they
will only know once they pick a flower each. If one of the flowers has
an even number of petals and the other has an odd number of petals it
means they are in love.
Write a function that will take the number of petals of each flower
and return true if they are in love and false if they aren't.
"""


def lovefunc(flower1, flower2):
    return True if (flower1 + flower2) % 2 else False


# Task 40
"""
You're writing code to control your town's traffic lights. You need a
function to handle each change from green, to yellow, to red, and then
to green again.
Complete the function that takes a string as an argument representing
the current state of the light and returns a string representing the
state the light should change to.
"""


def update_light(current):
    z = {
        "green": "yellow",
        "yellow": "red",
        "red": "green"
    }
    return z[current]


# Task 41
"""
You are given an odd-length array of integers, in which all of them are the
same, except for one single number. Complete the method which accepts such
an array, and returns that single different number. The input array will
always be valid! (odd-length >= 3)
"""


def stray(arr):
    z = list(set(arr))
    return z[0] if arr.count(z[0]) <= 1 else z[1]


# Task 42
"""
Make a function that can take any non-negative integer as an argument and
return it with its digits in descending order. Essentially, rearrange the
digits to create the highest possible number.
"""


def descending_order(num):
    num = [int(i) for i in str(num)]
    num = sorted(num, reverse=True)
    num = [str(i) for i in num]
    return int("".join(num))


# Task 43
"""
The cockroach is one of the fastest insects. Write a function which takes
its speed in km per hour and returns it in cm per second, rounded down
to the integer (= floored).
"""


def cockroach_speed(s):
    return int((100000 / 3600) * s)


# Task 44
"""
You will be given a number and you will need to return it as a string
in Expanded Form
"""


def expanded_form(num):
    s_num = str(num)
    result = []

    for i in range(len(s_num)):
        if s_num[i:].startswith("0"):
            continue
        else:
            result.append(int(s_num[i]) * (10 ** (int(len(s_num[i:])) - 1)))

    return "".join([str(i) + " + " for i in result])[:-3]


# Task 45
"""
Create a function that takes 2 integers in form of a string as an input,
and outputs the sum (also as a string)
"""


def sum_str(a, b):
    return str(int(a if a else 0) + int(b if b else 0))


# Task 46
"""
You will be given an array of numbers. You have to sort the odd numbers in
ascending order while leaving the even numbers at their original positions.
"""


def sort_array(source_array):
    no_odd = [i if not i % 2 else "x" for i in source_array]
    even_rev = sorted(i for i in source_array if i % 2)
    result = []
    k = 0
    for i in range(len(source_array)):
        if no_odd[i] != "x":
            result.append(no_odd[i])
        else:
            result.append(even_rev[k])
            k += 1

    return result


# Task 47
"""
When provided with a number between 0-9, return it in words. Note that the
input is guaranteed to be within the range of 0-9.
"""


def switch_it_up(n):
    d = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    return d[n]


# Task 48
"""
Create a function that turns a string into a Mexican Wave
"""


def wave(p):
    return [
        p[:i] + p[i:].capitalize() for i in range(len(p)) if p[i].isalpha()
    ]


# Task 49
"""
Complete the function/method so that it returns the url with anything after
the anchor (#) removed.
"""


def remove_url_anchor(url):
    return url[:url.index("#")] if "#" in url else url


# Task 50
"""
count all the occurring characters in a string. If you have a string like
aba, then the result should be {'a': 2, 'b': 1}.
"""


def count(s):
    return {i: s.count(i) for i in s}


print(count("aba"), "\n")
