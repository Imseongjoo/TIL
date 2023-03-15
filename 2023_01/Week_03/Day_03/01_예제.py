# 2789 유학 금지
# 문제
# 아주 멀리 떨어져 있는 작은 나라가 있다. 이 나라에서 가장 공부를 잘하는 학생들은 모두 다른 나라로 유학을 간다. 정부는 최고의 학생들이 자꾸 유학을 가는 이유를 찾으려고 했다. 하지만, 학생들의 이유가 모두 달랐기 때문에 정확한 이유를 찾을 수 없었다. 정부의 고위직은 뛰어난 학생들이 자꾸 유학을 가는 현상을 매우 불쾌해 했다.

# 가장 많은 학생들이 유학을 가는 대학교는 영국의 캠브리지 대학교이다. 정부는 인터넷 검열을 통해서 해외로 나가는 이메일의 내용 중 일부를 삭제하기로 했다. 이메일의 각 단어 중에서 CAMBRIDGE에 포함된 알파벳은 모두 지우기로 했다. 즉, 어떤 이메일에 LOVA란 단어가 있다면, A는 CAMBRIDGE에 포함된 알파벳이기 때문에, 받아보는 사람은 LOV로 받는다.

# 이렇게, 어떤 단어가 주어졌을 때, 검열을 거친 후에는 어떤 단어가 되는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 이 단어는 적어도 3글자이며, 많아야 100글자이다.

# 출력
# 입력으로 주어진 단어를 정부가 검열을 하면 어떻게 변하는지를 출력한다. 즉, 단어에서 CAMBRIDGE에 포함된 알파벳을 모두 지운 뒤 출력한다. 항상 정답의 길이는 0보다 크다.

T = input()
for i in 'CAMBRIDGE':
    T = T.replace(i, '')
print(T)

# string = "KARIJERA"

# compare_word = "CAMBRIDGE" # 비교 알파벳

# # 새로운 결과 문자열
# result = ""

# # 한 글자씩 비교
# # 인덱스 활용 순회
# for index in range(len(string)):
#     # print(string[index])
#     char = string[index]

#     # 포함되지 않은 문자 찾기
#     # print(char, char not in compare_word)
#     if char not in compare_word:
#         # 포함되지 않은 문자라면
#         # 방법 1. end 속성을 활용
#         # print(char, end="")

#         # 방법 2. 새로운 문자열 만들기 (추천)
#         result += char

# print(result)

# 2675 문자열 반복
# 문제
# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.

# QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다.

# 출력
# 각 테스트 케이스에 대해 P를 출력한다.

T = int(input())
for i in range(T):
    N, S = map(str, input().split())
    N = int(N)
    S = list(S)
    for j in range(len(S)):
        print(S[j] * N, end='')
    print('')

# 10988 팰린드롬인지 확인하기
# 문제
# 알파벳 소문자로만 이루어진 단어가 주어진다. 이때, 이 단어가 팰린드롬인지 아닌지 확인하는 프로그램을 작성하시오.

# 팰린드롬이란 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어를 말한다.

# level, noon은 팰린드롬이고, baekjoon, online, judge는 팰린드롬이 아니다.

# 입력
# 첫째 줄에 단어가 주어진다. 단어의 길이는 1보다 크거나 같고, 100보다 작거나 같으며, 알파벳 소문자로만 이루어져 있다.

# 출력
# 첫째 줄에 팰린드롬이면 1, 아니면 0을 출력한다.

W = input()
if W == W[::-1]:
    print(1)
else:
    print(0)

# word = 'tomato'
# print(int(word == word[::-1]))

# https://www.acmicpc.net/problem/10988
# 팰린드롬

# 1. Input
# word = '토마무우마토'
word = input()

# 2. 값 초기화(단어의 인덱스)
# start(시작) : 0
# end(끝) : len(word) - 1
start = 0
end = len(word) - 1
is_pal = True

# 3. while
# start 값이 end보다 작을 때....
while start < end:
    # word[start], word[end] 비교해서
    # 다르면, 팰린드롬이 아니다!
    if word[start] != word[end]:
        is_pal = False
        break
    # 매 반복이 끝나면
    # start는 1씩 증가하고
    # end는 1씩 감소
    start += 1
    end -= 1

# 4. 출력
# 팰린드롬이면 1, 아니면 0을 출력한다.
if is_pal:
    print(1)
else:
    print(0)

# print(int(is_pal))

# 17249 태보태보 총난타
# 문제
# 태보(TaeBo)란, 태권도와 복싱을 조합한 운동이다. 복싱의 공격 기술로는 민첩하게 앞주먹을 뻗으면서 가볍게 치는 잽, 옆으로 치는 펀치인 훅이 있다.

# 선풍적인 인기에 태보 강의를 들으며 태보를 마스터한 혜정이는 이제 펀치 속도가 워낙 빨라서 잽과 훅을 반복하다보면 잔상이 남는다.

# 얼굴의 왼편에 왼손의 잔상이, 오른편에는 오른손이 잔상이 남을 때 혜정이는 주먹을 몇 번 뻗었을까?

# 주먹의 잔상은 =로 시작하여 @로 끝나고, 잔상이 남지 않는 경우는 없다. 얼굴 형태가 (^0^) 꼴이고, 주먹의 잔상이 같은 곳에 위치하지 않는다.

# 입력
# 문자열의 길이는 1,000을 넘지 않는다.

# 출력
# 첫째 줄에 왼손의 잔상의 수와 오른손의 잔상의 수를 출력한다.

i = 0
r = [0, 0]
for c in input():
    if c == '@':
        r[i] += 1
    elif c == '(':
        i ^= 1
print(*r)

# 2941 크로아티아 알파벳
# 문제
# 예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다. 따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.

# 크로아티아 알파벳	변경
# č	c=
# ć	c-
# dž dz=
# đ	d-
# lj lj
# nj nj
# š	s=
# ž	z=
# 예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

# dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다. 위 목록에 없는 알파벳은 한 글자씩 센다.

# 입력
# 첫째 줄에 최대 100글자의 단어가 주어진다. 알파벳 소문자와 '-', '='로만 이루어져 있다.

# 단어는 크로아티아 알파벳으로 이루어져 있다. 문제 설명의 표에 나와있는 알파벳은 변경된 형태로 입력된다.

# 출력
# 입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

C = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
T = input()
for i in C:
    T = T.replace(i, 'a')
print(len(T))

# 10809 알파벳 찾기 h
# 문제
# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

# 출력
# 각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.

# 만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.

S = input()
A = 'abcdefghijklmnopqrstuvwxyz'
for i in A:
    if i in S:
        print(S.index(i), end=' ')
    else:
        print(-1, end=' ')
