import tkinter as tk
from tkinter import filedialog, ttk

from markovka.markov import (
    generate_text_backoff,
    get_tables,
)
from markovka.utils import clean_text, get_book_text, remove_header


def main():
    max_n = 3
    tables = None
    root = tk.Tk()
    root.title("markovka")
    title_label = ttk.Label(root, text="Markovka: An n-gram/markov text generator")
    title_label.pack(padx=10, pady=10)
    output_box = tk.Text(root, width=60, height=15)
    output_box.pack(padx=10, pady=10)

    def generate():
        if tables is None:
            output_box.delete("1.0", "end")
            output_box.insert("end", "Choose a book first!")
            return
        text, counts = generate_text_backoff(tables, max_n, 30)
        output_box.delete("1.0", "end")
        output_box.insert("end", text)

    def choose_book():
        nonlocal tables
        path = filedialog.askopenfilename()
        if not path:
            return
        book_text = get_book_text(path)
        no_headered = remove_header(book_text)
        cleaned = clean_text(no_headered)
        words = cleaned.split()
        tables = get_tables(words, max_n)
        output_box.delete("1.0", "end")
        output_box.insert("end", path)

    choose_button = ttk.Button(root, text="Choose book...", command=choose_book)
    button = ttk.Button(root, text="Generate", command=generate)
    button.pack(padx=10, pady=10)
    choose_button.pack()
    root.mainloop()


if __name__ == "__main__":
    main()
