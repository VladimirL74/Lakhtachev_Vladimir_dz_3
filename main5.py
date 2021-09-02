import random
import copy

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, unique=False):
    """
    возвращает n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого)
    nouns, adverbs, и adjectives. Если аргумент unique равен True, слова не будут повторяться.
    """
    jokes_nouns = copy.copy(nouns)
    jokes_adverbs = copy.copy(adverbs)
    jokes_adjectives = copy.copy(adjectives)
    jokes = []
    for el in range(n):
        if unique:
            if el <= n:
                a = random.choice(jokes_nouns)
                b = random.choice(jokes_adverbs)
                c = random.choice(jokes_adjectives)
                jokes.append(f"{a} " + f"{b} " + f"{c}")
                jokes_nouns.remove(a)
                jokes_adverbs.remove(b)
                jokes_adjectives.remove(c)
        if not unique:
            if el <= n:
                jokes.append(f"{random.choice(nouns)} " + f"{random.choice(adverbs)} " + f"{random.choice(adjectives)}")
    print(jokes)


get_jokes(5, True)
get_jokes(5)
get_jokes(6)
