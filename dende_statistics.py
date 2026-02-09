class Statistics:
    """
    Uma classe para realizar cálculos estatísticos em um conjunto de dados.

    Atributos
    ----------
    dataset : dict[str, list]
        O conjunto de dados, estruturado como um dicionário onde as chaves
        são os nomes das colunas e os valores são listas com os dados.
    """
    def __init__(self, dataset):
        """
        Inicializa o objeto Statistics.

        Parâmetros
        ----------
        dataset : dict[str, list]
            O conjunto de dados, onde as chaves representam os nomes das
            colunas e os valores são as listas de dados correspondentes.
        """
        self.dataset = dataset

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

    def itemset(self, column):
        """
        Retorna o conjunto de itens únicos em uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        set
            Um conjunto com os valores únicos da coluna.
        """
        pass

    def absolute_frequency(self, column):
        """
        Calcula a frequência absoluta de cada item em uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        dict
            Um dicionário onde as chaves são os itens e os valores são
            suas contagens (frequência absoluta).
        """
        pass

    def relative_frequency(self, column):
        """
        Calcula a frequência relativa de cada item em uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        dict
            Um dicionário onde as chaves são os itens e os valores são
            suas proporções (frequência relativa).
        """
        pass

    def cumulative_frequency(self, column, frequency_method='absolute'):
        """
        Calcula a frequência acumulada (absoluta ou relativa) de uma coluna.

        A frequência é calculada sobre os itens ordenados.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).
        frequency_method : str, opcional
            O método a ser usado: 'absolute' para contagem acumulada ou
            'relative' para proporção acumulada (padrão é 'absolute').

        Retorno
        -------
        dict
            Um dicionário ordenado com os itens como chaves e suas
            frequências acumuladas como valores.
        """
        pass

    def conditional_probability(self, column, value1, value2):
        """
        Calcula a probabilidade condicional P(X_i = value1 | X_{i-1} = value2).

        Este método trata a coluna como uma sequência e calcula a probabilidade
        de encontrar `value1` imediatamente após `value2`.

        Fórmula: P(A|B) = Contagem de sequências (B, A) / Contagem total de B

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).
        value1 : any
            O valor do evento consequente (A).
        value2 : any
            O valor do evento condicionante (B).

        Retorno
        -------
        float
            A probabilidade condicional, um valor entre 0 e 1.
        """
        pass

    def quartiles(self, column):
        """
        Calcula os quartis (Q1, Q2 e Q3) de uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        dict
            Um dicionário com os quartis Q1, Q2 (mediana) e Q3.
        """
        pass

    def histogram(self, column, bins):
        """
        Gera um histograma baseado em buckets (intervalos).

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).
        bins : int
            Número de buckets (intervalos).

        Retorno
        -------
        dict
            Um dicionário onde as chaves são os intervalos (tuplas)
            e os valores são as contagens.
        """
        pass

