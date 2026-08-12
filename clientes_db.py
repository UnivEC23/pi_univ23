# from datetime import datetime
# from flask_sqlalchemy import SQLAlchemy
# from flask import Flask, abort, redirect, render_template, request, jsonify, Response, send_from_directory, url_for
# import sys
# import os
# from interfaces import clientes_sql, clientes_sqla
# from init import app, db, engine
# # from init import client
# from modelos import Comentario, estados, idade, setor, genero
# from sqlalchemy import desc
# from sqlalchemy.orm import Session
# from sqlalchemy import select
# from modelos import Comentario_Turso, Base_Tur


# id_clientes = 0
# tClientes = clientes_sqla()

# login_usuario = "user"
# login_senha = "pass"
# # logado = False
# # debug
# logado = True


# def rodar():
#     tClientes.adicionar("nome", "email", "solicit", estados.Bahia, idade._20, setor.comercio, genero.vazio)
#     # app.run(debug=True, host='localhost', port=5000)


# if __name__ == "__main__":

#     if (len(sys.argv) > 1):
#         if (sys.argv[1] == "sql"):
#             tClientes = clientes_sql()

#     tClientes.criarTabela()
#     with app.app_context():
#         db.create_all()  # crias as tabelas

#     Base_Tur.metadata.create_all(engine)
#     rodar()


from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from modelos import Clientes,Comentario, Estados, Idade, Setor, Genero
from modelos import Comentario_Turso, Base_Tur
from interfaces import clientes_sqla
import sys

tClientes = clientes_sqla()

def lista_clientes() -> list[Clientes]:
    clientes_base : list[Clientes] = [
            Clientes("José abreu","contato@abrenegocios.com.br","Olá, gostaria de ajudar para ampliar minhas vendas",Estados.Alagoas, Idade._0, Setor.comercio, Genero.masculino),
            Clientes("Aliane Kelly","contato@alinebre.com.br","Preciso de orientação sobre marketing da nossa produção.",Estados.Mato_Grosso_do_Sul, Idade._40, Setor.industria, Genero.feminino),
            Clientes("Marçal José","contato@alinebre.com.br","Tenho uma lojinha aqui na minha cidade, estou querendo ampliar a clientela.",Estados.Paraíba, Idade._60, Setor.comercio, Genero.vazio)
        ]
    
    clientes_1_30: list[Clientes]  = [
        Clientes("José Abreu", "jose.abreu@novavendas.com.br", "Gostaria de ajuda para ampliar minhas vendas.", Estados.Alagoas, Idade._20, Setor.comercio, Genero.masculino),
        Clientes("Aliane Kelly", "aliane.kelly@conexaomkt.com.br", "Preciso de orientação para divulgar melhor minha produção.", Estados.Mato_Grosso_do_Sul, Idade._40, Setor.industria, Genero.feminino),
        Clientes("Marçal José", "marcal.jose@lojafacil.com.br", "Quero ampliar minha clientela e melhorar minhas vendas.", Estados.Paraíba, Idade._60, Setor.comercio, Genero.masculino),
        Clientes("Fernanda Oliveira", "fernanda.oliveira@belezaativa.com.br", "Preciso atrair mais clientes para meu negócio.", Estados.São_Paulo, Idade._20, Setor.servicos, Genero.feminino),
        Clientes("Carlos Eduardo", "carlos.eduardo@metalforte.com.br", "Quero aumentar as vendas dos meus produtos.", Estados.Minas_Gerais, Idade._40, Setor.industria, Genero.masculino),
        Clientes("Juliana Martins", "juliana.martins@modabrasil.com.br", "Busco ajuda para conquistar novos clientes.", Estados.Paraná, Idade._20, Setor.comercio, Genero.feminino),
        Clientes("Rafael Souza", "rafael.souza@agromais.com.br", "Gostaria de melhorar a divulgação da minha empresa.", Estados.Goiás, Idade._40, Setor.outros, Genero.masculino),
        Clientes("Camila Rodrigues", "camila.rodrigues@docesdalia.com.br", "Preciso aumentar o alcance dos meus produtos.", Estados.Pernambuco, Idade._20, Setor.comercio, Genero.feminino),
        Clientes("André Luiz", "andre.luiz@constrular.com.br", "Quero atrair mais clientes para minha empresa.", Estados.Bahia, Idade._40, Setor.servicos, Genero.masculino),
        Clientes("Patrícia Gomes", "patricia.gomes@estiloglamour.com.br", "Preciso de estratégias para aumentar minhas vendas.", Estados.Ceará, Idade._40, Setor.comercio, Genero.feminino),
        Clientes("Marcelo Ferreira", "marcelo.ferreira@tecnopecas.com.br", "Quero divulgar melhor meus produtos e vender mais.", Estados.Santa_Catarina, Idade._60, Setor.industria, Genero.masculino),
        Clientes("Larissa Almeida", "larissa.almeida@florarte.com.br", "Gostaria de conquistar novos clientes na região.", Estados.Rio_de_Janeiro, Idade._20, Setor.comercio, Genero.feminino),
        Clientes("Bruno Carvalho", "bruno.carvalho@solucaodigital.com.br", "Preciso ampliar o contato com meus clientes.", Estados.Distrito_Federal, Idade._40, Setor.servicos, Genero.masculino),
        Clientes("Mariana Costa", "mariana.costa@saboresdobrasil.com.br", "Quero aumentar minhas vendas pela internet.", Estados.Piauí, Idade._20, Setor.comercio, Genero.feminino),
        Clientes("Eduardo Mendes", "eduardo.mendes@madeirarte.com.br", "Busco ajuda para divulgar minha empresa.", Estados.Rio_Grande_do_Sul, Idade._60, Setor.industria, Genero.masculino),
        Clientes("Renata Lima", "renata.lima@consultmais.com.br", "Quero melhorar minha comunicação com clientes.", Estados.Espírito_Santo, Idade._40, Setor.servicos, Genero.feminino),
        Clientes("Felipe Santos", "felipe.santos@mercadobompreco.com.br", "Preciso aumentar o movimento da minha loja.", Estados.Pará, Idade._20, Setor.comercio, Genero.masculino),
        Clientes("Aline Barbosa", "aline.barbosa@costurarte.com.br", "Gostaria de alcançar novos clientes e vender mais.", Estados.Maranhão, Idade._40, Setor.industria, Genero.feminino),
        Clientes("Gustavo Rocha", "gustavo.rocha@translogbrasil.com.br", "Quero divulgar melhor meus serviços para empresas.", Estados.Rondônia, Idade._40, Setor.servicos, Genero.masculino),
        Clientes("Bianca Nunes", "bianca.nunes@emporiobela.com.br", "Preciso de ajuda para atrair novos consumidores.", Estados.Sergipe, Idade._20, Setor.comercio, Genero.feminino),
        Clientes("Rodrigo Martins", "rodrigo.martins@pecasamazon.com.br", "Quero aumentar a procura pelos meus produtos.", Estados.Amazonas, Idade._40, Setor.industria, Genero.masculino),
        Clientes("Isabela Freitas", "isabela.freitas@eventomais.com.br", "Busco estratégias para conseguir mais clientes.", Estados.Tocantins, Idade._20, Setor.servicos, Genero.feminino),
        Clientes("Thiago Pereira", "thiago.pereira@campoverde.com.br", "Gostaria de melhorar minhas vendas e divulgação.", Estados.Mato_Grosso, Idade._40, Setor.outros, Genero.masculino),
        Clientes("Carolina Vieira", "carolina.vieira@lojadasflores.com.br", "Quero ampliar minha clientela e fortalecer a marca.", Estados.Acre, Idade._60, Setor.comercio, Genero.feminino),
        Clientes("Leonardo Alves", "leonardo.alves@inovatech.com.br", "Preciso alcançar mais clientes para meus serviços.", Estados.Roraima, Idade._20, Setor.servicos, Genero.masculino),
        Clientes("Beatriz Monteiro", "beatriz.monteiro@artesanalmais.com.br", "Quero vender mais e divulgar melhor meu negócio.", Estados.Amapá, Idade._40, Setor.industria, Genero.feminino),
        Clientes("Daniel Oliveira", "daniel.oliveira@redecomercial.com.br", "Gostaria de atrair mais clientes para minha loja.", Estados.Rio_Grande_do_Norte, Idade._60, Setor.comercio, Genero.masculino),
        Clientes("Priscila Ramos", "priscila.ramos@clinicavida.com.br", "Preciso ampliar a divulgação dos meus serviços.", Estados.São_Paulo, Idade._40, Setor.servicos, Genero.feminino),
        Clientes("Marcelo Batista", "marcelo.batista@fabricaideal.com.br", "Quero conquistar novos clientes para minha indústria.", Estados.Pernambuco, Idade._60, Setor.industria, Genero.masculino),
        Clientes("Natália Castro", "natalia.castro@lojaconecta.com.br", "Busco ajuda para aumentar minhas vendas.", Estados.Paraná, Idade._20, Setor.comercio, Genero.feminino),
    ]
    
    clientes_2_30: list[Clientes]  = [
        Clientes("Amanda Ferreira", "amanda.ferreira@vivamais.com.br", "Quero aumentar minhas vendas e alcançar novos clientes.", Estados.Bahia, Idade._20, Setor.comercio, Genero.feminino),
        Clientes("Ricardo Almeida", "ricardo.almeida@primeindustrial.com.br", "Preciso melhorar a divulgação dos meus produtos.", Estados.São_Paulo, Idade._40, Setor.industria, Genero.masculino),
        Clientes("Vanessa Martins", "vanessa.martins@belezaeestilo.com.br", "Gostaria de atrair mais clientes para meu negócio.", Estados.Ceará, Idade._40, Setor.servicos, Genero.feminino),
        Clientes("Diego Barbosa", "diego.barbosa@mercadobrasil.com.br", "Quero ampliar minha clientela e vender mais.", Estados.Goiás, Idade._20, Setor.comercio, Genero.masculino),
        Clientes("Luciana Ribeiro", "luciana.ribeiro@artesanalbrasil.com.br", "Preciso divulgar melhor minha marca e aumentar vendas.", Estados.Minas_Gerais, Idade._40, Setor.industria, Genero.feminino),
        Clientes("Alexandre Moreira", "alexandre.moreira@solucoesvip.com.br", "Busco ajuda para conquistar novos clientes.", Estados.Rio_de_Janeiro, Idade._60, Setor.servicos, Genero.masculino),
        Clientes("Sabrina Teixeira", "sabrina.teixeira@modafeminina.com.br", "Quero aumentar o alcance da minha loja.", Estados.Pernambuco, Idade._20, Setor.comercio, Genero.feminino),
        Clientes("Marcelo Ribeiro", "marcelo.ribeiro@agroforte.com.br", "Preciso de estratégias para vender mais.", Estados.Mato_Grosso, Idade._40, Setor.outros, Genero.masculino),
        Clientes("Cristiane Lopes", "cristiane.lopes@docesdacidade.com.br", "Gostaria de atrair novos consumidores.", Estados.Pará, Idade._40, Setor.comercio, Genero.feminino),
        Clientes("Fábio Carvalho", "fabio.carvalho@techservice.com.br", "Quero ampliar o contato com meus clientes.", Estados.Distrito_Federal, Idade._40, Setor.servicos, Genero.masculino),
        Clientes("Elaine Souza", "elaine.souza@casadasplantas.com.br", "Preciso aumentar as vendas da minha loja.", Estados.Espírito_Santo, Idade._60, Setor.comercio, Genero.feminino),
        Clientes("Henrique Costa", "henrique.costa@metalurgicabrasil.com.br", "Quero divulgar melhor meus produtos industriais.", Estados.Rio_Grande_do_Sul, Idade._40, Setor.industria, Genero.masculino),
        Clientes("Tatiane Melo", "tatiane.melo@eventosmais.com.br", "Busco novos clientes para ampliar meus serviços.", Estados.Santa_Catarina, Idade._20, Setor.servicos, Genero.feminino),
        Clientes("João Victor Santos", "joao.victor@varejomais.com.br", "Quero melhorar a divulgação e vender mais.", Estados.Paraná, Idade._20, Setor.comercio, Genero.masculino),
        Clientes("Débora Martins", "debora.martins@costurafina.com.br", "Preciso alcançar mais clientes na minha região.", Estados.Maranhão, Idade._40, Setor.industria, Genero.feminino),
        Clientes("Márcio Fernandes", "marcio.fernandes@transportesul.com.br", "Gostaria de divulgar melhor meus serviços.", Estados.Rio_Grande_do_Sul, Idade._60, Setor.servicos, Genero.masculino),
        Clientes("Priscila Andrade", "priscila.andrade@emporiobrasil.com.br", "Quero ampliar minhas vendas pela internet.", Estados.Piauí, Idade._20, Setor.comercio, Genero.feminino),
        Clientes("Sérgio Oliveira", "sergio.oliveira@construmais.com.br", "Busco estratégias para conquistar clientes.", Estados.Tocantins, Idade._60, Setor.industria, Genero.masculino),
        Clientes("Mônica Cardoso", "monica.cardoso@florencanto.com.br", "Quero aumentar a procura pelos meus produtos.", Estados.Sergipe, Idade._40, Setor.comercio, Genero.feminino),
        Clientes("Anderson Lima", "anderson.lima@servicotec.com.br", "Preciso atrair mais empresas para meus serviços.", Estados.Amazonas, Idade._40, Setor.servicos, Genero.masculino),
        Clientes("Gabriela Duarte", "gabriela.duarte@lojaconforto.com.br", "Gostaria de conquistar novos clientes.", Estados.Paraíba, Idade._20, Setor.comercio, Genero.feminino),
        Clientes("Paulo Henrique", "paulo.henrique@fabrileste.com.br", "Quero fortalecer minha marca e aumentar as vendas.", Estados.Mato_Grosso_do_Sul, Idade._40, Setor.industria, Genero.masculino),
        Clientes("Juliana Castro", "juliana.castro@saudebem.com.br", "Preciso divulgar meus serviços para novos clientes.", Estados.Rio_de_Janeiro, Idade._40, Setor.servicos, Genero.feminino),
        Clientes("Rogério Mendes", "rogerio.mendes@supermercadobom.com.br", "Quero aumentar o movimento da minha loja.", Estados.Alagoas, Idade._60, Setor.comercio, Genero.masculino),
        Clientes("Letícia Moura", "leticia.moura@criativamkt.com.br", "Busco ajuda para ampliar minha carteira de clientes.", Estados.Acre, Idade._20, Setor.servicos, Genero.feminino),
        Clientes("Cláudio Nascimento", "claudio.nascimento@industriareal.com.br", "Quero encontrar novos clientes para minha empresa.", Estados.Rondônia, Idade._60, Setor.industria, Genero.masculino),
        Clientes("Renata Fernandes", "renata.fernandes@lojapopular.com.br", "Preciso melhorar minhas vendas e minha divulgação.", Estados.Ceará, Idade._40, Setor.comercio, Genero.feminino),
        Clientes("Wesley Araújo", "wesley.araujo@campobrasil.com.br", "Quero divulgar melhor meu negócio e vender mais.", Estados.Mato_Grosso, Idade._20, Setor.outros, Genero.masculino),
        Clientes("Flávia Correia", "flavia.correia@artesecia.com.br", "Gostaria de alcançar novos clientes para minha marca.", Estados.Amapá, Idade._40, Setor.industria, Genero.feminino),
        Clientes("Roberto Gonçalves", "roberto.goncalves@comercialnorte.com.br", "Quero aumentar minhas vendas e atrair clientes.", Estados.Roraima, Idade._60, Setor.comercio, Genero.masculino),
    ]

    clientes_3_40: list[Clientes]  = [
    Clientes("Ana Paula Martins", "ana.paula.martins@novonegocio.com.br", "Quero aumentar minhas vendas e conquistar clientes.", Estados.São_Paulo, Idade._40, Setor.comercio, Genero.feminino),
    Clientes("Marcos Vinícius Silva", "marcos.silva@industriabrasil.com.br", "Preciso divulgar melhor meus produtos industriais.", Estados.Minas_Gerais, Idade._40, Setor.industria, Genero.masculino),
    Clientes("Carolina Mendes", "carolina.mendes@estilomais.com.br", "Quero atrair novos clientes para minha loja.", Estados.Rio_de_Janeiro, Idade._20, Setor.comercio, Genero.feminino),
    Clientes("Rafael Martins", "rafael.martins@servicofacil.com.br", "Preciso ampliar minha carteira de clientes.", Estados.Bahia, Idade._40, Setor.servicos, Genero.masculino),
    Clientes("Simone Carvalho", "simone.carvalho@docesarte.com.br", "Gostaria de melhorar a divulgação da minha marca.", Estados.Pernambuco, Idade._40, Setor.comercio, Genero.feminino),
    Clientes("Eduardo Ramos", "eduardo.ramos@tecnoindustrial.com.br", "Quero aumentar a procura pelos meus produtos.", Estados.Paraná, Idade._60, Setor.industria, Genero.masculino),
    Clientes("Mariana Lopes", "mariana.lopes@belezaativa.com.br", "Preciso de ajuda para conseguir mais clientes.", Estados.Ceará, Idade._20, Setor.servicos, Genero.feminino),
    Clientes("Guilherme Costa", "guilherme.costa@mercadobom.com.br", "Quero aumentar as vendas da minha loja.", Estados.Goiás, Idade._20, Setor.comercio, Genero.masculino),
    Clientes("Patrícia Nogueira", "patricia.nogueira@artesanalbrasil.com.br", "Busco estratégias para ampliar minhas vendas.", Estados.Maranhão, Idade._60, Setor.industria, Genero.feminino),
    Clientes("Lucas Ferreira", "lucas.ferreira@solucaodigital.com.br", "Quero atrair mais clientes para meus serviços.", Estados.Distrito_Federal, Idade._20, Setor.servicos, Genero.masculino),
    Clientes("Rosângela Alves", "rosangela.alves@lojabemestar.com.br", "Preciso divulgar minha loja para novos clientes.", Estados.Alagoas, Idade._60, Setor.comercio, Genero.feminino),
    Clientes("Thiago Moreira", "thiago.moreira@metalforte.com.br", "Quero ampliar as vendas dos meus produtos.", Estados.Santa_Catarina, Idade._40, Setor.industria, Genero.masculino),
    Clientes("Isabela Martins", "isabela.martins@eventosbrasil.com.br", "Gostaria de conquistar mais clientes para meus serviços.", Estados.Espírito_Santo, Idade._20, Setor.servicos, Genero.feminino),
    Clientes("Fernando Oliveira", "fernando.oliveira@varejomais.com.br", "Quero melhorar a divulgação e vender mais.", Estados.Pará, Idade._40, Setor.comercio, Genero.masculino),
    Clientes("Luciana Freitas", "luciana.freitas@modafina.com.br", "Preciso alcançar mais clientes na minha região.", Estados.Piauí, Idade._40, Setor.comercio, Genero.feminino),
    Clientes("Carlos Henrique", "carlos.henrique@fabrileste.com.br", "Busco novos clientes para minha indústria.", Estados.Rio_Grande_do_Sul, Idade._60, Setor.industria, Genero.masculino),
    Clientes("Beatriz Almeida", "beatriz.almeida@saudebem.com.br", "Quero ampliar o contato com meus clientes.", Estados.Sergipe, Idade._40, Setor.servicos, Genero.feminino),
    Clientes("André Luiz Pereira", "andre.pereira@agroforte.com.br", "Preciso aumentar a divulgação do meu negócio.", Estados.Mato_Grosso, Idade._40, Setor.outros, Genero.masculino),
    Clientes("Camila Rocha", "camila.rocha@emporiobrasil.com.br", "Quero conquistar novos consumidores para minha loja.", Estados.Paraíba, Idade._20, Setor.comercio, Genero.feminino),
    Clientes("José Roberto Lima", "jose.lima@construmais.com.br", "Gostaria de atrair mais clientes para a empresa.", Estados.Tocantins, Idade._60, Setor.industria, Genero.masculino),
    Clientes("Natália Souza", "natalia.souza@florarte.com.br", "Quero aumentar as vendas dos meus produtos.", Estados.Amapá, Idade._20, Setor.comercio, Genero.feminino),
    Clientes("Ricardo Mendes", "ricardo.mendes@transportesul.com.br", "Preciso divulgar melhor meus serviços.", Estados.Rio_Grande_do_Norte, Idade._40, Setor.servicos, Genero.masculino),
    Clientes("Daniela Barbosa", "daniela.barbosa@costurarte.com.br", "Quero ampliar minha clientela e vender mais.", Estados.Mato_Grosso_do_Sul, Idade._40, Setor.industria, Genero.feminino),
    Clientes("Fábio Rodrigues", "fabio.rodrigues@superbom.com.br", "Busco ajuda para aumentar o movimento da loja.", Estados.Rondônia, Idade._40, Setor.comercio, Genero.masculino),
    Clientes("Helena Castro", "helena.castro@consultmais.com.br", "Quero atrair novos clientes para meus serviços.", Estados.Acre, Idade._60, Setor.servicos, Genero.feminino),
    Clientes("Rodrigo Almeida", "rodrigo.almeida@pecasbrasil.com.br", "Preciso melhorar a divulgação dos meus produtos.", Estados.Amazonas, Idade._40, Setor.industria, Genero.masculino),
    Clientes("Viviane Costa", "viviane.costa@lojadasflores.com.br", "Gostaria de ampliar minhas vendas pela internet.", Estados.Roraima, Idade._20, Setor.comercio, Genero.feminino),
    Clientes("Márcio Fernandes", "marcio.fernandes@servicotec.com.br", "Quero conquistar empresas para meus serviços.", Estados.Minas_Gerais, Idade._60, Setor.servicos, Genero.masculino),
    Clientes("Jéssica Oliveira", "jessica.oliveira@docesdalia.com.br", "Preciso alcançar novos clientes para minha marca.", Estados.Pernambuco, Idade._20, Setor.comercio, Genero.feminino),
    Clientes("Paulo Sérgio Santos", "paulo.santos@industriareal.com.br", "Quero aumentar a procura pelos meus produtos.", Estados.Bahia, Idade._60, Setor.industria, Genero.masculino),
    Clientes("Aline Cristina", "aline.cristina@belezaestilo.com.br", "Busco estratégias para melhorar minhas vendas.", Estados.Ceará, Idade._40, Setor.servicos, Genero.feminino),
    Clientes("Alexandre Gomes", "alexandre.gomes@mercadocentral.com.br", "Quero atrair mais consumidores para minha loja.", Estados.Goiás, Idade._40, Setor.comercio, Genero.masculino),
    Clientes("Priscila Mendes", "priscila.mendes@artesecia.com.br", "Preciso divulgar melhor meus produtos e serviços.", Estados.São_Paulo, Idade._20, Setor.outros, Genero.feminino),
    Clientes("Sérgio Carvalho", "sergio.carvalho@madeirarte.com.br", "Quero ampliar o alcance da minha empresa.", Estados.Pará, Idade._60, Setor.industria, Genero.masculino),
    Clientes("Gabriela Fernandes", "gabriela.fernandes@modabrasil.com.br", "Gostaria de conquistar novos clientes para minha loja.", Estados.Santa_Catarina, Idade._20, Setor.comercio, Genero.feminino),
    Clientes("Leonardo Souza", "leonardo.souza@inovatech.com.br", "Preciso aumentar a procura pelos meus serviços.", Estados.Distrito_Federal, Idade._40, Setor.servicos, Genero.masculino),
    Clientes("Mônica Ribeiro", "monica.ribeiro@campoverde.com.br", "Quero melhorar minha divulgação e aumentar vendas.", Estados.Mato_Grosso, Idade._60, Setor.outros, Genero.feminino),
    Clientes("Wellington Santos", "wellington.santos@comercialnorte.com.br", "Busco ajuda para ampliar minha carteira de clientes.", Estados.Rio_Grande_do_Norte, Idade._40, Setor.comercio, Genero.masculino),
    Clientes("Renata Vieira", "renata.vieira@clinicavida.com.br", "Quero divulgar meus serviços para novos clientes.", Estados.Paraná, Idade._40, Setor.servicos, Genero.feminino),
    Clientes("Otávio Martins", "otavio.martins@agropecuariabrasil.com.br", "Preciso aumentar as vendas do meu negócio.", Estados.Acre, Idade._60, Setor.outros, Genero.masculino),
]
    clientes_4_200: list[Clientes]  = [
    Clientes("Adriana Souza", "adriana.souza@lojaprimavera.com.br", "Quero aumentar minhas vendas e atrair clientes.", Estados.São_Paulo, Idade._40, Setor.comercio, Genero.feminino),
    Clientes("Bruno Almeida", "bruno.almeida@metalnova.com.br", "Preciso divulgar melhor meus produtos.", Estados.Minas_Gerais, Idade._40, Setor.industria, Genero.masculino),
    Clientes("Cristina Martins", "cristina.martins@belezaativa.com.br", "Quero conquistar novos clientes para meu negócio.", Estados.Bahia, Idade._20, Setor.servicos, Genero.feminino),
    Clientes("Diego Carvalho", "diego.carvalho@mercadobrasil.com.br", "Preciso aumentar o movimento da minha loja.", Estados.Goiás, Idade._20, Setor.comercio, Genero.masculino),
    Clientes("Elaine Ferreira", "elaine.ferreira@artesul.com.br", "Quero melhorar a divulgação da minha marca.", Estados.Paraná, Idade._40, Setor.industria, Genero.feminino),
    Clientes("Fabiano Ribeiro", "fabiano.ribeiro@servicofacil.com.br", "Busco ajuda para ampliar minha clientela.", Estados.Ceará, Idade._40, Setor.servicos, Genero.masculino),
    Clientes("Gabriela Costa", "gabriela.costa@modafina.com.br", "Quero vender mais e alcançar novos clientes.", Estados.Pernambuco, Idade._20, Setor.comercio, Genero.feminino),
    Clientes("Hugo Martins", "hugo.martins@agroforte.com.br", "Preciso divulgar melhor minha empresa.", Estados.Mato_Grosso, Idade._60, Setor.outros, Genero.masculino),
    Clientes("Ingrid Oliveira", "ingrid.oliveira@docesarte.com.br", "Quero ampliar o alcance dos meus produtos.", Estados.Alagoas, Idade._20, Setor.comercio, Genero.feminino),
    Clientes("João Pedro Lima", "joao.lima@techservicos.com.br", "Preciso atrair mais clientes para meus serviços.", Estados.Distrito_Federal, Idade._20, Setor.servicos, Genero.masculino),
    Clientes("Karina Mendes", "karina.mendes@lojabemestar.com.br", "Quero aumentar as vendas da minha loja.", Estados.Espírito_Santo, Idade._40, Setor.comercio, Genero.feminino),
    Clientes("Leandro Santos", "leandro.santos@fabrileste.com.br", "Busco novos clientes para minha indústria.", Estados.Santa_Catarina, Idade._40, Setor.industria, Genero.masculino),
    Clientes("Marina Alves", "marina.alves@eventomais.com.br", "Quero divulgar meus serviços para mais pessoas.", Estados.Rio_de_Janeiro, Idade._20, Setor.servicos, Genero.feminino),
    Clientes("Nicolas Rocha", "nicolas.rocha@varejofacil.com.br", "Preciso melhorar minhas vendas e divulgação.", Estados.Pará, Idade._20, Setor.comercio, Genero.masculino),
    Clientes("Olívia Nunes", "olivia.nunes@florencanto.com.br", "Quero conquistar novos clientes na região.", Estados.Sergipe, Idade._40, Setor.comercio, Genero.feminino),
    Clientes("Pedro Henrique", "pedro.henrique@metalforte.com.br", "Preciso aumentar a procura pelos produtos.", Estados.Rio_Grande_do_Sul, Idade._40, Setor.industria, Genero.masculino),
    Clientes("Queila Ramos", "queila.ramos@consultmais.com.br", "Quero ampliar minha carteira de clientes.", Estados.Piauí, Idade._40, Setor.servicos, Genero.feminino),
    Clientes("Rafael Gomes", "rafael.gomes@campoverde.com.br", "Busco estratégias para vender mais.", Estados.Tocantins, Idade._40, Setor.outros, Genero.masculino),
    Clientes("Sandra Vieira", "sandra.vieira@emporiobela.com.br", "Preciso atrair mais consumidores para a loja.", Estados.Paraíba, Idade._60, Setor.comercio, Genero.feminino),
    Clientes("Tiago Fernandes", "tiago.fernandes@constrular.com.br", "Quero ampliar o contato com novos clientes.", Estados.Rondônia, Idade._40, Setor.servicos, Genero.masculino),

    Clientes("Úrsula Castro", "ursula.castro@lojadascores.com.br", "Quero aumentar minhas vendas pela internet.", Estados.Maranhão, Idade._40, Setor.comercio, Genero.feminino),
    Clientes("Valter Moreira", "valter.moreira@industriareal.com.br", "Preciso divulgar melhor meus produtos.", Estados.Mato_Grosso_do_Sul, Idade._60, Setor.industria, Genero.masculino),
    Clientes("Wanda Pereira", "wanda.pereira@saudebem.com.br", "Quero conquistar clientes para meus serviços.", Estados.Amazonas, Idade._60, Setor.servicos, Genero.feminino),
    Clientes("Xavier Martins", "xavier.martins@mercadobom.com.br", "Busco ajuda para aumentar as vendas.", Estados.Amapá, Idade._20, Setor.comercio, Genero.masculino),
    Clientes("Yasmin Oliveira", "yasmin.oliveira@artesecia.com.br", "Quero divulgar minha marca para novos clientes.", Estados.Acre, Idade._20, Setor.industria, Genero.feminino),
    Clientes("Zeca Carvalho", "zeca.carvalho@transportesul.com.br", "Preciso ampliar minha base de clientes.", Estados.Rio_Grande_do_Norte, Idade._60, Setor.servicos, Genero.masculino),
    Clientes("Amanda Rodrigues", "amanda.rodrigues@modabrasil.com.br", "Quero aumentar o alcance da minha loja.", Estados.Pernambuco, Idade._20, Setor.comercio, Genero.feminino),
    Clientes("Breno Silva", "breno.silva@pecasbrasil.com.br", "Preciso melhorar a divulgação dos meus produtos.", Estados.Amazonas, Idade._40, Setor.industria, Genero.masculino),
    Clientes("Cecília Duarte", "cecilia.duarte@belezaeestilo.com.br", "Quero atrair mais clientes para meu negócio.", Estados.Rio_de_Janeiro, Idade._40, Setor.servicos, Genero.feminino),
    Clientes("Davi Monteiro", "davi.monteiro@supermercadobom.com.br", "Quero aumentar o movimento do meu comércio.", Estados.Bahia, Idade._20, Setor.comercio, Genero.masculino),
    Clientes("Ester Cardoso", "ester.cardoso@costurafina.com.br", "Busco estratégias para vender mais produtos.", Estados.Maranhão, Idade._60, Setor.industria, Genero.feminino),
    Clientes("Flávio Martins", "flavio.martins@solucaodigital.com.br", "Preciso conquistar mais clientes para meus serviços.", Estados.Goiás, Idade._40, Setor.servicos, Genero.masculino),
    Clientes("Giovana Lopes", "giovana.lopes@docesdalia.com.br", "Quero ampliar minha clientela e minhas vendas.", Estados.Alagoas, Idade._20, Setor.comercio, Genero.feminino),
    Clientes("Henrique Souza", "henrique.souza@agrovale.com.br", "Quero melhorar a divulgação da empresa.", Estados.Mato_Grosso, Idade._60, Setor.outros, Genero.masculino),
    Clientes("Isadora Lima", "isadora.lima@florarte.com.br", "Preciso alcançar novos clientes na região.", Estados.Sergipe, Idade._20, Setor.comercio, Genero.feminino),
    Clientes("Jorge Luiz", "jorge.luiz@metalcenter.com.br", "Quero aumentar as vendas dos meus produtos.", Estados.Minas_Gerais, Idade._60, Setor.industria, Genero.masculino),
    Clientes("Kelly Cristina", "kelly.cristina@eventosul.com.br", "Preciso divulgar melhor meus serviços.", Estados.Santa_Catarina, Idade._40, Setor.servicos, Genero.feminino),
    Clientes("Luiz Fernando", "luiz.fernando@lojacentral.com.br", "Quero atrair mais clientes para minha loja.", Estados.Paraná, Idade._40, Setor.comercio, Genero.masculino),
    Clientes("Manuela Freitas", "manuela.freitas@criativamais.com.br", "Busco ajuda para aumentar minhas vendas.", Estados.Piauí, Idade._20, Setor.outros, Genero.feminino),
    Clientes("Nelson Batista", "nelson.batista@fabricaideal.com.br", "Quero conquistar novos compradores.", Estados.Rio_Grande_do_Sul, Idade._60, Setor.industria, Genero.masculino),

    Clientes("Otávia Mendes", "otavia.mendes@consultoriaativa.com.br", "Quero ampliar minha rede de clientes.", Estados.Espírito_Santo, Idade._40, Setor.servicos, Genero.feminino),
    Clientes("Paulo Roberto", "paulo.roberto@comercialnorte.com.br", "Preciso aumentar as vendas do comércio.", Estados.Roraima, Idade._60, Setor.comercio, Genero.masculino),
    Clientes("Raquel Almeida", "raquel.almeida@artesanatobrasil.com.br", "Quero divulgar melhor meus produtos artesanais.", Estados.Acre, Idade._40, Setor.industria, Genero.feminino),
    Clientes("Samuel Costa", "samuel.costa@servicotec.com.br", "Preciso atrair empresas para meus serviços.", Estados.Tocantins, Idade._20, Setor.servicos, Genero.masculino),
    Clientes("Talita Nascimento", "talita.nascimento@lojapopular.com.br", "Quero melhorar minhas vendas e alcançar clientes.", Estados.Ceará, Idade._20, Setor.comercio, Genero.feminino),
    Clientes("Ulisses Ribeiro", "ulisses.ribeiro@construmais.com.br", "Busco novos clientes para minha empresa.", Estados.Pará, Idade._60, Setor.industria, Genero.masculino),
    Clientes("Valéria Souza", "valeria.souza@clinicavida.com.br", "Quero ampliar a divulgação dos meus serviços.", Estados.São_Paulo, Idade._40, Setor.servicos, Genero.feminino),
    Clientes("William Ferreira", "william.ferreira@mercadovital.com.br", "Preciso aumentar o fluxo de clientes.", Estados.Paraíba, Idade._40, Setor.comercio, Genero.masculino),
    Clientes("Yara Martins", "yara.martins@modaurbana.com.br", "Quero conquistar novos clientes para minha loja.", Estados.Rio_de_Janeiro, Idade._20, Setor.comercio, Genero.feminino),
    Clientes("Zuleica Ramos", "zuleica.ramos@industriaforte.com.br", "Preciso divulgar melhor minha produção.", Estados.Bahia, Idade._60, Setor.industria, Genero.feminino),

    Clientes("Adriano Lopes", "adriano.lopes@varejomais.com.br", "Quero aumentar as vendas do meu comércio.", Estados.Goiás, Idade._40, Setor.comercio, Genero.masculino),
    Clientes("Bárbara Teixeira", "barbara.teixeira@belezaexpress.com.br", "Preciso atrair mais clientes para meu serviço.", Estados.Minas_Gerais, Idade._20, Setor.servicos, Genero.feminino),
    Clientes("Caio Mendes", "caio.mendes@tecnoparts.com.br", "Quero ampliar a procura pelos meus produtos.", Estados.São_Paulo, Idade._20, Setor.industria, Genero.masculino),
    Clientes("Denise Oliveira", "denise.oliveira@docesdavovo.com.br", "Busco ajuda para vender mais.", Estados.Pernambuco, Idade._60, Setor.comercio, Genero.feminino),
    Clientes("Edson Carvalho", "edson.carvalho@agrobrasil.com.br", "Preciso melhorar a divulgação do negócio.", Estados.Mato_Grosso, Idade._60, Setor.outros, Genero.masculino),
    Clientes("Fabiana Souza", "fabiana.souza@eventofacil.com.br", "Quero conseguir mais clientes para meus serviços.", Estados.Bahia, Idade._40, Setor.servicos, Genero.feminino),
    Clientes("Gilberto Alves", "gilberto.alves@industrialeste.com.br", "Quero aumentar a venda dos meus produtos.", Estados.Paraná, Idade._60, Setor.industria, Genero.masculino),
    Clientes("Heloísa Martins", "heloisa.martins@lojabelavista.com.br", "Preciso atrair novos consumidores.", Estados.Ceará, Idade._40, Setor.comercio, Genero.feminino),
    Clientes("Igor Fernandes", "igor.fernandes@techmais.com.br", "Quero ampliar minha carteira de clientes.", Estados.Distrito_Federal, Idade._20, Setor.servicos, Genero.masculino),
    Clientes("Janaina Costa", "janaina.costa@modanobre.com.br", "Busco estratégias para aumentar minhas vendas.", Estados.Santa_Catarina, Idade._40, Setor.comercio, Genero.feminino),
    Clientes("Kleber Santos", "kleber.santos@metalurgicasul.com.br", "Quero conquistar novos clientes industriais.", Estados.Rio_Grande_do_Sul, Idade._40, Setor.industria, Genero.masculino),
    Clientes("Lívia Ramos", "livia.ramos@saudeevida.com.br", "Preciso divulgar meus serviços para mais clientes.", Estados.Rio_de_Janeiro, Idade._20, Setor.servicos, Genero.feminino),
    Clientes("Mateus Rocha", "mateus.rocha@mercadobrasil.com.br", "Quero aumentar o movimento da minha loja.", Estados.Piauí, Idade._20, Setor.comercio, Genero.masculino),
    Clientes("Nádia Pereira", "nadia.pereira@artesul.com.br", "Preciso ampliar o alcance dos produtos.", Estados.Maranhão, Idade._60, Setor.industria, Genero.feminino),
    Clientes("Osvaldo Lima", "osvaldo.lima@transportenorte.com.br", "Quero atrair mais empresas para meu serviço.", Estados.Amazonas, Idade._60, Setor.servicos, Genero.masculino),
    Clientes("Paula Cristina", "paula.cristina@lojaconecta.com.br", "Quero aumentar as vendas da minha loja.", Estados.Pará, Idade._20, Setor.comercio, Genero.feminino),
    Clientes("Renato Gomes", "renato.gomes@fabricaativa.com.br", "Busco ajuda para divulgar minha indústria.", Estados.Espírito_Santo, Idade._40, Setor.industria, Genero.masculino),
    Clientes("Sueli Andrade", "sueli.andrade@consultmais.com.br", "Quero conquistar novos clientes.", Estados.Rondônia, Idade._60, Setor.servicos, Genero.feminino),
    Clientes("Tadeu Martins", "tadeu.martins@comercialbompreco.com.br", "Preciso aumentar minhas vendas.", Estados.Alagoas, Idade._60, Setor.comercio, Genero.masculino),
    Clientes("Verônica Silva", "veronica.silva@florencanto.com.br", "Quero melhorar a divulgação da minha loja.", Estados.Sergipe, Idade._40, Setor.comercio, Genero.feminino),

    Clientes("Adalberto Souza", "adalberto.souza@industriabrasil.com.br", "Quero ampliar minha base de compradores.", Estados.Minas_Gerais, Idade._60, Setor.industria, Genero.masculino),
    Clientes("Bruna Martins", "bruna.martins@belezaurbana.com.br", "Preciso atrair mais clientes.", Estados.São_Paulo, Idade._20, Setor.servicos, Genero.feminino),
    Clientes("César Oliveira", "cesar.oliveira@mercadovale.com.br", "Quero melhorar minhas vendas.", Estados.Goiás, Idade._40, Setor.comercio, Genero.masculino),
    Clientes("Diana Carvalho", "diana.carvalho@modamix.com.br", "Busco novos clientes para minha loja.", Estados.Paraná, Idade._40, Setor.comercio, Genero.feminino),
    Clientes("Elias Ferreira", "elias.ferreira@metalvale.com.br", "Preciso divulgar melhor minha produção.", Estados.Bahia, Idade._60, Setor.industria, Genero.masculino),
    Clientes("Flávia Mendes", "flavia.mendes@eventosmais.com.br", "Quero aumentar a procura pelos meus serviços.", Estados.Pernambuco, Idade._40, Setor.servicos, Genero.feminino),
    Clientes("Gerson Lima", "gerson.lima@agromais.com.br", "Quero ampliar o contato com clientes.", Estados.Mato_Grosso_do_Sul, Idade._60, Setor.outros, Genero.masculino),
    Clientes("Helena Souza", "helena.souza@docesbrasil.com.br", "Preciso aumentar as vendas dos produtos.", Estados.Ceará, Idade._40, Setor.comercio, Genero.feminino),
    Clientes("Ivan Rocha", "ivan.rocha@servicoforte.com.br", "Quero conquistar novos clientes empresariais.", Estados.Tocantins, Idade._60, Setor.servicos, Genero.masculino),
    Clientes("Júlia Almeida", "julia.almeida@lojaviva.com.br", "Busco estratégias para vender mais.", Estados.Paraíba, Idade._20, Setor.comercio, Genero.feminino),
    Clientes("Kauã Pereira", "kaua.pereira@tecnologiaativa.com.br", "Preciso divulgar melhor meus serviços.", Estados.Distrito_Federal, Idade._20, Setor.servicos, Genero.masculino),
    Clientes("Laura Gomes", "laura.gomes@artesanatoarte.com.br", "Quero alcançar novos clientes para minha marca.", Estados.Acre, Idade._40, Setor.industria, Genero.feminino),
    Clientes("Miguel Santos", "miguel.santos@fabricaideal.com.br", "Quero aumentar a procura pelos produtos.", Estados.Santa_Catarina, Idade._20, Setor.industria, Genero.masculino),
    Clientes("Noemi Martins", "noemi.martins@consultoriaativa.com.br", "Preciso ampliar minha carteira de clientes.", Estados.Piauí, Idade._60, Setor.servicos, Genero.feminino),
    Clientes("Orlando Costa", "orlando.costa@varejofacil.com.br", "Quero atrair mais clientes para minha loja.", Estados.Rio_Grande_do_Norte, Idade._60, Setor.comercio, Genero.masculino),
    Clientes("Priscila Souza", "priscila.souza@clinicabem.com.br", "Quero divulgar melhor meus serviços.", Estados.Rio_de_Janeiro, Idade._40, Setor.servicos, Genero.feminino),
    Clientes("Rogério Alves", "rogerio.alves@industriatec.com.br", "Busco ajuda para aumentar as vendas.", Estados.Pará, Idade._60, Setor.industria, Genero.masculino),
    Clientes("Silvana Ribeiro", "silvana.ribeiro@emporiobrasil.com.br", "Preciso conquistar novos consumidores.", Estados.Maranhão, Idade._40, Setor.comercio, Genero.feminino),
    Clientes("Tomás Fernandes", "tomas.fernandes@agroforte.com.br", "Quero melhorar a divulgação do negócio.", Estados.Roraima, Idade._40, Setor.outros, Genero.masculino),
    Clientes("Valentina Lopes", "valentina.lopes@modafina.com.br", "Quero ampliar minhas vendas pela internet.", Estados.Amapá, Idade._20, Setor.comercio, Genero.feminino),

    Clientes("Alberto Mendes", "alberto.mendes@metalnova.com.br", "Preciso aumentar a procura pelos meus produtos.", Estados.Minas_Gerais, Idade._60, Setor.industria, Genero.masculino),
    Clientes("Bianca Ferreira", "bianca.ferreira@eventobrasil.com.br", "Quero atrair mais clientes para meus serviços.", Estados.Bahia, Idade._20, Setor.servicos, Genero.feminino),
    Clientes("Cristiano Lima", "cristiano.lima@mercadovale.com.br", "Quero melhorar o movimento da minha loja.", Estados.Sergipe, Idade._40, Setor.comercio, Genero.masculino),
    Clientes("Daniela Souza", "daniela.souza@costurarte.com.br", "Busco estratégias para aumentar minhas vendas.", Estados.Maranhão, Idade._40, Setor.industria, Genero.feminino),
    Clientes("Evandro Rocha", "evandro.rocha@transportesul.com.br", "Preciso divulgar melhor meus serviços.", Estados.Paraná, Idade._40, Setor.servicos, Genero.masculino),
    Clientes("Fernanda Lopes", "fernanda.lopes@lojacentral.com.br", "Quero conquistar novos clientes para a loja.", Estados.Alagoas, Idade._20, Setor.comercio, Genero.feminino),
    Clientes("Gilson Martins", "gilson.martins@industriaforte.com.br", "Quero ampliar minhas vendas industriais.", Estados.Rio_Grande_do_Sul, Idade._60, Setor.industria, Genero.masculino),
    Clientes("Hortência Alves", "hortencia.alves@saudebem.com.br", "Preciso aumentar a procura pelos meus serviços.", Estados.Espírito_Santo, Idade._60, Setor.servicos, Genero.feminino),
    Clientes("Iago Carvalho", "iago.carvalho@lojabompreco.com.br", "Quero atrair mais consumidores.", Estados.Pernambuco, Idade._20, Setor.comercio, Genero.masculino),
    Clientes("Jéssica Martins", "jessica.martins@docesarte.com.br", "Preciso divulgar melhor minha marca.", Estados.Ceará, Idade._20, Setor.comercio, Genero.feminino),
    Clientes("Kleiton Souza", "kleiton.souza@pecasfortes.com.br", "Quero aumentar a venda dos meus produtos.", Estados.Amazonas, Idade._40, Setor.industria, Genero.masculino),
    Clientes("Lorena Castro", "lorena.castro@belezaativa.com.br", "Busco ajuda para conquistar clientes.", Estados.São_Paulo, Idade._20, Setor.servicos, Genero.feminino),
    Clientes("Moisés Ferreira", "moises.ferreira@construmais.com.br", "Quero ampliar o contato com novos clientes.", Estados.Goiás, Idade._60, Setor.industria, Genero.masculino),
    Clientes("Natasha Gomes", "natasha.gomes@florarte.com.br", "Preciso aumentar as vendas da minha loja.", Estados.Rio_de_Janeiro, Idade._20, Setor.comercio, Genero.feminino),
    Clientes("Osmar Nascimento", "osmar.nascimento@agrovale.com.br", "Quero melhorar a divulgação da empresa.", Estados.Mato_Grosso, Idade._60, Setor.outros, Genero.masculino),
    Clientes("Paloma Ribeiro", "paloma.ribeiro@consultmais.com.br", "Quero conquistar mais clientes para meus serviços.", Estados.Rondônia, Idade._40, Setor.servicos, Genero.feminino),
    Clientes("Quirino Alves", "quirino.alves@fabrileste.com.br", "Preciso divulgar melhor meus produtos.", Estados.Tocantins, Idade._60, Setor.industria, Genero.masculino),
    Clientes("Regina Costa", "regina.costa@modaurbana.com.br", "Quero ampliar minha clientela.", Estados.Paraíba, Idade._60, Setor.comercio, Genero.feminino),
    Clientes("Sandro Martins", "sandro.martins@servicotec.com.br", "Busco novos clientes para minha empresa.", Estados.Distrito_Federal, Idade._40, Setor.servicos, Genero.masculino),
    Clientes("Tânia Oliveira", "tania.oliveira@lojaconecta.com.br", "Quero vender mais e melhorar a divulgação.", Estados.Acre, Idade._60, Setor.comercio, Genero.feminino),

    Clientes("Afonso Pereira", "afonso.pereira@industrialeste.com.br", "Quero aumentar o alcance dos meus produtos.", Estados.Bahia, Idade._60, Setor.industria, Genero.masculino),
    Clientes("Bárbara Nunes", "barbara.nunes@eventomais.com.br", "Preciso atrair mais clientes para meu negócio.", Estados.Santa_Catarina, Idade._20, Setor.servicos, Genero.feminino),
    Clientes("Celso Martins", "celso.martins@mercadobom.com.br", "Quero aumentar as vendas do comércio.", Estados.Mato_Grosso_do_Sul, Idade._60, Setor.comercio, Genero.masculino),
    Clientes("Dalva Ferreira", "dalva.ferreira@artesul.com.br", "Busco ajuda para divulgar meus produtos.", Estados.Piauí, Idade._60, Setor.industria, Genero.feminino),
    Clientes("Ernesto Lima", "ernesto.lima@servicofacil.com.br", "Quero ampliar minha base de clientes.", Estados.Rio_Grande_do_Norte, Idade._60, Setor.servicos, Genero.masculino),
    Clientes("Flávia Cardoso", "flavia.cardoso@lojabela.com.br", "Preciso melhorar minhas vendas.", Estados.Sergipe, Idade._40, Setor.comercio, Genero.feminino),
    Clientes("Geraldo Souza", "geraldo.souza@metalvale.com.br", "Quero conquistar novos compradores.", Estados.Pará, Idade._60, Setor.industria, Genero.masculino),
    Clientes("Heloísa Costa", "heloisa.costa@clinicavida.com.br", "Quero divulgar melhor meus serviços.", Estados.Ceará, Idade._40, Setor.servicos, Genero.feminino),
    Clientes("Ícaro Martins", "icaro.martins@varejomais.com.br", "Preciso atrair novos clientes para a loja.", Estados.Goiás, Idade._20, Setor.comercio, Genero.masculino),
    Clientes("Joana Ribeiro", "joana.ribeiro@docesdalia.com.br", "Quero aumentar o alcance dos meus produtos.", Estados.Alagoas, Idade._40, Setor.comercio, Genero.feminino),
    Clientes("Kleber Almeida", "kleber.almeida@agroforte.com.br", "Busco estratégias para divulgar meu negócio.", Estados.Mato_Grosso, Idade._40, Setor.outros, Genero.masculino),
    Clientes("Lara Souza", "lara.souza@modabrasil.com.br", "Quero conquistar novos clientes para minha loja.", Estados.Paraná, Idade._20, Setor.comercio, Genero.feminino),
    Clientes("Mauro Oliveira", "mauro.oliveira@fabricaideal.com.br", "Preciso aumentar a procura pelos produtos.", Estados.Minas_Gerais, Idade._60, Setor.industria, Genero.masculino),
    Clientes("Neusa Martins", "neusa.martins@consultoriaativa.com.br", "Quero ampliar minha carteira de clientes.", Estados.Rio_de_Janeiro, Idade._60, Setor.servicos, Genero.feminino),
    Clientes("Oto Rodrigues", "oto.rodrigues@comercialnorte.com.br", "Quero melhorar minhas vendas.", Estados.Roraima, Idade._60, Setor.comercio, Genero.masculino),
    Clientes("Paula Mendes", "paula.mendes@belezaurbana.com.br", "Preciso divulgar meus serviços para novos clientes.", Estados.Amapá, Idade._20, Setor.servicos, Genero.feminino),
    Clientes("Ronaldo Santos", "ronaldo.santos@industriareal.com.br", "Quero ampliar as vendas da indústria.", Estados.Acre, Idade._60, Setor.industria, Genero.masculino),
    Clientes("Sônia Carvalho", "sonia.carvalho@lojaviva.com.br", "Busco ajuda para aumentar minhas vendas.", Estados.Tocantins, Idade._60, Setor.comercio, Genero.feminino),
    Clientes("Túlio Fernandes", "tulio.fernandes@transportesul.com.br", "Quero conquistar mais clientes empresariais.", Estados.Amazonas, Idade._40, Setor.servicos, Genero.masculino),
    Clientes("Valquíria Lima", "valquiria.lima@artesanatobrasil.com.br", "Preciso melhorar a divulgação da minha marca.", Estados.Pernambuco, Idade._60, Setor.industria, Genero.feminino),

    Clientes("Ariovaldo Souza", "ariovaldo.souza@mercadovale.com.br", "Quero aumentar o movimento da minha loja.", Estados.Bahia, Idade._60, Setor.comercio, Genero.masculino),
    Clientes("Beatriz Martins", "beatriz.martins@eventofacil.com.br", "Preciso atrair mais clientes para meus serviços.", Estados.São_Paulo, Idade._20, Setor.servicos, Genero.feminino),
    Clientes("Cássio Pereira", "cassio.pereira@metalnova.com.br", "Busco ajuda para divulgar meus produtos.", Estados.Santa_Catarina, Idade._40, Setor.industria, Genero.masculino),
    Clientes("Débora Souza", "debora.souza@modamix.com.br", "Quero ampliar minha clientela.", Estados.Pernambuco, Idade._40, Setor.comercio, Genero.feminino),
    Clientes("Everaldo Costa", "everaldo.costa@agrobrasil.com.br", "Preciso aumentar minhas vendas.", Estados.Mato_Grosso, Idade._60, Setor.outros, Genero.masculino),
    Clientes("Fátima Almeida", "fatima.almeida@saudeevida.com.br", "Quero conquistar novos clientes.", Estados.Ceará, Idade._60, Setor.servicos, Genero.feminino),
    Clientes("Gustavo Martins", "gustavo.martins@lojacentral.com.br", "Quero melhorar a divulgação da loja.", Estados.Pará, Idade._20, Setor.comercio, Genero.masculino),
    Clientes("Ivone Ribeiro", "ivone.ribeiro@costurafina.com.br", "Busco estratégias para vender mais.", Estados.Maranhão, Idade._60, Setor.industria, Genero.feminino),
    Clientes("Joaquim Alves", "joaquim.alves@servicoforte.com.br", "Quero ampliar o contato com clientes.", Estados.Rio_Grande_do_Sul, Idade._60, Setor.servicos, Genero.masculino),
    Clientes("Larissa Nascimento", "larissa.nascimento@docesarte.com.br", "Preciso divulgar melhor meus produtos.", Estados.Paraíba, Idade._20, Setor.comercio, Genero.feminino),
    Clientes("Marcelo Duarte", "marcelo.duarte@industriaativa.com.br", "Quero aumentar a procura pelos produtos.", Estados.Espírito_Santo, Idade._40, Setor.industria, Genero.masculino),
    Clientes("Nair Gomes", "nair.gomes@lojabemestar.com.br", "Quero atrair mais clientes para a loja.", Estados.Alagoas, Idade._60, Setor.comercio, Genero.feminino),
    Clientes("Osvaldo Martins", "osvaldo.martins@consultmais.com.br", "Preciso divulgar melhor meus serviços.", Estados.Rondônia, Idade._60, Setor.servicos, Genero.masculino),
    Clientes("Rita de Cássia", "rita.cassia@florarte.com.br", "Quero aumentar as vendas dos produtos.", Estados.Sergipe, Idade._60, Setor.comercio, Genero.feminino),
    Clientes("Sebastião Lima", "sebastiao.lima@fabrileste.com.br", "Busco novos clientes para minha indústria.", Estados.Rio_Grande_do_Norte, Idade._60, Setor.industria, Genero.masculino),
    Clientes("Teresa Martins", "teresa.martins@eventosul.com.br", "Quero ampliar minha carteira de clientes.", Estados.Paraná, Idade._60, Setor.servicos, Genero.feminino),
    Clientes("Ubirajara Costa", "ubirajara.costa@mercadobrasil.com.br", "Preciso aumentar o movimento da loja.", Estados.Amazonas, Idade._60, Setor.comercio, Genero.masculino),
    Clientes("Vera Lúcia", "vera.lucia@modafina.com.br", "Quero conquistar novos consumidores.", Estados.Goiás, Idade._60, Setor.comercio, Genero.feminino),
    Clientes("Wagner Ferreira", "wagner.ferreira@metalforte.com.br", "Quero divulgar melhor minha produção.", Estados.Minas_Gerais, Idade._40, Setor.industria, Genero.masculino),
    Clientes("Zenaide Alves", "zenaide.alves@clinicavida.com.br", "Preciso atrair mais clientes para meus serviços.", Estados.Piauí, Idade._60, Setor.servicos, Genero.feminino),

    Clientes("Alexandre Ribeiro", "alexandre.ribeiro@varejofacil.com.br", "Quero aumentar minhas vendas.", Estados.Tocantins, Idade._40, Setor.comercio, Genero.masculino),
    Clientes("Amanda Castro", "amanda.castro@artesecia.com.br", "Busco ajuda para ampliar minha clientela.", Estados.Amapá, Idade._20, Setor.industria, Genero.feminino),
    Clientes("Bernardo Souza", "bernardo.souza@techmais.com.br", "Quero atrair novos clientes para meus serviços.", Estados.Distrito_Federal, Idade._20, Setor.servicos, Genero.masculino),
    Clientes("Clara Martins", "clara.martins@lojaviva.com.br", "Preciso melhorar a divulgação da minha loja.", Estados.Rio_de_Janeiro, Idade._20, Setor.comercio, Genero.feminino),
    Clientes("Douglas Pereira", "douglas.pereira@agroforte.com.br", "Quero ampliar o alcance da empresa.", Estados.Mato_Grosso_do_Sul, Idade._40, Setor.outros, Genero.masculino),
    Clientes("Elisa Rodrigues", "elisa.rodrigues@belezaativa.com.br", "Quero aumentar a procura pelos meus serviços.", Estados.Espírito_Santo, Idade._40, Setor.servicos, Genero.feminino),
    Clientes("Fabrício Lima", "fabricio.lima@fabricaideal.com.br", "Preciso divulgar melhor meus produtos.", Estados.São_Paulo, Idade._40, Setor.industria, Genero.masculino),
    Clientes("Graziella Costa", "graziella.costa@emporiobela.com.br", "Quero conquistar novos clientes para a loja.", Estados.Ceará, Idade._20, Setor.comercio, Genero.feminino),
    Clientes("Heitor Alves", "heitor.alves@servicotec.com.br", "Busco estratégias para ampliar minhas vendas.", Estados.Rio_Grande_do_Sul, Idade._40, Setor.servicos, Genero.masculino),
    Clientes("Isabel Ferreira", "isabel.ferreira@docesdalia.com.br", "Preciso aumentar as vendas dos meus produtos.", Estados.Bahia, Idade._60, Setor.comercio, Genero.feminino),
    Clientes("Jonas Martins", "jonas.martins@metalcenter.com.br", "Quero conquistar novos compradores.", Estados.Pará, Idade._60, Setor.industria, Genero.masculino),
    Clientes("Lúcia Helena", "lucia.helena@consultmais.com.br", "Quero ampliar minha rede de clientes.", Estados.Maranhão, Idade._60, Setor.servicos, Genero.feminino),
    Clientes("Murilo Souza", "murilo.souza@mercadobom.com.br", "Preciso atrair mais clientes para a loja.", Estados.Pernambuco, Idade._20, Setor.comercio, Genero.masculino),
    Clientes("Nicole Almeida", "nicole.almeida@modaurbana.com.br", "Quero vender mais e divulgar minha marca.", Estados.Santa_Catarina, Idade._20, Setor.comercio, Genero.feminino),
    Clientes("Otávio Ribeiro", "otavio.ribeiro@industriareal.com.br", "Busco ajuda para aumentar minhas vendas.", Estados.Mato_Grosso, Idade._40, Setor.industria, Genero.masculino),
    Clientes("Priscila Nunes", "priscila.nunes@eventomais.com.br", "Preciso conquistar mais clientes para meus serviços.", Estados.Paraná, Idade._40, Setor.servicos, Genero.feminino),
    Clientes("Rafael Duarte", "rafael.duarte@lojacentral.com.br", "Quero melhorar o movimento do comércio.", Estados.Alagoas, Idade._20, Setor.comercio, Genero.masculino),
    Clientes("Sabrina Martins", "sabrina.martins@artesanatobrasil.com.br", "Quero divulgar melhor meus produtos.", Estados.Acre, Idade._40, Setor.industria, Genero.feminino),
    Clientes("Túlio Nascimento", "tulio.nascimento@transportesul.com.br", "Quero ampliar minha carteira de clientes.", Estados.Rondônia, Idade._40, Setor.servicos, Genero.masculino),
    Clientes("Viviane Costa", "viviane.costa@florarte.com.br", "Preciso aumentar as vendas da minha loja.", Estados.Sergipe, Idade._40, Setor.comercio, Genero.feminino),

    Clientes("Anderson Souza", "anderson.souza@metalnova.com.br", "Quero melhorar a divulgação dos produtos.", Estados.Minas_Gerais, Idade._40, Setor.industria, Genero.masculino),
    Clientes("Brenda Oliveira", "brenda.oliveira@belezaeestilo.com.br", "Preciso atrair mais clientes.", Estados.Bahia, Idade._20, Setor.servicos, Genero.feminino),
    Clientes("Cauê Martins", "caue.martins@mercadovale.com.br", "Quero aumentar as vendas do comércio.", Estados.Goiás, Idade._20, Setor.comercio, Genero.masculino),
    Clientes("Débora Costa", "debora.costa@costurarte.com.br", "Busco novos clientes para minha marca.", Estados.Maranhão, Idade._40, Setor.industria, Genero.feminino),
    Clientes("Emerson Silva", "emerson.silva@servicofacil.com.br", "Quero divulgar melhor meus serviços.", Estados.Ceará, Idade._40, Setor.servicos, Genero.masculino),
    Clientes("Flávia Gomes", "flavia.gomes@lojapopular.com.br", "Preciso aumentar minha clientela.", Estados.Pernambuco, Idade._40, Setor.comercio, Genero.feminino),
    Clientes("Geraldo Ferreira", "geraldo.ferreira@fabrileste.com.br", "Quero ampliar as vendas da indústria.", Estados.Rio_Grande_do_Sul, Idade._60, Setor.industria, Genero.masculino),
    Clientes("Heloísa Carvalho", "heloisa.carvalho@clinicavida.com.br", "Quero conquistar novos clientes para os serviços.", Estados.São_Paulo, Idade._40, Setor.servicos, Genero.feminino),
    Clientes("Igor Mendes", "igor.mendes@mercadobrasil.com.br", "Quero atrair mais consumidores para a loja.", Estados.Pará, Idade._20, Setor.comercio, Genero.masculino),
    Clientes("Jéssica Almeida", "jessica.almeida@docesarte.com.br", "Preciso melhorar a divulgação da marca.", Estados.Piauí, Idade._20, Setor.comercio, Genero.feminino),
    Clientes("Kelvin Santos", "kelvin.santos@agrovale.com.br", "Quero ampliar o contato com meus clientes.", Estados.Mato_Grosso, Idade._20, Setor.outros, Genero.masculino),
    Clientes("Letícia Martins", "leticia.martins@modafina.com.br", "Busco estratégias para vender mais.", Estados.Paraíba, Idade._20, Setor.comercio, Genero.feminino),
    Clientes("Márcio Souza", "marcio.souza@industrialeste.com.br", "Preciso atrair novos compradores.", Estados.Espírito_Santo, Idade._60, Setor.industria, Genero.masculino),
    Clientes("Nathalia Ribeiro", "nathalia.ribeiro@eventosul.com.br", "Quero aumentar a procura pelos meus serviços.", Estados.Santa_Catarina, Idade._20, Setor.servicos, Genero.feminino),
    Clientes("Oscar Lima", "oscar.lima@varejomais.com.br", "Quero melhorar minhas vendas.", Estados.Roraima, Idade._60, Setor.comercio, Genero.masculino),
    Clientes("Paola Fernandes", "paola.fernandes@lojabela.com.br", "Preciso conquistar novos clientes.", Estados.Amapá, Idade._20, Setor.comercio, Genero.feminino),
    Clientes("Rômulo Costa", "romulo.costa@metalforte.com.br", "Busco ajuda para divulgar minha indústria.", Estados.Amazonas, Idade._40, Setor.industria, Genero.masculino),
    Clientes("Samara Souza", "samara.souza@consultmais.com.br", "Quero ampliar minha carteira de clientes.", Estados.Tocantins, Idade._40, Setor.servicos, Genero.feminino),
    Clientes("Valdemar Alves", "valdemar.alves@comercialnorte.com.br", "Quero aumentar as vendas da loja.", Estados.Rio_Grande_do_Norte, Idade._60, Setor.comercio, Genero.masculino),
    Clientes("Yasmin Ferreira", "yasmin.ferreira@florarte.com.br", "Preciso divulgar melhor meus produtos.", Estados.Sergipe, Idade._20, Setor.comercio, Genero.feminino),

    Clientes("Adriano Martins", "adriano.martins@fabricaativa.com.br", "Quero conquistar novos clientes para a indústria.", Estados.Bahia, Idade._40, Setor.industria, Genero.masculino),
    Clientes("Bruna Carvalho", "bruna.carvalho@saudebem.com.br", "Preciso aumentar a procura pelos meus serviços.", Estados.Rio_de_Janeiro, Idade._20, Setor.servicos, Genero.feminino),
    Clientes("Cláudio Souza", "claudio.souza@lojacentral.com.br", "Quero ampliar o movimento da minha loja.", Estados.Paraná, Idade._60, Setor.comercio, Genero.masculino),
    Clientes("Daniela Lima", "daniela.lima@artesul.com.br", "Busco ajuda para aumentar minhas vendas.", Estados.Minas_Gerais, Idade._40, Setor.industria, Genero.feminino),
    Clientes("Edmilson Costa", "edmilson.costa@servicotec.com.br", "Quero atrair empresas para meus serviços.", Estados.Distrito_Federal, Idade._60, Setor.servicos, Genero.masculino),
    Clientes("Fabiana Martins", "fabiana.martins@modabrasil.com.br", "Preciso conquistar novos clientes.", Estados.Ceará, Idade._40, Setor.comercio, Genero.feminino),
    Clientes("Gilmar Souza", "gilmar.souza@agroforte.com.br", "Quero divulgar melhor meu negócio.", Estados.Mato_Grosso_do_Sul, Idade._60, Setor.outros, Genero.masculino),
    Clientes("Helena Ribeiro", "helena.ribeiro@docesdalia.com.br", "Quero aumentar as vendas dos meus produtos.", Estados.Alagoas, Idade._60, Setor.comercio, Genero.feminino),
    Clientes("Ítalo Mendes", "italo.mendes@metalcenter.com.br", "Preciso ampliar minha base de compradores.", Estados.Santa_Catarina, Idade._20, Setor.industria, Genero.masculino),
    Clientes("Juliana Souza", "juliana.souza@eventomais.com.br", "Quero divulgar melhor meus serviços.", Estados.Pernambuco, Idade._20, Setor.servicos, Genero.feminino),
    Clientes("Levi Carvalho", "levi.carvalho@mercadobom.com.br", "Quero aumentar o fluxo de clientes.", Estados.Goiás, Idade._20, Setor.comercio, Genero.masculino),
    Clientes("Michele Alves", "michele.alves@lojaviva.com.br", "Preciso melhorar minhas vendas.", Estados.São_Paulo, Idade._40, Setor.comercio, Genero.feminino),
    Clientes("Nilton Fernandes", "nilton.fernandes@fabrileste.com.br", "Quero divulgar melhor meus produtos.", Estados.Rio_Grande_do_Sul, Idade._60, Setor.industria, Genero.masculino),
    Clientes("Olga Martins", "olga.martins@clinicavida.com.br", "Busco novos clientes para meus serviços.", Estados.Espírito_Santo, Idade._60, Setor.servicos, Genero.feminino),
    Clientes("Pablo Souza", "pablo.souza@varejofacil.com.br", "Quero ampliar minhas vendas.", Estados.Pará, Idade._20, Setor.comercio, Genero.masculino),
    Clientes("Rafaela Costa", "rafaela.costa@florencanto.com.br", "Preciso aumentar o alcance da minha loja.", Estados.Sergipe, Idade._20, Setor.comercio, Genero.feminino),
    Clientes("Samuel Martins", "samuel.martins@industriareal.com.br", "Quero conquistar novos clientes industriais.", Estados.Maranhão, Idade._40, Setor.industria, Genero.masculino),
    Clientes("Tatiana Almeida", "tatiana.almeida@consultmais.com.br", "Quero ampliar minha carteira de clientes.", Estados.Rondônia, Idade._40, Setor.servicos, Genero.feminino),
    Clientes("Ubiratan Souza", "ubiratan.souza@comercialnorte.com.br", "Preciso aumentar as vendas do comércio.", Estados.Roraima, Idade._60, Setor.comercio, Genero.masculino),
    Clientes("Viviane Martins", "viviane.martins@artesanatobrasil.com.br", "Quero divulgar melhor meus produtos.", Estados.Acre, Idade._40, Setor.industria, Genero.feminino),
]


    return clientes_1_30+clientes_2_30 + clientes_3_40

def deletar_clientes(): #testar dps
    engine = create_engine('sqlite:///db_dev.db')
    session = Session(engine)

    # clientes = session.query(Clientes).all()
    # Clientes.metadata.drop_all()
    session.query(Clientes).delete()
    session.commit()
    count = session.query(Clientes).count()
    if(count==0):
        print("clientes vazio")
    else:
        print("erro ao tentar limpar Clientes.")
    session.close()

def adicionar_clientes():
    engine = create_engine('sqlite:///db_dev.db')
    session = Session(engine)

    clientes = lista_clientes()

    for c in clientes:
        session.add(c)
    session.commit()

def ver_clientes():
    engine = create_engine('sqlite:///db_dev.db')
    session = Session(engine)

    clientes = session.query(Clientes).all()
    for c in clientes:
        print(c)
    session.close()  


if __name__ == "__main__":
    if (len(sys.argv) > 1):
            if (sys.argv[1] == "ver"):
                 ver_clientes()
            elif (sys.argv[1] == "adi"):
                 adicionar_clientes()
            elif (sys.argv[1] == "del"):
                deletar_clientes()
    else:
        print("comandos ver, adi, del.")