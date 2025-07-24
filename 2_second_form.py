import os
from zipfile import ZipFile, ZIP_DEFLATED
from tkinter import filedialog

# # Usado para entrar em arquivos de forma intensa.
# with ZipFile('zip-file.zip', "r") as zip_folder:
#     file_names = zip_folder.namelist() # Retorna uma lista com o nome dos arquivos
#     print(file_names)

#     for file in file_names:
#         # csv = pandas.read_csv(file) # Não funciona, pois irá procurar um arquivo fora do zip
#         csv = pandas.read_csv(zip_folder.open(file))
#         print(csv)



# # para ESCREVER dentro de um zip:
# with ZipFile('zip-file.zip', "W") as zip_folder:
#     zip_folder.write("test_file1.txt")
#     zip_folder.write("test_file2.txt")




# # Para COMPACTAR uma pasta para zip:
# with ZipFile('img/svgs_files.zip', "w", compression=ZIP_DEFLATED) as zip_folder:
#     zip_folder.write('img/Python.svg') # se eu não passar o arcname, ele vai assumir o mesmo nome (incluindo as pastas)
#     zip_folder.write('img/Python.svg','cobrinha.svg')



# # Para EXTRAIR um zip:
# with ZipFile('zip-file.zip', "r") as zip_folder:
#     zip_folder.extract('test_file1.txt')  # Posso extrair apenas um arquivos, passando só o nome do arquivo.
#     zip_folder.extract('test_file1.txt', 'test')  # Posso extrair um arquivo, passando o nome do arquivo e a pasta caso eu queira.
#     zip_folder.extractall("temp") # posso colocar uma string para passar o caminho de onde vou extrair tudo
#     zip_folder.extractall()  


def compactar_cada_arquivo(diretorio, ignore_zips=True):
    
    nomes_arquivos: list[str] = os.listdir(diretorio)
    # nomes_arquivos = zip_folder.namelist()
    if ignore_zips:
        nomes_arquivos = [fn for fn in nomes_arquivos if not fn.endswith('.zip')]


    for nome in nomes_arquivos:
        fullpath = os.path.join(diretorio, nome)
        if os.path.isdir(fullpath):
            nome_zip = os.path.join(diretorio,nome+'.zip')
            with ZipFile(nome_zip, 'a',compression=ZIP_DEFLATED) as zip_folder:
                for raiz, dirs, files in os.walk(fullpath): # Percorre TODAS as coisas
                    for arq in files:
                        relativo = os.path.join(raiz, diretorio)
                        zip_folder.write(os.path.join(raiz,arq),os.path.join(relativo,arq))
        else:
            semextensao = nome.split('.')[0]
            nome_zip = os.path.join(diretorio,semextensao+'.zip')
            with ZipFile(nome_zip, 'w',compression=ZIP_DEFLATED) as zip_folder:
                zip_folder.write(os.path.join(diretorio,nome),nome)
    return len(nomes_arquivos)

def compactar_diretorio(diretorio):
    nome_zip = os.path.join(diretorio+'.zip')
    with ZipFile(nome_zip, 'w',compression=ZIP_DEFLATED) as zip_folder:
        nomes_arquivos = zip_folder.namelist()
        for arquivo in nomes_arquivos():
            zip_folder.write(os.path.join(diretorio,arquivo),arquivo)
    return len(nomes_arquivos)

if __name__ == '__main__':
    pasta = input('Digite o endereço da pasta que deseja compactar')
    # pasta = filedialog.askdirectory()
    print(f'compactando arquivos em {pasta}: ')
    # n = compactar_cada_arquivo(pasta)
    n = compactar_diretorio(pasta)
    print(f'{n} arquivos compactados com sucesso')






