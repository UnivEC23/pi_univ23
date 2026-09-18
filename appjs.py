from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, abort, redirect, render_template, request, jsonify, Response, send_from_directory, url_for
import sys
import os
from interfaces import clientes_sql, clientes_sqla
from init import app, db, engine
# from init import client
from modelos import Comentario, Visitas_Turso
from sqlalchemy import desc
from sqlalchemy.orm import Session
from sqlalchemy import select
from modelos import Comentario_Turso, Base_Tur


id_clientes = 0
tClientes = clientes_sqla()

login_usuario = "user"
login_senha = "pass"
# logado = False
# debug
logado = True
# implementação anterior: contador acumulado
# def incrementar_visitas():
#     with Session(engine) as session:
#         visita = session.scalar(select(Visitas_Turso).limit(1))
#
#         if visita is None:
#             visita = Visitas_Turso(quantidade=1)
#             session.add(visita)
#         else:
#             visita.quantidade += 1
#
#         session.commit()


# nova implementação: registra cada acesso com data e horário
def registrar_visita():
    with Session(engine) as session:
        visita = Visitas_Turso()
        session.add(visita)
        session.commit()

@app.route('/api/visitas', methods=['GET'])
def api_visitas():
    with Session(engine) as session:
        visitas = session.scalars(
            select(Visitas_Turso).order_by(Visitas_Turso.data_hora.desc())
        ).all()

        return jsonify([
            {
                "id": visita.id,
                "data_hora": visita.data_hora.isoformat() if visita.data_hora else None
            }
            for visita in visitas
        ])

@app.route('/', methods=['GET'])
def home():
    registrar_visita()
    comentarios = pegar_comentarios_tur()
    # if request.method == 'GET':
    # return render_template('indexjs.html', comentarios=comentarios)
    return send_from_directory('frontend/dist/', 'index.html')
    # elif request.method == 'POST':
    #     novo = request.form
    #     if not novo.get("nome") or not novo.get("email") or not novo.get("solicit"):
    #         return render_template('indexjs.html', form_error="Por favor, preencha todos os campos do formulário.", comentarios=comentarios)

    # tClientes.adicionar(novo.get("nome"), novo.get(
    #     "email"), novo.get("solicit"))
    # return render_template('indexjs.html', comentarios=comentarios)


# @app.route('/clientes', methods=['POST'])
# def clientes():
#     login = request.form
#     # if not login.get("username") or not login.get("password"):
#     #     return render_template('indexjs.html', login_error="Por favor, preencha todos os campos do login.", comentarios=pegar_comentarios())

#     if login.get("username") == login_usuario and login.get("password") == login_senha:
#         return render_template('clientes.html')
#     else:
#         return render_template('indexjs.html', login_error="Usuário ou senha incorretos.", comentarios=pegar_comentarios())

# adicionado para testes sem login


# @app.route('/clientes.html', methods=['GET'])
@app.route('/clientes', methods=['GET'])
def clientesget():
    if logado == True:
        # return render_template('clientes.html')
        return send_from_directory('frontend/dist/', 'clientes.html')
    else:
        abort(401)
        # return jsonify({'msg': 'Acesso não autorizado!'}), 401


# --------api login-----------------


@app.route('/api/login', methods=['POST'])
def login():
    global logado
    try:
        data = request.get_json()
        usern = data.get('usern')
        passw = data.get('passw')

        if usern == login_usuario and passw == login_senha:
            # return clientesget(), 200
            logado = True
            return jsonify({'rota': url_for('clientesget')}), 200
            # return redirect(url_for('clientesget'))
            # with app.app_context():
            # return render_template('clientes.html')
        else:
            print('login ou senha incorretos!')
            return jsonify({'msg': 'login ou senha incorretos!'}), 401
    except Exception as e:
        print('Erro ao tentar login: ' + e)
        return 500


@app.route('/api/deslogin', methods=['POST'])
def deslogin():
    global logado
    logado = False
    # try:
    # print("saindo")
    # return redirect(url_for('home'))
    return jsonify({'rota': url_for('home')}), 200
    # return 200

    # except Exception as e:
    #     print('Erro ao tentar realizas deslogin: ' + e)
    #     return 500
# ------------------------------


# --------api clientes------------------

@app.route('/api/clientes', methods=['GET'])
def clientesGet():
    return tClientes.pegarTodos()


@app.route('/api/clientes', methods=['POST'])
def clientesPost():
    nome = request.json["nome"]
    email = request.json["email"]
    solicit = request.json["solicit"]
    estados = request.json["estados"]
    idade = request.json["idade"]
    setor = request.json["setor"]
    genero = request.json["genero"]

    print("\n\napi/clientes", nome, email, solicit, estados, idade, setor, genero)

    return tClientes.adicionar(nome, email, solicit, estados, idade, setor, genero)


@app.route('/api/clientes', methods=['DELETE'])
def clientesDel():
    # pegando nome
    nome = request.json["nome"]
    return tClientes.deletar(nome)

# --------api comentarios-----------------


def pegar_comentarios_tur():
    with Session(engine) as session:
        try:
            operação = select(Comentario_Turso)
            comentários = session. scalars(select(Comentario_Turso)).all()

            print("\n\nOs comentários são:")
            for item in session.scalars(operação):
                print(item)
            # print("\n\n")

            return comentários
            # return session.scalars(operação)
        except Exception as e:
            print("Erro ao buscar comentários:", e)
            return []


@app.route('/api/comentarios', methods=['POST'])
def comentariosPost_tur():
    with Session(engine) as session:
        try:
            data = request.get_json()
            autor = data.get('autor')
            texto = data.get('texto')

            # if not autor or not texto:
            #     return jsonify({'erro': 'Autor e texto são obrigatórios.'})

            novo_comentario = Comentario_Turso(autor=autor, texto=texto)
            # print(novo_comentario)
            session.add(novo_comentario)
            session.commit()

            # return jsonify({"error": "Incorrect credentials"}), 401

            # return jsonify({'msg': 'Comentário adicionado com sucesso!'}), 201
            comentarios = pegar_comentarios_tur()
            return render_template('indexjs.html', comentarios=comentarios)
        except Exception as e:
            print('Erro ao adicionar comentário: ' + e)
            return 500


# @app.route('/api/comentarios', methods=['POST'])
def comentariosPost():
    try:
        data = request.get_json()
        autor = data.get('autor')
        texto = data.get('texto')

        # if not autor or not texto:
        #     return jsonify({'erro': 'Autor e texto são obrigatórios.'})

        novo_comentario = Comentario(autor=autor, texto=texto)
        db.session.add(novo_comentario)
        db.session.commit()
        # return jsonify({"error": "Incorrect credentials"}), 401

        # return jsonify({'msg': 'Comentário adicionado com sucesso!'}), 201
        comentarios = pegar_comentarios()
        return render_template('indexjs.html', comentarios=comentarios)
    except Exception as e:
        print('Erro ao adicionar comentário: ' + e)
        return 500


@app.route('/api/comentarios', methods=['GET'])
def comentariosGet():
    try:
        comentarios = pegar_comentarios_tur()
        # clientes = Clientes.query.all()

        return jsonify([cmt.serializado() for cmt in comentarios]), 200
    except Exception as e:
        print("erro ao GET Clientes")
        print(e)
        return {}, 500
    # try:
    #     data = request.get_json()
    #     autor = data.get('autor')
    #     texto = data.get('texto')

    #     # if not autor or not texto:
    #     #     return jsonify({'erro': 'Autor e texto são obrigatórios.'})

    #     novo_comentario = Comentario(autor=autor, texto=texto)
    #     db.session.add(novo_comentario)
    #     db.session.commit()
    #     # return jsonify({"error": "Incorrect credentials"}), 401

    #     return jsonify({'msg': 'Comentário adicionado com sucesso!'}), 201
    # except Exception as e:
    #     print('Erro ao pegar comentários: ' + e)
    #     return 500


@app.route('/api/comentarios', methods=['DELETE'])
def comentariosDel_tur():
    with Session(engine) as session:
        try:
            autor = request.json["autor"]
            # data = request.json["data"]
            # dTime = datetime.strptime(data, )
            # print(data)
            # se filtrar pelo primeiro---
            # cmt = Comentario.query.filter_by(data_criacao=dTime).first()
            # db.session.delete(cmt)
            # ---

            # se pegar todos----
            # cmts = Comentario.query.filter_by(autor=autor).all()
            cmts = session. scalars(select(Comentario_Turso).where(
                Comentario_Turso.autor == autor)).all()
            for c in cmts:
                session.delete(c)
            # ----

            session.commit()
            # client.sync()
            return {}, 200
        except Exception as e:
            print("erro ao deletar comentário")
            print(e)
            return {}, 500


# @app.route('/api/comentarios', methods=['DELETE'])
def comentariosDel():
    try:
        autor = request.json["autor"]
        # data = request.json["data"]
        # dTime = datetime.strptime(data, )
        # print(data)
        # se filtrar pelo primeiro---
        # cmt = Comentario.query.filter_by(data_criacao=dTime).first()
        # db.session.delete(cmt)
        # ---

        # se pegar todos----
        cmts = Comentario.query.filter_by(autor=autor).all()
        for c in cmts:
            db.session.delete(c)
        # ----

        db.session.commit()
        return {}, 200
    except Exception as e:
        print("erro ao deletar comentário")
        print(e)
        return {}, 500

# ------------------------------

# --------api orçamento-----------------


@app.route('/api/orca', methods=['POST'])
def adicionar_orçamento():
    try:
        data = request.get_json()
        nome = data.get('nome')
        email = data.get('email')
        solicit = data.get('solicit')
        estados = request.json["estados"]
        idade = request.json["idade"]
        setor = request.json["setor"]
        genero = request.json["genero"]

        #print(nome, email, solicit)

        tClientes.adicionar(nome, email, solicit, estados, idade, setor, genero)

        return jsonify({'msg': 'Orçamento adicionado com sucesso!'}), 201
    except Exception as e:
        print('Erro ao adicionar orçamento: ' + e)
        return 500
# ------------------------------


def rodar():
    # port = int(os.environ.get('PORT', 5000))
    # app.run(debug=True, host='0.0.0.0', port=port)
    # app.run(debug=True, host='0.0.0.0', port=5000)
    # app.run(debug=True, host='127.0.0.1', port=5000)
    app.run(debug=True, host='localhost', port=5000)
    # app.run()


def pegar_comentarios():
    with app.app_context():
        try:
            # comentarios = Comentario.query.order_by(
            #     desc(Comentario.data_criacao)).limit(3).all()
            comentarios = Comentario.query.order_by(
                desc(Comentario.data_criacao)).all()
            return comentarios
        except Exception as e:
            print("Erro ao buscar comentários:", e)
            return []


if __name__ == "__main__":

    if (len(sys.argv) > 1):
        if (sys.argv[1] == "sql"):
            tClientes = clientes_sql()

    tClientes.criarTabela() # testar dps.
    # with app.app_context():
    #     db.create_all()  # crias as tabelas

    Base_Tur.metadata.create_all(engine)
    rodar()
