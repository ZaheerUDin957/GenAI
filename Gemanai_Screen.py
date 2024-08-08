import streamlit as st
import google.generativeai as genai

# Function to configure API key
def configure_api_key(api_key):
    genai.configure(api_key=api_key)

def get_gemini_response(prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text if response else "No response from the model."

# Define individual task functions
def fitness_plan_generator_app():
    prompt_input = st.text_area("Enter details for fitness plan:", "", height=300, max_chars=5000)
    if st.button('Generate Fitness Plan'):
        if prompt_input:
            prompt = f"Generate a fitness plan based on the following details:\n{prompt_input}"
            st.write("**Generated Fitness Plan:**")
            response = get_gemini_response(prompt)
            st.write(response)

def grammar_correction_app():
    text_input = st.text_area("Enter text to correct grammar:", "", height=300, max_chars=5000)
    if st.button('Correct Grammar'):
        if text_input:
            prompt = f"Correct the grammar in the following text:\n{text_input}"
            st.write("**Corrected Text:**")
            response = get_gemini_response(prompt)
            st.write(response)

def keyword_extractor_app():
    text_input = st.text_area("Enter text to extract keywords from:", "", height=300, max_chars=5000)
    if st.button('Extract Keywords'):
        if text_input:
            prompt = f"Extract keywords from the following text:\n{text_input}"
            st.write("**Extracted Keywords:**")
            response = get_gemini_response(prompt)
            st.write(response)

def language_translator_app():
    text_input = st.text_area("Enter text to translate:", "", height=150, max_chars=5000)
    target_language = st.text_input("Enter target language:", "")
    if st.button('Translate'):
        if text_input and target_language:
            prompt = f"Translate the following text into {target_language}:\n{text_input}"
            st.write("**Translated Text:**")
            response = get_gemini_response(prompt)
            st.write(response)

def memo_writer_app():
    prompt_input = st.text_area("Enter details for the memo:", "", height=300, max_chars=5000)
    if st.button('Write Memo'):
        if prompt_input:
            prompt = f"Write a memo based on the following details:\n{prompt_input}"
            st.write("**Generated Memo:**")
            response = get_gemini_response(prompt)
            st.write(response)

def personal_tutor_app():
    text_input = st.text_area("Enter topic or question for tutoring:", "", height=300, max_chars=5000)
    if st.button('Get Tutoring'):
        if text_input:
            prompt = f"Act as a personal tutor and explain the following topic in detail:\n{text_input}"
            st.write("**Tutoring Response:**")
            response = get_gemini_response(prompt)
            st.write(response)

def poetry_generator_app():
    prompt_input = st.text_area("Enter details for the poem:", "", height=300, max_chars=5000)
    if st.button('Generate Poem'):
        if prompt_input:
            prompt = f"Generate a poem based on the following details:\n{prompt_input}"
            st.write("**Generated Poem:**")
            response = get_gemini_response(prompt)
            st.write(response)

def python_debugger_app():
    code_input = st.text_area("Enter Python code to debug:", "", height=300, max_chars=5000)
    if st.button('Debug Code'):
        if code_input:
            prompt = f"Debug the following Python code and provide suggestions for fixes:\n{code_input}"
            st.write("**Debugging Suggestions:**")
            response = get_gemini_response(prompt)
            st.write(response)

def python_interpreter_app():
    code_input = st.text_area("Enter Python code to interpret:", "", height=300, max_chars=5000)
    if st.button('Interpret Code'):
        if code_input:
            prompt = f"Interpret the following Python code and explain its functionality:\n{code_input}"
            st.write("**Code Interpretation:**")
            response = get_gemini_response(prompt)
            st.write(response)

def sentiment_analysis_app():
    text_input = st.text_area("Enter text to analyze sentiment:", "", height=300, max_chars=5000)
    if st.button('Analyze Sentiment'):
        if text_input:
            prompt = f"Analyze the sentiment of the following text:\n{text_input}"
            st.write("**Sentiment Analysis Result:**")
            response = get_gemini_response(prompt)
            st.write(response)

def social_media_post_generator_app():
    prompt_input = st.text_area("Enter details for the social media post:", "", height=300, max_chars=5000)
    if st.button('Generate Post'):
        if prompt_input:
            prompt = f"Generate a social media post based on the following details:\n{prompt_input}"
            st.write("**Generated Social Media Post:**")
            response = get_gemini_response(prompt)
            st.write(response)

def text_generator_app():
    prompt_input = st.text_area("Enter details for text generation:", "", height=300, max_chars=5000)
    if st.button('Generate Text'):
        if prompt_input:
            prompt = f"Generate text based on the following details:\n{prompt_input}"
            st.write("**Generated Text:**")
            response = get_gemini_response(prompt)
            st.write(response)

def text_summarization_app():
    text_input = st.text_area("Enter text to summarize:", "", height=300, max_chars=5000)
    if st.button('Summarize Text'):
        if text_input:
            prompt = f"Summarize the following text:\n{text_input}"
            st.write("**Summarized Text:**")
            response = get_gemini_response(prompt)
            st.write(response)

def zero_shot_classification_app():
    text_input = st.text_area("Enter text for zero-shot classification:", "", height=300, max_chars=5000)
    categories = st.text_input("Enter categories (comma-separated):", "")
    if st.button('Classify Text'):
        if text_input and categories:
            prompt = f"Classify the following text into the categories: {categories}.\n\nText: {text_input}"
            st.write("**Classification Result:**")
            response = get_gemini_response(prompt)
            st.write(response)

def token_classification_app():
    text_input = st.text_area("Enter text for token classification:", "", height=300, max_chars=5000)
    if st.button('Classify Tokens'):
        if text_input:
            prompt = f"Classify the tokens in the following text:\n{text_input}"
            st.write("**Token Classification Result:**")
            response = get_gemini_response(prompt)
            st.write(response)

def feature_extraction_app():
    text_input = st.text_area("Enter text for feature extraction:", "", height=300, max_chars=5000)
    if st.button('Extract Features'):
        if text_input:
            prompt = f"Extract features from the following text:\n{text_input}"
            st.write("**Extracted Features:**")
            response = get_gemini_response(prompt)
            st.write(response)

def interview_question_generation_app():
    prompt_input = st.text_area("Enter details for interview question generation:", "", height=300, max_chars=5000)
    if st.button('Generate Interview Questions'):
        if prompt_input:
            prompt = f"Generate interview questions based on the following details:\n{prompt_input}"
            st.write("**Generated Interview Questions:**")
            response = get_gemini_response(prompt)
            st.write(response)

def brand_name_generation_app():
    prompt_input = st.text_area("Enter details for brand name generation:", "", height=300, max_chars=5000)
    if st.button('Generate Brand Name'):
        if prompt_input:
            prompt = f"Generate a brand name based on the following details:\n{prompt_input}"
            st.write("**Generated Brand Name:**")
            response = get_gemini_response(prompt)
            st.write(response)

def website_building_app():
    prompt_input = st.text_area("Enter details for website building:", "", height=300, max_chars=5000)
    if st.button('Build Website'):
        if prompt_input:
            prompt = f"Generate content for building a website based on the following details:\n{prompt_input}"
            st.write("**Generated Website Content:**")
            response = get_gemini_response(prompt)
            st.write(response)

def fill_masking_app():
    text_input = st.text_area("Enter text with missing words for fill-masking:", "", height=300, max_chars=5000)
    if st.button('Fill Mask'):
        if text_input:
            prompt = f"Fill in the missing words in the following text:\n{text_input}"
            st.write("**Filled Text:**")
            response = get_gemini_response(prompt)
            st.write(response)

def rap_writing_app():
    prompt_input = st.text_area("Enter details for rap writing:", "", height=300, max_chars=5000)
    if st.button('Write Rap'):
        if prompt_input:
            prompt = f"Generate a rap based on the following details:\n{prompt_input}"
            st.write("**Generated Rap:**")
            response = get_gemini_response(prompt)
            st.write(response)

def email_draft_app():
    prompt_input = st.text_area("Enter details for email drafting:", "", height=300, max_chars=5000)
    if st.button('Draft Email'):
        if prompt_input:
            prompt = f"Draft an email based on the following details:\n{prompt_input}"
            st.write("**Drafted Email:**")
            response = get_gemini_response(prompt)
            st.write(response)

def chat_with_gpt_app():
    chat_input = st.text_area("Enter your message for the chat:", "", height=300, max_chars=5000)
    if st.button('Send Message'):
        if chat_input:
            prompt = f"Chat with GPT-4 based on the following message:\n{chat_input}"
            st.write("**GPT-4 Response:**")
            response = get_gemini_response(prompt)
            st.write(response)

# Main application function
def Gemanai_App():
    # Display API key input and save it
    api_key = st.text_input("Enter your Gemini API Key:", type="password")
    
    if api_key:
        configure_api_key(api_key)
        
        # Display the task selection options
        st.header("Choose a Task")
        task = st.selectbox("Select a task:", [
            "Fitness Plan Generator",
            "Grammar Correction",
            "Keyword Extractor",
            "Language Translator",
            "Memo Writer",
            "Personal Tutor",
            "Poetry Generator",
            "Python Debugger",
            "Python Interpreter",
            "Sentiment Analysis",
            "Social Media Post Generator",
            "Text Generator",
            "Text Summarization",
            "Zero-Shot Classification",
            "Token Classification",
            "Feature Extraction",
            "Interview Question Generation",
            "Brand Name Generation",
            "Website Building",
            "Fill Masking",
            "Rap Writing",
            "Email Draft",
            "Chat with GPT"
        ])

        # Call the respective function based on the selected task
        if task == "Fitness Plan Generator":
            fitness_plan_generator_app()
        elif task == "Grammar Correction":
            grammar_correction_app()
        elif task == "Keyword Extractor":
            keyword_extractor_app()
        elif task == "Language Translator":
            language_translator_app()
        elif task == "Memo Writer":
            memo_writer_app()
        elif task == "Personal Tutor":
            personal_tutor_app()
        elif task == "Poetry Generator":
            poetry_generator_app()
        elif task == "Python Debugger":
            python_debugger_app()
        elif task == "Python Interpreter":
            python_interpreter_app()
        elif task == "Sentiment Analysis":
            sentiment_analysis_app()
        elif task == "Social Media Post Generator":
            social_media_post_generator_app()
        elif task == "Text Generator":
            text_generator_app()
        elif task == "Text Summarization":
            text_summarization_app()
        elif task == "Zero-Shot Classification":
            zero_shot_classification_app()
        elif task == "Token Classification":
            token_classification_app()
        elif task == "Feature Extraction":
            feature_extraction_app()
        elif task == "Interview Question Generation":
            interview_question_generation_app()
        elif task == "Brand Name Generation":
            brand_name_generation_app()
        elif task == "Website Building":
            website_building_app()
        elif task == "Fill Masking":
            fill_masking_app()
        elif task == "Rap Writing":
            rap_writing_app()
        elif task == "Email Draft":
            email_draft_app()
        elif task == "Chat with GPT":
            chat_with_gpt_app()

if __name__ == "__main__":
    Gemanai_App()
