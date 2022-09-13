def card_hide(card):
    card_str = str(card)
    return '*' * len(card_str[:-4]) + card_str[-4:]

print(card_hide(5456789515658562))
