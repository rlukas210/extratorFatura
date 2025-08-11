import sys
import fitz

class ExtratorPdf:
    """
    Class responsible for extracting information from PDF files.
    """

    def __init__(self):
        pass

    def extrair_texto_pdf(self, arquivo_pdf, senha):
        try:
            doc = fitz.open(arquivo_pdf)
            
            if doc.needs_pass:
                if not doc.authenticate(senha):
                    raise ValueError("❌Senha incorreta.")
            
            linhas = []
            for num_pagina, pagina in enumerate(doc, start=1):
                texto = pagina.get_text()
                linhas_pagina = texto.split('\n')
                linhas.extend([linha.strip() for linha in linhas_pagina])

                #print(f"\n--- Page {num_pagina} ---")
                ind = 0
                for linha in linhas:
                    print(f"[{ind}] {linha.strip()}")
                    #print(linha.strip())
                    ind += 1

            doc.close()
            return linhas
        except Exception as e:
            print(f"Erro ao processar o PDF: {e}")
            return None
        



       # args = sys.argv
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python extrair_pdf.py arquivo.pdf senha(opcional)")
    else:
        caminho_pdf = sys.argv[1]
        senha_pdf = sys.argv[2] if len(sys.argv) > 2 else ""
        extrator = ExtratorPdf()
        extrator.extrair_texto_pdf(caminho_pdf, senha_pdf)
        print("Texto extraído com sucesso.")