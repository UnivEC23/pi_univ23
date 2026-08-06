<script setup lang="ts">
import { inject, ref } from 'vue'
import API_URL from "@/api/api_url"
//import type { Cliente } from "@/clientes/types"
import { estados, setor, genero, idade } from "@/clientes/types"

//usando props
// const props = defineProps<{
// 	abrir: boolean
// }>()

// const emit = defineEmits<{
// 	(e: 'update:abrir', value: boolean): void
// }>()

// function toggle() {
// 	emit('update:abrir', !props.abrir)
// }

const abrir = defineModel<boolean>('abrir')


const pegar = inject<() => Promise<void>>('pegar')
function toggle() {
	abrir.value = !abrir.value
}

type Cliente = {
	nome: string
	email: string
	solicit: string
	estados:estados
	idade:idade
	setor:setor
	genero:genero
}

let form = ref<Cliente>({
	nome: '',
	email: '',
	solicit: '',
	estados:estados.vazio,
	idade:idade.vazio,
	setor:setor.vazio,
	genero:genero.vazio,
})

async function enviar() {
	// pegar?.(); //teste
	if (!valido()) {
		resetar();
		return;
	}
	// console.log(form.value)
	console.log({ ...form.value }) //shallow
	// console.log(JSON.parse(JSON.stringify(form.value))) //deep

	const response = await fetch(`/api/clientes`, {
		method: 'POST',
		body: JSON.stringify(form.value),
		headers: {
			'Content-Type': 'application/json'
		}
	})
	if (response.ok) {
		resetar()
		toggle()
		pegar?.();
		return;
	}
	else {
		console.error('Erro ao adicionar solicitação:', response.status);
		// alert(data.erro);
	}

	// reset everything at once
	resetar();
}

function resetar() {
	form.value = {
		nome: '',
		email: '',
		solicit: '',
		estados:estados.vazio,
		setor:setor.vazio,
		genero:genero.vazio,
		idade:idade.vazio,
	}
}


let erros = ref<boolean>(false);

function valido(): boolean {
	if (!form.value.nome.trim() || !form.value.email.trim() || !form.value.solicit.trim()) {
		erros.value = true;
		return false;
	}

	erros.value = false;
	return true;;
}

// type FormErrors = {
// 	nome?: string
// 	email?: string
// }


// let errors = ref<FormErrors>({})

// function validar(): boolean {
// 	let newErrors: FormErrors = {}

// 	if (!form.value.nome.trim()) {
// 		newErrors.nome = 'nome is required'
// 	} else if (form.value.nome.length < 3) {
// 		newErrors.nome = 'Name must be at least 3 characters'
// 	}

// 	if (!form.value.email.trim()) {
// 		newErrors.email = 'email is required'
// 	} else if (form.value.email.length < 10) {
// 		newErrors.email = 'Message must be at least 10 characters'
// 	}

// 	errors.value = newErrors

// 	return Object.keys(newErrors).length === 0
// }


// const isValid = computed(() => {
//   return form.value.nome.length >= 3 &&
//          form.value.email.length >= 10
// })

defineOptions({
	inheritAttrs: false
})
</script>

<template>
	<div class="box" v-bind="$attrs">
		<h2 class="title">Novo Cliente</h2>

		<form @submit.prevent="enviar">
			<div class="field is-grouped">
				<div class="control">
					<label class="label has-text-light">Setor</label>
					<select name="Setor" v-model="form.setor">
					  <option value="0">---</option>
					  <option value="1">Comércio</option>
					  <option value="2">Serviços</option>
					  <option value="3">Indústria</option>
					  <option value="4">Outros</option>
					</select>
				</div>
				<div class="control">
					<label class="label has-text-light">Estado</label>
					<select name="Estados" v-model="form.estados">
					  <option value="0">---</option>
					  <option value="1">Acre</option>
					  <option value="2">Alagoas</option>
					  <option value="3">Amapá</option>
					  <option value="4">Amazonas</option>
					  <option value="5">Bahia</option>
					  <option value="6">Ceará</option>
					  <option value="7">Espírito Santo</option>
					  <option value="8">Goiás</option>
					  <option value="9">Maranhão</option>
					  <option value="10">Mato Grosso</option>
					  <option value="11">Mato Grosso do Sul</option>
					  <option value="12">Minas Gerais</option>
					  <option value="13">Pará</option>
					  <option value="14">Paraíba</option>
					  <option value="15">Paraná</option>
					  <option value="16">Pernambuco</option>
					  <option value="17">Piauí</option>
					  <option value="18">Rio de Janeiro</option>
					  <option value="19">Rio Grande do Norte</option>
					  <option value="20">Rio Grande do Sul</option>
					  <option value="21">Rondônia</option>
					  <option value="22">Roraima</option>
					  <option value="23">Santa Catarina</option>
					  <option value="24">São Paulo</option>
					  <option value="25">Sergipe</option>
					  <option value="26">Tocantins</option>
					  <option value="27">Distrito Federal</option>
					</select>
				</div>


				<div class="control">
					<label class="label has-text-light">Idade</label>
					<select name="idade" v-model="form.idade">
					  <option value="0">---</option>
					  <option value="1">Até 20</option>
					  <option value="2">20+</option>
					  <option value="3">40+</option>
					  <option value="4">60+</option>
					</select>
				</div>
			
				<div class="control">
					<label class="label has-text-light">Gênero</label>
					<select name="genero" v-model="form.genero">
					  <option value="0">---</option>
					  <option value="1">Masculíno</option>
					  <option value="2">Feminíno</option>
					  <option value="3">Outro</option>
					</select>
				</div>
			</div>
			<div class="field">
				<label class="label has-text-light">Nome</label>
				<div class="control">
					<input v-model="form.nome" class="input is-info" type="text" name="nome" placeholder="Seu nome"
						required>
				</div>
			</div>

			<div class="field">
				<label class="label has-text-light">Email</label>
				<div class="control">
					<input v-model="form.email" class="input is-info" type="emai" name="email" placeholder="Seu email"
						required>
				</div>
			</div>

			<div class="field">
				<label class="label has-text-light">Solicitação</label>
				<div class="control">
					<textarea v-model="form.solicit" class="textarea is-info" type="text" name="solicit"
						placeholder="Descreve seu problema" required></textarea>
				</div>
			</div>
			<br>

			<div class="field is-grouped">
				<div class="control">
					<button :disabled="!form.nome || !form.email || !form.solicit" type="submit"
						class="button is-primary is-info">
						<span>Adicionar</span>
					</button>
				</div>
				<div class="control">
					<button class=" button is-light" type="button" @click="toggle">fechar</button>
				</div>
				<div class="is-flex is-justify-content-center is-align-items-center">
					<p v-if="erros" class="has-text-centered has-text-danger"> Por
						favor,preencha todos os campos. </p>
				</div>
			</div>
		</form>
		<!-- <div class="field is-grouped"> -->
		<!-- <div class="control is-expanded">
                    <input class="input is-info" type="text" id="novo-cliente" placeholder="Nome do cliente">
                     </div>
                     <br>
                    <div class="control is-expanded">
                    <input id="email" class="input is-info" type="email" name="email" placeholder="Seu email">
                    </div>
                    <div class="control">
                    <button onclick="adiClientes()" class="button is-info">
                        <span class="icon">
                            <i class="fas fa-plus"></i>
                        </span>
                        <span>Adicionar</span>
                    </button>
                 </div> -->
		<!-- </div> -->
	</div>

	<br>
</template>

<style scoped></style>