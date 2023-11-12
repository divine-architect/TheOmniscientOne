import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
import openai
from llama_index import SimpleDirectoryReader
from io import StringIO
from PyPDF2 import PdfReader
from pathlib import Path
import easyocr
import re
from youtube_transcript_api import YouTubeTranscriptApi
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="The Omniscient One", page_icon="👁️", layout="centered", initial_sidebar_state="auto", menu_items=None)
openai.api_key = os.getenv("token")
st.title("👁️ The Omniscient One 👁️")
st.caption("The Omniscient One (or 2 for short) is a web-app that utilizes the power of Open AI's GPT model and Llama Index's ability to train custom datasets to summarize any kind of text based file format [We're also working on OCR and NLP on output based on OCR]")

st.header("What can 2 do?")
st.caption("TOO (2) can currently interpret .docx, .pdf, .html, .txt, .png/.jpg images (OCR) and extract transcripts from youtube links and perform NLP on them") 
le_choice = st.selectbox("Select document type",('PDF','text/plain',"text/html","Microsoft Word Document","image(png/jpg)","youtube_transcript"))

st.header("How do I use it?")
st.caption("Scroll below, select one of the given formats and drop the required file/link and ask any question!")

if le_choice == 'PDF':
    uploaded_file = st.file_uploader("Choose a file:")
    if uploaded_file is not None:
        
        
        bytes_data = uploaded_file.read()
        reader = PdfReader(uploaded_file)
        number_of_pages = len(reader.pages)


        if uploaded_file:
            save_folder = './data'
            save_path = Path(save_folder, uploaded_file.name)
            with open(save_path, mode='wb') as w:
                w.write(uploaded_file.getvalue())

        st.write(uploaded_file.name)

elif le_choice == 'text/plain':
    uploaded_file = st.file_uploader("Choose a file:")
    if uploaded_file is not None:
       
        if uploaded_file:
            save_folder = './data'
            save_path = Path(save_folder, uploaded_file.name)
            with open(save_path, mode='wb') as w:
                w.write(uploaded_file.getvalue())

        st.write(uploaded_file.name)

elif le_choice =='text/html':
    uploaded_file = st.file_uploader("Choose a file:")
    if uploaded_file is not None:
        
        if uploaded_file:
            save_folder = './data'
            save_path = Path(save_folder, uploaded_file.name)
            with open(save_path, mode='wb') as w:
                w.write(uploaded_file.getvalue())

        st.write(uploaded_file.name)

elif le_choice == 'Microsoft Word Document':
    uploaded_file = st.file_uploader("Choose a file:")
    if uploaded_file is not None:
        
        if uploaded_file:
            save_folder = './data'
            save_path = Path(save_folder, uploaded_file.name)
            with open(save_path, mode='wb') as w:
                w.write(uploaded_file.getvalue())

        st.write(uploaded_file.name)      

elif le_choice == 'image(png/jpg)':
    uploaded_file = st.file_uploader("Choose a file:")
    if uploaded_file is not None:
        
        # Save the uploaded image file
        save_folder = './data'
        save_path_image = Path(save_folder, uploaded_file.name)
        with open(save_path_image, mode='wb') as w:
            w.write(uploaded_file.getvalue())

        # Perform OCR on the saved image using EasyOCR
        reader = easyocr.Reader(['en'])
        result = reader.readtext(str(save_path_image))  # Convert Path to string

        # Save the OCR result to a text file
        save_path_txt = Path(save_folder, uploaded_file.name + '.txt')
        with open(save_path_txt, mode='w', encoding='utf-8') as w:
            for detection in result:
                w.write(detection[1] + '\n')  # Writing the detected text to the file

        # Display the uploaded file name and the OCR result
        st.write(f"Uploaded File: {uploaded_file.name}")
        st.write("Text from Image:")
        for detection in result:
            st.write(detection[1])

elif le_choice == 'youtube_transcript':
    title = st.text_input('YouTube video link')

    def extract_video_code(youtube_url):
        # Regular expression pattern to match the video code
        pattern = re.compile(r'(?<=v=)[^&]+')

        # Search for the pattern in the URL
        match = pattern.search(youtube_url)

        # Check if a match is found
        if match:
            video_code = match.group(0)
            return video_code
        else:
            st.error("No video code found in the URL.")
            return None

    code_found = extract_video_code(title)

    if code_found:
        try:
            # Create the .data directory if it doesn't exist
            data_dir = ".data"
            os.makedirs(data_dir, exist_ok=True)

            # obtained by the .get_transcript() function
            srt = YouTubeTranscriptApi.get_transcript(code_found)

            # creating or overwriting a file "subtitles.txt" with
            # the info inside the context manager
            subtitles_file_path = os.path.join(data_dir, "subtitles.txt")
            with open(subtitles_file_path, "w") as f:
                # iterating through each element of list srt
                for i in srt:
                    # writing each element of srt on a new line
                    f.write("{}\n".format(i))

            # Read the content of the .txt file
            with open(subtitles_file_path, 'r') as file:
                content = file.read()

            # Use regex to extract 'text' field from each line
            matches = re.findall(r"'text': '(.*?)'", content)

            # Join the matches into a single string
            transcript = ' '.join(matches)

            # Write the transcript to a new .txt file
            transcript_file_path = "./data/transcript.txt"
            with open(transcript_file_path, 'w') as output_file:
                output_file.write(transcript)

            st.success(f"Transcript successfully extracted and written to '{transcript_file_path}'")
        except Exception as e:
            st.error(f"Error: {str(e)}")  

if "messages" not in st.session_state.keys(): # Initialize the chat messages history
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me anything!"}
    ]

@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text="Please wait while The Omniscient One fetches information for you."):
        reader = SimpleDirectoryReader(input_dir='./data', recursive=True)
        docs = reader.load_data()
        service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt="You're a bot who simply returns the subject in a sentence. Keep your answer as restrictive as possible, mostly limited to one word, if there are more than two words however instead of a space output them with an underscore between the words. Do not makeup the subject and do not hallucinate"))
        index = VectorStoreIndex.from_documents(docs, service_context=service_context)
        return index

index = load_data()

if "chat_engine" not in st.session_state.keys(): # Initialize the chat engine
        st.session_state.chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)

if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chat_engine.chat(prompt)
            st.write(response.response)
            translator= Translator(to_lang="hi")
            translation = translator.translate(response.response)

            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message) 
