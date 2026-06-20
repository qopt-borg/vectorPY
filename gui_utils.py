import tkinter as tk
from tkinter import messagebox

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# =========================
# FUENTES GLOBALES
# =========================

FONT_TITULO = ("Arial", 24, "bold")
FONT_SUBTITULO = ("Arial", 16, "bold")
FONT_TEXTO = ("Arial", 13)
FONT_BOTON = ("Arial", 12)


# =========================
# LIMPIEZA DE VENTANA
# =========================

def gui_limpiar_ventana(root):
    for widget in root.winfo_children():
        if not isinstance(widget, tk.Menu):
            widget.destroy()


# =========================
# MENÚ
# =========================

def gui_mostrar_acerca_de():
    messagebox.showinfo(
        "Acerca de este proyecto",
        "Este es VECTOR 1.0, una suite para entrenar aritmética de vectores.\n\n"
        "Desarrollado por los integrantes del cuerpo académico de Ciencias "
        "Aplicadas a la Ingeniería de la Facultad de Ingeniería Mecánica y Eléctrica "
        "(Unidad Laguna) de la Universidad Autónoma de Coahuila."
    )


def gui_crear_menu(root):
    barra_menu = tk.Menu(root)

    menu_acerca = tk.Menu(barra_menu, tearoff=0)
    menu_acerca.add_command(
        label="Acerca de...",
        command=gui_mostrar_acerca_de
    )

    barra_menu.add_cascade(label="INFO", menu=menu_acerca)

    root.config(menu=barra_menu)


# =========================
# LATEX EN TKINTER
# =========================

def tk_color_to_hex(widget, color):
    r, g, b = widget.winfo_rgb(color)
    return f"#{r//256:02x}{g//256:02x}{b//256:02x}"

def gui_mostrar_expresion_latex(
    contenedor,
    expresion,
    fontsize=12,
    ancho=4,
    alto=0.45,
    pady=0
):
    bg_tk = contenedor.cget("bg")
    bg = tk_color_to_hex(contenedor, bg_tk)

    fig = Figure(
        figsize=(ancho, alto),
        dpi=100,
        facecolor=bg
    )

    ax = fig.add_subplot(111)
    ax.set_facecolor(bg)
    ax.axis("off")

    ax.text(
        0.5,
        0.5,
        expresion,
        fontsize=fontsize,
        ha="center",
        va="center"
    )

    fig.subplots_adjust(
        left=0,
        right=1,
        top=1,
        bottom=0
    )

    canvas = FigureCanvasTkAgg(fig, master=contenedor)
    canvas.draw()

    widget = canvas.get_tk_widget()
    widget.configure(
        bg=bg_tk,
        highlightthickness=0,
        borderwidth=0
    )
    widget.pack(pady=pady)

    return canvas


def gui_vector_latex(nombre, v):
    componentes = [
        (v[0], r"\mathbf{i}"),
        (v[1], r"\mathbf{j}"),
        (v[2], r"\mathbf{k}")
    ]

    expresion = ""

    for valor, base in componentes:
        if valor == 0:
            continue

        signo = " + " if valor > 0 else " - "
        coef = abs(valor)

        if coef == 1:
            termino = base
        else:
            termino = rf"{coef}{base}"

        if expresion == "":
            expresion = termino if valor > 0 else rf"-{termino}"
        else:
            expresion += signo + termino

    if expresion == "":
        expresion = r"\mathbf{0}"

    return rf"$\mathbf{{{nombre}}} = {expresion}$"