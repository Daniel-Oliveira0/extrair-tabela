import pdfplumber
import csv
import zipfile
import os

pdf_file = "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
csv_file = "dados_extraidos.csv"
zip_file = "Teste_Daniel.zip"

substituicoes = {
    "OD": "Outros Procedimentos",
    "AMB": "Ambulatório"
}

dados_tabelas = []

try:
    with pdfplumber.open(pdf_file) as pdf:
        for i, page in enumerate(pdf.pages):
            tabela = page.extract_table()

            if tabela:
                print(f"Tabela encontrada na página {i+1}")

                tabela_formatada = [
                    [substituicoes.get(celula.strip() or "", celula.strip()) for celula in linha]
                    for linha in tabela
                ]

                dados_tabelas.extend(tabela_formatada)

    if dados_tabelas:
        with open(csv_file, mode="w", newline="", encoding="utf-8") as arquivo_csv:
            escritor = csv.writer(arquivo_csv, delimiter=";")
            escritor.writerows(dados_tabelas)

        print(f"Dados salvos em {csv_file}")

        with zipfile.ZipFile(zip_file, "w", zipfile.ZIP_DEFLATED) as arquivo_zip:
            arquivo_zip.write(csv_file)

        print(f"Arquivo compactado salvo como {zip_file}")

        os.remove(csv_file)
    else:
        print("Nenhuma tabela foi encontrada no PDF.")

except FileNotFoundError:
    print(f"Erro: O arquivo {pdf_file} não foi encontrado.")
except Exception as e:
    print(f"Erro inesperado: {e}")