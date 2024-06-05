import os
import zipfile

def descompactar_arquivos_zip(diretorio_zip, diretorio_destino):
    # Cria o diretório de destino se ele não existir
    if not os.path.exists(diretorio_destino):
        os.makedirs(diretorio_destino)

    # Itera sobre todos os arquivos no diretório fornecido
    for arquivo in os.listdir(diretorio_zip):
        caminho_completo_arquivo = os.path.join(diretorio_zip, arquivo)
        
        # Verifica se o arquivo é um zip
        if zipfile.is_zipfile(caminho_completo_arquivo):
            with zipfile.ZipFile(caminho_completo_arquivo, 'r') as zip_ref:
                # Extrai todos os arquivos para o diretório de destino
                zip_ref.extractall(diretorio_destino)
                print(f"Arquivo {arquivo} descompactado com sucesso.")
        else:
            print(f"Arquivo {arquivo} não é um arquivo zip válido.")

if __name__ == "__main__":
    diretorio_zip = input("Digite o caminho da pasta contendo os arquivos zip: ")
    diretorio_destino = os.path.join(diretorio_zip, "Descompactados")
    descompactar_arquivos_zip(diretorio_zip, diretorio_destino)
    print("Todos os arquivos zip foram descompactados na pasta 'Descompactados'.")
