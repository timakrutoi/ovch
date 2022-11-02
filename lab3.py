#!/usr/bin/python3
#encode=utf-8

import math

def l3t1(a, verbose=False):
    stat_letters = {}
    prob_letters = {}

    smt = {}

    for i in range(int(len(a))):        
        if a[i] not in stat_letters.keys():
            stat_letters[a[i]] = 1
        else:
            stat_letters[a[i]] += 1

    for k, v in stat_letters.items():
        prob_letters[k] = round(v / len(a), 2)

    prob_letters = {k: v for k, v in sorted(prob_letters.items(), key=lambda item: -item[1])}

    # if verbose:
    #     for k, v in prob_letters.items():
    #         print(f'{k} : {v}')

    m1 = math.ceil(len(prob_letters) / 3)
    m2 = math.ceil((len(prob_letters) - m1) / 2)
    # if verbose:
    #     print(f'm = {len(prob_letters)}, m1 = {m1}, m2 = {m2}, m3 = {len(prob_letters) - m1 - m2}')
    pz = [
        0,0
        # sum([v for i, v in enumerate(prob_letters.values()) if 0 <= i < m1]),
        # sum([v for i, v in enumerate(prob_letters.values()) if m1 + 1 <= i < m1 + m2]),
    ]

    for i, v in enumerate(prob_letters.values()):
        if i < m1:
            pz[0] += v
        elif i < m1 + m2:
            pz[1] += v


    pz.append(1 - pz[0] - pz[1])
    # print(pz)
    pz = [round(i, 2) for i in pz]
    entropy = -sum([(i * math.log(i, 2)) for i in pz])

    if verbose:
        z = 1
        for i, (k, v) in enumerate(prob_letters.items()):
            if i >= m1 + m2:
                z = 3
            elif i >= m1:
                z = 2
            print(f'{i}\t|\t{k}\t|\t{v}\t|\t{z}\t|\t{pz[z - 1]}')
        print()
        print(pz)
        print(entropy)

    n_max = 2
    # for i in [1,2,3]:
    out1 = {}
    out2 = {}
    alpha = ['a', 'b', 'c']
    for i in range(3):
        for j in range(3):
            out1[''.join([alpha[i],alpha[j]])] = pz[i] * pz[j]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                out2[''.join([alpha[i],alpha[j],alpha[k]])] = pz[i] * pz[j] * pz[k]
                # print(f'{alpha[i]}{alpha[j]}{alpha[k]} = {pz[i] * pz[j] * pz[k]}', )

    out1 = {k: v for k, v in sorted(out1.items(), key=lambda item: -item[1])}
    out2 = {k: v for k, v in sorted(out2.items(), key=lambda item: -item[1])}

    # for k, v in out1.items():
    #     print(f'{k} : {round(v, 4)}')
    # for k, v in out2.items():
    #     print(f'{k} : {round(v, 4)}')

    for N in [1,2,3]:
        nmax = math.ceil(math.log(3**N, 2))
        for n in range(nmax, 0, -1):
            o = 3 ** N - 2 ** n
            if o < 0:
                tot = 0.
            else:
                if N == 1:
                    tot = sum(pz[-o:])
                if N == 2:
                    tot = sum(list(out1.values())[-o:])
                if N == 3:
                    tot = sum(list(out2.values())[-o:])
            print(f'{N} | {n} | {round(tot, 4)}')



if __name__ == '__main__':
    tima = 'на дворе - трава, на траве - дрова, не руби дрова на траве двора!'
    vlad = 'и прыгают скороговорки, как караси на сковородке.'
    slav = 'павел павлушку пеленовал-пеленовал и распеленовывал.'
    ev4g = 'скреативлен креатив не по-креативному, нужно перекреативить!'
    artem = 'расскажите про покупки! про покупки, про покупки, про покупочки свои.'

    l2t1(artem, False)
