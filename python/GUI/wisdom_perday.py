import requests
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from threading import Thread

# Fetch a random quote from the API
def fetch_quote():
    try:
        # Replace the URL with the actual URL of your quote API
        response = requests.get("https://api.quotable.io/quotes/random?limit=1")
        if response.status_code == 200:
            data = response.json()
            quote = data[0]['content']
            author = data[0]['author']
            return quote, author
        else:
            messagebox.showerror("Error", "Failed to fetch quote from the API.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Update the quote and author labels
def update_quote():
    quote, author = fetch_quote()
    quote_text.set(f"\"{quote}\"")
    author_text.set(f"- {author}")

# Fetch a quote in a separate thread
def fetch_quote_thread():
    Thread(target=update_quote).start()

# 初始化 ttkbootstrap 窗口
app = ttk.Window(themename="litera")
app.geometry('400x300')
app.title('Random Quote Generator')

# 用于动态文本更新的 StringVar
quote_text = ttk.StringVar()
author_text = ttk.StringVar()

# 小工具
quote_label = ttk.Label(app, textvariable=quote_text, wraplength=400, anchor=CENTER, font=("Arial", 12))
quote_label.pack(pady=20)

author_label = ttk.Label(app, textvariable=author_text, font=("Arial", 10, "italic"))
author_label.pack(pady=(0, 20))

refresh_button = ttk.Button(app, text="Refresh Quote", command=fetch_quote_thread)
refresh_button.pack(pady=20)

# Fetch a quote when the app starts
fetch_quote_thread()

# Start the GUI event loop
app.mainloop()