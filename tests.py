def s_mostrar_producto_escalar(root):
    gui_limpiar_ventana(root)

    A = random_vector()
    B = random_vector()
    resultado_correcto = dot_product(A, B)

    titulo = tk.Label(
        root,
        text="Entrenando producto escalar",
        font=("Arial", 20)
    )
    titulo.pack(pady=(10, 5))

    texto1 = tk.Label(
        root,
        text="El producto escalar de dos vectores A y B se calcula mediante:",
        font=("Arial", 13)
    )
    texto1.pack(pady=5)

    gui_mostrar_expresion_latex(
        root,
        r"$\mathbf{A}\cdot\mathbf{B}=A_xB_x + A_yB_y + A_zB_z$",
        fontsize=16,
        ancho=5,
        alto=0.8
    )

    texto2 = tk.Label(
        root,
        text="Calcule el producto escalar de los siguientes vectores:",
        font=("Arial", 13)
    )
    texto2.pack(pady=5)

    expresion_vectores = (
        gui_vector_latex("A", A)[1:-1]
        + r"\qquad\qquad"
        + gui_vector_latex("B", B)[1:-1]
    )

    gui_mostrar_expresion_latex(
        root,
        f"${expresion_vectores}$",
        fontsize=15,
        ancho=7,
        alto=1.0
    )

    texto3 = tk.Label(
        root,
        text="Introduzca su respuesta numérica:",
        font=("Arial", 13)
    )
    texto3.pack(pady=(10, 5))

    respuesta_entry = tk.Entry(
        root,
        font=("Arial", 16),
        justify="center",
        width=10
    )
    respuesta_entry.pack(pady=5)

    resultado_label = tk.Label(
        root,
        text="",
        font=("Arial", 12)
    )
    resultado_label.pack(pady=5)

    estadisticas_label = tk.Label(
        root,
        text="Totales: 0 | Correctos: 0 | Incorrectos: 0",
        font=("Arial", 12, "bold")
    )
    estadisticas_label.pack(pady=5)

    def verificar():
        try:
            respuesta_usuario = float(respuesta_entry.get())

            desarrollo = (
                f"A·B = AxBx + AyBy + AzBz\n\n"
                f"A·B = ({A[0]})({B[0]}) + ({A[1]})({B[1]}) + ({A[2]})({B[2]})\n\n"
                f"A·B = ({A[0] * B[0]}) + ({A[1] * B[1]}) + ({A[2] * B[2]})\n\n"
                f"A·B = {resultado_correcto}"
            )

            if respuesta_usuario == resultado_correcto:
                resultado_label.config(
                    text="La respuesta es correcta.\n\n" + desarrollo,
                    fg="green",
                    font=("Arial", 12, "bold"),
                    justify="center"
                )
                estadisticas["totales"] += 1
                estadisticas["correctos"] += 1
            else:
                resultado_label.config(
                    text=(
                            f"Resultado incorrecto.\n\n"
                            f"La respuesta correcta es: {resultado_correcto}\n\n"
                            + desarrollo
                    ),
                    fg="red",
                    font=("Arial", 12, "bold"),
                    justify="center"
                )
                estadisticas["totales"] += 1
                estadisticas["incorrectos"] += 1

            estadisticas_label.config(
                text=(
                    f"Totales: {estadisticas['totales']} | "
                    f"Correctos: {estadisticas['correctos']} | "
                    f"Incorrectos: {estadisticas['incorrectos']}"
                )
            )

            verificar_btn.config(state="disabled")

        except ValueError:
            resultado_label.config(
                text="Ingrese un valor numérico válido",
                fg="orange",
                font=("Arial", 12, "bold")
            )
    # Botones principales
    botones_frame = tk.Frame(root)
    botones_frame.pack(pady=10)

    verificar_btn = tk.Button(
        botones_frame,
        text="Verificar",
        font=("Arial", 12),
        width=12,
        command=verificar
    )
    verificar_btn.pack(side="left", padx=10)

    siguiente_btn = tk.Button(
        botones_frame,
        text="Siguiente",
        font=("Arial", 12),
        width=12,
        command=lambda: s_mostrar_producto_escalar(root)
    )
    siguiente_btn.pack(side="left", padx=10)


    # Botón de navegación separado
    navegacion_frame = tk.Frame(root)
    navegacion_frame.pack(pady=20)

    volver_btn = tk.Button(
        navegacion_frame,
        text="Volver al inicio",
        font=("Arial", 12),
        width=18,
        command=lambda: s_mostrar_inicio(root)
    )
    volver_btn.pack()
