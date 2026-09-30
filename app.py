import streamlit as st

from vector_store import search_vector_store
from llm import generate_answer


# ============================================================
# Page configuration
# ============================================================

st.set_page_config(
    page_title="Company Document RAG",
    page_icon="📚",
    layout="wide"
)


# ============================================================
# Title
# ============================================================

st.title("📚 Company Document RAG Assistant")

st.write(
    "Ask questions about the company policies and employee handbook."
)


# ============================================================
# Question input
# ============================================================

question = st.text_input(
    "Enter your question:",
    placeholder="Example: What happens if an employee is absent?"
)


# ============================================================
# Ask button
# ============================================================

if st.button("🔍 Ask Question"):

    if not question.strip():

        st.warning("Please enter a question.")

    else:

        with st.spinner("Searching company documents..."):

            retrieved_chunks = search_vector_store(
                question,
                top_k=3
            )

        with st.spinner("Generating answer..."):

            result = generate_answer(
                question,
                retrieved_chunks
            )


        # ====================================================
        # Display answer
        # ====================================================

        st.subheader("💡 Answer")

        st.write(result["answer"])


        # ====================================================
        # Display sources
        # ====================================================

        st.subheader("📄 Sources")

        for source in result["sources"]:

            st.write(
                f"**{source['source']}** — "
                f"Page {source['page']}"
            )


        # ====================================================
        # Display retrieved snippets
        # ====================================================

        st.subheader("🔎 Retrieved Document Snippets")

        for i, chunk in enumerate(
            retrieved_chunks,
            start=1
        ):

            with st.expander(
                f"Result {i} — "
                f"{chunk['source']} "
                f"(Page {chunk['page']})"
            ):

                st.write(chunk["text"])

                st.caption(
                    f"FAISS distance: "
                    f"{chunk['distance']:.4f}"
                )