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

# Mapa de apoio: agrupamento por macrorregião (caso perfis por estado fiquem
# com amostra pequena demais — sugerido pelo `#class regiao`)
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


# ------------------------------------------------------------------ helpers

def _modo(valores: list[int], enum_cls) -> object:
    """Retorna o membro do Enum mais frequente (mode)."""
    mais_comum, _ = Counter(valores).most_common(1)[0]
    return enum_cls(mais_comum)


def _percentual(valores: list[int], valor_alvo: int) -> float:
    return 100.0 * valores.count(valor_alvo) / len(valores)


# ------------------------------------------------------------ segmentação

def segmentar(clientes: list[Clientes], n_clusters: int = 3) -> dict[int, list[Clientes]]:
    """
    Clusteriza clientes pelos atributos (estado, idade, setor, gênero)
    e retorna {cluster_id: [clientes]} ordenado por tamanho.
    """
    X = np.array([[c.estados.value, c.idade.value,
                   c.setor.value, c.genero.value] for c in clientes], dtype=int)

    # one-hot: evita que o k-means trate os códigos ordinais como escala contínua
    X_ohe = OneHotEncoder(sparse_output=False).fit_transform(X)

    km = KMeans(n_clusters=n_clusters, n_init=10, random_state=42)
    rotulos = km.fit_predict(X_ohe)

    # métricas para o relatório (transparência/credibilidade)
    sil = silhouette_score(X_ohe, rotulos)
    print(f"[perfil_ml] k={n_clusters} | inércia={km.inertia_:.1f} "
          f"| silhouette={sil:.3f} | n={len(clientes)}")

    grupos: dict[int, list[Clientes]] = {}
    for cliente, rotulo in zip(clientes, rotulos):
        grupos.setdefault(int(rotulo), []).append(cliente)
    return dict(sorted(grupos.items(), key=lambda kv: -len(kv[1])))


# --------------------------------------------------------------- perfis

def perfil_brasil(grupos: dict[int, list[Clientes]]) -> list[Clientes]:
    """Perfil típico de cada segmento, no formato `Clientes`."""
    total = sum(len(g) for g in grupos.values())
    perfis = []
    for i, (_, grupo) in enumerate(grupos.items(), start=1):
        estados_ = [c.estados.value for c in grupo]
        idades = [c.idade.value for c in grupo]
        setores = [c.setor.value for c in grupo]
        generos = [c.genero.value for c in grupo]

        perfis.append(Clientes(
            f"Perfil {i} — Brasil",
            "perfil@interno",
            (f"Segmento {i}: {len(grupo)} clientes "
             f"({100 * len(grupo) / total:.0f}% da base). "
             f"Dominante: {_modo(estados_, Estados).name} "
             f"({_percentual(estados_, _modo(estados_, Estados).value):.0f}%), "
             f"faixa {Idade(_modo(idades, Idade)).name}, "
             f"setor {Setor(_modo(setores, Setor)).name} "
             f"({_percentual(setores, _modo(setores, Setor).value):.0f}%), "
             f"gênero {Genero(_modo(generos, Genero)).name}."),
            _modo(estados_, Estados),
            _modo(idades, Idade),
            _modo(setores, Setor),
            _modo(generos, Genero),
        ))
    return perfis


def perfil_por_estado(clientes: list[Clientes],
                      uf: Estados) -> Clientes:
    """Perfil típico de um estado específico (modo dos atributos)."""
    grupo = [c for c in clientes if c.estados == uf]
    if not grupo:
        raise ValueError(f"Sem clientes registrados em {uf.name}")

    idades = [c.idade.value for c in grupo]
    setores = [c.setor.value for c in grupo]
    generos = [c.genero.value for c in grupo]

    return Clientes(
        f"Perfil — {uf.name}",
        "perfil@interno",
        (f"{len(grupo)} cliente(s) em {uf.name}. "
         f"Dominante: faixa {Idade(_modo(idades, Idade)).name} "
         f"({_percentual(idades, _modo(idades, Idade).value):.0f}%), "
         f"setor {Setor(_modo(setores, Setor)).name} "
         f"({_percentual(setores, _modo(setores, Setor).value):.0f}%), "
         f"gênero {Genero(_modo(generos, Genero)).name}."),
        uf,
        _modo(idades, Idade),
        _modo(setores, Setor),
        _modo(generos, Genero),
    )


def perfis_por_regiao(clientes: list[Clientes]) -> list[Clientes]:
    """Alternativa com amostra maior por grupo: perfis por macrorregião."""
    perfis = []
    for nome_regiao, ufs in REGIOES.items():
        grupo = [c for c in clientes if c.estados in ufs]
        if not grupo:
            continue
        idades = [c.idade.value for c in grupo]
        setores = [c.setor.value for c in grupo]
        generos = [c.genero.value for c in grupo]
        perfis.append(Clientes(
            f"Perfil — Região {nome_regiao}",
            "perfil@interno",
            (f"{len(grupo)} cliente(s). Dominante: faixa "
             f"{Idade(_modo(idades, Idade)).name}, setor "
             f"{Setor(_modo(setores, Setor)).name}, gênero "
             f"{Genero(_modo(generos, Genero)).name}."),
            _modo([c.estados.value for c in grupo], Estados),
            _modo(idades, Idade),
            _modo(setores, Setor),
            _modo(generos, Genero),
        ))
    return perfis


if __name__ == "__main__":
    from modelos import clientes_1_30

    grupos = segmentar(clientes_1_30, n_clusters=3)

    print("\n=== PERFIS — BRASIL (por segmento) ===")
    for p in perfil_brasil(grupos):
        print(f"{p.nome}: {p.solicit}")

    print("\n=== PERFIS — POR ESTADO ===")
    for uf in (Estados.São_Paulo, Estados.Pernambuco, Estados.Paraná):
        p = perfil_por_estado(clientes_1_30, uf)
        print(f"{p.nome}: {p.solicit}")

    print("\n=== PERFIS — POR REGIÃO (amostra maior, mais confiável) ===")
    for p in perfis_por_regiao(clientes_1_30):
        print(f"{p.nome}: {p.solicit}")