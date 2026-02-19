from dende_statistics import Statistics
import csv

"""
Espiando o csv :)

import csv

def espiar_csv(caminho):
    print(f"--- ESPIANDO: {caminho} ---\n")
    try:
        with open(caminho, mode='r', encoding='utf-8') as f:
            leitor = csv.reader(f)
            # Pega a primeira linha
            cabecalho = next(leitor) 
            # Pega a segunda linha (dados)
            primeira_linha = next(leitor) 
            
            print(f"COLUNAS ({len(cabecalho)}): {cabecalho}\n")
            print(f"EXEMPLO DE DADO: {primeira_linha}\n")
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}\n")

# Teste rápido
if __name__ == "__main__":
    espiar_csv('src/data/spotify_data_clean.csv')
"""



def carregar_dados_spotfy(caminho_arquivo):
    print(f"Carregando dados de: {caminho_arquivo}")
    
    # Estrutura para transdormar Linhas (CSV) em Colunas (Nosso requisito)
    dados = {
        'track_name': [],
        'artist_name': [],
        'artist_genres': [],
        'explicit': [],
        'track_popularity': [], # Inteiro
        'artist_popularity': [], # Inteiro
        'artist_followers': [], # Inteiro
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
                
                # Convertendo Números (Tratando possíveis erros de conversão)
                try:
                    dados['track_popularity'].append(int(linha['track_popularity']))
                except ValueError:
                    dados['track_popularity'].append(0) # Valor padrão em caso de erro
                
                try:
                    dados['artist_popularity'].append(int(linha['artist_popularity']))
                except ValueError:
                    dados['artist_popularity'].append(0) # Valor padrão em caso de erro
                
                try:
                    dados['artist_followers'].append(int(linha['artist_followers']))
                except ValueError:
                    dados['artist_followers'].append(0) # Valor padrão em caso de erro
                
                try:
                    dados['track_duration_min'].append(float(linha['track_duration_min']))
                except ValueError:
                    dados['track_duration_min'].append(0.0) # Valor padrão em caso de erro
                    
                contagem += 1
                    
        print(f"✅ Leitura concluída! {contagem} linhas processadas.\n")
        return dados
    except FileNotFoundError:
        print(f"❌ Erro: Arquivo não encontrado no caminho: {caminho_arquivo}")
        return {}

def main():
    caminho = 'src/data/spotify_data_clean.csv'
    
    # Carregar dados
    print("Carregando dados do Spotfy...\n")
    detaset_spotfy = carregar_dados_spotfy(caminho)
    
    if detaset_spotfy:
        try:        
            # Instanciar a Classe
            stats = Statistics(detaset_spotfy)
            
            # Gerar Relatório
            print("--- Análise Exploratória: ---\n")
            
            coluna_media = 'track_duration_min'
            if stats._is_numeric(coluna_media):
                print(f"Média de '{coluna_media}': {stats.mean(coluna_media):.2f}\n")
            else:
                print(f"A coluna {coluna_media} não é númerica\n")
                
            coluna_moda = 'artist_genres'
            print(f"Moda de '{coluna_moda}': {stats.mode(coluna_moda)}\n")
            
        except Exception as e:
            print(f"Erro na execução da Statistics: {e}")
            
            
if __name__ == "__main__":
    main()