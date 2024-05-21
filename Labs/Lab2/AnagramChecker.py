def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))
