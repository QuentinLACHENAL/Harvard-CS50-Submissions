dico = {}

while True:
    try:
        obj = input().upper()
    except EOFError:
        dico = dict(sorted(dico.items()))
        for cle, val in dico.items():
            print(f"{val} {cle}")
        exit(0)

    if not obj in dico:
        dico[obj] = 1
    else:
        dico[obj] += 1
