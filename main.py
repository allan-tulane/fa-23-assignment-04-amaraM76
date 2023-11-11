import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, MED={}):
    if (S, T) in MED:
        return MED[(S, T)]
    if S == "":
        result = len(T)
    elif T == "":
        result = len(S)
    else:
        if S[0] == T[0]:
            result = fast_MED(S[1:], T[1:], MED)
        else:
            result = 1 + min(fast_MED(S, T[1:], MED), fast_MED(S[1:], T, MED))


    MED[(S, T)] = result
    return result


for S, T in test_cases:
    result = fast_MED(S, T)
    print(result)


for (S, T), alignment in zip(test_cases, alignments):
    result = fast_MED(S, T)
    print(result)


def fast_align_MED(S, T, MED={}):
    # TODO - keep track of alignment
    if (S, T) in MED:
        return MED[(S, T)]

    if S == "":
        result = len(T), '-' * len(T), T
    elif T == "":
        result = len(S), S, '-' * len(S)
    else:
        if S[0] == T[0]:
            result = fast_align_MED(S[1:], T[1:], MED)
        else:
            del_cost, del_S, del_T = fast_align_MED(S, T[1:], MED)
            ins_cost, ins_S, ins_T = fast_align_MED(S[1:], T, MED)
            sub_cost, sub_S, sub_T = fast_align_MED(S[1:], T[1:], MED)


            if del_cost <= ins_cost and del_cost <= sub_cost:
                result = del_cost + 1, '-' + del_S, T[0] + del_T
            elif ins_cost <= del_cost and ins_cost <= sub_cost:
                result = ins_cost + 1, S[0] + ins_S, '-' + ins_T
            else:
                result = sub_cost + 1, S[0] + sub_S, T[0] + sub_T


    MED[(S, T)] = result
    return result


def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])
