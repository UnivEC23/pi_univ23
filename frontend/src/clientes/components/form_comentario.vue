<script setup lang="ts">
import { inject, ref } from 'vue'
import API_URL from "@/api/api_url"

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
}

let form = ref<Cliente>({
	nome: '',
	email: '',
	solicit: '',
})

type Coment = {
	autor: string
	texto: string
}

let formc = ref<Coment>({
	autor: '',
	texto: '',
})

async function enviar() {
	// pegar?.(); //teste
	if (!valido()) {
		resetar();
		return;
	}
	console.log(formc.value)
	console.log({ ...formc.value }) //shallow
	console.log(JSON.parse(JSON.stringify(formc.value))) //deep

	const response = await fetch(`/api/comentarios`, {
		method: 'POST',
		body: JSON.stringify(formc.value),
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
	formc.value = {
		autor: '',
		texto: '',
	}
}


let erros = ref<boolean>(false);

function valido(): boolean {
	if (!formc.value.autor.trim() || !formc.value.texto.trim()) {
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
		<h2 class="title">Novo Comentário</h2>

		<form @submit.prevent="enviar">

			<div class="field">
				<label class="label  has-text-light">Seu Nome</label>
				<div class="control">
					<input v-model="formc.autor" class="input" type="text" name="autor" placeholder="Seu nome" required>
				</div>
			</div>

			<div class="field">
				<label class="label  has-text-light">Comentário</label>
				<div class="control">
					<textarea v-model="formc.texto" class="textarea" name="texto" placeholder="Seu comentário"
						required></textarea>
				</div>
			</div>
			<!-- <div class="field">
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
			<br> -->

			<div class="field is-grouped">
				<div class="control">
					<button :disabled="!formc.autor || !formc.texto" type="submit" class="button is-primary is-info">
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