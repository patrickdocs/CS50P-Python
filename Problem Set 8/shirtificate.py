from fpdf import FPDF

class Shirtificate:
    def __init__(self, name: str):
        self.name = name
        self.pdf = FPDF(orientation='P', unit='mm', format='A4')

    def create_pdf(self):
        # Add a page
        self.pdf.add_page()

        # Set title font
        self.pdf.set_font("Helvetica", size=32, style='B')
        self.pdf.cell(0, 20, "CS50 Shirtificate", ln=True, align="C")

        # Add the shirt image
        self.pdf.image("shirtificate.png", x=50, y=60, w=110)

        # Print the user's name in white on top of the shirt
        self.pdf.set_text_color(255, 255, 255)  # White color
        self.pdf.set_font("Helvetica", size=24)
        self.pdf.text(x=65, y=140, txt=f"{self.name} took CS50!")

        # Output the PDF
        self.pdf.output("shirtificate.pdf")

def main():
    name = input("What's your name? ")
    shirtificate = Shirtificate(name)
    shirtificate.create_pdf()

if __name__ == "__main__":
    main()
