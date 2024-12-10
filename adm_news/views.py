from django.shortcuts import render
from django.conf import settings
import os
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
    confirmacao = ''
    if request.method == 'POST':
        ato_oficial = request.FILES.get('pdf_ia_analisa')
        
        temp_path = os.path.join(settings.MEDIA_ROOT, ato_oficial.name)
        with open(temp_path, 'wb+') as temp_file:
            for chunck in ato_oficial.chuncks():
                temp_file.write(chunck)
        
        try:
            ato_oficial = PyPDFLoader(temp_file)
            ato_oficial_analisado = ato_oficial.load()
            for ato in ato_oficial_analisado:
                confirmacao = confirmacao + ato.page_content
        except Exception as e:
            confirmacao = f"Erro ao processar o PDF: {str(e)}"
        finally: # Remover o arquivo temporário
            if os.path.exists(temp_path):
                os.remove(temp_path)
           
    return render(request, 'temp/atos_oficiais.html', {'confirmacao': confirmacao})
            
    