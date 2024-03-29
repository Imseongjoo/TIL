# 2576 홀수
# 문제
# 7개의 자연수가 주어질 때, 이들 중 홀수인 자연수들을 모두 골라 그 합을 구하고, 고른 홀수들 중 최솟값을 찾는 프로그램을 작성하시오.

# 예를 들어, 7개의 자연수 12, 77, 38, 41, 53, 92, 85가 주어지면 이들 중 홀수는 77, 41, 53, 85이므로 그 합은

# 77 + 41 + 53 + 85 = 256이 되고, 1 < 53 < 77 < 85이므로 홀수들 중 최솟값은 41이 된다.

# 입력
# 입력의 첫째 줄부터 일곱 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100보다 작다.

# 출력
# 홀수가 존재하지 않는 경우에는 첫째 줄에 -1을 출력한다. 홀수가 존재하는 경우 첫째 줄에 홀수들의 합을 출력하고, 둘째 줄에 홀수들 중 최솟값을 출력한다.

result = 0
ls = []
for i in range(7):
    num = int(input())
    if num % 2 != 0:
        ls.append(int(num))
    else:
        pass
if sum(ls) == 0:
    print(-1)
else:
    print(sum(ls))
    print(min(ls))

# 10822 더하기
# 문제
# 숫자와 콤마로만 이루어진 문자열 S가 주어진다. 이때, S에 포함되어있는 자연수의 합을 구하는 프로그램을 작성하시오.

# S의 첫 문자와 마지막 문자는 항상 숫자이고, 콤마는 연속해서 주어지지 않는다. 주어지는 수는 항상 자연수이다.

# 입력
# 첫째 줄에 문자열 S가 주어진다. S의 길이는 최대 100이다. 포함되어있는 정수는 1,000,000보다 작거나 같은 자연수이다.

# 출력
# 문자열 S에 포함되어 있는 자연수의 합을 출력한다.

string = input()
ls = string.split(',')
nls = list(map(int, ls))
print(sum(nls))

# 2754 학점계산
# 문제
# 어떤 사람의 C언어 성적이 주어졌을 때, 평점은 몇 점인지 출력하는 프로그램을 작성하시오.

# A+: 4.3, A0: 4.0, A-: 3.7

# B+: 3.3, B0: 3.0, B-: 2.7

# C+: 2.3, C0: 2.0, C-: 1.7

# D+: 1.3, D0: 1.0, D-: 0.7

# F: 0.0

# 입력
# 첫째 줄에 C언어 성적이 주어진다. 성적은 문제에서 설명한 13가지 중 하나이다.

# 출력
# 첫째 줄에 C언어 평점을 출력한다.

score = {"A+": 4.3, "A0": 4.0, "A-": 3.7,  "B+": 3.3,
         "B0": 3.0, "B-": 2.7, "C+": 2.3, "C0": 2.0, "C-": 1.7,
         "D+": 1.3, "D0": 1.0, "D-": 0.7, "F": 0.0}
print(score[input()])

# 5622 다이얼
# 문제
# 상근이의 할머니는 아래 그림과 같이 오래된 다이얼 전화기를 사용한다.

# 전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 돌려야 한다. 숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.

# 숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.

# 상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.

# 할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 단어의 길이는 2보다 크거나 같고, 15보다 작거나 같다.

# 출력
# 첫째 줄에 다이얼을 걸기 위해서 필요한 최소 시간을 출력한다.

number = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
alpha = input()
time = 0
for i in range(len(alpha)):
    for j in number:
        if alpha[i] in j:
            time += number.index(j)+3
print(time)

# 2577 숫자의 개수
# 문제
# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

# 예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고, 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.

# 입력
# 첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어진다. A, B, C는 모두 100보다 크거나 같고, 1,000보다 작은 자연수이다.

# 출력
# 첫째 줄에는 A × B × C의 결과에 0 이 몇 번 쓰였는지 출력한다. 마찬가지로 둘째 줄부터 열 번째 줄까지 A × B × C의 결과에 1부터 9까지의 숫자가 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력한다.

num1 = int(input())
num2 = int(input())
num3 = int(input())
result = list(str(num1 * num2 * num3))
for i in range(10):
    print(result.count(str(i)))

# 7785 회사에 있는 사람
# 문제
# 상근이는 세계적인 소프트웨어 회사 기글에서 일한다. 이 회사의 가장 큰 특징은 자유로운 출퇴근 시간이다. 따라서, 직원들은 반드시 9시부터 6시까지 회사에 있지 않아도 된다.

# 각 직원은 자기가 원할 때 출근할 수 있고, 아무때나 퇴근할 수 있다.

# 상근이는 모든 사람의 출입카드 시스템의 로그를 가지고 있다. 이 로그는 어떤 사람이 회사에 들어왔는지, 나갔는지가 기록되어져 있다. 로그가 주어졌을 때, 현재 회사에 있는 모든 사람을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 로그에 기록된 출입 기록의 수 n이 주어진다. (2 ≤ n ≤ 106) 다음 n개의 줄에는 출입 기록이 순서대로 주어지며, 각 사람의 이름이 주어지고 "enter"나 "leave"가 주어진다. "enter"인 경우는 출근, "leave"인 경우는 퇴근이다.

# 회사에는 동명이인이 없으며, 대소문자가 다른 경우에는 다른 이름이다. 사람들의 이름은 알파벳 대소문자로 구성된 5글자 이하의 문자열이다.

# 출력
# 현재 회사에 있는 사람의 이름을 사전 순의 역순으로 한 줄에 한 명씩 출력한다.

n = int(input())
dic = {}
for i in range(n):
    name, log = input().split()
    dic[name] = log
    if log == "leave":
        del dic[name]

d = sorted(dic.items(), reverse=True)
dic = dict(d)

for key in dic.keys():
    print(key)
