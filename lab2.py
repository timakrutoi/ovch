#!/usr/bin/python3
#encode=utf-8

import math

def l2t1(a):
    stat_pairs = {}
    stat_letters = {}

    prob_pairs = {}
    prob_letters = {}

    smt = {}

    for i in range(int(len(a))):
        if i % 2 == 0:
            pair = a[i:i+2]
            if pair not in stat_pairs.keys():
                stat_pairs[pair] = 1
            else:
                stat_pairs[pair] += 1
        
        if a[i] not in stat_letters.keys():
            stat_letters[a[i]] = 1
        else:
            stat_letters[a[i]] += 1

    for i in range(1, len(a)):
        if a[i-1:i+1] not in smt.keys():
            smt[a[i-1:i+1]] = 1
        else:
            smt[a[i-1:i+1]] += 1

    for k, v in stat_pairs.items():
        prob_pairs[k] = v / (len(a) / 2)
    for k, v in stat_letters.items():
        prob_letters[k] = v / len(a)

    # print(a1, a2)

    # for i in stat_pairs.keys():
    #     print(i, stat_pairs[i], round(prob_pairs[i], 2))

    # for k, v in smt.items():
    #     print(f'{k[1]}|{k[0]}\t{v}\t{stat_letters[k[0]]}\t{round(v / stat_letters[k[0]], 2)}')
        
    # print('-'*50)
    # for i in stat_letters.keys():
    #     print(i, stat_letters[i], round(prob_letters[i], 2))

    H = 0
    for k, v in stat_pairs.items():
        H += (prob_pairs[k] * math.log(prob_pairs[k], 2))

    print(f'H(X^2) = {-round(H, 2)}')
    print(f'H2(X) = {-round(H / 2, 2)}')

    H = 0
    for k, v in stat_letters.items():
        H += (prob_letters[k] * math.log(prob_letters[k], 2))

    print(f'H(X) = {-round(H, 2)}')

    H = 0
    for k, v in prob_letters.items():
        for x, y in smt.items():
            if x[0] != k:
                continue
            # print(k, x)
            # print(round(v, 2), round(y / stat_letters[k[0]], 2), round(math.log(y / stat_letters[k[0]], 2), 2))
            H += (v * y / stat_letters[k[0]] * math.log(y / stat_letters[k[0]], 2))

    print(f'H(X|X) = {-round(H, 2)}')


def l2t2(a):
    b = [i for i in a]

    stat_letters = {}
    smt = {}

    for i in range(int(len(a))):
        if a[i] not in stat_letters.keys():
            stat_letters[a[i]] = 1
        else:
            stat_letters[a[i]] += 1


    for i in range(1, len(b)):
        if a[i-1:i+1] not in smt.keys():
            smt[a[i-1:i+1]] = 1
        else:
            smt[a[i-1:i+1]] += 1

    for k, v in smt.items():
        print(f'{k[1]}|{k[0]}\t{v}\t{stat_letters[k[0]]}\t{round(v / stat_letters[k[0]], 2)}')



if __name__ == '__main__':
    tima = 'на дворе - трава, на траве - дрова, не руби дрова на траве двора!'
    vlad = 'и прыгают скороговорки, как караси на сковородке.'
    slav = 'павел павлушку пеленовал-пеленовал и распеленовывал.'
    ev4g = 'скреативлен креатив не по-креативному, нужно перекреативить!'
    artem = 'расскажите про покупки! про покупки, про покупки, про покупочки свои.'

    l2t1(artem, False)
