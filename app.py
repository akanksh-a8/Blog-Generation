import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## Function to get response from Llama 2 model
def getLLamaresponse(input_text, no_words, blog_style):
    ### Llama2 model
    llm = CTransformers(model='C:\\Users\\ragha\\OneDrive\\Desktop\\Blog Generation\\Models\\llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        config={'max_new_tokens': 256,
                                'temperature': 0.01})
    
    ## Prompt Template
    template = """
        Write a blog for {blog_style} job profile for a topic {input_text}
        within {no_words} words.
    """
    
    prompt = PromptTemplate(input_variables=["blog_style", "input_text", 'no_words'],
                            template=template)
    
    ## Generate the response from the Llama 2 model
    response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    print(response)
    return response

## Streamlit application setup
st.set_page_config(page_title="Generate Blogs",
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.markdown("""
    <style>
        body {
            background-color: #000000;
        }
        .main {
            background-color: #1e1e1e;
            padding: 20px;
            border-radius: 10px;
            color: white;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
        .stButton button:hover {
            background-color: #45a049;
        }
        .stTextInput input, .stSelectbox select {
            border: 1px solid #ccc;
            padding: 10px;
            border-radius: 5px;
            width: 100%;
            box-sizing: border-box;
            background-color: #333;
            color: white;
        }
        .stSelectbox select {
            background-color: #000000; /* Set the background color for select box */
        }
        .header {
            font-size: 36px;
            font-weight: bold;
            color: white;
            text-align: center;
        }
        .description {
            font-size: 18px;
            color: #ccc;
            text-align: center;
            margin-bottom: 30px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="header">Generate Blogs 🤖</div>', unsafe_allow_html=True)
st.markdown('<div class="description">Generate engaging blogs tailored to different job profiles using the Llama 2 model.</div>', unsafe_allow_html=True)

input_text = st.text_input("Enter the Blog Topic", placeholder="e.g., Latest Trends in Data Science")

## Creating two more columns for additional fields
col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('Number of Words', placeholder="e.g., 500")
with col2:
    blog_style = st.selectbox('Writing the blog for', ('Researchers', 'Data Scientist', 'Common People'), index=0, key='blog_style_select')

submit = st.button("Generate")

## Final response
if submit:
    with st.spinner('Generating blog...'):
        response = getLLamaresponse(input_text, no_words, blog_style)
        st.success("Blog generated successfully!")
        st.markdown("### Generated Blog:")
        st.write(response)
