# nums = [1,2,3,4]
# nums
# nums.remove(3)
# nums

# nums.pop()
# nums

# nums.pop(0)
# nums

# nums = [2]
# nums.extend([3,4])
# nums

# nums.insert(0,1)
# nums.insert(2,'two-and-a-half')
# nums

# phrase = "Don't panic!"
# plist = list(phrase)
# phrase
# plist

# for i in range(4):
# 	plist.pop()

# plist.pop(0)
# plist.remove("'")
# plist

# first = [1,2,3,4,5]
# first

# second = first
# second

# second.append(6)
# second
# first

# third = second.copy()
# third

# third.append(7)
# third
# second

# saying = "Don't panic!"
# letters = list(saying)

# letters

# letters[0]
# letters[-1]



vowels = ['a', 'e', 'i', 'o', 'u']

word = input("Provide a word to search for vowels: ")
found = []

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
            
for vowel in found:
    print(vowel)


found = {}
found

found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0
found

found['e'] = found['e'] + 1
found
found['e'] += 1
found

for k in found:
    print(k, 'was found', found[k], 'time(s).')

for k in sorted(found):
    print(k, 'was found', found[k], 'time(s).')

for k,v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')