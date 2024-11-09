import os

# Caminho da pasta onde deseja criar os arquivos (caminho completo)
caminho_pasta = r"C:\programming\curso-em-video\Curso-Python\anotações, aulas e exercicios\mundo 3\aula 21 - Funções (Parte 2)"

# Cria a pasta se ela não existir
os.makedirs(caminho_pasta, exist_ok=True)

# Intervalo de números para os arquivos (de 28 a 35)
for i in range(101, 106):
    nome_arquivo = f"Desafio{i:03}.py"  # Nome dos arquivos, ex: Desafio028.py
    caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)

    # Abre o arquivo em modo de escrita para criar o arquivo vazio
    with open(caminho_arquivo, 'w') as arquivo:
        arquivo.write(f"#")

    print(f"{nome_arquivo} criado com sucesso!")
