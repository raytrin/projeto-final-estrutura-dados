import random

import pandas as pd


def atribui_cidade() -> str:
    dados = pd.read_csv(
        "dados/cidades_vizinhas_estrutura_dados.csv",
        sep=";",
        header=None,
        names=["cidade_origem", "cidade_vizinha", "distancia_km"],
    )

    cidades = dados["cidade_vizinha"].astype(str).tolist()
    return random.choice(cidades)
