import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
from datetime import datetime

class PDFReport:
    def __init__(self, csv_path, output_pdf="rapor.pdf", grafik_path="grafik.png"):
        self.csv_path = csv_path
        self.output_pdf = output_pdf
        self.grafik_path = grafik_path

    def generate(self):
        df = pd.read_csv(self.csv_path)
        summary = df.groupby("Class")["Count"].sum()

        plt.figure(figsize=(8, 5))
        summary.plot(kind="bar", color="coral", edgecolor="black")
        plt.title("Araç Türüne Göre Toplam Sayı")
        plt.xlabel("Sınıf")
        plt.ylabel("Adet")
        plt.grid(axis='y', linestyle="--", alpha=0.7)
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.savefig(self.grafik_path)
        plt.close()

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=14)
        pdf.cell(200, 10, txt="Araç Tespiti Otomatik Rapor", ln=True, align='C')
        pdf.set_font("Arial", size=11)
        pdf.cell(200, 10, txt=f"Tarih: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
        pdf.ln(10)
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Toplam Tespitler:", ln=True)
        for cls, count in summary.items():
            pdf.cell(200, 10, txt=f"{cls}: {count} adet", ln=True)
        pdf.ln(5)
        pdf.image(self.grafik_path, x=30, w=150)
        pdf.output(self.output_pdf)
        print(f"📄 PDF raporu oluşturuldu: {self.output_pdf}")
