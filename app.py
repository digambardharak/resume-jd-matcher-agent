import streamlit as st
from src.parser import extract_text_from_pdf
from src.llm_client import match_resume_to_jd
from src.agent import get_resources_for_missing_skills
from src.db import init_db, log_match
import tempfile

st.set_page_config(page_title="Resume-JD Matcher Agent")
init_db()

st.title("AI Resume-JD Matcher Agent")
st.write("Upload your resume and paste a job description to see how well they match.")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
jd_text = st.text_area("Paste the Job Description here", height=250)

if st.button("Analyze Match"):
    if uploaded_file is None or not jd_text.strip():
        st.warning("Please upload a resume and paste a job description.")
    else:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        with st.spinner("Analyzing with Gemini..."):
            resume_text = extract_text_from_pdf(tmp_path)
            result = match_resume_to_jd(resume_text, jd_text)

        if result:
            st.subheader(f"Match Score: {result['match_score']}/100")
            st.progress(result['match_score'] / 100)

            col1, col2 = st.columns(2)
            with col1:
                st.markdown("### Matched Skills")
                for skill in result['matched_skills']:
                    st.markdown(f"- {skill}")
            with col2:
                st.markdown("### Missing Skills")
                for skill in result['missing_skills']:
                    st.markdown(f"- {skill}")

            st.markdown("### Summary")
            st.write(result['summary'])

            log_match(uploaded_file.name, result)

            if result['missing_skills']:
                with st.spinner("Finding learning resources for your skill gaps..."):
                    resources = get_resources_for_missing_skills(result['missing_skills'])

                st.markdown("### Suggested Resources to Close Your Gaps")
                for skill, links in resources.items():
                    st.markdown(f"**{skill}**")
                    for link in links:
                        st.markdown(f"- [{link['title']}]({link['url']})")
        else:
            st.error("Something went wrong getting a response. Please try again.")