"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    import pandas as pd

    with open('files/input/clusters_report.txt', 'r') as f:
        lines = f.readlines()
    del lines[3]
    col_spans = [(0, 9), (9, 24), (24, 41), (41, None)]
    empty_row = ["", "", "", ""]
    data = [empty_row]
    for current, line in enumerate(lines):
        if line.strip() == "":
            data[-1] = [cell.strip() for cell in data[-1]]
            data.append(empty_row)
        else:
            line = [line[i:j].strip() for i, j in col_spans]
            data[-1] = [f"{i} {j}" for i, j in zip(data[-1], line)]
    headers = list(map(lambda x: x.lower().replace(" ", "_"), data[0]))
    data = data[1:-1]
    df = pd.DataFrame(data, columns=headers)
    df.principales_palabras_clave = (df.principales_palabras_clave
                                     .str.replace(r" +", " ", regex=True)
                                     .str.replace(".", ""))
    df.porcentaje_de_palabras_clave = (df.porcentaje_de_palabras_clave
                                       .str.replace(r"%| *", "", regex=True)
                                       .str.replace(",", ".")
                                       .astype(float))
    int_cols = ['cluster', 'cantidad_de_palabras_clave']
    df[int_cols] = df[int_cols].astype(int)
    return df
