while True:
    e = int(input())
    if e == 0:
        break
    I = 100
    while I**3 > e:
        I = I - 1
    J = 173
    e1 = e - I**3
    while J**2 > e1:
        J = J - 1
    m = I + J + e - I**3 - J**2
    i = I - 1
    j = J
    while i >= 0:
        e1 = e - i**3
        if e1 <= (m-i)**2:
            while j ** 2 <= e1:
                J = j
                j = j + 1
            j = J
            if i + j + e1 - j **2 < m:
                m = i + j + e1 - j **2
        i = i - 1
    print(m)