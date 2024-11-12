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


print(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3), "\n")
