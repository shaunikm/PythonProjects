def card_hide(card):
    j = str(card)
    x = len(str(card))
    f = x-4
    c = str(f*"*")
    d = str(c + j[-4:-1] + j[-1])
    return d


k = card_hide(255958)
print(k)