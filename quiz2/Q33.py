N = int(input())
calls = []
left_days = N
earned_money = [0] * (N+6)
for _ in range(N):
    a, b = map(int, input().split())
    calls.append((a, b))

for i in range(N+1):
    for j in range(i):
        days = calls[j][0]
        earned_money[j+days] = max(earned_money[j+days], calls[j][1] + earned_money[j])
    earned_money[i] = max(earned_money[:i+1])


print(max(earned_money[:N+1]))