
################# String - 1 #################



# Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".
# make_out_word('<<>>', 'Yay') → '<<Yay>>'
# make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
# make_out_word('[[]]', 'word') → '[[word]]'
def make_out_word(out, word):
   return out[:2] + word + out[2:]
# print(make_out_word('<<>>','Yay'))

#Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.
# extra_end('Hello') → 'lololo'
# extra_end('ab') → 'ababab'
# extra_end('Hi') → 'HiHiHi'
def extra_end(str):
   return str[-2:]*3
# print(extra_end('Hello'))

# Given a string, return the string made of its first two chars, so the String "Hello" yields "He". 
# If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".
# first_two('Hello') → 'He'
# first_two('abcdefg') → 'ab'
# first_two('ab') → 'ab'
def first_two(str):
  return str[:2]
# print(first_two('Hello'))

#Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
def first_half(str):
    return str[:(len(str))//2]
# print(first_half('WooHoo'))

# Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.
# without_end('Hello') → 'ell'
# without_end('java') → 'av'
# without_end('coding') → 'odin'

def without_end(str):
   return str[1:-1]
# print(without_end('Hello'))


# Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. 
# The strings will not be the same length, but they may be empty (length 0).
# combo_string('Hello', 'hi') → 'hiHellohi'
# combo_string('hi', 'Hello') → 'hiHellohi'
# combo_string('aaa', 'b') → 'baaab'

def combo_string(a, b):
    if a == '': return b
    elif b == '': return a
    if len(a) < len(b):
       return a+b+a
    elif len(b) < len(a):
       return b+a+b
# print(combo_string('Hello','hi'))

# Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.
# non_start('Hello', 'There') → 'ellohere'
# non_start('java', 'code') → 'avaode'
# non_start('shotl', 'java') → 'hotlava'
def non_start(a, b):
   return a[1:] + b[1:]
# print(non_start('Hello', 'There'))

# Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.
# left2('Hello') → 'lloHe'
# left2('java') → 'vaja'
# left2('Hi') → 'Hi'
def left2(str):
   return str[2:] +str[:2]
# print(left2('Hello'))


################# List - 1 #################
# Given an array of ints, return True if 6 appears as either the first or last element in the array. 
# The array will be length 1 or more.
# first_last6([1, 2, 6]) → True
# first_last6([6, 1, 2, 3]) → True
# first_last6([13, 6, 1, 2, 3]) → False
def first_last6(nums):
    if nums[0] == 6 or nums[-1] == 6:
        return True
    else:
        return False
# print(first_last6([13, 6, 1, 2, 3]))

# Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.
# same_first_last([1, 2, 3]) → False
# same_first_last([1, 2, 3, 1]) → True
# same_first_last([1, 2, 1]) → True
def same_first_last(nums):
    if len(nums) >= 1:
        if nums[0] == nums[-1]:
            return True
        else:
            return False
    else:
        return False
# print(same_first_last([1]))

# Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
# make_pi() → [3, 1, 4]
def make_pi():
   array = [3,1,4]
   return array
# print(make_pi())

# Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.
# common_end([1, 2, 3], [7, 3]) → True
# common_end([1, 2, 3], [7, 3, 2]) → False
# common_end([1, 2, 3], [1, 3]) → True
def common_end(a, b):
    if a[0] == b[0] or a[-1] == b[-1]:
        return True
    else:
        return False
# print(common_end([1, 2, 3], [7, 3]))

# Given an array of ints length 3, return the sum of all the elements.
# sum3([1, 2, 3]) → 6
# sum3([5, 11, 2]) → 18
# sum3([7, 0, 0]) → 7
def sum3(nums):
    return nums[0]+nums[1]+nums[2]
# print(sum3([1,2,3]))

# Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
# rotate_left3([1, 2, 3]) → [2, 3, 1]
# rotate_left3([5, 11, 9]) → [11, 9, 5]
# rotate_left3([7, 0, 0]) → [0, 0, 7]
def rotate_left3(nums):
    return [nums[1],nums[2],nums[0]]
# print(rotate_left3([1,2,3]))

# Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.
# reverse3([1, 2, 3]) → [3, 2, 1]
# reverse3([5, 11, 9]) → [9, 11, 5]
# reverse3([7, 0, 0]) → [0, 0, 7]
def reverse3(nums):
    return [nums[2],nums[1],nums[0]]
# print(reverse3([]))

# Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.
# max_end3([1, 2, 3]) → [3, 3, 3]
# max_end3([11, 5, 9]) → [11, 11, 11]
# max_end3([2, 11, 3]) → [3, 3, 3]
def max_end3(nums):
    if nums[0] > nums[-1]:
        return [nums[0],nums[0],nums[0]]
    if nums[0] < nums[-1]:
        return [nums[-1],nums[-1],nums[-1]]
    else:
        return [nums[0],nums[0],nums[0]]
# print(max_end3([1,2,3]))

# Given an array of ints, return the sum of the first 2 elements in the array. 
# If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.
# sum2([1, 2, 3]) → 3
# sum2([1, 1]) → 2
# sum2([1, 1, 1, 1]) → 2
def sum2(nums):
    if len(nums) < 1:
        return 0
    elif len(nums) >= 1 and len(nums)<2:
        return nums[0]
    elif len(nums) >= 2:
        return nums[0] + nums[1]
# print(sum2([1, 3]) )

# Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.
# middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
# middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
# middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]
def middle_way(a, b):
    return [a[1], b[1]]
# print(middle_way([1, 2, 3], [4, 5, 6]))

# Given an array of ints, return a new array length 2 containing the first and last elements from the original array. 
# The original array will be length 1 or more.
# make_ends([1, 2, 3]) → [1, 3]
# make_ends([1, 2, 3, 4]) → [1, 4]
# make_ends([7, 4, 6, 2]) → [7, 2]
def make_ends(nums):
    return[nums[0], nums[-1]]
# print(make_ends([1,2,3]))

# Given an int array length 2, return True if it contains a 2 or a 3.
# has23([2, 5]) → True
# has23([4, 3]) → True
# has23([4, 5]) → False
def has23(nums):
    if 2 in nums or 3 in nums:
        return True
    else:
        return False
# print(has23([4, 5]) )

################# Logic - 1 #################

# When squirrels get together for a party, they like to have cigars. 
# A squirrel party is successful when the number of cigars is between 40 and 60, inclusive.
# Unless it is the weekend, in which case there is no upper bound on the number of cigars. 
# Return True if the party with the given values is successful, or False otherwise.

# cigar_party(30, False) → False
# cigar_party(50, False) → True
# cigar_party(70, True) → True
def cigar_party(cigars, is_weekend):
    if is_weekend and cigars < 40 and cigars > 60:
        return False 

        
print(cigar_party(30, False))