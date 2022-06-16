def q_hofstadter(q_seq) -> list:
    if q_seq == [1, 2]:
        raise IndexError
    else:
        for _ in range(20):
            n = len(q_seq)
            q_seq.append(q_seq[n - q_seq[n - 1]] + q_seq[n - q_seq[n - 2]])
            yield q_seq


gen = q_hofstadter([1, 1])
for value in gen:
    print(value)
