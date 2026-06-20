import tkinter as tk


def layout_inicio(root):
    root.geometry("900x700")
    root.resizable(False, False)

    contenedor = tk.Frame(root)
    contenedor.pack(fill="both", expand=True, padx=40, pady=40)

    titulo = tk.Frame(contenedor)
    menu = tk.Frame(contenedor)

    titulo.pack(fill="x", pady=20)
    menu.pack(expand=True)

    return titulo, menu


def layout_ejercicio(root):

    # Ventana principal
    root.geometry("900x700")
    root.resizable(False, False)

    # =========================
    # HEADER
    # =========================
    header = tk.Frame(
        root,
        width=880,
        height=80
    )

    header.pack(padx=10, pady=10)
    header.pack_propagate(False)

    # =========================
    # BODY
    # =========================
    body = tk.Frame(
        root,
        width=880,
        height=580
    )

    body.pack()
    body.pack_propagate(False)

    # =========================
    # COLUMNAS
    # =========================
    left_column = tk.Frame(
        body,
        width=400,
        height=580,
        bg="lightgray"
    )
    left_column.pack(side="left", padx=5)
    left_column.pack_propagate(False)

    right_column = tk.Frame(
        body,
        width=460,
        height=580,
        bg="lightgray"
    )
    right_column.pack(side="left", padx=5)
    right_column.pack_propagate(False)

    # =========================
    # CUADRANTES
    # =========================
    left1 = tk.Frame(
        left_column,
        width=400,
        height=450
    )

    left2 = tk.Frame(
        left_column,
        width=400,
        height=120
    )

    right1 = tk.Frame(
        right_column,
        width=460,
        height=235
    )

    right2 = tk.Frame(
        right_column,
        width=460,
        height=335
    )

    # Empaquetado
    left1.pack(padx=5, pady=5)
    left2.pack(padx=5, pady=5)

    right1.pack(padx=5, pady=5)
    right2.pack(padx=5, pady=5)

    # Desactivar autoajuste
    left1.pack_propagate(False)
    left2.pack_propagate(False)

    right1.pack_propagate(False)
    right2.pack_propagate(False)

    return header, left1, left2, right1, right2
