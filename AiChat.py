import tkinter as tk
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

# generar respuesta
def generar_respuesta(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    mensaje = completions.choices[0].text
    return mensaje

# interface
def display_response():
    input_text = input_field.get()
    response = generar_respuesta(input_text)
    output_field.config(state='normal')
    output_field.delete(1.0, tk.END)
    output_field.insert(tk.END, response)
    output_field.config(state='disabled')

# ventana principal
root = tk.Tk()
root.title("AiChat")
root.geometry("600x700")

input_field = tk.Entry(root, font=("Arial", 14), width=50)
input_field.pack(pady=20)

submit_button = tk.Button(root, text="Enviar", font=("Arial", 14), command=display_response)
submit_button.pack(pady=10)

output_field = tk.Text(root, font=("Arial", 14), state='disabled')
output_field.pack(pady=30)


root.mainloop()