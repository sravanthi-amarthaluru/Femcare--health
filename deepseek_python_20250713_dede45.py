from fpdf import FPDF
from datetime import datetime

class PCOSReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'FemCare Health Report', 0, 1, 'C')
        self.ln(10)
    
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def generate_report(user_data, risk_data):
    pdf = PCOSReport()
    pdf.add_page()
    
    # Add content
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, f"Patient: {user_data['name']}", 0, 1)
    pdf.cell(0, 10, f"Age: {user_data['age']}", 0, 1)
    pdf.ln(5)
    
    # Risk summary
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'PCOS Risk Assessment:', 0, 1)
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, 
        f"Risk Level: {risk_data['predicted_class']}\n"
        f"Confidence: {max(risk_data.values()):.1%}")
    
    # Save file
    filename = f"reports/{user_data['id']}_{datetime.now().strftime('%Y%m%d')}.pdf"
    pdf.output(filename)
    return filename