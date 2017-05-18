"""
Given an input list, return it in reverse.
>>> backwards([56, 57, 58, 59, 60])
[60, 59, 58, 57, 56]


Find the max number in a given list.  Then, change every element in the list containing the first number of the maximum to the maximum number.
>>> maximus([56, 57, 58, 59, 60])
[60, 57, 58, 59, 60]

>>> maximus([56, 67, 56, 59, 60])
[67, 67, 67, 59, 67]


Given two lists, return True of the first two items are the equal.
>>> compare_first_element(['migratory', 'birds', 'fly', 'south'], ['migratory', 'monopoloy', 'mind'])
True

Return True if the first letter of the second element in each list is equal. (Case Insensitive)
>>> compare_second_letter(['migratory', 'penguins', 'fly', 'south'], ['One', 'Pound', 'Coconut'])
True

>>> compare_second_letter(['migratory', 'birds', 'fly', 'south'], ['One', 'Pound', 'Coconut'])
False


Given two lists, return one list, with all of the items of the first list, then the second
>>> smoosh(['mama', 'llama'], ['baba', 'yaga'])
['mama', 'llama', 'baba', 'yaga']


Use a default argument to allow the user to reverse the order!
>>> smoosh(['mama', 'llama'], ['baba', 'yaga'], reverse=True)
['yaga', 'baba', 'llama', 'mama']


"""
def compare_first_element(first, second):
    if first[0] == second[0]:
        return True
    else:
        return False

def compare_second_letter(first_list, second_list):

    if first_list[1][0].upper() == second_list[1][0]:
        return True
    else:
        return False



# def backwards(a):
#     x = list(a)
#     x = x[::-1]
#     print(x)

# a = [21, 32, 54, 12]
def backwards(a):
    a.reverse()
    return a



def maximus(nums):
    result = []
    biggest = max(nums)
    first_digit = str(biggest)[0]
    print(biggest, )

def maximus(nums):
    result = []
    biggest = max(nums)
    first_digit = str(biggest)[0]
    for num in nums:
        if first_digit in str(num):
            result.append(biggest)
        else:
            result.append(num)
    return result


def smoosh(first_list, second_list, reverse=False):
    result = first_list + second_list
    if reverse:
        result.reverse()

    return result


def gather_input():
    first = input('Enter something')
    second = input('Enter something')
    smoosh(first, second)




