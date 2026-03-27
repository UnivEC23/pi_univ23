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

async function enviar() {
	// pegar?.(); //teste
	if (!valido()) {
		resetar();
		return;
	}
	console.log(form.value)
	console.log({ ...form.value }) //shallow
	console.log(JSON.parse(JSON.stringify(form.value))) //deep

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