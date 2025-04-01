import pdfplumber
import csv
import zipfile
import os

pdf_file = "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
csv_file = "dados_extraidos.csv"
zip_file = "Teste_Daniel.zip"

dados_tabelas = []

with pdfplumber.open(pdf_file) as pdf:
    for i, page in enumerate(pdf.pages):
        print(f"Verificando página {i+1}")
        tabela = page.extract_table()
        if tabela:
            print(f"Tabela encontrada na página {i+1}")
            dados_tabelas.extend(tabela)

if dados_tabelas:
    with open(csv_file, mode="w", newline="", encoding="utf-8") as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerows(dados_tabelas)

    print(f"Dados salvos em {csv_file}")

    with zipfile.ZipFile(zip_file, "w", zipfile.ZIP_DEFLATED) as arquivo_zip:
        arquivo_zip.write(csv_file)
    
    print(f"Arquivo compactado salvo como {zip_file}")

    os.remove(csv_file)
else:
    print("Nenhuma tabela foi encontrada no PDF.")