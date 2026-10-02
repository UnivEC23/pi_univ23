"""
perfil_ml.py — Segmentação não supervisionada (k-means) da base de clientes.
Gera perfis típicos (modo de cada atributo) no formato `Clientes`.
Execução offline: não interfere no fluxo operacional.
"""
from collections import Counter

import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import OneHotEncoder

from modelos import Clientes, Estados, Idade, Setor, Genero

REGIOES = {
    "Norte":     {Estados.Acre, Estados.Amapá, Estados.Amazonas, Estados.Pará,
                  Estados.Rondônia, Estados.Roraima, Estados.Tocantins},
    "Nordeste":  {Estados.Alagoas, Estados.Bahia, Estados.Ceará, Estados.Maranhão,
                  Estados.Paraíba, Estados.Pernambuco, Estados.Piauí,
                  Estados.Rio_Grande_do_Norte, Estados.Sergipe},
    "Centro-Oeste": {Estados.Distrito_Federal, Estados.Goiás,
                     Estados.Mato_Grosso, Estados.Mato_Grosso_do_Sul},
    "Sudeste":   {Estados.Espírito_Santo, Estados.Minas_Gerais,
                  Estados.Rio_de_Janeiro, Estados.São_Paulo},
    "Sul":       {Estados.Paraná, Estados.Santa_Catarina, Estados.Rio_Grande_do_Sul},
}

# Amostra mínima para gerar perfil por estado (abaixo disso, sem estatística)
MIN_AMOSTRA_ESTADO = 3

# ------------------------------------------------------------------ helpers

def _modo(valores: list[int], enum_cls) -> object:
    """Retorna o membro do Enum mais frequente (mode)."""
    mais_comum, _ = Counter(valores).most_common(1)[0]
    return enum_cls(mais_comum)

def _percentual(valores: list[int], valor_alvo: int) -> float:
    return 100.0 * valores.count(valor_alvo) / len(valores)

# ------------------------------------------------------------ segmentação

def _matriz_features(clientes: list[Clientes]) -> np.ndarray:
    """One-hot dos atributos categóricos (Enums são ordinais arbitrários;
    sem one-hot, o k-means calcularia distâncias sem sentido)."""
    X = np.array([[c.estados.value, c.idade.value,
                   c.setor.value, c.genero.value] for c in clientes], dtype=int)
    return OneHotEncoder(sparse_output=False).fit_transform(X)

def segmentar(clientes: list[Clientes],
              k_min: int = 2,
              k_max: int = 6) -> tuple[dict[int, list[Clientes]], int]:
    """
    Clusteriza clientes pelos atributos (estado, idade, setor, gênero),
    selecionando k automaticamente pelo melhor silhouette médio.
    Retorna ({cluster_id: [clientes]}, k_escolhido).
    """
    if len(clientes) < k_max + 1:
        k_max = max(k_min, len(clientes) - 1)

    X_ohe = _matriz_features(clientes)

    melhor_k, melhor_sil, melhor_rotulos = None, -1.0, None
    for k in range(k_min, k_max + 1):
        km = KMeans(n_clusters=k, n_init=10, random_state=42)
        rotulos = km.fit_predict(X_ohe)
        sil = silhouette_score(X_ohe, rotulos)
        print(f"[perfil_ml] k={k} | inércia={km.inertia_:.1f} | silhouette={sil:.3f}")
        if sil > melhor_sil:
            melhor_k, melhor_sil, melhor_rotulos = k, sil, rotulos

    print(f"[perfil_ml] >>> k escolhido: {melhor_k} (silhouette={melhor_sil:.3f})")

    grupos: dict[int, list[Clientes]] = {}
    for cliente, rotulo in zip(clientes, melhor_rotulos):
        grupos.setdefault(int(rotulo), []).append(cliente)
    return dict(sorted(grupos.items(), key=lambda kv: -len(kv[1]))), melhor_k

# --------------------------------------------------------------- perfis

def perfil_brasil(grupos: dict[int, list[Clientes]]) -> list[Clientes]:
    """Perfil típico de cada segmento, no formato `Clientes`.
    Segmentos ordenados por tamanho (Perfil 1 = mais comum)."""
    total = sum(len(g) for g in grupos.values())
    perfis = []
    for i, (_, grupo) in enumerate(grupos.items(), start=1):
        estados_ = [c.estados.value for c in grupo]
        idades = [c.idade.value for c in grupo]
        setores = [c.setor.value for c in grupo]
        generos = [c.genero.value for c in grupo]

        uf_moda = _modo(estados_, Estados)
        idade_moda = _modo(idades, Idade)
        setor_moda = _modo(setores, Setor)
        genero_moda = _modo(generos, Genero)

        perfis.append(Clientes(
            f"Perfil {i} — Brasil",
            "perfil@interno",
            (f"Segmento {i}: {len(grupo)} clientes "
             f"({100 * len(grupo) / total:.0f}% da base). "
             f"Dominante: {uf_moda.name} "
             f"({_percentual(estados_, uf_moda.value):.0f}%), "
             f"faixa {idade_moda.name} "
             f"({_percentual(idades, idade_moda.value):.0f}%), "
             f"setor {setor_moda.name} "
             f"({_percentual(setores, setor_moda.value):.0f}%), "
             f"gênero {genero_moda.name} "
             f"({_percentual(generos, genero_moda.value):.0f}%)."),
            uf_moda,
            idade_moda,
            setor_moda,
            genero_moda,
        ))
    return perfis

def perfil_por_estado(clientes: list[Clientes],
                      uf: Estados) -> Clientes | None:
    """Perfil típico de um estado; retorna None se a amostra for
    insuficiente (< MIN_AMOSTRA_ESTADO)."""
    grupo = [c for c in clientes if c.estados == uf]
    if len(grupo) < MIN_AMOSTRA_ESTADO:
        return None

    idades = [c.idade.value for c in grupo]
    setores = [c.setor.value for c in grupo]
    generos = [c.genero.value for c in grupo]

    idade_moda = _modo(idades, Idade)
    setor_moda = _modo(setores, Setor)
    genero_moda = _modo(generos, Genero)

    return Clientes(
        f"Perfil — {uf.name}",
        "perfil@interno",
        (f"{len(grupo)} cliente(s) em {uf.name}. "
         f"Dominante: faixa {idade_moda.name} "
         f"({_percentual(idades, idade_moda.value):.0f}%), "
         f"setor {setor_moda.name} "
         f"({_percentual(setores, setor_moda.value):.0f}%), "
         f"gênero {genero_moda.name} "
         f"({_percentual(generos, genero_moda.value):.0f}%)."),
        uf,
        idade_moda,
        setor_moda,
        genero_moda,
    )

def perfis_estados_disponiveis(clientes: list[Clientes]) -> list[Clientes]:
    """Perfis de todos os estados com amostra suficiente."""
    perfis = []
    for uf in Estados:
        p = perfil_por_estado(clientes, uf)
        if p is not None:
            perfis.append(p)
    return perfis

def perfis_por_regiao(clientes: list[Clientes]) -> list[Clientes]:
    """Perfis por macrorregião (amostras maiores, mais confiáveis)."""
    perfis = []
    for nome_regiao, ufs in REGIOES.items():
        grupo = [c for c in clientes if c.estados in ufs]
        if not grupo:
            continue
        idades = [c.idade.value for c in grupo]
        setores = [c.setor.value for c in grupo]
        generos = [c.genero.value for c in grupo]

        idade_moda = _modo(idades, Idade)
        setor_moda = _modo(setores, Setor)
        genero_moda = _modo(generos, Genero)

        perfis.append(Clientes(
            f"Perfil — Região {nome_regiao}",
            "perfil@interno",
            (f"{len(grupo)} cliente(s). Dominante: faixa "
             f"{idade_moda.name} "
             f"({_percentual(idades, idade_moda.value):.0f}%), setor "
             f"{setor_moda.name} "
             f"({_percentual(setores, setor_moda.value):.0f}%), gênero "
             f"{genero_moda.name} "
             f"({_percentual(generos, genero_moda.value):.0f}%)."),
            _modo([c.estados.value for c in grupo], Estados),
            idade_moda,
            setor_moda,
            genero_moda,
        ))
    return perfis

if __name__ == "__main__":
    from modelos import clientes_1_30

    grupos, k = segmentar(clientes_1_30)

    print(f"\n=== PERFIS — BRASIL ({k} segmentos, k escolhido por silhouette) ===")
    for p in perfil_brasil(grupos):
        print(f"{p.nome}: {p.solicit}")

    print(f"\n=== PERFIS — POR ESTADO (apenas UFs com >= {MIN_AMOSTRA_ESTADO} clientes) ===")
    for p in perfis_estados_disponiveis(clientes_1_30):
        print(f"{p.nome}: {p.solicit}")

    print("\n=== PERFIS — POR REGIÃO ===")
    for p in perfis_por_regiao(clientes_1_30):
        print(f"{p.nome}: {p.solicit}")