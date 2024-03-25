from openai import OpenAI

client = OpenAI(api_key='')

def bodyGenerator(description, genres):
    messages = [
        {
            "role": "system", "content": "Sei un assistente che genera una storia data una descrizione e un set di generi"
        },
        {
            "role": "system", "content": "I generi sono: " + ', '.join(genres)
        },
        {
            "role": "user", "content": description
        }
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=1024
        )

        return response.choices[0].message.content
    except Exception as e:
        print(f'Error openai: {e}')