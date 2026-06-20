import tkinter as tk
from gui_utils import *
from mathematical_functions import *
from layout import *

estadisticas = {
    "totales": 0,
    "correctos": 0,
    "incorrectos": 0
}

def s_mostrar_inicio(root):

    gui_limpiar_ventana(root)

    titulo_frame, menu_frame= layout_inicio(root)

    titulo = tk.Label(
        titulo_frame,
        text="VECTOR",
        font=FONT_TITULO
    )

    titulo.pack(pady=(20, 5))

    subtitulo = tk.Label(
        titulo_frame,
        text="Suite de entrenamiento de aritmética vectorial",
        font=FONT_SUBTITULO
    )

    subtitulo.pack(pady=5)

    instrucciones = tk.Label(
        titulo_frame,
        text="Seleccione el área que desea reforzar",
        font=FONT_TEXTO
    )

    instrucciones.pack(pady=(10, 20))

    botones = [
        ("Sumas", s_mostrar_sumas),
        ("Restas", s_mostrar_restas),
        ("Norma de un vector", s_mostrar_norma),
        ("Producto escalar", s_mostrar_producto_escalar),
        ("Ángulo entre vectores", s_mostrar_angulo),
        ("Producto vectorial", s_mostrar_producto_vectorial),
    ]

    for texto, funcion in botones:

        boton = tk.Button(
            menu_frame,
            text=texto,
            font=FONT_BOTON,
            width=28,
            height=2,
            command=lambda f=funcion: f(root)
        )

        boton.pack(pady=8)

def s_mostrar_sumas(root):
    gui_limpiar_ventana(root)

    header, left1, left2, right1, right2 = layout_ejercicio(root)

    A = random_vector()
    B = random_vector()
    resultado_correcto = add(A, B)

    # =========================
    # HEADER
    # =========================

    titulo = tk.Label(
        header,
        text="Suma de vectores",
        font=FONT_TITULO
    )
    titulo.pack(expand=True)

    # =========================
    # LEFT1: EXPLICACIÓN
    # =========================

    contenido_left1 = tk.Frame(left1)
    contenido_left1.pack(expand=True)

    texto1 = tk.Label(
        contenido_left1,
        text="Consideremos los siguientes dos vectores de tres dimensiones:",
        font=FONT_TEXTO,
        wraplength=350,
        justify="left"
    )
    texto1.pack(pady=10)

    gui_mostrar_expresion_latex(
        contenido_left1,
        r"$\mathbf{A}=A_x \mathbf{i} + A_y \mathbf{j}+ A_z \mathbf{k},$",
        fontsize=12, ancho=6, alto=0.4, pady=0
    )

    gui_mostrar_expresion_latex(
        contenido_left1,
        r"$\mathbf{B}=B_x \mathbf{i} + B_y \mathbf{j}+ B_z \mathbf{k}.$",
        fontsize=12, ancho=6, alto=0.4, pady=0
    )

    texto2 = tk.Label(
        contenido_left1,
        text="La suma de vectores se calcula componente a componente:",
        font=FONT_TEXTO,
        wraplength=350,
        justify="left"
    )
    texto2.pack(pady=10)

    gui_mostrar_expresion_latex(
        contenido_left1,
        r"$\mathbf{A}+\mathbf{B}=(A_x+B_x)\mathbf{i}+(A_y+B_y)\mathbf{j}+(A_z+B_z)\mathbf{k}.$",
        fontsize=12, ancho=6, alto=0.4, pady=0
    )

    texto3 = tk.Label(
        contenido_left1,
        text="El resultado es un nuevo vector.",
        font=FONT_TEXTO,
        wraplength=350,
        justify="left"
    )
    texto3.pack(pady=10)

    # =========================
    # LEFT2: ESTADÍSTICAS
    # =========================

    contenido_left2 = tk.Frame(left2)
    contenido_left2.pack(expand=True)

    estadisticas_label = tk.Label(
        contenido_left2,
        text=(
            f"Totales: {estadisticas['totales']} | "
            f"Correctos: {estadisticas['correctos']} | "
            f"Incorrectos: {estadisticas['incorrectos']}"
        ),
        font=FONT_TEXTO,
        justify="center"
    )
    estadisticas_label.pack(pady=5)

    volver_btn = tk.Button(
        contenido_left2,
        text="Volver al inicio",
        font=FONT_BOTON,
        command=lambda: s_mostrar_inicio(root)
    )
    volver_btn.pack(pady=5)

    # =========================
    # RIGHT1: EJERCICIO
    # =========================

    contenido_right1 = tk.Frame(right1)
    contenido_right1.pack(expand=True)

    texto_ejercicio = tk.Label(
        contenido_right1,
        text="Calcule la suma de vectores:",
        font=FONT_SUBTITULO
    )
    texto_ejercicio.pack(pady=10)

    expresion_vectores = (
        gui_vector_latex("A", A)[1:-1]
        + r"\qquad\qquad"
        + gui_vector_latex("B", B)[1:-1]
    )

    gui_mostrar_expresion_latex(
        contenido_right1,
        f"${expresion_vectores}$",
        fontsize=12, ancho=6, alto=0.45, pady=0
    )

    # Tres campos: i, j, k
    campos_frame = tk.Frame(contenido_right1)
    campos_frame.pack(pady=(10, 5))

    for col, label in enumerate(["i", "+j", "+k"]):
        tk.Label(
            campos_frame,
            text=label,
            font=FONT_TEXTO
        ).grid(row=0, column=col * 2, padx=(10, 2))

    entry_i = tk.Entry(campos_frame, font=FONT_TEXTO, justify="center", width=6)
    entry_j = tk.Entry(campos_frame, font=FONT_TEXTO, justify="center", width=6)
    entry_k = tk.Entry(campos_frame, font=FONT_TEXTO, justify="center", width=6)

    entry_i.grid(row=0, column=1, padx=(0, 10))
    entry_j.grid(row=0, column=3, padx=(0, 10))
    entry_k.grid(row=0, column=5, padx=(0, 10))

    # =========================
    # RIGHT2: RETROALIMENTACIÓN
    # =========================

    titulo_retro = tk.Label(
        right2,
        text="Retroalimentación:",
        font=("Arial", 12, "bold"),
        anchor="w"
    )
    titulo_retro.pack(anchor="w", padx=10, pady=(10, 5))

    retro_text = tk.Text(
        right2,
        width=50,
        height=10,
        wrap="word",
        font=("Arial", 12),
        relief="flat"
    )
    retro_text.pack(fill="both", expand=True, padx=10, pady=(0, 10))

    retro_text.tag_config("correcto", foreground="green")
    retro_text.tag_config("incorrecto", foreground="red")
    retro_text.tag_config("error", foreground="orange")
    retro_text.tag_config("normal", foreground="black")
    retro_text.config(state="disabled")

    # =========================
    # LÓGICA DE VERIFICACIÓN
    # =========================

    def formatear_vector(i, j, k):
        return f"{i}i {j:+d}j {k:+d}k"

    def verificar():
        try:
            resp = [int(entry_i.get()), int(entry_j.get()), int(entry_k.get())]

            ri = int(resultado_correcto[0])
            rj = int(resultado_correcto[1])
            rk = int(resultado_correcto[2])

            desarrollo = (
                f"A + B = (Ax+Bx)i + (Ay+By)j + (Az+Bz)k\n\n"
                f"Componente i: {A[0]} + {B[0]} = {ri}\n\n"
                f"Componente j: {A[1]} + {B[1]} = {rj}\n\n"
                f"Componente k: {A[2]} + {B[2]} = {rk}\n\n"
                f"A + B = {formatear_vector(ri, rj, rk)}"
            )

            estadisticas["totales"] += 1
            retro_text.config(state="normal")
            retro_text.delete("1.0", tk.END)

            if resp == [ri, rj, rk]:
                estadisticas["correctos"] += 1
                retro_text.insert(tk.END, "Correcto\n\n", "correcto")
                retro_text.insert(tk.END, desarrollo, "normal")
            else:
                estadisticas["incorrectos"] += 1
                retro_text.insert(tk.END, "Incorrecto\n\n", "incorrecto")
                retro_text.insert(
                    tk.END,
                    f"La respuesta correcta es: {formatear_vector(ri, rj, rk)}\n\n",
                    "normal"
                )
                retro_text.insert(tk.END, desarrollo, "normal")

            retro_text.config(state="disabled")
            estadisticas_label.config(
                text=(
                    f"Totales: {estadisticas['totales']} | "
                    f"Correctos: {estadisticas['correctos']} | "
                    f"Incorrectos: {estadisticas['incorrectos']}"
                )
            )
            verificar_btn.config(state="disabled")

        except ValueError:
            retro_text.config(state="normal")
            retro_text.delete("1.0", tk.END)
            retro_text.insert(tk.END, "Ingrese valores enteros en los tres campos.", "error")
            retro_text.config(state="disabled")

    # =========================
    # BOTONES DEL EJERCICIO
    # =========================

    botones_frame = tk.Frame(right1)
    botones_frame.pack(pady=10)

    verificar_btn = tk.Button(
        botones_frame,
        text="Verificar",
        font=FONT_BOTON,
        width=12,
        command=verificar
    )
    verificar_btn.pack(side="left", padx=5)

    siguiente_btn = tk.Button(
        botones_frame,
        text="Siguiente",
        font=FONT_BOTON,
        width=12,
        command=lambda: s_mostrar_sumas(root)
    )
    siguiente_btn.pack(side="left", padx=5)

def s_mostrar_restas(root):
    gui_limpiar_ventana(root)

    header, left1, left2, right1, right2 = layout_ejercicio(root)

    A = random_vector()
    B = random_vector()
    resultado_correcto = diff(A, B)

    # =========================
    # HEADER
    # =========================

    titulo = tk.Label(
        header,
        text="Resta de vectores",
        font=FONT_TITULO
    )
    titulo.pack(expand=True)

    # =========================
    # LEFT1: EXPLICACIÓN
    # =========================

    contenido_left1 = tk.Frame(left1)
    contenido_left1.pack(expand=True)

    texto1 = tk.Label(
        contenido_left1,
        text="Consideremos los siguientes dos vectores de tres dimensiones:",
        font=FONT_TEXTO,
        wraplength=350,
        justify="left"
    )
    texto1.pack(pady=10)

    gui_mostrar_expresion_latex(
        contenido_left1,
        r"$\mathbf{A}=A_x \mathbf{i} + A_y \mathbf{j}+ A_z \mathbf{k},$",
        fontsize=12, ancho=6, alto=0.4, pady=0
    )

    gui_mostrar_expresion_latex(
        contenido_left1,
        r"$\mathbf{B}=B_x \mathbf{i} + B_y \mathbf{j}+ B_z \mathbf{k}.$",
        fontsize=12, ancho=6, alto=0.4, pady=0
    )

    texto2 = tk.Label(
        contenido_left1,
        text="La resta de vectores se calcula componente a componente:",
        font=FONT_TEXTO,
        wraplength=350,
        justify="left"
    )
    texto2.pack(pady=10)

    gui_mostrar_expresion_latex(
        contenido_left1,
        r"$\mathbf{A}-\mathbf{B}=(A_x-B_x)\mathbf{i}+(A_y-B_y)\mathbf{j}+(A_z-B_z)\mathbf{k}.$",
        fontsize=12, ancho=6, alto=0.4, pady=0
    )

    texto3 = tk.Label(
        contenido_left1,
        text="El resultado es un nuevo vector.",
        font=FONT_TEXTO,
        wraplength=350,
        justify="left"
    )
    texto3.pack(pady=10)

    # =========================
    # LEFT2: ESTADÍSTICAS
    # =========================

    contenido_left2 = tk.Frame(left2)
    contenido_left2.pack(expand=True)

    estadisticas_label = tk.Label(
        contenido_left2,
        text=(
            f"Totales: {estadisticas['totales']} | "
            f"Correctos: {estadisticas['correctos']} | "
            f"Incorrectos: {estadisticas['incorrectos']}"
        ),
        font=FONT_TEXTO,
        justify="center"
    )
    estadisticas_label.pack(pady=5)

    volver_btn = tk.Button(
        contenido_left2,
        text="Volver al inicio",
        font=FONT_BOTON,
        command=lambda: s_mostrar_inicio(root)
    )
    volver_btn.pack(pady=5)

    # =========================
    # RIGHT1: EJERCICIO
    # =========================

    contenido_right1 = tk.Frame(right1)
    contenido_right1.pack(expand=True)

    texto_ejercicio = tk.Label(
        contenido_right1,
        text="Calcule la resta de vectores:",
        font=FONT_SUBTITULO
    )
    texto_ejercicio.pack(pady=10)

    expresion_vectores = (
        gui_vector_latex("A", A)[1:-1]
        + r"\qquad\qquad"
        + gui_vector_latex("B", B)[1:-1]
    )

    gui_mostrar_expresion_latex(
        contenido_right1,
        f"${expresion_vectores}$",
        fontsize=12, ancho=6, alto=0.45, pady=0
    )

    # Tres campos: i, j, k
    campos_frame = tk.Frame(contenido_right1)
    campos_frame.pack(pady=(10, 5))

    for col, label in enumerate(["i", "+j", "+k"]):
        tk.Label(
            campos_frame,
            text=label,
            font=FONT_TEXTO
        ).grid(row=0, column=col * 2, padx=(10, 2))

    entry_i = tk.Entry(campos_frame, font=FONT_TEXTO, justify="center", width=6)
    entry_j = tk.Entry(campos_frame, font=FONT_TEXTO, justify="center", width=6)
    entry_k = tk.Entry(campos_frame, font=FONT_TEXTO, justify="center", width=6)

    entry_i.grid(row=0, column=1, padx=(0, 10))
    entry_j.grid(row=0, column=3, padx=(0, 10))
    entry_k.grid(row=0, column=5, padx=(0, 10))

    # =========================
    # RIGHT2: RETROALIMENTACIÓN
    # =========================

    titulo_retro = tk.Label(
        right2,
        text="Retroalimentación:",
        font=("Arial", 12, "bold"),
        anchor="w"
    )
    titulo_retro.pack(anchor="w", padx=10, pady=(10, 5))

    retro_text = tk.Text(
        right2,
        width=50,
        height=10,
        wrap="word",
        font=("Arial", 12),
        relief="flat"
    )
    retro_text.pack(fill="both", expand=True, padx=10, pady=(0, 10))

    retro_text.tag_config("correcto", foreground="green")
    retro_text.tag_config("incorrecto", foreground="red")
    retro_text.tag_config("error", foreground="orange")
    retro_text.tag_config("normal", foreground="black")
    retro_text.config(state="disabled")

    # =========================
    # LÓGICA DE VERIFICACIÓN
    # =========================
    def formatear_vector(i, j, k):
        return f"{i}i {j:+d}j {k:+d}k"

    def verificar():
        try:
            resp = [int(entry_i.get()), int(entry_j.get()), int(entry_k.get())]

            ri = int(resultado_correcto[0])
            rj = int(resultado_correcto[1])
            rk = int(resultado_correcto[2])

            desarrollo = (
                f"A - B = (Ax-Bx)i + (Ay-By)j + (Az-Bz)k\n\n"
                f"Componente i: {A[0]} - {B[0]} = {ri}\n\n"
                f"Componente j: {A[1]} - {B[1]} = {rj}\n\n"
                f"Componente k: {A[2]} - {B[2]} = {rk}\n\n"
                f"A + B = {formatear_vector(ri, rj, rk)}"
            )

            estadisticas["totales"] += 1
            retro_text.config(state="normal")
            retro_text.delete("1.0", tk.END)

            if resp == [ri, rj, rk]:
                estadisticas["correctos"] += 1
                retro_text.insert(tk.END, "Correcto\n\n", "correcto")
                retro_text.insert(tk.END, desarrollo, "normal")
            else:
                estadisticas["incorrectos"] += 1
                retro_text.insert(tk.END, "Incorrecto\n\n", "incorrecto")
                retro_text.insert(
                    tk.END,
                    f"La respuesta correcta es: {formatear_vector(ri, rj, rk)}\n\n",
                    "normal"
                )
                retro_text.insert(tk.END, desarrollo, "normal")

            retro_text.config(state="disabled")
            estadisticas_label.config(
                text=(
                    f"Totales: {estadisticas['totales']} | "
                    f"Correctos: {estadisticas['correctos']} | "
                    f"Incorrectos: {estadisticas['incorrectos']}"
                )
            )
            verificar_btn.config(state="disabled")

        except ValueError:
            retro_text.config(state="normal")
            retro_text.delete("1.0", tk.END)
            retro_text.insert(tk.END, "Ingrese valores enteros en los tres campos.", "error")
            retro_text.config(state="disabled")

    # =========================
    # BOTONES DEL EJERCICIO
    # =========================

    botones_frame = tk.Frame(right1)
    botones_frame.pack(pady=10)

    verificar_btn = tk.Button(
        botones_frame,
        text="Verificar",
        font=FONT_BOTON,
        width=12,
        command=verificar
    )
    verificar_btn.pack(side="left", padx=5)

    siguiente_btn = tk.Button(
        botones_frame,
        text="Siguiente",
        font=FONT_BOTON,
        width=12,
        command=lambda: s_mostrar_restas(root)
    )
    siguiente_btn.pack(side="left", padx=5)

def s_mostrar_producto_escalar(root):
    gui_limpiar_ventana(root)

    header, left1, left2, right1, right2 = layout_ejercicio(root)

    A = random_vector()
    B = random_vector()
    resultado_correcto = dot_product(A, B)

    # =========================
    # HEADER
    # =========================

    titulo = tk.Label(
        header,
        text="Producto escalar",
        font=FONT_TITULO
    )
    titulo.pack(expand=True)

    # =========================
    # LEFT1: EXPLICACIÓN
    # =========================

    contenido_left1 = tk.Frame(left1)
    contenido_left1.pack(expand=True)

    texto1 = tk.Label(
        contenido_left1,
        text="Consideremos los siguientes dos vectores de tres dimensiones:",
        font=FONT_TEXTO,
        wraplength=350,
        justify="left"
    )
    texto1.pack(pady=10)

    gui_mostrar_expresion_latex(
        contenido_left1,
        r"$\mathbf{A}=A_x \mathbf{i} + A_y \mathbf{j}+ A_z \mathbf{k},$",
        fontsize=12,
        ancho=6,
        alto=0.4,
        pady=0
    )

    gui_mostrar_expresion_latex(
        contenido_left1,
        r"$\mathbf{B}=B_x \mathbf{i} + B_y \mathbf{j}+ B_z \mathbf{k}.$",
        fontsize=12,
        ancho=6,
        alto=0.4,
        pady=0
    )

    texto2 = tk.Label(
        contenido_left1,
        text="En física, el producto escalar se calcula mediante la siguiente expresión:",
        font=FONT_TEXTO,
        wraplength=350,
        justify="left"
    )
    texto2.pack(pady=10)

    gui_mostrar_expresion_latex(
        contenido_left1,
        r"$\mathbf{A}\cdot\mathbf{B}=A_xB_x + A_yB_y + A_zB_z$.",
        fontsize=12,
        ancho=6,
        alto=0.4,
        pady=0
    )

    texto3 = tk.Label(
        contenido_left1,
        text="El resultado es un número real, es decir, un escalar.",
        font=FONT_TEXTO,
        wraplength=350,
        justify="left"
    )
    texto3.pack(pady=10)

    # =========================
    # LEFT2: ESTADÍSTICAS
    # =========================

    contenido_left2 = tk.Frame(left2)
    contenido_left2.pack(expand=True)

    estadisticas_label = tk.Label(
        contenido_left2,
        text=(
            f"Totales: {estadisticas['totales']} | "
            f"Correctos: {estadisticas['correctos']} | "
            f"Incorrectos: {estadisticas['incorrectos']}"
        ),
        font=FONT_TEXTO,
        justify="center"
    )
    estadisticas_label.pack(pady=5)

    volver_btn = tk.Button(
        contenido_left2,
        text="Volver al inicio",
        font=FONT_BOTON,
        command=lambda: s_mostrar_inicio(root)
    )
    volver_btn.pack(pady=5)

    # =========================
    # RIGHT1: EJERCICIO
    # =========================

    contenido_right1 = tk.Frame(right1)
    contenido_right1.pack(expand=True)

    texto2 = tk.Label(
        contenido_right1,
        text="Calcule el producto escalar:",
        font=FONT_SUBTITULO
    )
    texto2.pack(pady=10)

    expresion_vectores = (
            gui_vector_latex("A", A)[1:-1]
            + r"\qquad\qquad"
            + gui_vector_latex("B", B)[1:-1]
    )

    gui_mostrar_expresion_latex(
        contenido_right1,
        f"${expresion_vectores}$",
        fontsize=12,
        ancho=6,
        alto=0.45,
        pady=0
    )

    texto_respuesta = tk.Label(
        contenido_right1,
        text="Introduzca su respuesta numérica:",
        font=FONT_TEXTO
    )
    texto_respuesta.pack(pady=(10, 5))

    respuesta_entry = tk.Entry(
        contenido_right1,
        font=FONT_TEXTO,
        justify="center",
        width=12
    )
    respuesta_entry.pack(pady=5)

    # =========================
    # RIGHT2: RETROALIMENTACIÓN
    # =========================

    titulo_retro = tk.Label(
        right2,
        text="Retroalimentación:",
        font=("Arial", 12, "bold"),
        anchor="w"
    )
    titulo_retro.pack(anchor="w", padx=10, pady=(10, 5))

    retro_text = tk.Text(
        right2,
        width=50,
        height=10,
        wrap="word",
        font=("Arial", 12),
        relief="flat"
    )

    retro_text.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=(0, 10)
    )

    retro_text.tag_config("correcto", foreground="green")
    retro_text.tag_config("incorrecto", foreground="red")
    retro_text.tag_config("error", foreground="orange")
    retro_text.tag_config("normal", foreground="black")

    retro_text.config(state="disabled")

    # =========================
    # LÓGICA DE VERIFICACIÓN
    # =========================

    def verificar():
        try:
            respuesta_usuario = float(respuesta_entry.get())

            desarrollo = (
                f"A·B = AxBx + AyBy + AzBz\n\n"
                f"A·B = ({A[0]})({B[0]}) + ({A[1]})({B[1]}) + ({A[2]})({B[2]})\n\n"
                f"A·B = ({A[0] * B[0]}) + ({A[1] * B[1]}) + ({A[2] * B[2]})\n\n"
                f"A·B = {resultado_correcto}"
            )

            estadisticas["totales"] += 1

            retro_text.config(state="normal")
            retro_text.delete("1.0", tk.END)

            if abs(respuesta_usuario - resultado_correcto) <= 0.01:

                estadisticas["correctos"] += 1

                retro_text.insert(
                    tk.END,
                    "Correcto\n\n",
                    "correcto"
                )

                retro_text.insert(
                    tk.END,
                    desarrollo,
                    "normal"
                )

            else:

                estadisticas["incorrectos"] += 1

                retro_text.insert(
                    tk.END,
                    "Incorrecto\n\n",
                    "incorrecto"
                )

                retro_text.insert(
                    tk.END,
                    f"La respuesta correcta es: {resultado_correcto}\n\n",
                    "normal"
                )

                retro_text.insert(
                    tk.END,
                    desarrollo,
                    "normal"
                )

            retro_text.config(state="disabled")

            estadisticas_label.config(
                text=(
                    f"Totales: {estadisticas['totales']} | "
                    f"Correctos: {estadisticas['correctos']} | "
                    f"Incorrectos: {estadisticas['incorrectos']}"
                )
            )

            verificar_btn.config(state="disabled")

        except ValueError:

            retro_text.config(state="normal")
            retro_text.delete("1.0", tk.END)

            retro_text.insert(
                tk.END,
                "Ingrese un valor numérico válido.",
                "error"
            )

            retro_text.config(state="disabled")

    # =========================
    # BOTONES DEL EJERCICIO
    # =========================

    botones_frame = tk.Frame(right1)
    botones_frame.pack(pady=10)

    verificar_btn = tk.Button(
        botones_frame,
        text="Verificar",
        font=FONT_BOTON,
        width=12,
        command=verificar
    )
    verificar_btn.pack(side="left", padx=5)

    siguiente_btn = tk.Button(
        botones_frame,
        text="Siguiente",
        font=FONT_BOTON,
        width=12,
        command=lambda: s_mostrar_producto_escalar(root)
    )
    siguiente_btn.pack(side="left", padx=5)

def s_mostrar_producto_vectorial(root):
    gui_limpiar_ventana(root)

    header, left1, left2, right1, right2 = layout_ejercicio(root)

    A = random_vector()
    B = random_vector()
    resultado_correcto = cross_product(A, B)

    # =========================
    # HEADER
    # =========================

    titulo = tk.Label(
        header,
        text="Producto vectorial",
        font=FONT_TITULO
    )
    titulo.pack(expand=True)

    # =========================
    # LEFT1: EXPLICACIÓN
    # =========================

    contenido_left1 = tk.Frame(left1)
    contenido_left1.pack(fill="x", expand=True)

    texto1 = tk.Label(
        contenido_left1,
        text="Consideremos los siguientes dos vectores de tres dimensiones:",
        font=FONT_TEXTO,
        wraplength=350,
        justify="left",
        anchor="nw"
    )
    texto1.pack(fill="x", pady=10)

    gui_mostrar_expresion_latex(
        contenido_left1,
        r"$\mathbf{A}=A_x \mathbf{i} + A_y \mathbf{j}+ A_z \mathbf{k},$",
        fontsize=12, ancho=6, alto=0.4, pady=0
    )

    gui_mostrar_expresion_latex(
        contenido_left1,
        r"$\mathbf{B}=B_x \mathbf{i} + B_y \mathbf{j}+ B_z \mathbf{k}.$",
        fontsize=12, ancho=6, alto=0.4, pady=0
    )

    texto2 = tk.Label(
        contenido_left1,
        text="El producto vectorial se calcula como:",
        font=FONT_TEXTO,
        wraplength=350,
        justify="left",
        anchor="w"
    )
    texto2.pack(fill="x", pady=10)

    gui_mostrar_expresion_latex(
        contenido_left1,
        r"$\mathbf{A}\times\mathbf{B}= (A_yB_z-A_zB_y)\mathbf{i}-(A_xB_z-A_zB_x)\mathbf{j}$",
        fontsize=12,
        ancho=4,
        alto=0.4,
        pady=0
    )

    gui_mostrar_expresion_latex(
        contenido_left1,
        r"$+(A_xB_y-A_yB_x)\mathbf{k}$",
        fontsize=12,
        ancho=5,
        alto=0.4,
        pady=0
    )

    texto3 = tk.Label(
        contenido_left1,
        text="El resultado es un nuevo vector perpendicular a ambos.",
        font=FONT_TEXTO,
        wraplength=350,
        justify="left",
        anchor="sw"
    )
    texto3.pack(fill="x", pady=10)

    # =========================
    # LEFT2: ESTADÍSTICAS
    # =========================

    contenido_left2 = tk.Frame(left2)
    contenido_left2.pack(expand=True)

    estadisticas_label = tk.Label(
        contenido_left2,
        text=(
            f"Totales: {estadisticas['totales']} | "
            f"Correctos: {estadisticas['correctos']} | "
            f"Incorrectos: {estadisticas['incorrectos']}"
        ),
        font=FONT_TEXTO,
        justify="center"
    )
    estadisticas_label.pack(pady=5)

    volver_btn = tk.Button(
        contenido_left2,
        text="Volver al inicio",
        font=FONT_BOTON,
        command=lambda: s_mostrar_inicio(root)
    )
    volver_btn.pack(pady=5)

    # =========================
    # RIGHT1: EJERCICIO
    # =========================

    contenido_right1 = tk.Frame(right1)
    contenido_right1.pack(expand=True)

    texto_ejercicio = tk.Label(
        contenido_right1,
        text="Calcule el producto vectorial A × B:",
        font=FONT_SUBTITULO
    )
    texto_ejercicio.pack(pady=10)

    expresion_vectores = (
        gui_vector_latex("A", A)[1:-1]
        + r"\qquad\qquad"
        + gui_vector_latex("B", B)[1:-1]
    )

    gui_mostrar_expresion_latex(
        contenido_right1,
        f"${expresion_vectores}$",
        fontsize=12, ancho=6, alto=0.45, pady=0
    )

    # Tres campos: i, j, k
    campos_frame = tk.Frame(contenido_right1)
    campos_frame.pack(pady=(10, 5))

    for col, label in enumerate(["i", "+j", "+k"]):
        tk.Label(
            campos_frame,
            text=label,
            font=FONT_TEXTO
        ).grid(row=0, column=col * 2, padx=(10, 2))

    entry_i = tk.Entry(campos_frame, font=FONT_TEXTO, justify="center", width=6)
    entry_j = tk.Entry(campos_frame, font=FONT_TEXTO, justify="center", width=6)
    entry_k = tk.Entry(campos_frame, font=FONT_TEXTO, justify="center", width=6)

    entry_i.grid(row=0, column=1, padx=(0, 10))
    entry_j.grid(row=0, column=3, padx=(0, 10))
    entry_k.grid(row=0, column=5, padx=(0, 10))

    # =========================
    # RIGHT2: RETROALIMENTACIÓN
    # =========================

    titulo_retro = tk.Label(
        right2,
        text="Retroalimentación:",
        font=("Arial", 12, "bold"),
        anchor="w"
    )
    titulo_retro.pack(anchor="w", padx=10, pady=(10, 5))

    retro_text = tk.Text(
        right2,
        width=50,
        height=10,
        wrap="word",
        font=("Arial", 12),
        relief="flat"
    )
    retro_text.pack(fill="both", expand=True, padx=10, pady=(0, 10))

    retro_text.tag_config("correcto", foreground="green")
    retro_text.tag_config("incorrecto", foreground="red")
    retro_text.tag_config("error", foreground="orange")
    retro_text.tag_config("normal", foreground="black")
    retro_text.config(state="disabled")

    # =========================
    # LÓGICA DE VERIFICACIÓN
    # =========================

    def formatear_vector(i, j, k):
        return f"{i}i {j:+d}j {k:+d}k"

    def verificar():
        try:
            resp = [int(entry_i.get()), int(entry_j.get()), int(entry_k.get())]

            ri = int(resultado_correcto[0])
            rj = int(resultado_correcto[1])
            rk = int(resultado_correcto[2])

            i1 = A[1] * B[2]
            i2 = A[2] * B[1]

            j1 = A[0] * B[2]
            j2 = A[2] * B[0]

            k1 = A[0] * B[1]
            k2 = A[1] * B[0]

            def resta_legible(a, b):
                signo = "-" if b >= 0 else "+"
                return f"{a} {signo} {abs(b)}"

            desarrollo = (
                f"A×B = (AyBz - AzBy)i - (AxBz - AzBx)j + (AxBy - AyBx)k\n\n"

                f"Componente i: ({A[1]})({B[2]}) - ({A[2]})({B[1]}) = "
                f"{resta_legible(i1, i2)} = {ri}\n\n"

                f"Componente j: -(({A[0]})({B[2]}) - ({A[2]})({B[0]})) = "
                f"-({resta_legible(j1, j2)}) = {rj}\n\n"

                f"Componente k: ({A[0]})({B[1]}) - ({A[1]})({B[0]}) = "
                f"{resta_legible(k1, k2)} = {rk}\n\n"

                f"A×B = {formatear_vector(ri, rj, rk)}"
            )

            estadisticas["totales"] += 1
            retro_text.config(state="normal")
            retro_text.delete("1.0", tk.END)

            if resp == [ri, rj, rk]:
                estadisticas["correctos"] += 1
                retro_text.insert(tk.END, "Correcto\n\n", "correcto")
                retro_text.insert(tk.END, desarrollo, "normal")
            else:
                estadisticas["incorrectos"] += 1
                retro_text.insert(tk.END, "Incorrecto\n\n", "incorrecto")
                retro_text.insert(
                    tk.END,
                    f"La respuesta correcta es: {formatear_vector(ri, rj, rk)}\n\n",
                    "normal"
                )
                retro_text.insert(tk.END, desarrollo, "normal")

            retro_text.config(state="disabled")
            estadisticas_label.config(
                text=(
                    f"Totales: {estadisticas['totales']} | "
                    f"Correctos: {estadisticas['correctos']} | "
                    f"Incorrectos: {estadisticas['incorrectos']}"
                )
            )
            verificar_btn.config(state="disabled")

        except ValueError:
            retro_text.config(state="normal")
            retro_text.delete("1.0", tk.END)
            retro_text.insert(tk.END, "Ingrese valores enteros en los tres campos.", "error")
            retro_text.config(state="disabled")

    # =========================
    # BOTONES DEL EJERCICIO
    # =========================

    botones_frame = tk.Frame(right1)
    botones_frame.pack(pady=10)

    verificar_btn = tk.Button(
        botones_frame,
        text="Verificar",
        font=FONT_BOTON,
        width=12,
        command=verificar
    )
    verificar_btn.pack(side="left", padx=5)

    siguiente_btn = tk.Button(
        botones_frame,
        text="Siguiente",
        font=FONT_BOTON,
        width=12,
        command=lambda: s_mostrar_producto_vectorial(root)
    )
    siguiente_btn.pack(side="left", padx=5)

def s_mostrar_angulo(root):
    gui_limpiar_ventana(root)

    header, left1, left2, right1, right2 = layout_ejercicio(root)

    A = random_vector()
    B = random_vector()
    resultado_correcto = round(float(angle_between_vectors(A, B)), 2)

    # =========================
    # HEADER
    # =========================

    titulo = tk.Label(
        header,
        text="Ángulo entre vectores",
        font=FONT_TITULO
    )
    titulo.pack(expand=True)

    # =========================
    # LEFT1: EXPLICACIÓN
    # =========================

    contenido_left1 = tk.Frame(left1)
    contenido_left1.pack(expand=True)

    texto1 = tk.Label(
        contenido_left1,
        text="Consideremos los siguientes dos vectores de tres dimensiones:",
        font=FONT_TEXTO,
        wraplength=350,
        justify="left"
    )
    texto1.pack(pady=10)

    gui_mostrar_expresion_latex(
        contenido_left1,
        r"$\mathbf{A}=A_x \mathbf{i} + A_y \mathbf{j}+ A_z \mathbf{k},$",
        fontsize=12, ancho=6, alto=0.4, pady=0
    )

    gui_mostrar_expresion_latex(
        contenido_left1,
        r"$\mathbf{B}=B_x \mathbf{i} + B_y \mathbf{j}+ B_z \mathbf{k}.$",
        fontsize=12, ancho=6, alto=0.4, pady=0
    )

    texto2 = tk.Label(
        contenido_left1,
        text="El ángulo entre ambos vectores se obtiene a partir del producto escalar:",
        font=FONT_TEXTO,
        wraplength=350,
        justify="left"
    )
    texto2.pack(pady=10)

    gui_mostrar_expresion_latex(
        contenido_left1,
        r"$\cos\theta = \dfrac{\mathbf{A}\cdot\mathbf{B}}{\|\mathbf{A}\|\,\|\mathbf{B}\|},$",
        fontsize=12, ancho=6, alto=0.5, pady=0
    )

    gui_mostrar_expresion_latex(
        contenido_left1,
        r"$\theta = \arccos\!\left(\dfrac{\mathbf{A}\cdot\mathbf{B}}{\|\mathbf{A}\|\,\|\mathbf{B}\|}\right).$",
        fontsize=12, ancho=6, alto=0.5, pady=0
    )

    texto3 = tk.Label(
        contenido_left1,
        text="Aquí expresaremos el resultado en grados.",
        font=FONT_TEXTO,
        wraplength=350,
        justify="left"
    )
    texto3.pack(pady=10)

    # =========================
    # LEFT2: ESTADÍSTICAS
    # =========================

    contenido_left2 = tk.Frame(left2)
    contenido_left2.pack(expand=True)

    estadisticas_label = tk.Label(
        contenido_left2,
        text=(
            f"Totales: {estadisticas['totales']} | "
            f"Correctos: {estadisticas['correctos']} | "
            f"Incorrectos: {estadisticas['incorrectos']}"
        ),
        font=FONT_TEXTO,
        justify="center"
    )
    estadisticas_label.pack(pady=5)

    volver_btn = tk.Button(
        contenido_left2,
        text="Volver al inicio",
        font=FONT_BOTON,
        command=lambda: s_mostrar_inicio(root)
    )
    volver_btn.pack(pady=5)

    # =========================
    # RIGHT1: EJERCICIO
    # =========================

    contenido_right1 = tk.Frame(right1)
    contenido_right1.pack(expand=True)

    texto_ejercicio = tk.Label(
        contenido_right1,
        text="Calcule el ángulo (en grados):",
        font=FONT_SUBTITULO,
        wraplength=420,
        justify="center"
    )
    texto_ejercicio.pack(pady=10)

    expresion_vectores = (
        gui_vector_latex("A", A)[1:-1]
        + r"\qquad\qquad"
        + gui_vector_latex("B", B)[1:-1]
    )

    gui_mostrar_expresion_latex(
        contenido_right1,
        f"${expresion_vectores}$",
        fontsize=12, ancho=6, alto=0.45, pady=0
    )

    texto_respuesta = tk.Label(
        contenido_right1,
        text="Introduzca su respuesta en grados (ej: 45.73):",
        font=FONT_TEXTO
    )
    texto_respuesta.pack(pady=(10, 5))

    respuesta_entry = tk.Entry(
        contenido_right1,
        font=FONT_TEXTO,
        justify="center",
        width=12
    )
    respuesta_entry.pack(pady=5)

    # =========================
    # RIGHT2: RETROALIMENTACIÓN
    # =========================

    titulo_retro = tk.Label(
        right2,
        text="Retroalimentación:",
        font=("Arial", 12, "bold"),
        anchor="w"
    )
    titulo_retro.pack(anchor="w", padx=10, pady=(10, 5))

    retro_text = tk.Text(
        right2,
        width=50,
        height=10,
        wrap="word",
        font=("Arial", 12),
        relief="flat"
    )
    retro_text.pack(fill="both", expand=True, padx=10, pady=(0, 10))

    retro_text.tag_config("correcto", foreground="green")
    retro_text.tag_config("incorrecto", foreground="red")
    retro_text.tag_config("error", foreground="orange")
    retro_text.tag_config("normal", foreground="black")
    retro_text.config(state="disabled")

    # =========================
    # LÓGICA DE VERIFICACIÓN
    # =========================

    def verificar():
        try:
            respuesta_usuario = float(respuesta_entry.get())

            punto = int(dot_product(A, B))
            norma_a = round(float(vector_norm(A)), 4)
            norma_b = round(float(vector_norm(B)), 4)
            cos_theta = round(punto / (norma_a * norma_b), 4)

            desarrollo = (
                f"A·B = ({A[0]})({B[0]}) + ({A[1]})({B[1]}) + ({A[2]})({B[2]}) = {punto}\n\n"
                f"||A|| = sqrt(({A[0]})({A[0]}) + ({A[1]})({A[1]}) + ({A[2]})({A[2]})) = {norma_a}\n\n"
                f"||B|| = sqrt(({B[0]})({B[0]}) + ({B[1]})({B[1]}) + ({B[2]})({B[2]})) = {norma_b}\n\n"
                f"cos (theta) = {punto} / ({norma_a} × {norma_b}) = {cos_theta}\n\n"
                f"theta = arccos({cos_theta}) = {resultado_correcto} grados"
            )

            estadisticas["totales"] += 1
            retro_text.config(state="normal")
            retro_text.delete("1.0", tk.END)

            if abs(respuesta_usuario - resultado_correcto) <= 0.01:
                estadisticas["correctos"] += 1
                retro_text.insert(tk.END, "Correcto\n\n", "correcto")
                retro_text.insert(tk.END, desarrollo, "normal")
            else:
                estadisticas["incorrectos"] += 1
                retro_text.insert(tk.END, "Incorrecto\n\n", "incorrecto")
                retro_text.insert(
                    tk.END,
                    f"La respuesta correcta es: {resultado_correcto} grados\n\n",
                    "normal"
                )
                retro_text.insert(tk.END, desarrollo, "normal")

            retro_text.config(state="disabled")
            estadisticas_label.config(
                text=(
                    f"Totales: {estadisticas['totales']} | "
                    f"Correctos: {estadisticas['correctos']} | "
                    f"Incorrectos: {estadisticas['incorrectos']}"
                )
            )
            verificar_btn.config(state="disabled")

        except ValueError:
            retro_text.config(state="normal")
            retro_text.delete("1.0", tk.END)
            retro_text.insert(tk.END, "Ingrese un valor numérico válido (ej: 45.73).", "error")
            retro_text.config(state="disabled")

    # =========================
    # BOTONES DEL EJERCICIO
    # =========================

    botones_frame = tk.Frame(right1)
    botones_frame.pack(pady=10)

    verificar_btn = tk.Button(
        botones_frame,
        text="Verificar",
        font=FONT_BOTON,
        width=12,
        command=verificar
    )
    verificar_btn.pack(side="left", padx=5)

    siguiente_btn = tk.Button(
        botones_frame,
        text="Siguiente",
        font=FONT_BOTON,
        width=12,
        command=lambda: s_mostrar_angulo(root)
    )
    siguiente_btn.pack(side="left", padx=5)

def s_mostrar_norma(root):
    gui_limpiar_ventana(root)

    header, left1, left2, right1, right2 = layout_ejercicio(root)

    A = random_vector()
    resultado_correcto = round(float(vector_norm(A)), 2)

    # =========================
    # HEADER
    # =========================

    titulo = tk.Label(
        header,
        text="Norma de un vector",
        font=FONT_TITULO
    )
    titulo.pack(expand=True)

    # =========================
    # LEFT1: EXPLICACIÓN
    # =========================

    contenido_left1 = tk.Frame(left1)
    contenido_left1.pack(expand=True)

    texto1 = tk.Label(
        contenido_left1,
        text="Consideremos el siguiente vector de tres dimensiones:",
        font=FONT_TEXTO,
        wraplength=350,
        justify="left"
    )
    texto1.pack(pady=10)

    gui_mostrar_expresion_latex(
        contenido_left1,
        r"$\mathbf{A}=A_x \mathbf{i} + A_y \mathbf{j}+ A_z \mathbf{k}.$",
        fontsize=12, ancho=6, alto=0.4, pady=0
    )

    texto2 = tk.Label(
        contenido_left1,
        text="La norma (o módulo) de un vector es su magnitud. Se calcula como:",
        font=FONT_TEXTO,
        wraplength=350,
        justify="left"
    )
    texto2.pack(pady=10)

    gui_mostrar_expresion_latex(
        contenido_left1,
        r"$\|\mathbf{A}\| = \sqrt{A_x^2 + A_y^2 + A_z^2}.$",
        fontsize=12, ancho=6, alto=0.4, pady=0
    )

    texto3 = tk.Label(
        contenido_left1,
        text="El resultado es un número real no negativo. Ingrese su respuesta redondeada a 2 decimales.",
        font=FONT_TEXTO,
        wraplength=350,
        justify="left"
    )
    texto3.pack(pady=10)

    # =========================
    # LEFT2: ESTADÍSTICAS
    # =========================

    contenido_left2 = tk.Frame(left2)
    contenido_left2.pack(expand=True)

    estadisticas_label = tk.Label(
        contenido_left2,
        text=(
            f"Totales: {estadisticas['totales']} | "
            f"Correctos: {estadisticas['correctos']} | "
            f"Incorrectos: {estadisticas['incorrectos']}"
        ),
        font=FONT_TEXTO,
        justify="center"
    )
    estadisticas_label.pack(pady=5)

    volver_btn = tk.Button(
        contenido_left2,
        text="Volver al inicio",
        font=FONT_BOTON,
        command=lambda: s_mostrar_inicio(root)
    )
    volver_btn.pack(pady=5)

    # =========================
    # RIGHT1: EJERCICIO
    # =========================

    contenido_right1 = tk.Frame(right1)
    contenido_right1.pack(expand=True)

    texto_ejercicio = tk.Label(
        contenido_right1,
        text="Calcule la norma del vector:",
        font=FONT_SUBTITULO
    )
    texto_ejercicio.pack(pady=10)

    gui_mostrar_expresion_latex(
        contenido_right1,
        gui_vector_latex("A", A),
        fontsize=12, ancho=6, alto=0.45, pady=0
    )

    texto_respuesta = tk.Label(
        contenido_right1,
        text="Introduzca su respuesta (2 decimales):",
        font=FONT_TEXTO
    )
    texto_respuesta.pack(pady=(10, 5))

    respuesta_entry = tk.Entry(
        contenido_right1,
        font=FONT_TEXTO,
        justify="center",
        width=12
    )
    respuesta_entry.pack(pady=5)

    # =========================
    # RIGHT2: RETROALIMENTACIÓN
    # =========================

    titulo_retro = tk.Label(
        right2,
        text="Retroalimentación:",
        font=("Arial", 12, "bold"),
        anchor="w"
    )
    titulo_retro.pack(anchor="w", padx=10, pady=(10, 5))

    retro_text = tk.Text(
        right2,
        width=50,
        height=10,
        wrap="word",
        font=("Arial", 12),
        relief="flat"
    )
    retro_text.pack(fill="both", expand=True, padx=10, pady=(0, 10))

    retro_text.tag_config("correcto", foreground="green")
    retro_text.tag_config("incorrecto", foreground="red")
    retro_text.tag_config("error", foreground="orange")
    retro_text.tag_config("normal", foreground="black")
    retro_text.config(state="disabled")

    # =========================
    # LÓGICA DE VERIFICACIÓN
    # =========================

    def verificar():
        try:
            respuesta_usuario = round(float(respuesta_entry.get()), 2)

            desarrollo = (
                f"||A|| = sqrt((Ax)(Ax) + (Ay)(Ay) + (Az)(Az))\n\n"
                f"||A|| = sqrt((A[0])(A[0]) + (A[1])(A[1]) + (A[2])(A[2]))\n\n"
                f"||A|| = sqrt({A[0] ** 2} + {A[1] ** 2} + {A[2] ** 2})\n\n"
                f"||A|| = sqrt({A[0] ** 2 + A[1] ** 2 + A[2] ** 2})\n\n"
                f"||A|| = {resultado_correcto}"
            )

            estadisticas["totales"] += 1
            retro_text.config(state="normal")
            retro_text.delete("1.0", tk.END)

            if respuesta_usuario == resultado_correcto:
                estadisticas["correctos"] += 1
                retro_text.insert(tk.END, "Correcto\n\n", "correcto")
                retro_text.insert(tk.END, desarrollo, "normal")
            else:
                estadisticas["incorrectos"] += 1
                retro_text.insert(tk.END, "Incorrecto\n\n", "incorrecto")
                retro_text.insert(
                    tk.END,
                    f"La respuesta correcta es: {resultado_correcto}\n\n",
                    "normal"
                )
                retro_text.insert(tk.END, desarrollo, "normal")

            retro_text.config(state="disabled")
            estadisticas_label.config(
                text=(
                    f"Totales: {estadisticas['totales']} | "
                    f"Correctos: {estadisticas['correctos']} | "
                    f"Incorrectos: {estadisticas['incorrectos']}"
                )
            )
            verificar_btn.config(state="disabled")

        except ValueError:
            retro_text.config(state="normal")
            retro_text.delete("1.0", tk.END)
            retro_text.insert(tk.END, "Ingrese un valor numérico válido (ej: 3.74).", "error")
            retro_text.config(state="disabled")

    # =========================
    # BOTONES DEL EJERCICIO
    # =========================

    botones_frame = tk.Frame(right1)
    botones_frame.pack(pady=10)

    verificar_btn = tk.Button(
        botones_frame,
        text="Verificar",
        font=FONT_BOTON,
        width=12,
        command=verificar
    )
    verificar_btn.pack(side="left", padx=5)

    siguiente_btn = tk.Button(
        botones_frame,
        text="Siguiente",
        font=FONT_BOTON,
        width=12,
        command=lambda: s_mostrar_norma(root)
    )
    siguiente_btn.pack(side="left", padx=5)

