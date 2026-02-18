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

    def mean(self, column):
        """
        Calcula a média aritmética de uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        float
            A média dos valores na coluna.
        """
        pass

    def median(self, column):
        """
        Calcula a mediana de uma coluna.

        A mediana é o valor central de um conjunto de dados ordenado.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        float
            O valor da mediana da coluna.
        """
        pass

    def mode(self, column):
        """
        Encontra a moda (ou modas) de uma coluna.

        A moda é o valor que aparece com mais frequência no conjunto de dados.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        list
            Uma lista contendo o(s) valor(es) da moda.
        """
        pass

    def variance(self, column):
        """
        Calcula a variância populacional de uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        float
            A variância dos valores na coluna.
        """
        pass

    def stdev(self, column):
        """
        Calcula o desvio padrão populacional de uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        float
            O desvio padrão dos valores na coluna.
        """
        pass

    def covariance(self, column_a, column_b):
        """
        Calcula a covariância entre duas colunas.

        Parâmetros
        ----------
        column_a : str
            O nome da primeira coluna (X).
        column_b : str
            O nome da segunda coluna (Y).

        Retorno
        -------
        float
            O valor da covariância entre as duas colunas.
        """
        pass

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

    def absolute_frequency(self, column):
        data = self.dataset[column]
        freq = {}
        for item in data:
            freq[item] = freq.get(item, 0) + 1
            
        return freq

    def relative_frequency(self, column):
        abs_freq = self.absolute_frequency(column)
        total = len(self.dataset[column])
        rel_freq = {}
        
        for k, v in abs_freq.items(): 
            rel_freq[k] = v / total 
            
        return rel_freq 

    def cumulative_frequency(self, column, frequency_method='absolute'):
        
        data = sorted(self.dataset[column])
        
        if frequency_method == 'absolute':
            freq = self.absolute_frequency(column)
        else: 
            freq = self.relative_frequency(column)
            
        cumulative = {}
        total = 0
        for item in data:
            total += freq[item]
            cumulative[item] = total
            
        return cumulative

    def conditional_probability(self, column, value1, value2):
        data = self.dataset[column] 
        count_b = 0
        count_ba = 0
        for i in range(len(data) - 1):
            if data[i] == value2:
                count_b += 1
                if data[i + 1] == value1:
                    count_ba += 1
        
        return count_ba / count_b if count_b > 0 else 0

    def histogram(self, column, bins):
        data = self.dataset[column]
        min_val, max_val = min(data), max(data)
        interval = (max_val - min_val) / bins
        hist = {}
        for i in range(bins):
            start = min_val + i * interval
            end = start + interval
            count = 0
            for x in data:
                if start <= x < end or (i == bins - 1 and x == max_val):
                    count += 1
            hist[(start, end)] = count
            
        return hist