import tkinter as tk
import subprocess


# Function to send the user input to the model and get a response
def send_prompt(event=None):
    user_input = entry.get()
    if user_input.lower() == "exit":
        window.quit()  # Close the window if 'exit' is typed
    else:
        response = subprocess.check_output(["ollama", "run", "deepseek-r1:1.5b", user_input])
        chat_box.insert(tk.END, f"You: {user_input}\n")
        chat_box.insert(tk.END, f"Bot: {response.decode()}\n")
    entry.delete(0, tk.END)  # Clear the input field

# Initialize the main window
window = tk.Tk()
window.title("DeepSeek Chatbot")

# Create the chat box (Text widget)
chat_box = tk.Text(window, height=20, width=50)
chat_box.pack(padx=10, pady=10)

# Create the input field
entry = tk.Entry(window, width=50)
entry.pack(padx=10, pady=10)

# Bind the Enter key to the send_prompt function
entry.bind("<Return>", send_prompt)

# Run the Tkinter event loop
window.mainloop()
