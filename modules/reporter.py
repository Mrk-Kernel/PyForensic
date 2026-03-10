from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime

def generate_report(data, output_path="reports/forensic_report.pdf"):
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter
    y = height - 50

    c.setFont("Helvetica-Bold", 18)
    c.drawString(200, y, "PyForensic - Forensic Report")
    y -= 30

    c.setFont("Helvetica", 10)
    c.drawString(50, y, f"Generated: {datetime.datetime.now()}")
    y -= 30

    c.line(50, y, 550, y)
    y -= 20

    for section, content in data.items():
        c.setFont("Helvetica-Bold", 13)
        c.drawString(50, y, f"[ {section} ]")
        y -= 20

        c.setFont("Helvetica", 10)
        if isinstance(content, dict):
            for key, value in content.items():
                text = f"  {key}: {value}"
                c.drawString(50, y, text[:90])
                y -= 15
                if y < 60:
                    c.showPage()
                    y = height - 50
        y -= 10

    c.save()
    print(f"\n✅ Report saved to: {output_path}")
