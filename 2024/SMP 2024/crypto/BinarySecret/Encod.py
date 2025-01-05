def x(y, z, w):
    q = []
    for t in y:
        u = ord(t)
        p = u * (z + w)
        q.append(bin(p)[2:])
    return q

def n():
    z = 69
    w = 67
    y = "SMP{thisislooklikeflagisn'tit?}"
    q = x(y, z, w)
    d = ' '.join(q)
    print(d)

if __name__ == "__main__":
    n()
