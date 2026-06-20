import tkinter as tk

from screens import s_mostrar_inicio
from gui_utils import gui_crear_menu


def main():
    root = tk.Tk()

    root.title("VECTOR")

    # Menú superior
    gui_crear_menu(root)

    # Pantalla inicial
    s_mostrar_inicio(root)

    root.mainloop()


if __name__ == "__main__":
    main()