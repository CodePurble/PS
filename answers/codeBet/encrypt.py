T = int(input())
cases = {}

for i in range(T):
    params = input().split(" ")
    message = input()
    cases[message] = params

for message in cases.keys():
    N = int(message.params[0])
    X = int(message.params[1])
    Y = int(message.params[2])

