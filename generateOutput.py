def generate_output(transcript, model_name, word_count):
    import os
    from groq import Groq
    import streamlit as st
    #Variables
    # model_name = "llama3-70b-8192"
    word_count = 300

    client = Groq(
        api_key=st.secrets["GROQ_API_KEY"],
    )

    if transcript is None:
        return None

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"{transcript}, generate a {word_count} word article from the above transcript",
            }
        ],
        model=f"{model_name}",
    )

    response = chat_completion.choices[0].message.content

    return response

if __name__ == "__main__":
    generate_output()