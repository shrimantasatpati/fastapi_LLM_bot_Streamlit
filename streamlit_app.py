import streamlit as st
import requests

# Set the title of the app
st.title("RAG With Haystack Mistral & Pinecone")

# Input for the question
question = st.text_area("Write Your Query", height=100)

# Submit button
if st.button("Submit"):
    if question.strip() == "":
        st.error("Please enter your query!")
    else:
        # Send the question to the FastAPI backend
        response = requests.post("http://localhost:8001/get_answer", data={"question": question})
        
        if response.status_code == 200:
            answer = response.json().get("answer", "No answer found.")
            st.text_area("Answer", value=answer, height=100)
        else:
            st.error("Error: Unable to get a response from the server.")