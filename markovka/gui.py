import tkinter as tk
from pathlib import Path
from tkinter import filedialog, ttk

from markovka.chat import load_chat_messages
from markovka.markov import (
    generate_text_backoff,
    get_tables_from_texts,
    normalize,
)
from markovka.utils import clean_text, get_book_text, remove_header


def main():
    max_n = 3
    tables = None
    source_name = "Bot"
    texts = list()
    source_names = list()
    root = tk.Tk()
    root.title("markovka")
    title_label = ttk.Label(root, text="Markovka: An n-gram/markov text generator")
    sender_label = ttk.Label(root, text="Sender name (for chats):")
    sender_entry = ttk.Entry(root, width=30)
    sentence_length_label = ttk.Label(root, text="Set ammount of words in text")
    title_label.pack(padx=10, pady=10)
    output_box = tk.Text(root, width=60, height=15)
    output_box.pack(padx=10, pady=10)

    def generate():
        if tables is None:
            output_box.delete("1.0", "end")
            output_box.insert("end", "Choose a book first!")
            return
        length = int(length_box.get())
        text, counts = generate_text_backoff(tables, max_n, length)
        output_box.delete("1.0", "end")
        output_box.insert("end", text)

    def choose_book():
        nonlocal tables, source_name
        path = filedialog.askopenfilename()
        if not path:
            return
        book_text = get_book_text(path)
        no_headered = remove_header(book_text)
        cleaned = clean_text(no_headered)
        words = cleaned.split()
        texts.append(words)
        tables = get_tables_from_texts(texts, max_n)
        output_box.delete("1.0", "end")
        output_box.insert("end", f"Loaded {source_name}!")

    def choose_chat():
        nonlocal tables, max_n, source_name
        sender = sender_entry.get().strip()
        if not sender:
            output_box.delete("1.0", "end")
            output_box.insert("end", "Type the sender name first!")
            return
        path = filedialog.askopenfilename()
        if not path:
            return
        messages = load_chat_messages(path, sender)
        if not messages:
            output_box.delete("1.0", "end")
            output_box.insert("end", f"No messages from {sender}, check the spelling")
            return
        for message in messages:
            texts.append(message.split())
        max_n = 2
        if sender not in source_names:
            source_names.append(sender)
        source_name = "+".join(source_names)
        tables = get_tables_from_texts(texts, max_n)
        output_box.delete("1.0", "end")
        output_box.insert("end", f"Loaded {len(messages)} messages from {sender}!")

    def open_talk_window():
        talk_window = tk.Toplevel(root)
        talk_window.title("markovka- talk")
        talk_log = tk.Text(
            talk_window,
            width=60,
            height=20,
            background="#C0C0C0",
            foreground="black",
            font=("Courier", 12),
        )
        talk_log.tag_configure(
            "you_name", foreground="blue", font=("Courier", 12, "bold")
        )
        talk_log.tag_configure(
            "bot_name", foreground="red", font=("Courier", 12, "bold")
        )
        talk_entry = ttk.Entry(talk_window, width=60)
        talk_log.pack()
        talk_entry.pack()

        def talk(event=None):
            user_text = talk_entry.get().strip()
            if not user_text:
                return
            talk_log.insert("end", "You: ", "you_name")
            talk_log.insert("end", f"{user_text}\n")
            talk_entry.delete(0, "end")
            if tables is None:
                talk_log.insert("end", f"Load a book or chat first!\n")
                return
            known = set()
            for key in tables[max_n]:
                known.add(normalize(key[0]))
            candidates = list()
            for word in user_text.split():
                if normalize(word) in known:
                    candidates.append(word)
            if not candidates:
                start = None
            else:
                start = max(candidates, key=len)
            text, counts = generate_text_backoff(
                tables,
                max_n,
                int(length_box.get()),
                start_word=start,
            )
            talk_log.insert("end", f"{source_name}: ", "bot_name")
            talk_log.insert("end", f"{text}\n")
            talk_log.see("end")

        send_button = ttk.Button(talk_window, text="Send", command=talk)
        send_button.pack()
        talk_entry.bind("<Return>", talk)

    choose_button = ttk.Button(root, text="Choose book...", command=choose_book)
    chat_button = ttk.Button(root, text="Choose chat...", command=choose_chat)
    button = ttk.Button(root, text="Generate", command=generate)
    talk_button = ttk.Button(root, text="Talk...", command=open_talk_window)
    choose_button.pack()
    sender_label.pack()
    sender_entry.pack()
    chat_button.pack()
    length_box = ttk.Spinbox(root, from_=5, to=300)
    length_box.set(30)
    sentence_length_label.pack()
    length_box.pack()
    button.pack(padx=10, pady=10)
    talk_button.pack()
    root.mainloop()


if __name__ == "__main__":
    main()
