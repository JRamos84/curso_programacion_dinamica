import random
import collections

PALOS = ['espada','corazon','rombo','trebol']
VALORES = ['as','2','3','4','5','6','7','8','9','10','jota','reina','rey']

def crear_baraja():
    barajas =[]
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo,valor))
    return barajas
def obtener_mano(barajas, tamano_mano):
    mano = random.sample(barajas,tamano_mano)
    return mano
    
def main(tamano_mano, intentos):
    barajas = crear_baraja()
    
    manos = []
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)
        
        
    corrida = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])
       # print(valores) 
        
        ## Ordenar valores 
        convertir_mano = []
        for i in range(len(valores)):
            for j in range(len(VALORES)):
                if valores[i] == VALORES[j]:
                    convertir_mano.append(j)
        #print(convertir_mano)
        ## Ordenar la mano
        ordenar_mano=[]
        for i in range(len(convertir_mano)):
            for j in range(len(convertir_mano)):
                if convertir_mano[i] < convertir_mano[j]:
                    r = convertir_mano[j]
                    convertir_mano[j] = convertir_mano[i]
                    convertir_mano[i] = r
       # print(convertir_mano)
        ## comparar con la corrida
        cuenta = 0 
        for i in range(tamano_mano):
            if i == convertir_mano[i]:
                cuenta +=1
        if cuenta == tamano_mano:
            corrida +=1
                
    print(corrida/intentos)

                    
                
            
        
        
        ## Comparar con la lista de valores 
        
        
        
        
    
              
              
if __name__ == '__main__':
    tamano_mano = int(input('De cuantas barajas sera la mano: '))
    intentos = int(input('Cuantos intentos para calcular la probabilidad: '))
    main(tamano_mano,intentos)
        

