
def wordPattern(pattern, s):
    """
    :type pattern: str
    :type s: str
    :rtype: bool
    """
    dictionary = {}
    t = s.split(" ")
    for i in range(len(pattern)):
        if pattern[i] not in dictionary and t[i] not in dictionary.values():
            dictionary[pattern[i]] = t[i] 
        elif pattern[i] not in dictionary and t[i] in dictionary.values():
            return False
        elif pattern[i] in dictionary and dictionary[pattern[i]] != t[i]:
            return False
    return True


print(wordPattern('abba', 'dog dog dog dog'))
    
            