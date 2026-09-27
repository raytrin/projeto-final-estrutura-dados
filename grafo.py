import pandas as pd


class Grafo:
    
    def __init__(self, caminho_csv="dados/cidades_vizinhas_estrutura_dados.csv"):
        self.adjacencia = {} 
        self._carrega_csv(caminho_csv)

    def _carrega_csv(self, caminho_csv):
        dados = pd.read_csv(
            caminho_csv,
            sep=";",
            header=None,
            names=["cidade_origem", "cidade_vizinha", "distancia_km"],
        )

        for _, linha in dados.iterrows():
            origem = str(linha["cidade_origem"])
            destino = str(linha["cidade_vizinha"])
            distancia = float(linha["distancia_km"])
            self._adiciona_aresta(origem, destino, distancia)

    def _adiciona_aresta(self, cidade_a, cidade_b, distancia):
        self.adjacencia.setdefault(cidade_a, {})[cidade_b] = distancia
        self.adjacencia.setdefault(cidade_b, {})[cidade_a] = distancia  

    def caminho_minimo(self, origem, destino):
       
        if origem not in self.adjacencia or destino not in self.adjacencia:
            return None, None

        distancias, anteriores = self._dijkstra(origem)

        if distancias[destino] == float("inf"):
            return None, None

        caminho = self._reconstroi_caminho(anteriores, origem, destino)
        return caminho, distancias[destino]

    def caminho_minimo_passando_por(self, origem, intermediaria, destino):
    
        caminho1, distancia1 = self.caminho_minimo(origem, intermediaria)
        caminho2, distancia2 = self.caminho_minimo(intermediaria, destino)

        if caminho1 is None or caminho2 is None:
            return None, None

       
        caminho_completo = caminho1 + caminho2[1:]
        distancia_total = distancia1 + distancia2
        return caminho_completo, distancia_total

    def todas_as_distancias(self, origem):
    
        distancias, _ = self._dijkstra(origem)
        return distancias

    def _dijkstra(self, origem):
        distancias = {cidade: float("inf") for cidade in self.adjacencia}
        anteriores = {cidade: None for cidade in self.adjacencia}
        distancias[origem] = 0

        visitados = set()

        while len(visitados) < len(distancias):
            atual = self._cidade_nao_visitada_mais_proxima(distancias, visitados)
            if atual is None:
                break  

            visitados.add(atual)

            for vizinha, peso in self.adjacencia[atual].items():
                nova_distancia = distancias[atual] + peso
                if nova_distancia < distancias[vizinha]:
                    distancias[vizinha] = nova_distancia
                    anteriores[vizinha] = atual

        return distancias, anteriores

    def _cidade_nao_visitada_mais_proxima(self, distancias, visitados):
        menor_distancia = float("inf")
        cidade_escolhida = None

        for cidade, distancia in distancias.items():
            if cidade not in visitados and distancia < menor_distancia:
                menor_distancia = distancia
                cidade_escolhida = cidade

        return cidade_escolhida

    def _reconstroi_caminho(self, anteriores, origem, destino):
        caminho = []
        atual = destino

        while atual is not None:
            caminho.append(atual)
            if atual == origem:
                break
            atual = anteriores[atual]

        caminho.reverse()
        return caminho