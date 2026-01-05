def calculate_love_score(name1, name2):
    names = name1.lower() + name2.lower()
    true_score = 0
    love_score = 0
    true_score += names.count('t')
    true_score += names.count('r')
    true_score += names.count('u')
    true_score += names.count('e')
    love_score += names.count('l')
    love_score += names.count('o')
    love_score += names.count('v')
    love_score += names.count('e')
    print(f"{str(true_score)}"+f"{str(love_score)}")

