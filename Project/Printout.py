import os
from fpdf import FPDF
company="Devansh Pharmacy Co."
address="Jalandhar City, 144008"
contact="+91 89680 96689"
class my_cust_PDF(FPDF):
    def header(self):
        self.set_text_color(249, 113, 10)
        self.set_font('Helvetica', 'B', 20)
        w = self.get_string_width(company) + 6
        self.set_x((210 - w) / 2)
        self.cell(w, 9, company)
        self.ln(10) # line break

        self.set_font('Helvetica', 'B', 12)
        w = self.get_string_width(address) + 6
        self.set_x((210 - w) / 2)
        self.cell(w, 9, address)
        self.ln(10)

        w = self.get_string_width(contact) + 6
        self.set_x((210 - w) / 2)
        self.cell(w, 9, contact)
        self.ln(10)

        self.ln(20)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def chapter_content(self,data,headings,cols):
        self.set_fill_color(200, 220, 255)
        self.ln()
        self.ln()

        self.set_font('Arial', 'B', 11)
        spacing=1
        col_width = self.w /(cols+1)   # 9 = no of columns +1 to adjust columns to screen
        row_height = self.font_size+2

        #Table heading
        for i in headings:  # for headings
            self.cell(col_width, row_height * spacing, txt=i, border=1)
        self.ln(row_height * spacing)

        #table body
        self.set_font('Arial', '', 11)
        for row in data:
            for item in row:
                self.cell(col_width, row_height * spacing, txt=str(item), border=1)
            self.ln(row_height * spacing)
        # Line break
        self.ln()

        # Mention in italics
        self.ln()
        self.ln()
        self.ln()
        self.set_font('', 'I')
        text1 = '<------------------------------END----------------------------------->'
        w = self.get_string_width(text1) + 6
        self.set_x((210 - w) / 2)
        self.cell(0, 6, text1)

    def print_chapter(self,data,headings,cols):
        self.add_page()
        self.chapter_content(data,headings,cols)

if __name__ == '__main__':
    pdf = my_cust_PDF()
    data=[['Ref.No.', 'Medicine', 'Company', 'Type', 'Expiry Date', 'Price', 'Stock'],
          ['Ref.No.', 'Medicine', 'Company', 'Type', 'Expiry Date', 'Price', 'Stock'],
          ['Ref.No.', 'Medicine', 'Company', 'Type', 'Expiry Date', 'Price', 'Stock']]

    headings = ['Ref.No.', 'Medicine', 'Company', 'Type', 'Expiry Date', 'Price', 'Stock']
    pdf.print_chapter(data,headings,7)
    pdf.output('pdf_file1.pdf')
    os.system('explorer.exe "pdf_file1.pdf"')