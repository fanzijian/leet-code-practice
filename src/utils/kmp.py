class KMP():
    def __init__(self):
        pass

    def fail(self, P):
        M = len(P)
        j, k = 1, 0
        fail_list = [0 for i in range(M)]
        while j < M:
            if P[j] == P[k]:
                k += 1
                fail_list[j] = k
                j += 1
            elif k > 0:
                k = fail_list[k-1]
            else:
                j += 1
        return fail_list

    def kmp(self, S, P):
        N, M = len(S), len(P)
        if M == 0:
            return 0
        i, j = 0, 0
        fail_list = self.fail(P)
        while i < N:
            if S[i] == P[j]:
                i += 1
                j += 1
                if j >= M:
                    return i - M
            elif j > 0:
                j = fail_list[j-1]
            else:
                i += 1
        return -1

if __name__ == "__main__":
    P = "abcabdab"
    S = "aaaabcacdabcabdabcabcabcabdab"
    obj = KMP()
    print obj.fail(P)
    print obj.kmp(S, P)
    pass
