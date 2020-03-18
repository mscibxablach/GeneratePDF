from __future__ import unicode_literals
from fpdf import FPDF
import datetime
from fontTools.ttLib import TTFont
#python -m pip install fpdf
#pip install fpdf
#pip install unicode-string-literal
#pip install fonttools
#pip install --user fonttools


class CustomPDF(FPDF):

    def header(self):
        # Set up a logo
        d = datetime.date.today()
        d_string = d.__str__()

        self.set_font('Times', 'B', 20)

        # Add an address
        self.cell(0, 0, 'Wyniki badania ultrasonograficznego', ln=1, align='L')

        self.set_font('Times', 'B', 13)
        self.cell(0, 0, d_string, ln=1, align='R')

        # self.set_draw_color(176, 224, 230)
        # self.set_draw_color(65, 105, 225)
        self.set_draw_color(217,217,245)


        self.set_line_width(1)
        self.line(10, 30, 150, 30)


        # Line break
        self.ln(20)

    def footer(self):
        self.set_y(-10)

        self.set_font('Times', 'I', 8)

        self.set_draw_color(230, 230, 250)
        self.line(10, 285, 200, 285)


        # Add a page number
        page = 'Strona ' + str(self.page_no()) + '/{nb}'
        self.cell(0, 10, page, 0, 0, 'C')


def form(self, name, surname, pesel, birth_date, phone, email):
    self.set_font("Times", size=12)
    self.cell(0, 10, txt="Imie: " + " " + name, ln=1)
    self.cell(0, 10, txt="Nazwisko:" + " " + surname, ln=1)
    self.cell(0, 10, txt="Pesel:" + " " + pesel, ln=1)
    self.cell(0, 10, txt="Data urodzenia:" + " " + birth_date, ln=1)
    self.cell(0, 10, txt="Numer telefonu:" + " " + phone, ln=1)
    self.cell(0, 10, txt="E-mail:" + " " + email, ln=1)
    self.ln(10)


def description_of_examination(self, vein, description):
    self.set_font("Times", 'B', size=12)
    self.cell(0, 10, txt="Rozpoznanie:", ln=1)
    self.set_font("Times", size=12)
    self.multi_cell(w=0, h=10, txt=vein, border=1, align='J')
    self.set_font("Times", 'B', size=12)
    self.cell(0, 10, txt="Opis badania:", ln=1)
    self.set_font("Times", size=12)
    self.multi_cell(w=0, h=10, txt=description, border=1, align='J')
    self.ln(5)


def create_pdf(pdf_path):
    pdf = CustomPDF()
    pdf.set_margins(left=12, top=20)

    # Create the special value {nb}
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Times', '', 12)

    form(pdf, "Agata", "Blachowiak", "96070642841", "06.07.1996", "536728321", "agata.blachowiak@gmail.com")
    pdf.image("/Users/agatablachowiak/Desktop/GeneratePDF/veins.jpg", x=130, y=35, w=60, h=75)
    description_of_examination(pdf, "Zyla odpiszczelowa prawa", "This method allows printing text with line breaks. They can be automatic (as soon as the text reaches the right border of the cell) or explicitutputned,k can be framed and the background painted." )
    pdf.image("/Users/agatablachowiak/Desktop/GeneratePDF/USG.jpg", w=120, h=55)


    pdf.output(pdf_path)


if __name__ == '__main__':
    create_pdf('Badanie.pdf')