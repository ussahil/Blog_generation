import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## Function to get response from LLama 2
def getLamaresponse(input_text,no_words,blog_style):
  
  llm = CTransformers(model='model/llama-2-7b-chat.ggmlv3.q8_0.bin',model_type='llama',config={'max_new_tokens':256,'temperature':0.01})
  
  ### Prompote Template
  
  template ='''
  Write a blog for {blog_style} job profile for a topic {input_text} within {no_words} words.
  '''
  
  prompt = PromptTemplate(input_variables=['blog_style','input_text','no_words'],template=template)
  
  ### Generate the response 
  response = llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words =no_words))
  print(response)
  return response

st.set_page_config(page_title='Generate Blogs',page_icon= '-_-',layout='centered',initial_sidebar_state='collapsed')

st.header('Generate Blogs -_-')

input_text = st.text_input('Enter the Blog Topic')

# Creating 2 cols for additional info

col1,col2 =st.columns([5,5])

with col1:
  no_words = st.text_input('No of words')

with col2:
  blog_style = st.selectbox('Writing the blog for',('Reseachers','Data Analyst','Common people'),index=0)

submit = st.button('Generate')

### Final Response

if submit:
  # Function
  st.write(getLamaresponse(blog_style,input_text,no_words))