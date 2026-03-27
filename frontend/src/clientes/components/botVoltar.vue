<script setup lang="ts">
// import sairLogin from "../api/sairLogin"
import axios from "axios"

async function sairLogin() {

	// try {
	// 	const response = await fetch(`${API_URL}/deslogin`, {
	// 		// const response = await fetch('/api/deslogin', {
	// 		method: 'POST',
	// 		headers: {
	// 			'Content-Type': 'application/json'
	// 		},
	// 		// body: JSON.stringify({ msg: "gogo" })
	// 	});
	// 	const data = await response.json();
	// 	if (response.ok) {
	// 		// console.log("saindo")
	// 		window.location = data.rota;
	// 	}
	// } catch (error) {
	// 	console.error('Erro ao sair da area logada:', error);
	// 	// alert(data.mensagemoff)
	// }
	// return true;

	// try {
	axios.post("/api/deslogin").then(response => {
		console.log(response.data);
		window.location = response.data.rota;
	}).catch(error => {
		console.error('Erro ao sair da area logada:', error);
	});
	// 	comentarios.value = response.data
	// 	// fetchSuccess.value = true  // mark success
	// } catch (erro: any) {
	// 	console.error("Erro ao buscar comentários:", erro)
	// 	error("Erro ao buscar comentários:" + erro.message)
	// 	// fetchSuccess.value = false
	// }
}

</script>

<template>

	<div>
		<!-- <a href="{{ url_for('home') }}" class="button is-light mt-4"> -->
		<button class="button is-light mt-4" type="button" @click="sairLogin()">
			<span class="icon">
				<i class="fas fa-arrow-left"></i>
			</span>
			<span>Voltar para a Página Inicial</span>
		</button>
		<!-- </a> -->
	</div>
</template>