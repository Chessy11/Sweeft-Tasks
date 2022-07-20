# Exercise 1: ⬤
# You are given words. Some words may repeat. For each word, output its number of
# occurrences. The output order should correspond with the input order of appearance of the
# word. See the sample input/output for clarification.
# Note: Each input line ends with a &quot;\n&quot; character.
# Constraints:
# 1 ≤ n ≤ 10 5
# The sum of the lengths of all the words do not exceed 10 6
# All the words are composed of lowercase English letters
# only.
# Input Format
# The first line contains the integer, n.
# The next n lines each contain a word.
# Output Format
# Output 2 lines.
# On the first line, output the number of distinct words from the input.
# On the second line, output the number of occurrences for each distinct word according to
# their appearance in the input.
# Sample Input:
# 4
# bcde
# f
# abcd
# efg
# bcde
# bcde
# f
# Sample Output
# 3
# 2 1 1
# Explanation

# There are 3 distinct words. Here, &quot;bcdef&quot; appears twice in the input at the first and last
# positions. The other words appear once each. The order of the first appearances are
# &quot;bcdef&quot;, &quot;abcdefg&quot; and &quot;bcde&quot; which corresponds to the output.





#I assume  inputs are : 
# 4
# bcdef
# abcdefg
# bcde
# bcdef

#Otherwise it doesnot makes senses comparing with sample output


from collections import Counter


n = int(input())
ls = []
for i in range(n):
    ls.append(input().strip())
counter = Counter(ls)
print(len(counter))
print(*counter.values())
