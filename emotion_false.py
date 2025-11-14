import random
from fractions import Fraction #파이썬의 소수점 계산 오차를 줄이기 위한 라이브러리(분수로 표현)

most_selected_index = [0,0,0,0,0]
for l in range(1000):
    #초기값 설정
    lr = Fraction(1/10) #오차 변경값

    #가중치를 랜덤값으로 설정
    num_list = [Fraction(random.randint(0, 10), 10) for _ in range(5)]
    w1, w2, w3, w4, b = num_list

    print(f"""
    
    [ 최단거리 선로 탐색 모델 ]
    
    오차 변경값 : {float(lr)}
    초기 가중치 설정:
    w1 : {float(w1)}
    w2 : {float(w2)}
    w3 : {float(w3)}
    
    편향 : {float(b)}
    """)

    #입력값 = 거리, 사람 수, 연료소비
    def perceptron(x1,x2,x3):
        p = w1 * x1 + w2 * x2 + w3 + x3 + b
        return p

    def update_weights(x1, x2, x3, reward):
        global w1, w2, w3, b
        #퍼셉트론 학습 규칙을 적용한 가중치 없데이트
        w1 += lr * reward * x1
        w2 += lr * reward * x2
        w3 += lr * reward * x3
        b  += lr * reward
        print(f"변경된 가중치: {float(w1)},{float(w2)},{float(w3)},{float(w4)},{float(b)}")

    case1 = {
        1:[Fraction(1/10), Fraction(10 / 10), Fraction(1 / 10)],
        2:[Fraction(3/10), Fraction(5 / 10), Fraction(3 / 10)],
        3:[Fraction(5/10), Fraction(0 / 10), Fraction(5 / 10)],
        4:[Fraction(8/10), Fraction(0 / 10), Fraction(8 / 10)],
        5:[Fraction(8/10), Fraction(0 / 10), Fraction(8 / 10)],
    }
    case2 = {
        1:[Fraction(2/10), Fraction(8 / 10), Fraction(2 / 10)],
        2:[Fraction(4/10), Fraction(3 / 10), Fraction(5 / 10)],
        3:[Fraction(6/10), Fraction(1 / 10), Fraction(7 / 10)],
        4:[Fraction(9/10), Fraction(1 / 10), Fraction(8 / 10)],
        5:[Fraction(10/10), Fraction(0 / 10), Fraction(10 / 10)],
    }
    case3 = {
        1:[Fraction(3/10), Fraction(7 / 10), Fraction(4 / 10)],
        2:[Fraction(6/10), Fraction(5 / 10), Fraction(6 / 10)],
        3:[Fraction(8/10), Fraction(2 / 10), Fraction(8 / 10)],
        4:[Fraction(10/10), Fraction(0 / 10), Fraction(10 / 10)],
        5:[Fraction(10/10), Fraction(0 / 10), Fraction(10 / 10)],
    }

    index_count = [0,0,0,0,0]
    after_500_index_count = [0,0,0,0,0]
    reward_list = [2, 1, -1, -2, -3]

    def case_1():
        result = []
        for k in range(5):
            result.append(perceptron(*case1[k + 1]))
        result_min = min(result)
        result_min_index = result.index(result_min)

        reward = -float(result_min)

        x1, x2, x3 = case1[result_min_index + 1]
        update_weights(x1, x2, x3, reward)
        return result_min_index

    def case_2():
        result = []
        for k in range(5):
            result.append(perceptron(*case2[k + 1]))
        result_min = min(result)
        result_min_index = result.index(result_min)

        reward = -float(result_min)

        x1, x2, x3 = case2[result_min_index + 1]
        update_weights(x1, x2, x3, reward)
        return result_min_index

    def case_3():
        result = []
        for k in range(5):
            result.append(perceptron(*case3[k + 1]))
        result_min = min(result)
        result_min_index = result.index(result_min)

        reward = -float(result_min)

        x1, x2, x3 = case3[result_min_index + 1]
        update_weights(x1, x2, x3, reward)
        return result_min_index
    for j in range(2000):
        a, b, c = case_1(), case_2(), case_3()
        index_count[a] += 1
        index_count[b] += 1
        index_count[c] += 1

        if j >= 1000:
            after_500_index_count[a] += 1
            after_500_index_count[b] += 1
            after_500_index_count[c] += 1

    print(f"""
    
[학습 결과]
case1 선택됨 : {index_count[0]}
case2 선택됨 : {index_count[1]}
case3 선택됨 : {index_count[2]}
case4 선택됨 : {index_count[3]}
case5 선택됨 : {index_count[4]}

[after 500]
case1 선택됨 : {after_500_index_count[0]}
case2 선택됨 : {after_500_index_count[1]}
case3 선택됨 : {after_500_index_count[2]}
case4 선택됨 : {after_500_index_count[3]}
case5 선택됨 : {after_500_index_count[4]}

[학습된 퍼셉트론]
{w1} * x1 + {w2} * x2 + {w3} * x3 + {b}
    """)

    most_selected_index[index_count.index(max(index_count))] += 1

print(f"""

[최종 결과]
case1 : {most_selected_index[0]/10}%
case2 : {most_selected_index[1]/10}%
case3 : {most_selected_index[2]/10}%
case4 : {most_selected_index[3]/10}%
case5 : {most_selected_index[4]/10}%
""")