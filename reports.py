#!/usr/bin/env python3

# 4. generate pdf report using data from supplier-data/descriptions/

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(filename, title, table_data):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles["h1"])
    table_style = [('ALIGN', (0, 0), (-1, -1), 'LEFT')]
    report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
    empty_line = Spacer(1, 20)
    report.build([report_title, empty_line, report_table])
