def checkvowels(text):
    vowel = False
    for i in text:
        if i in set('aeiou'):
            if vowel:
                return 'Positive'
            else:
                vowel = True
        else:
            vowel = False
    return 'Negative'
def checkvowels2(text):
    return 'Positive' if len([1 for i in range(len(text)-1) if set(text[i:i+2]) - set('aeiou') == set()]) > 0 else 'Negative'
def checkvowels3(text):
    for i in range(len(text)-1):
        if set(text[i:i+2]) - set('aeiou') == set():
            return 'Positive'
    return 'Negative'