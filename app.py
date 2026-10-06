import os
import base64
import requests
import streamlit as st
from dotenv import load_dotenv
from pypdf import PdfReader

# ============================================================
# MULTIMAX AURA
# Multimodal AI Workspace
# ============================================================

load_dotenv()

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Multimax Aura",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# API CONFIGURATION
# ============================================================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Use a currently supported Gemini Flash model.
GEMINI_MODEL = "gemini-3.5-flash"

GEMINI_URL = (
    "https://generativelanguage.googleapis.com/v1beta/interactions"
)

# ============================================================
# PREMIUM AURA UI
# ============================================================

st.markdown(
    """
<style>

.stApp {
    background:
        radial-gradient(
            circle at 15% 10%,
            rgba(105, 55, 210, 0.18),
            transparent 28%
        ),
        radial-gradient(
            circle at 85% 10%,
            rgba(0, 180, 255, 0.10),
            transparent 28%
        ),
        linear-gradient(
            135deg,
            #07080d 0%,
            #090a12 50%,
            #050a10 100%
        );
    color: #f5f5f7;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #090a10 0%,
            #08090e 100%
        );
    border-right: 1px solid rgba(255,255,255,0.07);
}

section[data-testid="stSidebar"] > div {
    padding-top: 25px;
}

section[data-testid="stSidebar"] * {
    color: #eeeeee;
}

/* BRAND */

.brand {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 28px;
}

.brand-icon {
    width: 44px;
    height: 44px;
    min-width: 44px;
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    background:
        linear-gradient(
            135deg,
            #8b5cf6,
            #4f46e5
        );
    box-shadow:
        0 0 25px rgba(124,58,237,0.45);
    font-size: 22px;
}

.brand-name {
    font-size: 19px;
    font-weight: 750;
    letter-spacing: 0.3px;
}

.brand-sub {
    color: #777b89;
    font-size: 9px;
    margin-top: 3px;
    letter-spacing: 1.7px;
}

/* STATUS */

.status-card {
    background:
        rgba(255,255,255,0.035);
    border:
        1px solid rgba(255,255,255,0.08);
    border-radius: 15px;
    padding: 14px;
    margin-bottom: 28px;
}

.status-row {
    display: flex;
    align-items: center;
    gap: 9px;
    font-size: 13px;
}

.status-dot {
    width: 8px;
    height: 8px;
    background: #4ade80;
    border-radius: 50%;
    box-shadow:
        0 0 12px #4ade80;
}

/* SIDEBAR TITLES */

.sidebar-title {
    color: #8c8f9e;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 25px;
    margin-bottom: 12px;
}

/* HERO */

.eyebrow {
    color: #9b8cff;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 3px;
    margin-top: 20px;
    margin-bottom: 18px;
}

.hero-title {
    font-size: clamp(52px, 7vw, 92px);
    line-height: 0.94;
    font-weight: 850;
    letter-spacing: -5px;

    background:
        linear-gradient(
            100deg,
            #ffffff 10%,
            #d1c7ff 48%,
            #9adfff 90%
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-description {
    max-width: 760px;
    color: #9296a8;
    font-size: 16px;
    line-height: 1.75;
    margin-top: 25px;
    margin-bottom: 30px;
}

/* AURA CORE */

.aura-container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 330px;
}

.aura-core {
    position: relative;
    width: 180px;
    height: 180px;
    border-radius: 50%;

    display: flex;
    align-items: center;
    justify-content: center;

    background:
        radial-gradient(
            circle,
            rgba(139,92,246,1) 0%,
            rgba(92,70,230,0.85) 25%,
            rgba(44,37,115,0.45) 50%,
            rgba(10,10,25,0) 72%
        );

    box-shadow:
        0 0 45px rgba(124,58,237,0.45),
        0 0 100px rgba(59,130,246,0.18);
}

.aura-ring-one {
    position: absolute;
    width: 220px;
    height: 220px;
    border-radius: 50%;
    border:
        1px solid rgba(139,92,246,0.35);
}

.aura-ring-two {
    position: absolute;
    width: 270px;
    height: 270px;
    border-radius: 50%;
    border:
        1px solid rgba(96,165,250,0.12);
}

.aura-symbol {
    font-size: 55px;
    color: white;
    text-shadow:
        0 0 25px rgba(255,255,255,0.9),
        0 0 45px rgba(139,92,246,0.8);
}

/* FEATURE CARDS */

.feature-card {
    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.055),
            rgba(255,255,255,0.015)
        );

    border:
        1px solid rgba(255,255,255,0.08);

    border-radius: 18px;
    padding: 23px;
    min-height: 165px;
    transition: 0.25s;
}

.feature-card:hover {
    border-color:
        rgba(139,92,246,0.45);

    transform:
        translateY(-3px);

    box-shadow:
        0 15px 45px rgba(0,0,0,0.25);
}

.feature-icon {
    font-size: 27px;
    margin-bottom: 13px;
}

.feature-title {
    font-size: 16px;
    font-weight: 750;
    margin-bottom: 8px;
}

.feature-text {
    color: #858998;
    font-size: 13px;
    line-height: 1.55;
}

/* SECTION */

.section-title {
    font-size: 25px;
    font-weight: 750;
    margin-top: 35px;
    margin-bottom: 7px;
}

.section-description {
    color: #777b89;
    margin-bottom: 20px;
}

/* RESPONSE */

.response-card {
    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.045),
            rgba(255,255,255,0.015)
        );

    border:
        1px solid rgba(255,255,255,0.08);

    border-radius: 18px;
    padding: 25px;
    margin-top: 20px;
    line-height: 1.75;
}

/* INPUTS */

textarea {
    background: #101118 !important;
    color: white !important;
    border:
        1px solid rgba(255,255,255,0.08) !important;
    border-radius: 13px !important;
}

textarea:focus {
    border:
        1px solid rgba(139,92,246,0.65) !important;

    box-shadow:
        0 0 0 1px rgba(139,92,246,0.2) !important;
}

input {
    color: white !important;
}

/* BUTTONS */

.stButton > button {
    border-radius: 12px;

    border:
        1px solid rgba(139,92,246,0.35);

    background:
        linear-gradient(
            135deg,
            rgba(139,92,246,0.25),
            rgba(59,130,246,0.18)
        );

    color: white;
    font-weight: 650;
    min-height: 45px;
    transition: 0.25s;
}

.stButton > button:hover {
    border-color: #8b5cf6;

    box-shadow:
        0 0 25px rgba(139,92,246,0.25);

    transform:
        translateY(-1px);
}

/* FILE UPLOADER */

[data-testid="stFileUploader"] {
    background:
        rgba(255,255,255,0.025);

    border:
        1px dashed rgba(139,92,246,0.35);

    border-radius: 16px;
    padding: 10px;
}

/* FOOTER */

.footer {
    text-align: center;
    color: #555866;
    font-size: 12px;
    margin-top: 75px;
    padding-top: 22px;
    border-top:
        1px solid rgba(255,255,255,0.06);
}

div[data-testid="stAlert"] {
    border-radius: 13px;
}

</style>
""",
    unsafe_allow_html=True
)

# ============================================================
# GEMINI API
# ============================================================

def ask_gemini(prompt):

    if not GEMINI_API_KEY:
        return "⚠️ Gemini API key is missing. Check your .env file."

    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": GEMINI_API_KEY
    }

    data = {
        "model": GEMINI_MODEL,
        "input": prompt,
        "generation_config": {
            "thinking_level": "low"
        }
    }

    try:

        response = requests.post(
            GEMINI_URL,
            headers=headers,
            json=data,
            timeout=120
        )

        if response.status_code != 200:
            return (
                f"⚠️ Gemini API Error ({response.status_code})\n\n"
                f"{response.text}"
            )

        result = response.json()

        # The Interactions API provides output_text
        if result.get("output_text"):
            return result["output_text"]

        # Fallback: read model_output steps
        for step in result.get("steps", []):

            if step.get("type") == "model_output":

                for item in step.get("content", []):

                    if item.get("type") == "text":

                        text = item.get("text", "")

                        if text:
                            return text

        return "⚠️ Gemini returned no text."

    except requests.exceptions.Timeout:

        return "⚠️ Gemini request timed out. Please try again."

    except requests.exceptions.RequestException as e:

        return f"⚠️ Network error:\n\n{str(e)}"

    except Exception as e:

        return f"⚠️ Unexpected error:\n\n{str(e)}"
# ============================================================
# PDF EXTRACTION
# ============================================================

def extract_pdf_text(uploaded_file):

    try:

        reader = PdfReader(
            uploaded_file
        )

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:

                text += page_text
                text += "\n"

        return text

    except Exception as e:

        return (
            f"PDF extraction failed: {str(e)}"
        )


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
<div class="brand">
    <div class="brand-icon">✦</div>
    <div>
        <div class="brand-name">Multimax Aura</div>
        <div class="brand-sub">MULTIMODAL INTELLIGENCE</div>
    </div>
</div>
""",
        unsafe_allow_html=True
    )

    st.markdown(
        """
<div class="status-card">
    <div class="status-row">
        <span class="status-dot"></span>
        <span>Aura systems ready</span>
    </div>
</div>
""",
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-title">Workspace</div>',
        unsafe_allow_html=True
    )

    mode = st.radio(
        "Choose Aura",
        [
            "✦ Aura Home",
            "📝 Text Aura",
            "📄 Document Aura",
            "🖼️ Vision Aura",
            "🎙️ Voice Aura"
        ],
        label_visibility="collapsed"
    )

    st.markdown(
        '<div class="sidebar-title">AI Settings</div>',
        unsafe_allow_html=True
    )

    temperature = st.slider(
        "Creativity",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1
    )

    st.markdown("---")

    st.caption("✦ MULTIMAX AURA")
    st.caption("One workspace. Multiple modalities.")


# ============================================================
# HOME
# ============================================================

if mode == "✦ Aura Home":

    st.markdown(
        '<div class="eyebrow">MULTIMODAL AI WORKSPACE</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
<div class="hero-title">
    Intelligence,<br>
    without limits.
</div>
""",
        unsafe_allow_html=True
    )

    st.markdown(
        """
<div class="hero-description">
    Transform images, documents, text and voice
    through connected AI experiences.
    One workspace. Multiple modalities.
    One intelligent Aura.
</div>
""",
        unsafe_allow_html=True
    )

    st.markdown(
        """
<div class="aura-container">
    <div class="aura-core">
        <div class="aura-ring-one"></div>
        <div class="aura-ring-two"></div>
        <div class="aura-symbol">✦</div>
    </div>
</div>
""",
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">What can Aura do?</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-description">'
        'One intelligent workspace for multiple forms of information.'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.markdown(
            """
<div class="feature-card">
    <div class="feature-icon">📝</div>
    <div class="feature-title">Text Intelligence</div>
    <div class="feature-text">
        Ask questions, generate ideas,
        explain concepts and create content.
    </div>
</div>
""",
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
<div class="feature-card">
    <div class="feature-icon">📄</div>
    <div class="feature-title">Document Intelligence</div>
    <div class="feature-text">
        Upload PDFs and extract,
        summarize and understand information.
    </div>
</div>
""",
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            """
<div class="feature-card">
    <div class="feature-icon">🖼️</div>
    <div class="feature-title">Vision Intelligence</div>
    <div class="feature-text">
        Analyze images and understand
        visual information with AI.
    </div>
</div>
""",
            unsafe_allow_html=True
        )

    with col4:

        st.markdown(
            """
<div class="feature-card">
    <div class="feature-icon">🎙️</div>
    <div class="feature-title">Voice Intelligence</div>
    <div class="feature-text">
        Bring natural voice interaction
        into the Aura workspace.
    </div>
</div>
""",
            unsafe_allow_html=True
        )


# ============================================================
# TEXT AURA
# ============================================================

elif mode == "📝 Text Aura":

    st.markdown(
        '<div class="eyebrow">TEXT AURA</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
<div class="hero-title">
    Think.<br>
    Create.
</div>
""",
        unsafe_allow_html=True
    )

    st.markdown(
        """
<div class="hero-description">
    Your intelligent text workspace.
    Ask anything, generate content,
    learn concepts and solve problems.
</div>
""",
        unsafe_allow_html=True
    )

    prompt = st.text_area(
        "What would you like Aura to do?",
        placeholder=(
            "Ask Aura anything...\n\n"
            "Example: Explain quantum computing "
            "like I'm a beginner."
        ),
        height=180
    )

    col1, col2 = st.columns([4, 1])

    with col1:

        task = st.selectbox(
            "Response style",
            [
                "Normal",
                "Explain simply",
                "Professional",
                "Detailed",
                "Step-by-step",
                "Creative"
            ]
        )

    with col2:

        st.write("")

        generate = st.button(
            "✦ Generate",
            use_container_width=True
        )

    if generate:

        if not prompt.strip():

            st.warning(
                "Please enter something for Aura to process."
            )

        else:

            enhanced_prompt = f"""
You are Multimax Aura,
an advanced multimodal AI assistant.

User request:

{prompt}

Response style:

{task}

Creativity level:

{temperature}

Give a useful, accurate and well-structured answer.
"""

            with st.spinner(
                "Aura is thinking..."
            ):

                answer = ask_gemini(
                    enhanced_prompt
                )

            st.markdown(
                '<div class="section-title">Aura Response</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<div class="response-card">',
                unsafe_allow_html=True
            )

            st.markdown(answer)

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )


# ============================================================
# DOCUMENT AURA
# ============================================================

elif mode == "📄 Document Aura":

    st.markdown(
        '<div class="eyebrow">DOCUMENT AURA</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
<div class="hero-title">
    Understand<br>
    your documents.
</div>
""",
        unsafe_allow_html=True
    )

    st.markdown(
        """
<div class="hero-description">
    Upload a PDF and let Aura summarize,
    explain or answer questions from it.
</div>
""",
        unsafe_allow_html=True
    )

    uploaded_pdf = st.file_uploader(
        "Upload your PDF",
        type=["pdf"]
    )

    if uploaded_pdf:

        st.success(
            f"Loaded: {uploaded_pdf.name}"
        )

        document_text = extract_pdf_text(
            uploaded_pdf
        )

        if document_text:

            word_count = len(
                document_text.split()
            )

            st.info(
                f"Extracted approximately "
                f"{word_count:,} words."
            )

            document_action = st.selectbox(
                "Choose an action",
                [
                    "Summarize document",
                    "Explain document simply",
                    "Extract key points",
                    "Generate questions"
                ]
            )

            document_question = st.text_area(
                "Optional question",
                placeholder=(
                    "Ask something about this document..."
                )
            )

            if st.button(
                "✦ Analyze Document",
                use_container_width=True
            ):

                if document_action == "Summarize document":

                    instruction = """
Summarize the document clearly.
Include the most important ideas,
facts and conclusions.
"""

                elif document_action == "Explain document simply":

                    instruction = """
Explain the document in very simple language,
as if teaching a beginner.
"""

                elif document_action == "Extract key points":

                    instruction = """
Extract the most important points
from the document as clear bullet points.
"""

                else:

                    instruction = """
Create useful questions and answers
based on the document.
"""

                if document_question.strip():

                    instruction += f"""

Also answer this question:

{document_question}
"""

                prompt = f"""
You are Multimax Aura Document Intelligence.

{instruction}

Document content:

{document_text[:30000]}
"""

                with st.spinner(
                    "Aura is reading your document..."
                ):

                    answer = ask_gemini(
                        prompt
                    )

                st.markdown(
                    '<div class="section-title">Document Insight</div>',
                    unsafe_allow_html=True
                )

                st.markdown(answer)

        else:

            st.error(
                "No readable text was found in this PDF."
            )


# ============================================================
# VISION AURA
# ============================================================

elif mode == "🖼️ Vision Aura":

    st.markdown(
        '<div class="section-title">Vision Aura</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Upload an image and let Aura understand what it sees.'
        '</div>',
        unsafe_allow_html=True
    )

    uploaded_image = st.file_uploader(
        "Upload an image",
        type=["png", "jpg", "jpeg", "webp"],
        key="vision_upload"
    )

    vision_prompt = st.text_area(
        "What should Aura analyze?",
        placeholder=(
            "Example: Describe this image in detail, "
            "identify objects, and explain what is happening."
        ),
        height=120,
        key="vision_prompt"
    )

    if uploaded_image:

        st.image(
            uploaded_image,
            caption="Uploaded Image",
            use_container_width=True
        )

        if st.button(
            "✦ Analyze with Aura",
            use_container_width=True,
            key="vision_button"
        ):

            if not vision_prompt.strip():
                st.warning("Please enter what you want Aura to analyze.")

            else:

                image_bytes = uploaded_image.getvalue()
                encoded_image = base64.b64encode(image_bytes).decode("utf-8")

                mime_type = uploaded_image.type

                headers = {
                    "Content-Type": "application/json",
                    "x-goog-api-key": GEMINI_API_KEY
                }

                data = {
                    "model": GEMINI_MODEL,
                    "input": [
                        {
                            "type": "text",
                            "text": vision_prompt
                        },
                        {
                            "type": "image",
                            "mime_type": mime_type,
                            "data": encoded_image
                        }
                    ]
                }

                try:

                    with st.spinner("Aura is analyzing your image..."):

                        response = requests.post(
                            GEMINI_URL,
                            headers=headers,
                            json=data,
                            timeout=120
                        )

                    if response.status_code != 200:

                        st.error(
                            f"Vision API Error ({response.status_code})"
                        )

                        st.code(response.text)

                    else:

                        result = response.json()

                        answer = result.get("output_text", "")

                        if not answer:

                            for step in result.get("steps", []):

                                if step.get("type") == "model_output":

                                    for item in step.get("content", []):

                                        if item.get("type") == "text":

                                            text = item.get("text", "")

                                            if text:
                                                answer = text
                                                break

                                    if answer:
                                        break

                        if answer:

                            st.markdown(
                                '<div class="response-card">',
                                unsafe_allow_html=True
                            )

                            st.markdown(
                                "### ✦ Aura Vision Response"
                            )

                            st.write(answer)

                            st.markdown(
                                '</div>',
                                unsafe_allow_html=True
                            )

                        else:

                            st.warning(
                                "Aura received the image but returned no text."
                            )

                except requests.exceptions.Timeout:

                    st.error(
                        "Vision request timed out. Please try again."
                    )

                except requests.exceptions.RequestException as e:

                    st.error(
                        f"Network error: {str(e)}"
                    )

                except Exception as e:

                    st.error(
                        f"Unexpected error: {str(e)}"
                    )
# ============================================================
# VOICE AURA
# ============================================================

elif mode == "🎙️ Voice Aura":

    st.markdown(
        '<div class="eyebrow">VOICE AURA</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
<div class="hero-title">
    Speak.<br>
    Aura listens.
</div>
""",
        unsafe_allow_html=True
    )

    st.markdown(
        """
<div class="hero-description">
    Voice interaction brings natural
    conversation into the Aura workspace.
</div>
""",
        unsafe_allow_html=True
    )

    st.info(
        "🎙️ Voice interface ready. "
        "Speech recognition can be connected to this module."
    )

    voice_text = st.text_area(
        "Voice transcript",
        placeholder=(
            "For now, type what you would say..."
        ),
        height=150
    )

    if st.button(
        "✦ Process Voice Request",
        use_container_width=True
    ):

        if voice_text.strip():

            prompt = f"""
You are Multimax Aura Voice Intelligence.

The user said:

{voice_text}

Respond naturally like a voice assistant.

Keep the answer conversational,
clear and useful.
"""

            with st.spinner(
                "Aura is listening..."
            ):

                answer = ask_gemini(
                    prompt
                )

            st.markdown(
                '<div class="section-title">Aura Voice Response</div>',
                unsafe_allow_html=True
            )

            st.markdown(answer)

        else:

            st.warning(
                "Please enter a voice transcript."
            )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
<div class="footer">
    ✦ MULTIMAX AURA
    &nbsp;•&nbsp;
    Multimodal Intelligence Workspace
    <br><br>
    Text · Documents · Vision · Voice
</div>
""",
    unsafe_allow_html=True
)