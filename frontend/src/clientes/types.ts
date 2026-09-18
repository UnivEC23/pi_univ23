export enum estados{
	vazio = 0,
    Acre = 1,
    Alagoas = 2,
    Amapá = 3,
    Amazonas = 4,
    Bahia = 5,
    Ceará = 6,
    Espírito_Santo = 7,
    Goiás = 8,
    Maranhão = 9,
    Mato_Grosso = 10,
    Mato_Grosso_do_Sul = 11,
    Minas_Gerais = 12,
    Pará = 13,
    Paraíba = 14,
    Paraná = 15,
    Pernambuco = 16,
    Piauí = 17,
    Rio_de_Janeiro = 18,
    Rio_Grande_do_Norte = 19,
    Rio_Grande_do_Sul = 20,
    Rondônia = 21,
    Roraima = 22,
    Santa_Catarina = 23,
    São_Paulo = 24,
    Sergipe = 25,
    Tocantins = 26,
    Distrito_Federal= 27
}

export function estados_str(valor:estados):string{
switch (valor) {
        case estados.vazio:
            return "Vazio";
        case estados.Acre:
            return "Acre";
        case estados.Alagoas:
            return "Alagoas";
        case estados.Amapá:
            return "Amapá";
        case estados.Amazonas:
            return "Amazonas";
        case estados.Bahia:
            return "Bahia";
        case estados.Ceará:
            return "Ceará";
        case estados.Espírito_Santo:
            return "Espírito Santo";
        case estados.Goiás:
            return "Goiás";
        case estados.Maranhão:
            return "Maranhão";
        case estados.Mato_Grosso:
            return "Mato Grosso";
        case estados.Mato_Grosso_do_Sul:
            return "Mato Grosso do Sul";
        case estados.Minas_Gerais:
            return "Minas Gerais";
        case estados.Pará:
            return "Pará";
        case estados.Paraíba:
            return "Paraíba";
        case estados.Paraná:
            return "Paraná";
        case estados.Pernambuco:
            return "Pernambuco";
        case estados.Piauí:
            return "Piauí";
        case estados.Rio_de_Janeiro:
            return "Rio de Janeiro";
        case estados.Rio_Grande_do_Norte:
            return "Rio Grande do Norte";
        case estados.Rio_Grande_do_Sul:
            return "Rio Grande do Sul";
        case estados.Rondônia:
            return "Rondônia";
        case estados.Roraima:
            return "Roraima";
        case estados.Santa_Catarina:
            return "Santa Catarina";
        case estados.São_Paulo:
            return "São Paulo";
        case estados.Sergipe:
            return "Sergipe";
        case estados.Tocantins:
            return "Tocantins";
        case estados.Distrito_Federal:
            return "Distrito Federal";
        default:
            return "Vazio";
    }

}

export enum setor{
	vazio = 0,
    comercio = 1,
    servicos = 2,
    industria = 3,
    outros = 4
}

export function setor_str(valor: setor): string {
    switch (valor) {
        case setor.vazio:
            return "Vazio";
        case setor.comercio:
            return "Comercio";
        case setor.servicos:
            return "Servicos";
        case setor.industria:
            return "Industria";
        case setor.outros:
            return "Outros";
        default:
            return "Vazio";
    }
}

export enum genero{
	vazio = 0,
    masculino = 1,
    feminino = 2,
    outro = 3
}

export function genero_str(value: genero): string {
    switch (value) {
        case genero.vazio:
            return "Vazio";
        case genero.masculino:
            return "Masculino";
        case genero.feminino:
            return "Feminino";
        case genero.outro:
            return "Outro";
        default:
            return "Vazio";
    }
}

export enum idade{
	vazio= 0,
    _0 = 1, //0+
    _20 = 2, //20+
    _40 = 3, //40+
    _60 = 4, //60+
}

export function idade_str(valor: idade): string {
    switch (valor) {
        case idade.vazio:
            return "Vazio";
        case idade._0:
            return "Até 20";
        case idade._20:
            return "21–39";
        case idade._40:
            return "40–59";
        case idade._60:
            return "60+";
        default:
            return "Vazio";
    }
}

export interface Cliente {
	email: string;
	id: number;
	nome: string;
	solicit: string;
	estados:estados;
	setor:setor;
	genero:genero;
	idade:idade;
}

//   {
//     "email": "teste@roseira",
//     "id": 2,
//     "nome": "Teste",
//     "solicit": "a"
//   },