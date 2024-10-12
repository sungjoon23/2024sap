import smtplib
import streamlit as st
import pandas as pd
from email.mime.text import MIMEText

# 앱 제목
st.title("농업인의 안전관리 지침")

# 서브 타이틀
st.subheader("안전한 농작업을 위한 기본 지침")

# 농업 작업 중 발생할 수 있는 위험 요소를 설명
st.write("""
농업 작업 중 발생할 수 있는 주요 위험 요소는 다음과 같습니다:
1. 기계와 도구의 부적절한 사용
2. 무거운 물건을 들 때 발생하는 근골격계 손상
3. 농약 및 화학물질 노출
4. 기상 조건에 따른 열사병 및 탈진
5. 미끄러짐 및 넘어짐
""")

# 예방 방법을 안내하는 표 생성
data = {
    "위험 요소": ["기계와 도구 사용", "무거운 물건 들기", "농약 노출", "열사병 및 탈진", "미끄러짐/넘어짐"],
    "예방 방법": [
        "안전 장비 착용 및 사용법 숙지",
        "올바른 자세로 물건 들기 및 보조 장비 사용",
        "보호 장비 착용 및 안전한 농약 사용법 교육",
        "충분한 수분 섭취 및 작업 중 휴식",
        "작업장 정리정돈 및 미끄럼 방지 신발 착용"
    ]
}
df = pd.DataFrame(data)

# 테이블 표시
st.table(df)

# PDF 파일 읽기
pdf_path = "C:/code/pythonProject3/hw5/2023 농작업 안전재해 주요통계.pdf"
with open(pdf_path, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

pdf_path = "C:\code\pythonProject3\hw5\(2023) 농업인 안전 기본교육자료_농작업 안전재해 예방.pdf"
with open(pdf_path, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# PDF 다운로드 버튼 추가
st.download_button(label="2023 농작업 안전재해 주요통계 PDF 다운로드",
                   data=PDFbyte,
                   file_name="2023_농작업_안전재해_주요통계.pdf",
                   mime="application/pdf")

# PDF 다운로드 버튼 추가
st.download_button(label="(2023) 농업인 안전 기본교육자료_농작업 안전재해 예방 PDF 다운로드",
                   data=PDFbyte,
                   file_name="2023_농작업_안전 기본교육자료_농작업 안전재해 예방.pdf",
                   mime="application/pdf")

