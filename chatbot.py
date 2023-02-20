import openai
import os
import threading
import json

openai.api_key = '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'

def chatbot(entrada: str):
    entrada_de_dados = str(entrada).strip()
    try:
        response = openai.Completion.create(
            model = "text-davinci-002",
            prompt = entrada_de_dados,
            temperature =0.7,
            max_tokens = 200,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        return response["choices"][0]["text"]
    except Exception as err:
        print(err)
        return False
