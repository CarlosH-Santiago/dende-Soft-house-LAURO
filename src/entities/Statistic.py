def calcular_media(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)

def calcular_mediana(lista):
    if not lista:
        return 0
    sorted_lista = sorted(lista)
    n = len(sorted_lista)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lista[mid - 1] + sorted_lista[mid]) / 2
    else:
        return sorted_lista[mid]

def calcular_moda(lista):
    if not lista:
        return None
    from collections import Counter
    counter = Counter(lista)
    moda = counter.most_common(1)[0][0]
    return moda

def calcular_variancia(lista):
    if not lista:
        return 0
    media = calcular_media(lista)
    variancia = sum((x - media) ** 2 for x in lista) / len(lista)
    return variancia

def calcular_desvio_padrao(lista):
    variancia = calcular_variancia(lista)
    return variancia ** 0.5

def calcular_percentil(lista, percentil):
    if not lista:
        return 0
    sorted_lista = sorted(lista)
    k = (len(sorted_lista) - 1) * (percentil / 100)
    f = int(k)
    c = k - f
    if f + 1 < len(sorted_lista):
        return sorted_lista[f] + c * (sorted_lista[f + 1] - sorted_lista[f])
    else:
        return sorted_lista[f]

def calcular_quartis(lista):
    if not lista or len(lista) < 4:
        return None
    sorted_lista = sorted(lista)
    n = len(sorted_lista)

    q1 = calcular_percentil(sorted_lista, 25)

    q2 = calcular_percentil(sorted_lista, 50)
 
    q3 = calcular_percentil(sorted_lista, 75)
    
    return {
        'Q1': q1,
        'Q2': q2,
        'Q3': q3,
        'IQR': q3 - q1
    }

def calcular_covariancia(lista_x, lista_y):
    if not lista_x or not lista_y or len(lista_x) != len(lista_y):
        return 0
    
    media_x = calcular_media(lista_x)
    media_y = calcular_media(lista_y)
    
    covariancia = sum((lista_x[i] - media_x) * (lista_y[i] - media_y) for i in range(len(lista_x))) / len(lista_x)
    
    return covariancia

