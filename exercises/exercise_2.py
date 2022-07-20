# Exercise 2: ⬤
# Lexicographical order is often known as alphabetical order when dealing with strings. A
# string is greater than another string if it comes later in a lexicographically sorted list.
# Given a word, create a new word by swapping some or all of its characters. This new word
# must meet two criteria:
# ● It must be greater than the original word
# ● It must be the smallest word that meets the first condition
# Example
# w =
# abc
# d
# The next largest word is abdc.
# Create the function bigger_Is_greater and return the new string meeting the criteria. If it is
# not possible, return no answer.
# Function Description
# Function has the following parameter(s):
# ● string w: a word
# Returns
# - string: the smallest lexicographically higher string possible or no answer
# Input Format
# The first line of input contains T, the number of test cases.
# Each of the next T lines contains w.
# Constraints
# ● 1 ≤ T ≤ 10 5
# ● 1 ≤ length of w ≤ 100
# ● w will contain only letters in the range ascii[a...z]
# Sample Input:

# 5
# a
# b
# b
# b
# h
# e
# f
# g
# d
# h
# c
# k
# d
# k
# h
# c
# Sample
# Output
# ba no
# answer
# hegf
# dhkc
# hcdk
# Explanation Test case 1: ba is the only string which can be made by
# rearranging ab. It is greater.
# Test case 2:
# It is not possible to rearrange bb and get a greater string.
# Test case 3: hegf is the next string
# greater than hefg.
# Test case 4: dhkc is the next string greater
# than dhck. Test case 5: hcdk is the next
# string greater than dkhc.
# Sample
# Input: 6
# lmno dcba
# dcbb abdc
# abcd
# fedcbabcd
# Sample
# Output lmon

# no answer
# no answer
# acbd abdc
# Fedcbabdc






# I assume inputs are :

# 5
# ab
# bb
# hefg
# dhck
# dkhc


# 6
# lmno
# dcba
# dcbb
# abdc
# abcd
# fedcbabcd


# Otherwiese sample outputs doesn't makes sense





for _ in range(int(input())):
    s = input()
    s = list(s[::-1])
    done = 0
    for i in range(1, len(s)):
        if s[i-1] > s[i]:
            for j in range(i):
                if s[j] > s[i]:
                    s[j],s[i] = s[i],s[j]
                    s = sorted(s[:i])[::-1] + s[i:]
                    print("".join(s[::-1]))
                    break
            break
    else:
        print("no answer")
        
        
