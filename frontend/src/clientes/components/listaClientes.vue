<script setup lang="ts">
import { ref, onMounted, computed, provide } from "vue"
import API_URL from "@/api/api_url"
import { BTable } from "buefy";
import axios from "axios"
// import usarClientes from "../composables/pegarClientes"
import { OTable, OTableColumn } from "@oruga-ui/oruga-next";
import box_comentario from "./box_coment.vue"
import type { Cliente } from "../types"
import { useToast } from "@/composables/useToast"
import form_cliente from "@/components/form_cliente.vue";


const { error } = useToast()

let abrir = ref<boolean>(false)


// const pegarClientes = usarClientes()

const clientes = ref<Cliente[]>([])
const fetchCliSuccess = ref(false)
// const data = ref()
// const columns = ref([
// 	{
// 		field: "nome",
// 		label: "Nome",
// 		width: "40",
// 		// numeric: true,
// 	},
// 	{
// 		field: "email",
// 		label: "Email",
// 	},
// 	{
// 		field: "solicit",
// 		label: "Solicitação",
// 	},
// ])

// Reactive array for dynamic comments from API
// const comentarios = ref<{ autor: string; texto: string }[]>([])
// const fetchCmtSuccess = ref(false)

const clientesValidos = computed(() => {
	// Only proceed if fetch was successful
	if (!fetchCliSuccess.value) return [];
	// data.value = clientes.value.map(({ id, ...rest }) => rest);
	// console.log("computando: ", clientes.value)
	return clientes.value
});

async function pegarClientes() {
	try {
		const response = await axios.get(`/api/clientes`)
		clientes.value = response.data
		// console.log("pegando: ", clientes.value)
		fetchCliSuccess.value = true  // mark success
	} catch (erro: any) {
		console.error("Erro ao buscar clientes:", erro)
		error("Erro ao buscar clientes: " + erro.message)
		fetchCliSuccess.value = false
	}
}

provide('pegar', pegarClientes)

// Fetch comments from API
// async function pegarComentarios() {
// 	try {
// 		const response = await axios.get("/api/comentarios")
// 		comentarios.value = response.data
// 		fetchCmtSuccess.value = true  // mark success
// 	} catch (error) {
// 		console.error("Erro ao buscar comentários:", error)
// 		fetchCmtSuccess.value = false
// 	}
// }

onMounted(() => {
	pegarClientes()
	// pegarComentarios()
})

const clientesExemplo = [
	{
		"email": "teste@roseira",
		"id": 2,
		"nome": "Teste",
		"solicit": "a"
	},
	{
		"email": "comenta@foi.com",
		"id": 3,
		"nome": "abriu",
		"solicit": "aqui tive algo"
	},
	{
		"email": "novo@oi",
		"id": 4,
		"nome": "haml",
		"solicit": "projeto para ..."
	},
	{
		"email": "zezi@email.com",
		"id": 5,
		"nome": "tio z\u00e9",
		"solicit": "Queria saber mais"
	}
]

let hover = ref(false)

async function removerCliente(_nome: string) {
	// const response = await fetch(`${API_URL}/clientes`, {
	// 	method: 'DELETE',
	// 	headers: {
	// 		'Content-Type': 'application/json',
	// 	},
	// 	body: JSON.stringify({ nome: _nome }),
	// });

	// if (response.ok) {
	// 	pegarClientes();
	// }
	axios.delete(`/api/clientes`, {
		headers: {
			'Content-Type': 'application/json',
		}, data: JSON.stringify({ nome: _nome })
	}).then(response => {
		pegarClientes();
		console.log(response.data);
	}).catch(error => {
		console.error(error);
	});

}

</script>

<template v-if="fetchCliSuccess && clientesValidos.length > 0">
	<div class="box has-background-grey-darker" @mouseenter="hover = true" @mouseleave="hover = false">
		<h2 class="title is-3 has-text-info">Lista de Clientes</h2>
		<!-- <o-table class="table has-background-grey-darker" :data="clientesExemplo">
			<o-table-column field="nome" label="Nome" width="170" sortable />
			<o-table-column field="email" label="Email" width="200" position="centered" sortable />
			<o-table-column field="solicit" label="Solicitação" position="centered" sortable />

		</o-table> -->

		<o-table class="table has-background-grey-darker" :data="clientesValidos">
			<o-table-column field="nome" label="Nome" width="170" sortable />

			<!-- <o-table-column field="email" label="Email" width="200" sortable header-class="has-text-centered" /> -->
			<o-table-column field="email" label="Email" width="200" sortable header-class="has-text-centered"
				cell-class="has-text-centered" />


			<!-- <o-table-column id="solicit" field="solicit" label="Solicitação" sortable header-class="has-text-centered"
				cell-class="has-text-centered" /> -->
			<!-- <o-table-column field="solicit" label="Solicitação" sortable :class="'has-text-centered'" v-slot="{ row }">
				<div class="has-text-centered">
					{{ row.solicit }}</div>
			</o-table-column> -->

			<o-table-column field="solicit" sortable>
				<template #header>
					<div class="has-text-centered">Solicitação</div>
				</template>

				<template #default="{ row }">
					<div class="has-text-centered">
						{{ row.solicit }}
					</div>
				</template>
			</o-table-column>
			<o-table-column field="nome" width="80">
				<template #header>
					<div class="has-text-centered"></div>
				</template>

				<template #default="{ row }">
					<div class="has-text-centered">
						<button v-if="hover" type="button" @click="removerCliente?.(row.nome)"
							class="button is-hoverable is-danger list-item-controls removcli">
							<span class="icon">
								<i class="fas fa-plus"></i>
							</span>
							<span>Remover</span>
						</button>
					</div>
				</template>
			</o-table-column>
		</o-table>

		<!--<o-table :data="clientesExemplo">
			<o-table-column v-for="col in columns" :key="col.field" :field="col.field" :label="col.label"
				:width="col.width" sortable>
				<template #default="{ row }">
					{{ row[col.field] }}
				</template>
			</o-table-column>
		</o-table>

		<o-table :data="clientesExemplo">
			<o-table-column v-for="col in columns" :key="col.field" :field="col.field" :label="col.label"
				:width="col.width" sortable :header-class="'has-text-centered'" :cell-class="'has-text-centered'">
				<template #default="{ row }">
					<span :class="'has-text-centered'">
						{{ row[col.field] }}
					</span>
				</template>
			</o-table-column>
		</o-table> -->

	</div>
	<!-- usando props -->
	<!-- <form_cliente :abrir="abrir" @update:abrir="abrir = $event" v-if="abrir" /> -->

	<form_cliente v-model:abrir="abrir" v-if="abrir" />

	<div v-if="!abrir">
		<button id="botaoComent" type="button" @click="abrir = true" class="button is-white">
			<span class="icon">
				<i class="fas fa-plus"></i>
			</span>
			<span>Adicionar Novo Cliente</span>
		</button>
	</div>

</template>

<style scoped>
button.removcli,
button.removcli>span {
	font-size: small;
	/* width: 2em; */
}

/* :deep(.o-table td:nth-child(3)) {
	text-align: center;
}

:deep(.o-table th:nth-child(3)) {
	text-align: center;
} */
</style>