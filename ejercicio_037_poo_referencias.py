class Factura:
    def __init__(self, numero, cif, importe):
        self.numero = numero
        self.cif = cif
        self.importe = importe
        self.pdf_generado = False

class PDFGenerator:
    def __init__(self, factura : Factura):
        self.factura = factura

    def generate_pdf(self, file_name : str):
        print(f'Generando el pdf de la factura {self.factura.numero}')
        self.factura.pdf_generado = True

f_100 = Factura(100,'B1838438A',2_500)
print(f_100.pdf_generado) # False
pdf_generator = PDFGenerator(f_100)
pdf_generator.generate_pdf('factura.pdf')
print(f_100.pdf_generado) # True, porque se asigna por referencia