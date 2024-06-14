import random


def dos_tirar_dado(numero_de_tiros):
    secuencia_de_tiros =[]
    for _ in range(numero_de_tiros):
        tiro_1 = random.choice([1, 2, 3, 4, 5, 6])
        tiro_2 = random.choice([1, 2, 3, 4, 5, 6])
        secuencia_de_tiros.append([tiro_1,tiro_2])
    return secuencia_de_tiros

def main(numero_de_tiros, numero_de_intentos):
    tiros =[]
    for _ in range(numero_de_intentos):
        secuencia_de_tiros = dos_tirar_dado(numero_de_tiros)
        tiros.append(secuencia_de_tiros)

    tiros_con_12 = 0
    for tiro in tiros:
        #print(tiro)
        for i in tiro:
            #print(i[0] + i [1])
            if (i[0] + i [1]) == 12:
                print(i)
                tiros_con_12 += 1
    print(tiros_con_12/numero_de_intentos)
    print(numero_de_intentos * numero_de_tiros)
    # probabilidad_tiro_con_12 = tiros_con_12 /numero_de_intentos
    # print(f'probabilidad de obtener un 12 por lo menos en un {numero_de_intentos} tiros =  {probabilidad_tiro_con_12} ')

if __name__ == '__main__':
    numero_de_tiros = int(input('Cuantas tiros de dado: '))
    numero_de_intentos = int(input('Cuantas veces correra la simulación: '))

    main(numero_de_tiros, numero_de_intentos)