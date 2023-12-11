import tkinter as tk
from tkinter import filedialog
import codecs

# Функція для дешифрування шифру Цезаря
def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                # Дешифруємо символ нижнього регістру
                decrypted_text += chr((ord(char) - shift - ord('a') + 26) % 26 + ord('a'))
            else:
                # Дешифруємо символ верхнього регістру
                decrypted_text += chr((ord(char) - shift - ord('A') + 26) % 26 + ord('A'))
        else:
            # Якщо символ не є літерою, залишаємо його без змін
            decrypted_text += char
    return decrypted_text

# Функція для відкриття файлу та дешифрування тексту
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            # Відкриваємо файл та читаємо зашифрований текст
            with codecs.open(file_path, 'r', encoding='utf-8') as file:
                ciphertext = file.read()
                # Очищаємо відображення попереднього тексту та вставляємо дешифрований текст
                entry.delete(1.0, tk.END)
                entry.insert(tk.END, caesar_decrypt(ciphertext, shift_value.get()))
        except Exception as e:
            # Виводимо повідомлення про помилку, якщо виникла проблема з читанням файлу
            tk.messagebox.showerror("Помилка", f"Виникла помилка: {str(e)}")

# Функція для збереження дешифрованого тексту у файл
def save_file():
    decrypted_text = entry.get(1.0, tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            # Зберігаємо дешифрований текст у новий файл
            with codecs.open(file_path, 'w', encoding='utf-8') as file:
                file.write(decrypted_text)
            # Виводимо повідомлення про успішне збереження
            tk.messagebox.showinfo("Успішно", "Файл успішно збережено.")
        except Exception as e:
            # Виводимо повідомлення про помилку, якщо виникла проблема зі збереженням файлу
            tk.messagebox.showerror("Помилка", f"Виникла помилка: {str(e)}")

# Функція для відображення інформації про автора
def show_about():
    tk.messagebox.showinfo("Інформація про автора", "Програма для дешифрування шифру Цезаря\n\nАвтор: Гнєдова Владислава")

# Основне вікно програми
root = tk.Tk()
root.title("Дешифрування шифру Цезаря")

# Меню
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Відкрити", command=open_file)
file_menu.add_command(label="Зберегти", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Вийти", command=root.destroy)

help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Довідка", menu=help_menu)
help_menu.add_command(label="Інформація про автора", command=show_about)

# Введення значення зсуву
shift_label = tk.Label(root, text="Зсув:")
shift_label.pack()

shift_value = tk.IntVar()
shift_entry = tk.Entry(root, textvariable=shift_value)
shift_entry.pack()

# Введення для відображення дешифрованого тексту
entry = tk.Text(root, height=10, width=50)
entry.pack()

# Запуск головного циклу подій
root.mainloop()