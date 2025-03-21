# -*- coding: utf-8 -*-
"""Resume Analyzer for keywords and skills.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fvV29fbcTCRApVwYcFWWDtfN7FOCyMq8
"""

pip install pypdf2

import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

import re
import PyPDF2

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import string

keywords = ["python","data analysis","machine learning","deep learning","artificial intelligence","nlp","tensorflow","keras","data visualization","data science","sql","r"]


stop_words = set(stopwords.words("english"))



"""bold text# New Section"""

def pdf(file_path):
  text = ""
  with open(file_path,"rb") as file:
    pdf_reader=PyPDF2.PdfReader(file)

    for page in pdf_reader.pages:
      page_text = page.extract_text()
      if page_text:
        text += page_text

  return text

def token(text):
  text = text.lower()
  text = text.translate(str.maketrans("","",string.punctuation))

  tokens = word_tokenize(text)


  filter = [token for token in tokens if token not in stop_words]
  print(filter)

  return filter

def match_keywords(tokens,keywords):
  matched_keywords = [word for word in tokens if word in keywords]

  return matched_keywords

def analyse_resume(file_path):
  if file_path.endswith(".pdf"):
    text = pdf(file_path)

  else :
    return "UNSUPPORTED FORMAT"

  tokens = token(text)

  matched_keys = match_keywords(tokens,keywords)

  match_score = len(matched_keys)

  print("Matched_keywords : ",matched_keys)
  print("Matched Score : ",match_score)
  print(f"Skills Found : , {match_score} /len {keywords}")

file_path = "/content/resume.pdf"
analyse_resume(file_path)