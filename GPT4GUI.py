import tkinter as tk
from tkinter import scrolledtext, font
import openai
import threading

def send_request(event=None):
    def api_call():
        user_input = user_input_box.get("1.0", tk.END).strip()
        user_input_box.delete("1.0", tk.END)  # Clear input box after sending
        if user_input.lower() == 'exit':
            root.quit()
        else:
            try:
                loading_label.config(text="Asking ChatGPT4 now...")  # Show loading indicator
                response = openai.ChatCompletion.create(
                    model="gpt-4-1106-preview",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": user_input}
                    ],
                    max_tokens=4096
                )
                output_box.configure(state='normal')
                output_box.insert(tk.END, "You: " + user_input + "\nGPT-4: " + response['choices'][0]['message']['content'] + "\n\n")
                output_box.configure(state='disabled')
                output_box.yview(tk.END)  # Auto-scroll to the bottom
                loading_label.config(text="")  # Hide loading indicator
            except Exception as e:
                output_box.configure(state='normal')
                output_box.insert(tk.END, "Error: " + str(e) + "\n")
                output_box.configure(state='disabled')
                loading_label.config(text="")  # Hide loading indicator

    threading.Thread(target=api_call).start()  # Run the API call in a separate thread

# Set your OpenAI API key here
openai.api_key = ''

# Creating main window
root = tk.Tk()
root.title("GPT-4 GUI")
root.geometry("1500x1000")
root.configure(bg="#f0f0f0")  # Light grey background

# Define fonts
input_font = font.Font(family="Times New Roman", size=14)
output_font = font.Font(family="Times New Roman", size=14)

# Creating a frame for the input box, send button, and loading label
input_frame = tk.Frame(root)
input_frame.pack(padx=10, pady=5, fill='both', expand=True)

# Creating a text box for user input
user_input_box = scrolledtext.ScrolledText(input_frame, height=4, width=70, font=input_font, bg="#7FFFD4")  # Aquamarine background
user_input_box.pack(side='left', fill='both', expand=True)
user_input_box.bind("<Return>", send_request)  # Bind Enter key to send_request

# Button to send request
send_button = tk.Button(input_frame, text="Send", command=send_request, bg="#4CAF50", fg="white", padx=10, pady=5)
send_button.pack(side='right', padx=10)
send_button.bind("<Enter>", lambda e: e.widget.config(bg="#45a049"))  # Darker shade on hover
send_button.bind("<Leave>", lambda e: e.widget.config(bg="#4CAF50"))

# Label for loading indicator
loading_label = tk.Label(input_frame, text="", font=("Helvetica", 10))
loading_label.pack(side='right')

# Text box for output
output_box = scrolledtext.ScrolledText(root, height=15, width=100, font=output_font, bg="#ADD8E6")  # Light blue background
output_box.pack(padx=10, pady=5, fill='both', expand=True)
output_box.configure(state='disabled')  # Make the output box read-only

# Start the GUI event loop
root.mainloop()
