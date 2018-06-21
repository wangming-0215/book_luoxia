
import reportlab.pdfbase.ttfonts
import copy

from reportlab.platypus import Paragraph, SimpleDocTemplate, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
import re


reportlab.pdfbase.pdfmetrics.registerFont(reportlab.pdfbase.ttfonts.TTFont(
    'song', r'C:\Windows\Fonts\simhei.TTF'))


def create_pdf(input, output="disk.pdf"):
    stylesheet = getSampleStyleSheet()
    normalStyle = copy.deepcopy(stylesheet['Normal'])
    normalStyle.fontName = 'song'
    normalStyle.fontSize = 16
    normalStyle.leading = 20
    story = []
    for paragraph in re.split(r'\n', input):
        p = Paragraph(paragraph, normalStyle)
        story.append(p)
    pdf = SimpleDocTemplate(output)
    pdf.build(story)
