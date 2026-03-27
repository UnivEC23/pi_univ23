<script setup lang="ts">
import { ref, onMounted, computed } from "vue"
import axios from "axios"
import box_comentario from "./box_coment.vue"

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
	} catch (error) {
		console.error("Erro ao buscar comentários:", error)
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
	<div class="box has-background-grey-darker">
		<h2 class="title is-3 has-text-info">Comentários Recentes</h2>

		<!-- Render fixed comments -->
		<box_comentario v-for="(c, i) in comentariosFixos" :key="'fixed-' + i" :autor="c.autor" :texto="c.texto" />

		<!-- Render dynamic comments ONLY if fetch succeeded -->
		<template v-if="fetchSuccess && comentariosValidos.length > 0">
			<box_comentario v-for="(c, i) in comentariosValidos" :key="'dynamic-' + i" :autor="c.autor"
				:texto="c.texto" />
		</template>

		<!-- Optional fallback message -->
		<!-- <p v-if="comentarios.length === 0" class="has-text-white-ter">
			Nenhum comentário encontrado.
		</p> -->
	</div>
</template>