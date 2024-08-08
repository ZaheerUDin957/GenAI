import streamlit as st
import openai

def authenticate_api_key():
    api_key = st.text_input("Enter your OpenAI API key:", type="password")
    if api_key:
        openai.api_key = api_key
        return True
    else:
        st.error("API key is required to proceed.")
        return False

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt["system"]},
            {"role": "user", "content": prompt["user"]}
        ],
        max_tokens=50
    )
    return response.choices[0].message.content.strip()

# Define individual task functions
def fitness_plan_generator_app():
    prompt_input = st.text_area("Enter details for fitness plan:", "", height=300, max_chars=5000)
    if st.button('Generate Fitness Plan'):
        if prompt_input:
            st.write("**Generated Fitness Plan:**")
            st.write(generate_response({"system": "Generate a fitness plan based on the following prompt.", "user": prompt_input}))

def grammar_correction_app():
    text_input = st.text_area("Enter text to correct grammar:", "", height=300, max_chars=5000)
    if st.button('Correct Grammar'):
        if text_input:
            st.write("**Corrected Text:**")
            st.write(generate_response({"system": "Correct the grammar in the following text.", "user": text_input}))

def keyword_extractor_app():
    text_input = st.text_area("Enter text to extract keywords from:", "", height=300, max_chars=5000)
    if st.button('Extract Keywords'):
        if text_input:
            st.write("**Extracted Keywords:**")
            st.write(generate_response({"system": "Extract keywords from the following text.", "user": text_input}))

def language_translator_app():
    text_input = st.text_area("Enter text to translate:", "", height=150, max_chars=5000)
    target_language = st.text_input("Enter target language:", "")
    if st.button('Translate'):
        if text_input and target_language:
            prompt = f"Translate the following text into {target_language}:\n\nText: {text_input}"
            st.write("**Translated Text:**")
            st.write(generate_response({"system": "Translate the following text.", "user": prompt}))

def memo_writer_app():
    prompt_input = st.text_area("Enter details for the memo:", "", height=300, max_chars=5000)
    if st.button('Write Memo'):
        if prompt_input:
            st.write("**Generated Memo:**")
            st.write(generate_response({"system": "Write a memo based on the following prompt.", "user": prompt_input}))

def personal_tutor_app():
    text_input = st.text_area("Enter topic or question for tutoring:", "", height=300, max_chars=5000)
    if st.button('Get Tutoring'):
        if text_input:
            st.write("**Tutoring Response:**")
            st.write(generate_response({"system": "Act as a personal tutor and explain the following topic in detail.", "user": text_input}))

def poetry_generator_app():
    prompt_input = st.text_area("Enter details for the poem:", "", height=300, max_chars=5000)
    if st.button('Generate Poem'):
        if prompt_input:
            st.write("**Generated Poem:**")
            st.write(generate_response({"system": "Generate a poem based on the following prompt.", "user": prompt_input}))

def python_debugger_app():
    code_input = st.text_area("Enter Python code to debug:", "", height=300, max_chars=5000)
    if st.button('Debug Code'):
        if code_input:
            st.write("**Debugging Suggestions:**")
            st.write(generate_response({"system": "Debug the following Python code and provide suggestions for fixes.", "user": code_input}))

def python_interpreter_app():
    code_input = st.text_area("Enter Python code to interpret:", "", height=300, max_chars=5000)
    if st.button('Interpret Code'):
        if code_input:
            st.write("**Code Interpretation:**")
            st.write(generate_response({"system": "Interpret the following Python code and explain its functionality.", "user": code_input}))

def sentiment_analysis_app():
    text_input = st.text_area("Enter text to analyze sentiment:", "", height=300, max_chars=5000)
    if st.button('Analyze Sentiment'):
        if text_input:
            st.write("**Sentiment Analysis Result:**")
            st.write(generate_response({"system": "Analyze the sentiment of the following text.", "user": text_input}))

def social_media_post_generator_app():
    prompt_input = st.text_area("Enter details for the social media post:", "", height=300, max_chars=5000)
    if st.button('Generate Post'):
        if prompt_input:
            st.write("**Generated Social Media Post:**")
            st.write(generate_response({"system": "Generate a social media post based on the following prompt.", "user": prompt_input}))

def text_generator_app():
    prompt_input = st.text_area("Enter details for text generation:", "", height=300, max_chars=5000)
    if st.button('Generate Text'):
        if prompt_input:
            st.write("**Generated Text:**")
            st.write(generate_response({"system": "Generate text based on the following prompt.", "user": prompt_input}))

def text_summarization_app():
    text_input = st.text_area("Enter text to summarize:", "", height=300, max_chars=5000)
    if st.button('Summarize Text'):
        if text_input:
            st.write("**Summarized Text:**")
            st.write(generate_response({"system": "Summarize the following text.", "user": text_input}))

def zero_shot_classification_app():
    text_input = st.text_area("Enter text for zero-shot classification:", "", height=300, max_chars=5000)
    categories = st.text_input("Enter categories (comma-separated):", "")
    if st.button('Classify Text'):
        if text_input and categories:
            prompt = f"Classify the following text into the categories: {categories}.\n\nText: {text_input}"
            st.write("**Classification Result:**")
            st.write(generate_response({"system": "Classify the following text into the provided categories.", "user": prompt}))

def token_classification_app():
    text_input = st.text_area("Enter text for token classification:", "", height=300, max_chars=5000)
    if st.button('Classify Tokens'):
        if text_input:
            st.write("**Token Classification Result:**")
            st.write(generate_response({"system": "Classify the tokens in the following text.", "user": text_input}))

def feature_extraction_app():
    text_input = st.text_area("Enter text for feature extraction:", "", height=300, max_chars=5000)
    if st.button('Extract Features'):
        if text_input:
            st.write("**Extracted Features:**")
            st.write(generate_response({"system": "Extract features from the following text.", "user": text_input}))

def interview_question_generation_app():
    prompt_input = st.text_area("Enter details for interview question generation:", "", height=300, max_chars=5000)
    if st.button('Generate Interview Questions'):
        if prompt_input:
            st.write("**Generated Interview Questions:**")
            st.write(generate_response({"system": "Generate interview questions based on the following prompt.", "user": prompt_input}))

def brand_name_generation_app():
    prompt_input = st.text_area("Enter details for brand name generation:", "", height=300, max_chars=5000)
    if st.button('Generate Brand Name'):
        if prompt_input:
            st.write("**Generated Brand Name:**")
            st.write(generate_response({"system": "Generate a brand name based on the following prompt.", "user": prompt_input}))

def website_building_app():
    prompt_input = st.text_area("Enter details for website building:", "", height=300, max_chars=5000)
    if st.button('Build Website'):
        if prompt_input:
            st.write("**Generated Website Content:**")
            st.write(generate_response({"system": "Generate content for building a website based on the following prompt.", "user": prompt_input}))

def fill_masking_app():
    text_input = st.text_area("Enter text with missing words for fill-masking:", "", height=300, max_chars=5000)
    if st.button('Fill Mask'):
        if text_input:
            st.write("**Filled Text:**")
            st.write(generate_response({"system": "Fill in the missing words in the following text.", "user": text_input}))

def rap_writing_app():
    prompt_input = st.text_area("Enter details for rap writing:", "", height=300, max_chars=5000)
    if st.button('Write Rap'):
        if prompt_input:
            st.write("**Generated Rap:**")
            st.write(generate_response({"system": "Generate a rap based on the following prompt.", "user": prompt_input}))

def similarity_computing_app():
    text_input1 = st.text_area("Enter the first text:", "", height=150, max_chars=5000, key='text1')
    text_input2 = st.text_area("Enter the second text:", "", height=150, max_chars=5000, key='text2')
    if st.button('Compute Similarity'):
        if text_input1 and text_input2:
            prompt = f"Compute the similarity between the following two texts:\n\nText 1: {text_input1}\nText 2: {text_input2}"
            st.write("**Similarity Result:**")
            st.write(generate_response({"system": "Compute the similarity between the following two texts.", "user": prompt}))

def test_main_app():
    st.title("OpenAI Streamlit App")

    app_options = [
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
        "Fill-Masking",
        "Rap Writing",
        "Similarity Computing"
    ]
    selected_option = st.selectbox("Select an app:", app_options)

    if selected_option == "Fitness Plan Generator":
        fitness_plan_generator_app()
    elif selected_option == "Grammar Correction":
        grammar_correction_app()
    elif selected_option == "Keyword Extractor":
        keyword_extractor_app()
    elif selected_option == "Language Translator":
        language_translator_app()
    elif selected_option == "Memo Writer":
        memo_writer_app()
    elif selected_option == "Personal Tutor":
        personal_tutor_app()
    elif selected_option == "Poetry Generator":
        poetry_generator_app()
    elif selected_option == "Python Debugger":
        python_debugger_app()
    elif selected_option == "Python Interpreter":
        python_interpreter_app()
    elif selected_option == "Sentiment Analysis":
        sentiment_analysis_app()
    elif selected_option == "Social Media Post Generator":
        social_media_post_generator_app()
    elif selected_option == "Text Generator":
        text_generator_app()
    elif selected_option == "Text Summarization":
        text_summarization_app()
    elif selected_option == "Zero-Shot Classification":
        zero_shot_classification_app()
    elif selected_option == "Token Classification":
        token_classification_app()
    elif selected_option == "Feature Extraction":
        feature_extraction_app()
    elif selected_option == "Interview Question Generation":
        interview_question_generation_app()
    elif selected_option == "Brand Name Generation":
        brand_name_generation_app()
    elif selected_option == "Website Building":
        website_building_app()
    elif selected_option == "Fill-Masking":
        fill_masking_app()
    elif selected_option == "Rap Writing":
        rap_writing_app()
    elif selected_option == "Similarity Computing":
        similarity_computing_app()

def OpenAI_App():
    if authenticate_api_key():
        test_main_app()

# Run the OpenAI_App function
if __name__ == "__main__":
    OpenAI_App()
