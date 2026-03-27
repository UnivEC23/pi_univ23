<script setup lang="ts">
import { ref, onMounted, computed } from "vue"
import { provide } from 'vue'
import axios from "axios"
import box_comentario from "./box_coment.vue"
import form_cliente from "../../components/form_cliente.vue"
import { useToast } from "@/composables/useToast"
import API_URL from "@/api/api_url"
import form_comentario from "./form_comentario.vue"


let abrir = ref<boolean>(false)

const removerComent = async (_nome: string) => {
	console.log("remover " + _nome)
	// const response = await fetch(`${API_URL}/comentarios`, {
	// const response = await fetch(`/api/comentarios`, {
	// 	method: 'DELETE',
	// 	headers: {
	// 		'Content-Type': 'application/json',
	// 	},
	// 	body: JSON.stringify({ nome: _nome }),
	// });
	// if (response.ok) {
	// 	pegarComentarios();
	// }

	axios.delete(`/api/comentarios`, {
		headers: {
			'Content-Type': 'application/json',
		}, data: JSON.stringify({ autor: _nome })
	}).then(response => {
		pegarComentarios();
		console.log(response.data);
	}).catch(error => {
		console.error(error);
	});


}
provide('remover', removerComent)
provide('pegar', pegarComentarios)

// let hover = ref(false)
const { error } = useToast()
// Reactive array for dynamic comments from API
const comentarios = ref<{ autor: string; texto: string }[]>([])
const fetchSuccess = ref(false)

const comentariosValidos = computed(() => {
	// Only proceed if fetch was successful
	if (!fetchSuccess.value) return [];

	// Filter out any objects that have empty strings for autor or texto
	return comentarios.value.filter(c => c.autor.trim() !== "" && c.texto.trim() !== "");
});


// Fetch comments from API
async function pegarComentarios() {
	try {
		const response = await axios.get("/api/comentarios")
		comentarios.value = response.data
		fetchSuccess.value = true  // mark success
	} catch (erro: any) {
		console.error("Erro ao buscar comentários:", erro)
		error("Erro ao buscar comentários:" + erro.message)
		fetchSuccess.value = false
	}
}

onMounted(() => {
	pegarComentarios()
})

// Fixed comments
const comentariosFixos = [
	{ autor: "Rose Alves, Cabeleireira", texto: "Serviço rápido e eficiente!" },
	{ autor: "Aldo Marcus, Marceneiro", texto: "Meu caso era complicado, mas eles resolveram" },
]
</script>

<template>
	<div class="box has-text-centered has-background-grey-darker">
		<h2 class="title is-3 has-text-info">Lista de Comentários</h2>

		<!-- Render fixed comments -->
		<box_comentario v-for="(c, i) in comentariosFixos" :key="'fixed-' + i" :autor="c.autor" :texto="c.texto" />


		<!-- Render dynamic comments ONLY if fetch succeeded -->
		<template v-if="fetchSuccess && comentariosValidos.length > 0">
			<box_comentario v-for="(c, i) in comentariosValidos" :key="'dynamic-' + i" :autor="c.autor"
				:texto="c.texto" />
			<!-- <button type="button" onclick="abrirComent()" class="button is-active is-danger list-item-controls">
				<span class="icon">
					<i class="fas fa-plus"></i>
				</span>
				<span>Remover</span>
			</button> -->
		</template>


		<!-- Optional fallback message -->
		<!-- <p v-if="comentarios.length === 0" class="has-text-white-ter">
			Nenhum comentário encontrado.
		</p> -->
	</div>

	<form_comentario v-model:abrir="abrir" v-if="abrir" />

	<div v-if="!abrir">
		<button id="botaoComent" type="button" @click="abrir = true" class="button is-white">
			<span class="icon">
				<i class="fas fa-plus"></i>
			</span>
			<span>Adicionar Novo Comentário</span>
		</button>
	</div>
</template>