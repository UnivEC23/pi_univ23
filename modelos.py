from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import DateTime, String
from dataclasses import dataclass
from init import db, engine
from datetime import datetime  # Importe o módulo datetime
from enum import IntEnum, Enum


class Setor(Enum):
    vazio = 0
    comercio = 1
    servicos = 2
    industria = 3
    outros = 4


class Idade(Enum):
    vazio= 0
    _0 = 1 #0+
    _20 = 2 #20+
    #30 = 3 #30+
    _40 = 3 #40+
    _60 = 4 #60+

#class regiao(Enum):


class Estados(Enum):
    vazio = 0
    Acre = 1
    Alagoas = 2
    Amapá = 3
    Amazonas = 4
    Bahia = 5
    Ceará = 6
    Espírito_Santo = 7
    Goiás = 8
    Maranhão = 9
    Mato_Grosso = 10
    Mato_Grosso_do_Sul = 11
    Minas_Gerais = 12
    Pará = 13
    Paraíba = 14
    Paraná = 15
    Pernambuco = 16
    Piauí = 17
    Rio_de_Janeiro = 18
    Rio_Grande_do_Norte = 19
    Rio_Grande_do_Sul = 20
    Rondônia = 21
    Roraima = 22
    Santa_Catarina = 23
    São_Paulo = 24
    Sergipe = 25
    Tocantins = 26
    Distrito_Federal= 27

class Genero(Enum):
    vazio = 0
    masculino = 1
    feminino = 2
    outro = 3

@dataclass
class Clientes(db.Model):
    id: int
    nome: str
    email: str
    solicit: str
    estados: int
    idade:int
    setor:int
    genero:int

    id = db.Column(db.Integer, unique=True,
                   primary_key=True, autoincrement=True)
    nome = db.Column(db.String(80), unique=False,
                     nullable=True, primary_key=False)
    email = db.Column(db.String(80), unique=False,
                      nullable=True, primary_key=False)
    solicit = db.Column(db.String(500), unique=False,
                        nullable=True, primary_key=False)

    #informa dados
    estados = db.Column(db.Integer, unique=False,
                            nullable=True, primary_key=False)
    idade = db.Column(db.Integer, unique=False,
                                nullable=True, primary_key=False)
    setor = db.Column(db.Integer, unique=False,
                                nullable=True, primary_key=False)
    genero = db.Column(db.Integer, unique=False,
                                nullable=True, primary_key=False)


    def __init__(self, nome:str, email: str, solicit: str, estados: Estados, idade: Idade, setor: Setor, genero: Genero):
            self.nome = nome
            self.email = email
            self.solicit = solicit
            self.estados = estados.value
            self.idade = idade.value
            self.setor = setor.value
            self.genero = genero.value

    def __repr__(self):
        return "<Nome: {}>".format(self.nome)+ " <email: {}>".format(self.email)+ " <estados: {}>".format(Estados(self.estados).name)+ " <idade: {}>".format(Idade(self.idade).name)+ " <setor: {}>".format(Setor(self.setor).name)+ " <genero: {}>".format(Genero(self.genero).name) + "\n <solicit: {}>".format(self.solicit)


@dataclass
class Comentario(db.Model):
    id: int
    autor: str
    texto: str
    data_criacao: datetime

    id = db.Column(db.Integer, unique=True,
                   primary_key=True, autoincrement=True)
    autor = db.Column(db.String(80), nullable=False)
    texto = db.Column(db.String(500), nullable=False)
    # data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    data_criacao = db.Column(db.DateTime, default=datetime.now)

    # def __init__(self, autor:str, texto: str):
    #             self.autor = autor
    #             self.texto = texto

    def __repr__(self):
        return "<Comentario Autor: {}>".format(self.autor) + " <texto: {}>".format(self.texto) + " <data: {}>".format(self.data_criacao)

#MappedAsDataclass, dps init=false

class Base_Tur(DeclarativeBase):
    pass
class Comentario_Turso(Base_Tur):
    __tablename__ = "comentarios"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    autor: Mapped[str] = mapped_column(String(80))
    texto: Mapped[str] = mapped_column(String(500))
    data_criacao: Mapped[datetime] = mapped_column(default=datetime.now)

    def __repr__(self) -> str:
        return "<Comentario Autor: {}>".format(self.autor) + "\n<Comentario Texto: {}>".format(self.texto) + "\n<data: {}>".format(self.data_criacao)

    def serializado(self):
        return {
            'id': self.id,
            'autor': self.autor,
            'texto': self.texto,
            'data_criacao': self.data_criacao,
        }
