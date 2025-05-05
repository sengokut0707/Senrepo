#!/usr/bin/env python3

import tkinter as tk
import pyperclip
import sys, time


def main():
    def get_text(event=None):
        result = text.get()
        pyperclip.copy(result)
        print(f"copy \"{result}\"")
        root.destroy()

    def close_window(event=None):
        root.destroy()

    root = tk.Tk()
    root.geometry("600x60")

    text = tk.Entry(root, width=40, font=("",15))
    text.focus_set()
    text.pack(side=tk.LEFT, expand=True)
    button = tk.Button(root, text='Enter', font=("",12), command=get_text)
    button.pack(side=tk.LEFT, expand=True)

    root.bind("<Return>", get_text)
    root.bind("<Escape>", close_window)
    root.mainloop()

main()
