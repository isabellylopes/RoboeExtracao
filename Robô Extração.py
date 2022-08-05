
""" 
Robô que descompacta arquivos de um diretório e joga em outro já descompactado.

            Criado por: Isabelly Cristine Lopes

            Você pode me encontrar em: 

            Linkedin ->  https://www.linkedin.com/in/isabelly-cristine-lopes-8a9b59204/
            Instagram -> @isabellyloppess
"""

from zipfile import ZipFile
import os


diretorio = r'****' # Pasta Fonte
destino = r'****'   # Pasta de Destino

try:
    with os.scandir(diretorio) as elemento: # Escanea o diretório
        for pasta in elemento:
            if not pasta.name.startswith('.') and not pasta.name.startswith('~') and pasta.name.endswith(
                    '.ZIP') or pasta.name.endswith('.zip') and pasta.is_file(): # Faz o tratamento nos arquivos
                print(pasta.name)
                pasta_zipada_tratada = diretorio + '/' + pasta.name # Cria nome para os arquivos
                with ZipFile(pasta_zipada_tratada, 'r') as ZipObj:
                    for zip in ZipObj.namelist():
                        ZipObj.extract(zip, destino) # Joga os arquivos descompactados na pasta destino
except:
    print('erro')





