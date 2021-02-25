
def ackermann(M, N):
    if M == 0:
        return N + 1
    elif M > 0 and N == 0:
        return ackermann(M - 1, 1)
    elif M > 0 and N > 0:
        return ackermann(M - 1, ackermann(M, N - 1))


print(ackermann(3, 5))
