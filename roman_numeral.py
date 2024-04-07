def romanToInt(s: str) -> int:
    m = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    ans = 0
    for i in range(len(s)):
        if i < len(s) -1 and m[s[i]] < m[s[i+1]]: # we have to do lens(s) - 1 because we do s + 1 later and this keeps us in range
            ans -= m[s[i]]
        else:
            ans += m[s[i]]
    return ans 

result = romanToInt(s = 'IV')
print(result)


