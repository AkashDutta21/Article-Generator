def generate_output(transcript):
    import os
    from groq import Groq

    #Variables
    model_name = "llama3-70b-8192"
    word_count = 300
    # file_name = "Output.txt"

    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
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

    chat_completion2 = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"{response}, split this article into 4 parapraphs",
            }
        ],
        model=f"{model_name}",
    )
    response2 = chat_completion2.choices[0].message.content
    return response

if __name__ == "__main__":
    generate_output()