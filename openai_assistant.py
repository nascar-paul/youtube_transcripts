import openai

def get_api_key():
    """
    Prompts the user to enter their OpenAI API key.
    :return: The OpenAI API key as a string.
    """
    api_key = input("Please enter your OpenAI API key: ").strip()
    return api_key

def initialize_openai_client(api_key):
    """
    Initializes the OpenAI client with the given API key.
    :param api_key: Your OpenAI API key.
    """
    openai.api_key = api_key

def interact_with_custom_assistant(text, assistant_id="asst_HaVkg1QI1bmlLxMFeJlswWrO"):
    """
    Sends text to the specified custom assistant and returns the response.
    :param text: The text to send to the custom assistant.
    :param assistant_id: The unique ID of the custom assistant.
    :return: The assistant's response as a string.
    """
    try:
        response = openai.ChatCompletion.create(
            model=assistant_id,  # Note: OpenAI has replaced 'model' with 'assistant_id' in some API versions
            messages=[
                {"role": "user", "content": text}
            ]
        )
        # Assuming the response contains a single message and correctly extracting it
        assistant_response = response.choices[0].message['content'].strip()
        return assistant_response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
