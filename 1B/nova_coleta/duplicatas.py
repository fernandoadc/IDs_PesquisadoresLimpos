import csv

def remover_registros_duplicados(arquivo_entrada, arquivo_saida):
    ids_unicos = set()  # Cria um conjunto para armazenar os IDs únicos
    linhas_unicas = []  # Lista para armazenar as linhas únicas

    with open(arquivo_entrada, 'r') as entrada, open(arquivo_saida, 'w', newline='') as saida:
        leitor_csv = csv.reader(entrada)
        escritor_csv = csv.writer(saida)

        for linha in leitor_csv:
            id_usuario = linha[0]  # Supondo que o ID do usuário está na primeira coluna

            if id_usuario not in ids_unicos:
                ids_unicos.add(id_usuario)
                linhas_unicas.append(linha)

        escritor_csv.writerows(linhas_unicas)

    print(f"Registros duplicados removidos. Resultado salvo em '{arquivo_saida}'.")

# Exemplo de uso
arquivo_entrada = '1B.csv'
arquivo_saida = 'dados_sem_duplicatas_1B_novo.csv'

remover_registros_duplicados(arquivo_entrada, arquivo_saida)
