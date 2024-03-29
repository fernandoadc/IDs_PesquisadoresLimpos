import csv
import os

diretorio = 'C:\\Users\\tinho\\IDs_PesquisadoresLimpos\\1A\\nova_coleta'
arquivo_saida = os.path.join(diretorio, "1A.csv")

arquivos_csv = []

for arquivo in os.listdir(diretorio):
    if arquivo.endswith(".csv"):
        arquivos_csv.append(arquivo)

arquivos_csv.sort()  # Ordenar a lista de arquivos CSV

with open(arquivo_saida, 'w', newline='') as arquivo_final:
    writer = csv.writer(arquivo_final)

    for arquivo_csv in arquivos_csv:
        with open(os.path.join(diretorio, arquivo_csv), 'r') as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                writer.writerow(linha[1:])  # Passar sem a coluna de IDs

# Fechar o arquivo de saída após o loop de escrita
arquivo_final.close()