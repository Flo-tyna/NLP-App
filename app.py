"""
## App: NLP App with Streamlit (NLPiffy)
Author: [Florentyna Rodrigues](https://github.com/Flo-tyna))\n
Source: [Github](https://https://github.com/Text_Summarizer_App/)
Credits: (Brain Station DataScience and Streamlit Team)
Description
This is a Natural Language Processing App (NLP) Based App useful for basic Natural Language Processing Such as:
+ Tokenization & Lemmatization
+ Named Entity Recognition(NER) 
+Spell Check
+ Document/Text Summarization 

"""
import streamlit as st
from gensim.summarization import summarize
import spacy
import spacy_streamlit
from nltk.corpus import wordnet
from textblob import TextBlob
from pattern.web import Google
import streamlit.components.v1 as components
from pattern.en import pluralize , singularize,comparative, superlative
import codecs
nlp = spacy.load('en_core_web_sm')

#custom funtion 
def summary(text):
    return summarize(text)

# Custom Components Fxn
def st_calculator(calc_html,width=1000,height=1350):
	calc_file = codecs.open(calc_html,'r')
	page = calc_file.read()
	components.html(page,width=width,height=height,scrolling=False)

  

def main():
    activites = ["Summary","Named Entity Recognition","Search","Keywords"]
    choice = st.sidebar.selectbox("Select Activity",activites)
    if choice == "Summary":
        html_temp = """
	<div style="background-color:#16A085;"><p style="color:white;font-size:60px;">Text Summarizer</p></div>
	"""
        components.html(html_temp)
        text = st.text_area("Input Text For Summary",height=300)
        if st.button("summarize"):
            st.success(summary(text))
        text_range= st.sidebar.slider("Summarize words Range",25,500)
 
      

    # Named Entity Recognition 
    elif choice == "Named Entity Recognition":
        html_temp1 = """
	<div style="background-color:#16A085;"><p style="color:white;font-size:60px;">Text Tokenizer</p></div>
	"""
        components.html(html_temp1)
        row_data = st.text_area("write Text For Tokenizer")
        docx= nlp(row_data)
        if st.button("Tokenizer"):
            spacy_streamlit.visualize_tokens(docx,attrs=['text','pos_','dep_','ent_type_'])
        if st.button("NER"):
            spacy_streamlit.visualize_ner(docx,labels=nlp.get_pipe('ner').labels)
        if st.button("Text Relationship"):
            spacy_streamlit.visualize_parser(docx)
      
     
    #Search Bar
    elif choice == "Search":
        html_temp4 = """
	<div style="background-color:#16A085;"><p style="color:white;font-size:60px;,text-align:center;">Search Bar</p></div>
	""" 
        components.html(html_temp4)
        row_text= st.text_input("Search Anything")
        google = Google(license=None)
        if st.button("search"):
            for search_result in google.search(row_text):
                st.write(search_result.text)
                st.warning(search_result.url)
        
st.sidebar.subheader("BioMedical Natural Language Processing App")
st.sidebar.text("developed by ")
st.sidebar.text("Florentyna Rodrigues")
st.sidebar.text("BrainStation Data Science Candidate")
        
        

        
            
        
            
        
            
            
           
            
            
      
        
   

        
    
       
    
if __name__ == '__main__':
    main()