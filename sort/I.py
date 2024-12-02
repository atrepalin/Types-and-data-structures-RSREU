def anagrams(word1, word2):
    if len(word1) != len(word2):
        return "NO"
    
    count = {}
    
    for char in word1:
        if char not in count:
            count[char] = 0
        count[char] += 1
    
    for char in word2:
        if char in count:
            count[char] -= 1
            if count[char] < 0:
                return "NO"
        else:
            return "NO"
    
    return "YES"

word1 = input()
word2 = input()

result = anagrams(word1, word2)
print(result)