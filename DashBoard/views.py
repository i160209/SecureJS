#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from random import *

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .models import *
import numpy as np
from gensim.models import Word2Vec,KeyedVectors
import nltk
from gensim.test.utils import datapath
wv_from_bin = KeyedVectors.load_word2vec_format("model.bin", binary=True)
import pickle
filename = './DashBoard/securejsModel.sav'
loaded_model = pickle.load(open(filename, 'rb'))

scanlist = []
sourcecode = []

def predict(X):
    result = loaded_model.predict(X[0].reshape(1,-1))
    return result[0]

def sumVec(X):
    temp = X
    for j in range(1,np.shape(X)[0]-1):
        temp = np.add(temp, X[j])
    X = temp
    return X

# Create your views here.

def DashBoard(request):
    if request.method == 'GET':
        return render(request,'dBoard/index.html')


def handle_uploaded_file(f):  
    with open('DashBoard/static/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)


def DetectVulnerability_File(request):
    if request.method == 'GET':
        return render(request,'DetectVulnerability/File/index.html')

    my_uploaded_file = request.FILES['file'].read()
    #print (type(request.FILES['file']))
    #file = open(request.FILES['file'])

    #line = file.read().replace("\n", " ")
    #file.close()
    #print (line)
    #print (type(line))
    str_file = str(my_uploaded_file, 'utf-8')
    answer=predict(sumVec(list(createEmbedding(str_file))))
    scanlist.append(answer)
    sourcecode.append(str_file)
    print (scanlist)
    print (str_file)
    
    #print ('-------------------------------777----------------------------------', answer)
    context = {
        'code': answer,
    }
    return render(request,'DetectVulnerability/Code/invoice.html', context)

    #print(type(my_uploaded_file))
    #print (str(my_uploaded_file, 'utf-8'))
    #answer=predict(sumVec(createEmbedding(my_uploaded_file)))
    #print ('-----------------------------------------------------------------',answer)
    #return render(request,'DetectVulnerability/File/invoice.html')



def DetectVulnerability_Library(request):
    if request.method == 'GET':
        obj = VulnerableLibraries.objects.all()
        print ("111111111111111111111111111",obj[1].Vulnerability)
        context = {
            'object': obj,
        }
        return render(request,'DetectVulnerability/Libraries/index.html', context)


def XSS(request):
    if request.method == 'GET':
        return render(request,'Vulnerabilities/XSS/index.html')

def Injection(request):
    if request.method == 'GET':
        return render(request,'Vulnerabilities/Injection/index.html')

def BAC(request):
    if request.method == 'GET':
        return render(request,'Vulnerabilities/BrokenAccessControl/index.html')

def BA(request):
    if request.method == 'GET':
        return render(request,'Vulnerabilities/BrokenAuthentication/index.html')

def Scan(request):
    if request.method == 'GET':
        context = {
            'object': scanlist,
            'code': sourcecode,
        }
        return render(request,'Scans/index.html', context)


def removeRedundant(row):
    stop_words=["(",'.','$',',',')','=','}','{','!',';','*','/**',"''",'"']
    
    if(type(row)!=None):
        for token in stop_words:
            row = [s.replace(token,'') for s in row]
    row = list(filter(None, row))

    return row



def createEmbedding(inputcode):
    #Tokenize Code
    tokenizedcode = nltk.word_tokenize(inputcode)
    tokenizedcode = removeRedundant(tokenizedcode)
    embedding=[]
    for token in tokenizedcode:
        try:
            embedding.append(wv_from_bin[token])
        except:
            continue
        
    return embedding







def DetectVulnerability_Code(request):
    if request.method == 'GET':
        return render(request,'DetectVulnerability/Code/index.html')

    code = request.POST.getlist('SourceCode')
    #print ('-----------------------------------------------------------------', code[0])
    
    
    answer=predict(sumVec(list(createEmbedding(code[0]))))
    scanlist.append(answer)
    sourcecode.append(code[0])
    print (scanlist)
    
    print ('-------------------------------777----------------------------------', answer)
    context = {
        'code': answer,
    }
    return render(request,'DetectVulnerability/Code/invoice.html', context)
# In[ ]:




