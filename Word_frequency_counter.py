def word_freq(text):
    from collections import Counter
    return Counter(text.lower().split())