# coding:utf-8
import random

DRAW = "引き分け" 
A_WINS = "Aの勝ち" 
B_WINS = "Bの勝ち"

# 対応する辞書
HAND = {0: "グー", 1: "チョキ", 2: "パー"}

def junken(a, b):
    
    # judgement[a][b] : A vs B の勝敗
    judgement = [[DRAW, A_WINS, B_WINS], [B_WINS, DRAW, A_WINS], [A_WINS, B_WINS, DRAW]]
    
    # print("Aの手: " + hand[a] + " v.s. Bの手: " + hand[b] + " -> " + judgement[a][b])
    return HAND[a], HAND[b], judgement[a][b]

def junken_3_times():

    count = {DRAW: 0, A_WINS: 0, B_WINS: 0}
    
    for i in range(3):
        # a, bそれぞれの手を生成する
        a = random.randint(0, 2)
        b = random.randint(0, 2)
        a, b, judge = junken(a, b)
        count[judge] += 1
        
    if count[A_WINS] == count[B_WINS]:
        return count[A_WINS], count[B_WINS], DRAW
    elif count[A_WINS] > count[B_WINS]:
        return count[A_WINS], count[B_WINS], A_WINS
    else:
        return count[A_WINS], count[B_WINS], B_WINS
    
def junken_n_players(n):
    n_hands = [random.randint(0, 2) for i in range(n)]
    print(n_hands)
    
    count = {DRAW: 0, A_WINS: 0, B_WINS: 0}
    for i in range(n-1):
        a, b, judge = junken(n_hands[0], n_hands[i+1])
        count[judge] += 1
    
    if (count[A_WINS] > 0 and count[B_WINS] > 0) or count[DRAW] == n-1:
        return DRAW
    elif count[A_WINS] > 0:
        return str([chr(i+65) for i in range(n) if n_hands[0] == n_hands[i]]) + "の勝ち"
    else:
        return str([chr(i+65) for i in range(n) if n_hands[0] != n_hands[i]]) + "の勝ち"
    
if __name__ == "__main__":
    # hand_a, hand_b, judge = junken()
    # print("Aの手: " + hand_a + " v.s. Bの手: " + hand_b + " -> " + judge)
    # print(junken_3_times())
    
    while True:
        result = junken_n_players(10)
        print(result)
        if result != DRAW:
            break