#n1 USAR ESSE para perfil dominante no brasil
def perfil_dominante_brasil(clientes: list[Clientes]) -> Clientes:
    """O perfil mais comum da base: cluster maior + modo dos atributos globais.
    Alternativa 1: modo simples sobre TODOS os clientes (sem clustering)."""
    idade_moda = _modo([c.idade.value for c in clientes], Idade)
    setor_moda = _modo([c.setor.value for c in clientes], Setor)
    genero_moda = _modo([c.genero.value for c in clientes], Genero)
    uf_moda = _modo([c.estados.value for c in clientes], Estados)

    return Clientes(
        "Perfil Dominante — Brasil",
        "perfil@interno",
        (f"Cliente típico da base ({len(clientes)} registros): "
         f"UF {uf_moda.name} ({_percentual([c.estados.value for c in clientes], uf_moda.value):.0f}%), "
         f"faixa {idade_moda.name} ({_percentual([c.idade.value for c in clientes], idade_moda.value):.0f}%), "
         f"setor {setor_moda.name} ({_percentual([c.setor.value for c in clientes], setor_moda.value):.0f}%), "
         f"gênero {genero_moda.name} ({_percentual([c.genero.value for c in clientes], genero_moda.value):.0f}%)."),
        uf_moda, idade_moda, setor_moda, genero_moda,
    )

#n2
def perfil_dominante_por_cluster(grupos: dict[int, list[Clientes]]) -> Clientes:
    """Maior segmento identificado pelo k-means."""
    return perfil_brasil(grupos)[0]


#A diferença prática: n1, "estado mais comum" = moda global (São_Paulo nos seus dados de exemplo); 
#na n2, o estado do maior cluster, que pode coincidir ou não. 
#Com one-hot no k-means, clusters tendem a separar por combinações (ex.: comércio+feminino+20+ vs. industria+masculino), então o perfil dominante por cluster carrega uma combinação coerente — mais interessante narrativamente, e é onde o ML aparece de fato no resultado.