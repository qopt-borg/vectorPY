import numpy as np

# Generador moderno de números aleatorios
_rng = np.random.default_rng()


def _validate_vector(a, name="vector"):
    """
    Verifica que el argumento sea un arreglo NumPy
    unidimensional de tres elementos.
    """
    if not isinstance(a, np.ndarray):
        raise TypeError(f"{name} debe ser un arreglo de NumPy")

    if a.shape != (3,):
        raise ValueError(f"{name} debe ser un vector de 3 elementos")


def random_vector(low=-5, high=6):
    """
    Genera un vector aleatorio de tres componentes enteras.
    """
    return _rng.integers(low=low, high=high, size=3)


def vector_norm(a):
    """
    Calcula la norma euclidiana de un vector.
    """
    _validate_vector(a, "a")
    return np.linalg.norm(a)


def angle_between_vectors(a, b):
    """
    Calcula el ángulo entre dos vectores en grados.
    """
    _validate_vector(a, "a")
    _validate_vector(b, "b")

    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    if norm_a == 0 or norm_b == 0:
        raise ValueError("No puede calcularse el ángulo con un vector nulo")

    cos_theta = np.dot(a, b) / (norm_a * norm_b)

    # evita errores numéricos
    cos_theta = np.clip(cos_theta, -1.0, 1.0)

    return np.degrees(np.arccos(cos_theta))


def add(a, b):
    """
    Suma de vectores.
    """
    _validate_vector(a, "a")
    _validate_vector(b, "b")
    return a + b


def diff(a, b):
    """
    Resta de vectores.
    """
    _validate_vector(a, "a")
    _validate_vector(b, "b")
    return a - b


def dot_product(a, b):
    """
    Producto punto.
    """
    _validate_vector(a, "a")
    _validate_vector(b, "b")
    return np.dot(a, b)


def cross_product(a, b):
    """
    Producto cruz.
    """
    _validate_vector(a, "a")
    _validate_vector(b, "b")
    return np.cross(a, b)