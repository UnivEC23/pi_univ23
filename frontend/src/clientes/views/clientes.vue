<script setup lang="ts">
// import comentarios from "@/components/comentarios.vue"
import botVoltar from '../components/botVoltar.vue';
import listaClientes from '../components/listaClientes.vue';
import listaComentarios from '../components/listaComentarios.vue';


</script>

<template>
	<main class="has-background-grey-darker">
		<section class="hero is-dark is-fullheight-with-navbar">
			<div class="hero-body">
				<div class="container">
					<listaClientes />
					<br>
					<listaComentarios />

					<!-- botão adicionar clientes e comentários -->
					<!-- <botVoltar /> foi para a navbar-->
				</div>
			</div>
		</section>
	</main>


</template>