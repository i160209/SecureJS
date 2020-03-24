#!/usr/bin/env python
# coding: utf-8

# In[39]:


from gensim.models import Word2Vec
VectorModel = Word2Vec.load("VectorizationModel.model")
import nltk
nltk.download('punkt')


def removeRedundant(row):
    stop_words=["(",'.','$',',',')','=','}','{','!',';','*','/**',"''",'"']
    
    if(type(row)!=None):
        for token in stop_words:
            row = [s.replace(token,'') for s in row]
    row = list(filter(None, row))

    return row


# In[42]:


def createEmbedding(inputcode):
    #Tokenize Code
    tokenizedcode = nltk.word_tokenize(inputcode)
    tokenizedcode = removeRedundant(tokenizedcode)
    embedding=[]
    for token in tokenizedcode:
        try:
            embedding.append(VectorModel[token])
        except:
            continue
        
    return embedding

