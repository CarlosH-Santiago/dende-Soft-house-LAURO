class Statistics:
    """Uma classe para realizar cálculos estatísticos em um conjunto de dados."""

    def __init__(self, dataset):
        """Inicializa o objeto Statistics."""
        
        # 1. Validação: É um dicionário?
        if not isinstance(dataset, dict): 
            raise ValueError("O dataset deve ser um dicionário (mapa)")
        
        # 2. Validação: Todas as listas têm o mesmo tamanho?
        # Pega o tamanho da primeira lista para comparar com as outras
        lengths = [len(v) for v in dataset.values() if isinstance(v, list)]
        if len(set(lengths)) > 1 :
            raise ValueError("Todas as colunas devem possuir o mesmo tamanho.")
        
        # 3. Validação: Dados de uma coluna são do mesmo tipo?
        for column_name, values in dataset.items():
            if not isinstance(values, list) :
                raise ValueError(f"O valor da chave '{column_name}' deve ser uma lista.")
            
            if len(values) > 0 :
                first_type = type(values[0])
                if not all(isinstance(item, first_type) for item in values):
                    raise ValueError(f"A coluna '{column_name}' pussui tipos de dados mistos.")
        
        self.dataset = dataset
        
        # Mapa de ordem para colunas ordinais (Hardcoded para atender ao domínio do problema)
        self.ordinal_map = {
            "priority": ["baixa", "media", "alta"]
        }


    def _is_numeric(self, column):
        """Verifica se uma coluna possui dados numéricos (int ou float). Método auxiliar para validação antes de cálculos matemáticos."""
        
        # 1. Verifica se a coluna existe no dataset
        if column not in self.dataset: 
            raise KeyError(f"A coluna '{column}' não existe no dataset")
        
        # 2. Pega a lista de dados
        values = self.dataset[column]
        
        # 3. Se a lista estiver vazia, não é numérica (ou não importa)
        if not values:
            return False
        
        # 4. Verifica o tipo do primeiro elemento
        # (Como o __init__ já garantiu que todos são iguais, basta olhar o primeiro)
        return isinstance(values[0], (int, float))
        
    def _sort_values(self, values, column):
        """Ordena uma lista de valores. Se a coluna for ordinal, usa a ordem definida."""
        if column in self.ordinal_map:
            # Cria um dicionário de peso para cada valor: {'baixa': 0, 'media': 1, ...}
            order_weights = {val: i for i, val in enumerate(self.ordinal_map[column])}
            # Ordena usando o peso. Valores não mapeados vão para o fim.
            return sorted(values, key=lambda x: order_weights.get(x, float('inf')))
        
        # Ordenação padrão (numérica ou alfabética)
        return sorted(values)
        
    def mean(self, column):
        """Calcula a média aritmética de uma coluna."""

        if not self._is_numeric(column):
            raise ValueError(f"A coluna '{column}' não é numérica.")
            
        lista = self.dataset[column]
        if not lista:
            return 0.0
            
        return sum(lista) / len(lista)

    def median(self, column):
        """Calcula a mediana de uma coluna."""

        data = self._sort_values(self.dataset[column], column)
        n = len(data)
        if n == 0:
            return 0.0
            
        mid = n // 2
        if n % 2 == 0:
            if self._is_numeric(column):
                return (data[mid - 1] + data[mid]) / 2.0
            # Para dados não numéricos, a convenção é pegar o elemento inferior.
            return data[mid - 1]
        else:
            return data[mid]


    def mode(self, column):
        """Encontra a moda (ou modas) de uma coluna."""

        if column not in self.dataset:
            raise KeyError(f"A coluna '{column}' não existe no dataset.")
            
        lista = self.dataset[column]
        if not lista:
            return []
            
        frequencias = {}
        for item in lista:
            if item in frequencias:
                frequencias[item] += 1
            else:
                frequencias[item] = 1
                
        max_freq = max(frequencias.values())
        return [k for k, v in frequencias.items() if v == max_freq]

    def variance(self, column):
        """Calcula a variância populacional de uma coluna."""

        if not self._is_numeric(column):
            raise ValueError(f"A coluna '{column}' não é numérica.")
            
        lista = self.dataset[column]
        if not lista:
            return 0.0
            
        media = self.mean(column)
        return sum((x - media) ** 2 for x in lista) / len(lista)

    def stdev(self, column):
        """Calcula o desvio padrão populacional de uma coluna."""

        return self.variance(column) ** 0.5

    def covariance(self, column_a, column_b):
        """Calcula a covariância entre duas colunas."""

        if not self._is_numeric(column_a) or not self._is_numeric(column_b):
            raise ValueError("Ambas as colunas devem ser numéricas para calcular covariância.")
            
        lista_a = self.dataset[column_a]
        lista_b = self.dataset[column_b]
        
        media_a = self.mean(column_a)
        media_b = self.mean(column_b)
        n = len(lista_a)
        
        if n == 0:
            return 0.0
            
        return sum((lista_a[i] - media_a) * (lista_b[i] - media_b) for i in range(n)) / n

    def itemset(self, column):
        """ Retorna o conjunto de itens únicos em uma coluna."""

        return set(self.dataset[column])

    def absolute_frequency(self, column):
        """Calcula a frequência absoluta de cada item em uma coluna."""

        data = self.dataset[column]
        freq = {}
        for item in data:
            freq[item] = freq.get(item, 0) + 1
            
        return freq

    def relative_frequency(self, column):
        """Calcula a frequência relativa de cada item em uma coluna."""

        abs_freq = self.absolute_frequency(column)
        total = len(self.dataset[column])
        rel_freq = {}
        
        for k, v in abs_freq.items(): 
            rel_freq[k] = v / total 
            
        return rel_freq 

    def cumulative_frequency(self, column, frequency_method='absolute'):
        """Calcula a frequência acumulada (absoluta ou relativa) de uma coluna."""
        
        if frequency_method == 'absolute':
            freq = self.absolute_frequency(column)
        else: 
            freq = self.relative_frequency(column)
        
        sorted_keys = self._sort_values(list(freq.keys()), column)

        cumulative = {}
        total = 0
        for item in sorted_keys:
            total += freq[item]
            cumulative[item] = total
            
        return cumulative

    def conditional_probability(self, column, value1, value2):
        """Calcula a probabilidade condicional P(X_i = value1 | X_{i-1} = value2)."""

        data = self.dataset[column] 
        count_b = 0
        count_ba = 0
        for i in range(len(data) - 1):
            if data[i] == value2:
                count_b += 1
                if data[i + 1] == value1:
                    count_ba += 1
        
        return count_ba / count_b if count_b > 0 else 0

    def quartiles(self, column):
        """Calcula os quartis (Q1, Q2 e Q3) de uma coluna."""

        if not self._is_numeric(column):
            raise ValueError(f"A coluna '{column}' não é numérica.")
            
        lista = sorted(self.dataset[column])
        n = len(lista)
        if n < 4:
            return None
            
        def calcular_percentil(sorted_lista, percentil):
            # Método Inclusivo (N-1) - Padrão estatístico comum
            k = (len(sorted_lista) - 1) * (percentil / 100.0)
            f = int(k)
            c = k - f
            if f + 1 < len(sorted_lista):
                return sorted_lista[f] + c * (sorted_lista[f + 1] - sorted_lista[f])
            return sorted_lista[f]

        q1 = calcular_percentil(lista, 25)
        q2 = calcular_percentil(lista, 50)
        q3 = calcular_percentil(lista, 75)
        
        return {
            'Q1': q1,
            'Q2': q2,
            'Q3': q3,
        }

    def histogram(self, column, bins):
        """Gera um histograma baseado em buckets (intervalos)."""
        
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