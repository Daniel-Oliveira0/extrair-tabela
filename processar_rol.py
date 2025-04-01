import pdfplumber

pdf_file = "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"

with pdfplumber.open(pdf_file) as pdf:
    for i, page in enumerate(pdf.pages):
        print(f"Verificando página {i+1}")
        tabela = page.extract_table()
        if tabela:
            print(f"Tabela encontrada na página {i+1}:")
            print(tabela[:5])  
        else:
            print(f"Nenhuma tabela encontrada na página {i+1}")