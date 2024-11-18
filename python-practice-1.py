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


print(number(["a", "b", "c"]), "\n")
