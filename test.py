import tkinter as tk

def button_click(symbol):
    current = display_var.get()
    if current == "Error":
        display_var.set("")  # エラーの場合は画面をクリア
        current=""
    if symbol == "=":
        try:
            result = eval(current)
            display_var.set(str(result))
        except:
            display_var.set("Error")
    elif symbol == "C":
        display_var.set("")  # 入力をクリア
    else:
        display_var.set(current + symbol)

root = tk.Tk()
root.title("電卓")

display_var = tk.StringVar()
display = tk.Entry(root, textvariable=display_var, font=("Arial", 18), bd=10, insertwidth=4, width=14, justify="right")
display.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 18), padx=20, pady=20,
                       command=lambda symbol=text: button_click(symbol))
    button.grid(row=row, column=col)

root.mainloop()
