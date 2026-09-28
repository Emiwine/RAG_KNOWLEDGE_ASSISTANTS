
import requests
import streamlit as st


# -----------------------------
# Application configuration
# -----------------------------

API_URL = "http://127.0.0.1:8000/api/v1/ask"

st.set_page_config(
    page_title="RAG Knowledge Assistant",
    page_icon="📚",
    layout="centered",
)


# -----------------------------
# Page header
# -----------------------------

st.title("📚 RAG Knowledge Assistant")

st.caption(
    "Ask questions about your documents and get "
    "answers with supporting sources."
)

with st.sidebar:
    st.header("About")
    st.write(
        "This assistant uses Retrieval-Augmented Generation "
        "(RAG) to answer questions from the indexed documents."
    )

    st.divider()

    st.subheader("Backend")
    st.code(API_URL, language="text")

    if st.button("Clear chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# -----------------------------
# Initialize chat history
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# -----------------------------
# Display previous messages
# -----------------------------

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        # Show sources for assistant responses
        if message["role"] == "assistant":
            sources = message.get("sources", [])

            if sources:
                with st.expander("View sources"):
                    for index, source in enumerate(sources, start=1):
                        st.markdown(f"**Source {index}**")

                        page = source.get("page")
                        filename = source.get("source")

                        if page is not None:
                            st.write(f"Page: {page}")

                        if filename:
                            st.write(f"Document: {filename}")

                        st.divider()


# -----------------------------
# Send question to FastAPI
# -----------------------------

question = st.chat_input(
    "Ask a question about your documents...",
    max_chars=2000,
)

if question:
    # Display and store the user's message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # Call the FastAPI backend
    with st.chat_message("assistant"):
        try:
            with st.spinner("Searching documents and generating an answer..."):
                response = requests.post(
                    API_URL,
                    json={"question": question},
                    timeout=120,
                )

            if response.status_code == 200:
                result = response.json()

                answer = result.get(
                    "answer",
                    "The API returned no answer.",
                )

                sources = result.get("sources", [])

                st.markdown(answer)

                if sources:
                    with st.expander("View sources"):
                        for index, source in enumerate(sources, start=1):
                            st.markdown(f"**Source {index}**")

                            page = source.get("page")
                            filename = source.get("source")

                            if page is not None:
                                st.write(f"Page: {page}")

                            if filename:
                                st.write(f"Document: {filename}")

                            st.divider()

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer,
                        "sources": sources,
                    }
                )

            else:
                st.error(
                    f"The backend returned HTTP "
                    f"{response.status_code}."
                )

                # Show a validation message when FastAPI provides one
                try:
                    detail = response.json().get("detail")
                    if detail:
                        st.write(detail)
                except ValueError:
                    pass

        except requests.exceptions.Timeout:
            st.error(
                "The request timed out. The RAG pipeline may be taking "
                "too long. Please try again."
            )

        except requests.exceptions.ConnectionError:
            st.error(
                "Could not connect to FastAPI. Make sure the backend "
                "is running at http://127.0.0.1:8000."
            )

        except requests.exceptions.RequestException:
            st.error(
                "A network error occurred while contacting the backend."
            )

        except ValueError:
            st.error(
                "The backend returned an invalid JSON response."
            )