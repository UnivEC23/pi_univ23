<script setup lang="ts">
// import comentarios from "@/components/comentarios.vue"
import botVoltar from '../components/botVoltar.vue';
import listaClientes from '../components/listaClientes.vue';
import listaComentarios from '../components/listaComentarios.vue';
import dashboardClientes from '../components/dashboardClientes.vue';
import dashboardVisitantes from '../components/dashboardVisitantes.vue';
import { ref } from 'vue';

const dashboardSelecionado = ref('clientes');

</script>

<template>
	<main class="has-background-grey-darker">
		<section class="hero is-dark is-fullheight-with-navbar">
			<div class="hero-body">
				<div class="container">

    <div class="buttons is-centered mb-5">
        <button
            class="button"
            :class="{ 'is-info': dashboardSelecionado === 'lista' }"
            @click="dashboardSelecionado = 'lista'"
        >
            👥 Lista de Clientes
        </button>

        <button
            class="button"
            :class="{ 'is-info': dashboardSelecionado === 'clientes' }"
            @click="dashboardSelecionado = 'clientes'"
        >
            📊 Dashboard de Clientes
        </button>

        <button
            class="button"
            :class="{ 'is-info': dashboardSelecionado === 'visitantes' }"
            @click="dashboardSelecionado = 'visitantes'"
        >
            👁 Dashboard de Visitantes
        </button>
    </div>

    <div v-if="dashboardSelecionado === 'lista'">
        <listaClientes />
    </div>

    <div v-if="dashboardSelecionado === 'clientes'">
        <dashboardClientes />
    </div>

    <div v-if="dashboardSelecionado === 'visitantes'">
        <dashboardVisitantes />
    </div>

    <br>
   	
					<listaComentarios />

					<!-- botão adicionar clientes e comentários -->
					<!-- <botVoltar /> foi para a navbar-->
				</div>
			</div>
		</section>
	</main>


</template>