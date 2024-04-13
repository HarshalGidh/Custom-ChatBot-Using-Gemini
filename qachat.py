# from dotenv import load_dotenv
# # Loading all the dotenv variables
# load_dotenv()

# import streamlit as st
# import os
# import google.generativeai as genai

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Load Gemini Model
# model = genai.GenerativeModel("gemini-pro")
# chat = model.start_chat(history=[])

# def get_gemini_response(question):
#     response = chat.send_message(question,stream = True)
#     return response

# ##initialize our streamlit app

# st.set_page_config(page_title="Q&A ")

# st.header("Conversational Question and Answer")

# # if chat history doesn't exist create a list
# if 'chat_history' not in st.session_state :
#     st.session_state['chat_history'] = []

# input = st.text_input("Input:",key = "input")
# submit = st.button("Ask a Question ")

# if input and submit :
#     response = get_gemini_response(input)
#     # Add user query and response to chat history
#     st.session_state['chat_history'].append(("You",input))
#     st.subheader("The Response is ")
#     st.write(response)
#     for chunk in response:
#         st.write(chunk.text)
#         st.session_state['chat_history'].append(("Bot",chunk.text))
        
# st.subheader("The Chat History is ")

# for role,text in st.session_state['chat_history']:
#     st.write(f"{role}: {text}")


from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini Pro model and get repsonses
model=genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])
def get_gemini_response(question):
    
    response=chat.send_message(question,stream=True)
    return response

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Question and Answer ChatBot")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input=st.text_input("Input: ",key="input")
submit=st.button("Ask a question")

if submit and input:
    response=get_gemini_response(input)
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))
st.subheader("The Chat History is")
    
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
