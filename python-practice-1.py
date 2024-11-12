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


print(reverse_seq(5), "\n")
