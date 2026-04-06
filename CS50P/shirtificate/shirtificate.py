from fpdf import FPDF

name = input("Name: ")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("helvetica", style="B", size=30)
pdf.cell(0, 30, text="CS50 Shirtificate", align='C')
pdf.ln(20)
pdf.image("./shirtificate.png", x="C", y=60, w=170)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 200, text=name, new_x="LMARGIN", new_y="NEXT",  align='C')
pdf.output("shirtificate.pdf")
