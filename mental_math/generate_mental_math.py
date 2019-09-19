"""This program was used to generate random math question for interview"""
import random
from docx import Document
from docx.shared import Pt


def generate_math_pdf(opt: str, num1_len: int , num2_len: int, path: str, font: int = 16):
    document = Document()
    obj_styles = document.styles['Normal']
    obj_font = obj_styles.font
    obj_font.size = Pt(font)
    obj_font.name = 'Times New Roman'
    for idx in range(115):
        line = []
        for operator in opt:
            num1 = random.randint(10 ** (num1_len - 1), 10 ** num1_len)
            num2 = random.randint(10 ** (num2_len - 1), 10 ** num2_len)
            line.append(f'{num1} {operator} {num2} = ')
        document.add_paragraph((' ' * 20).join(line))
    document.save(path)


def main():
    generate_math_pdf('+-*', 2, 2, 'docs/mental_math_2_digits.docx')
    generate_math_pdf('+-*', 3, 3, 'docs/mental_math_3_digits.docx')
    generate_math_pdf('+-*', 4, 4, 'docs/mental_math_4_digits.docx', font=14)


if __name__ == '__main__':
    main()