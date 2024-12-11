from django.shortcuts import render
import os
import tempfile
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader


# Chave da API
api_key = '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'
os.environ['GROQ_API_KEY'] = api_key
chat = ChatGroq(model='llama3-groq-70b-8192-tool-use-preview') # modelo do LLama que está sendo usando

def index(request):
    return render(request, 'base.html')

def dashboard(request):
    return render(request, 'temp/dashboard.html')

def atos_oficiais(request):
    return render(request, 'temp/atos_oficiais.html')

def ia_atos_oficiais(request):
    caminho = 'https://it-solucoes.inf.br/admnews/CM_GARANHUNS/202412040954.pdf'
    loader = PyPDFLoader(caminho)
    lista_documentos = loader.load()
    documentos = ''
    for doc in lista_documentos:
        documentos = documentos + doc.page_content

    return render(request, 'temp/atos_oficiais.html', {'documentos': documentos})

# def ia_atos_oficiais(request):
#     pdf = ''
#     if request.method == 'POST':
#         confirmacao = ''
#         ato_oficial = request.FILES.get('pdf_ia_analisa')
#         if ato_oficial:
#             for chunk in ato_oficial.chunks(): 
#                 pdf = pdf + chunk
                
#             pdf_ia = PyPDFLoader(pdf)
#             pdf_ia_analisado = pdf_ia.load()
#             for ato in pdf_ia_analisado:
#                 confirmacao = confirmacao + ato.page_content    
#     return render(request, 'temp/atos_oficiais.html', {'confirmacao': confirmacao})
            
    