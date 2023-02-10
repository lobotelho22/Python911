# Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo
# (8min15s por quilômetro), então 3 quilômetros a um passo mais rápido
# (7min12s por quilômetro) e 1 quilômetro no mesmo passo usado em
# primeiro lugar, que horas chego em casa para o café da manhã?

stt = (6, 52, 0)


def calculate_hor():
    fst = (0, 8, 15)
    snd = (0, 3 * 7, 3 * 12)
    thd = (0, 8, 15)

    fin = [
        stt[0] + fst[0] + snd[0] + thd[0],
        stt[1] + fst[1] + snd[1] + thd[1],
        stt[2] + fst[2] + snd[2] + thd[2],
    ]

    for index, n in enumerate(fin):
        if index == 0:
            continue
        fin[-index - 1] += fin[-index] // 60
        fin[-index] = fin[-index] % 60

    final_hour = (fin[0], fin[1], fin[2])

    print(final_hour)


calculate_hor()
