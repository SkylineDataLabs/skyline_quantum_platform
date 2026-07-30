from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime


def create_pdf_report(domain, risk_score, findings, tls_results):
    filename = f"{domain.replace('.', '_')}_quantum_report.pdf"

    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    y = height - 50

    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, y, "Skyline Data Labs")
    y -= 25

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Post-Quantum Cryptography Readiness Report")
    y -= 35

    c.setFont("Helvetica", 10)
    c.drawString(50, y, f"Domain: {domain}")
    y -= 18
    c.drawString(50, y, f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    y -= 18
    c.drawString(50, y, f"Quantum Risk Score: {risk_score}/100")
    y -= 35

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Findings")
    y -= 20

    c.setFont("Helvetica", 10)
    for finding in findings:
        c.drawString(60, y, f"- {finding}")
        y -= 15

    y -= 20

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "TLS Metadata")
    y -= 20

    c.setFont("Helvetica", 10)
    c.drawString(60, y, f"TLS Version: {tls_results.get('tls_version')}")
    y -= 15
    c.drawString(60, y, f"Cipher: {tls_results.get('cipher')}")
    y -= 15
    c.drawString(60, y, f"Key Bits: {tls_results.get('key_bits')}")
    y -= 25

    c.setFont("Helvetica-Oblique", 8)
    c.drawString(
        50,
        50,
        "This report is based on public TLS metadata only and is not a penetration test."
    )

    c.save()

    return filename