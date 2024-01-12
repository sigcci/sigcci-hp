# -*- coding: utf-8 -*-

import io
from glob import glob
from decimal import Decimal
from PyPDF2 import PdfWriter
from PyPDF2 import PdfReader
from reportlab.lib.colors import Color
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

pdfmetrics.registerFont(
    TTFont(
        'Yu Mincho Regular',
        '/mnt/c/Windows/Fonts/yumin.ttf'
    )
)

prefix = "SIG-CCI-011-"

for filename in glob("[0-9][0-9].pdf"):
    print(filename)
    out_filename = prefix + filename
    id = out_filename[:len(out_filename)-4]
    pdf = PdfReader(filename)
    page = pdf.pages[0]
    
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=A4)
    
    font_size = 8
    can.setFont('Yu Mincho Regular', font_size)
    can.setFillColor(Color(0, 0, 0, alpha=1))
    can.drawString(426, 812, "人工知能学会第二種研究会資料")
    can.drawString(474, 803, "市民共創知研究会")
    can.drawString(478, 794, id)

    can.drawString(57, 812, "電子情報通信学会")
    can.drawString(57, 803, "合意と共創研究会 研究報告")

    can.save()
    
    packet.seek(0)
    new_pdf = PdfReader(packet)
    page.merge_page(new_pdf.pages[0])
    

    output = PdfWriter()
    output.add_page(page)
    for i in range(1, len(pdf.pages)):
        output.add_page(pdf.pages[i])
        
    with open(out_filename, "wb") as fout:
        output.write(fout)
        print(out_filename)
        
