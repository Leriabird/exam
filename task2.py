__author__ = 'Leria'
from operator import mul
from functools import reduce

adj_amount = 0
noun_amount = 0
verb_amount = 0
adj_suffix = 'yo'
noun_suffix = 'ka'
with open('dict.txt', 'r') as vocab:
    vocab_list = [line.strip() for line in vocab]
    for char in vocab_list:
        if char.endswith(adj_suffix):
            adj_amount += 1
        elif char.endswith(noun_suffix):
            noun_amount += 1
        else:
            verb_amount += 1
adj_comb = (lambda n: sum(map(lambda k: reduce(mul, range(n-k+1, n+1), 1), range(n+1))))(adj_amount)
sentences = adj_comb*noun_amount*verb_amount
print(sentences)
