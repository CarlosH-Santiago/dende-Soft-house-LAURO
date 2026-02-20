from dende_statistics import Statistics
import csv

def carregar_dados_spotify(caminho_arquivo):
    print(f"Carregando dados de: {caminho_arquivo}")
    
    # Estrutura para transdormar Linhas (CSV) em Colunas (Nosso requisito)
    dados = {
        'track_name': [],
        'artist_name': [],
        'artist_genres': [],
        'explicit': [],
        'album_type': [],
        'track_popularity': [], # Inteiro
        'artist_popularity': [], # Inteiro
        'artist_followers': [], # Inteiro
        'album_total_tracks': [],  # Inteiro
        'track_duration_min': [] # Float
    }
    
    try:   
        
        with open(caminho_arquivo, mode='r', encoding='utf-8') as file:
            leitor = csv.DictReader(file)
            
            contagem = 0
            for linha in leitor:
                # Preenchendo linhas
                dados['track_name'].append(linha['track_name'])
                dados['artist_name'].append(linha['artist_name'])
                dados['artist_genres'].append(linha['artist_genres'])
                dados['explicit'].append(linha['explicit'])
                dados['album_type'].append(linha['album_type'])

                # Convertendo Números (Tratando possíveis erros de conversão)
                try:
                    dados['track_popularity'].append(int(linha['track_popularity']))
                except ValueError:
                    dados['track_popularity'].append(0) # Valor padrão em caso de erro
                
                try:
                    dados['artist_popularity'].append(int(linha['artist_popularity']))
                except ValueError:
                    dados['artist_popularity'].append(0) 
                
                try:
                    dados['artist_followers'].append(int(linha['artist_followers']))
                except ValueError:
                    dados['artist_followers'].append(0) 

                try:
                    dados['album_total_tracks'].append(int(linha['album_total_tracks']))
                except ValueError:
                    dados['album_total_tracks'].append(0) 
                
                try:
                    dados['track_duration_min'].append(float(linha['track_duration_min']))
                except ValueError:
                    dados['track_duration_min'].append(0.0) 
                    
                contagem += 1
                    
        print(f"Leitura concluída! {contagem} linhas processadas.\n")
        return dados
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado no caminho: {caminho_arquivo}")
        return {}

def main():
    caminho = 'src/data/spotify_data_clean.csv'
    
    # Carregar dados
    print("Carregando dados do Spotify...\n")
    detaset_spotify = carregar_dados_spotify(caminho)
    
    if detaset_spotify:
        try:        
            # Instanciar a Classe
            stats = Statistics(detaset_spotify)
            
            # Gerar Relatório
            print("--- Análise Exploratória: ---\n")
            
            print("1. TENDÊNCIA CENTRAL")
            print(f"Média de duração: {stats.mean('track_duration_min'):.2f} min")
            print(f"Mediana de duração: {stats.median('track_duration_min'):.2f} min")
            print(f"Moda (Tipo de Álbum): {stats.mode('album_type')}\n")

            print("2. DISPERSÃO E POSIÇÃO")
            print(f"Desvio Padrão (Seguidores): {stats.stdev('artist_followers'):.2f}")
            print(f"Quartis de Popularidade: {stats.quartiles('track_popularity')}\n")

            print("3. FREQUÊNCIAS E CONJUNTOS")
            print(f"Tipos únicos (Itemset Explícito): {stats.itemset('explicit')}")
            print(f"Freq. Absoluta (Explícito): {stats.absolute_frequency('explicit')}")
            print(f"Freq. Relativa (Explícito): {stats.relative_frequency('explicit')}\n")

            print("4. RELAÇÕES E AVANÇADOS")
            print(f"Covariância (Pop. Faixa vs Artista): {stats.covariance('track_popularity', 'artist_popularity'):.2f}")
            
            # Estes retornarão 'None' até que sejam implementados no dende_statistics.py
            print(f"Prob. Condicional (Explícito -> Explícito): {stats.conditional_probability('explicit', 'TRUE', 'TRUE')}")
            print(f"Histograma de Duração (5 bins): {stats.histogram('track_duration_min', bins=5)}\n")
            
        except Exception as e:
            print(f"Erro na execução da Statistics: {e}")
            
            
if __name__ == "__main__":
    main()