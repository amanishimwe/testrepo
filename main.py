import os
import warnings
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText
import pywhatkit
import spacy
from Spacy_custom import customize_spacy
import wikipedia
from functools import lru_cache
from functools import cache
import tensorflow as tf
from openfabric_pysdk.context import OpenfabricExecutionRay
from openfabric_pysdk.loader import ConfigClass
from time import time


############################################################
# Callback function called on update config
############################################################
def config(configuration: ConfigClass):
    # TODO Add code here
    pass


############################################################
# Callback function called on each execution pass
############################################################
@lru_cache() # we want to cache the loaded custom Spacy
def get_label(text): # lets be sure rthe question is scientific
    status = None
    #@lru_cache()
    nlp = customize_spacy()
    y = nlp(tex)

    for x in y.ents:
        
        if x.label == 12096978277017718205:
            status = True
        else:
            pass
    return status # we return the type of the question whether or not its science

def answer_science(qtn): # lets give an answer to a science question
    response = None
    try:
        ans = wikipedia.summary()
    except wikipedia.HTTPTimeoutError: # incase our internet fails
        pass
    except wikipedia.PageError:
        response = 'Sorry, I havent learn about that' # if wikipedia can not find the response
        
    
    
    
    
def execute(request: SimpleText, ray: OpenfabricExecutionRay):
    output = []
    for text in request.text:
        # we determine if the text is a science word  
        stat = get_label(text) # we use the customly trained spacy to determine science label
        # we trained a custom spacy to recognize science words
        if stat == True: # if the labell was science, we go ahead
            response = answer_science(text) # we then find answers from wikipedia and give the reply
            
        # TODO Add code here
        
        output.append(response)

    return SimpleText(dict(text=output))
