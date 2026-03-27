<script setup lang="ts">
import { ref } from "vue";
import { useAuth } from "../composables/useAuth";
import { useToast } from "@/composables/useToast"

const isModalActive = ref(false);

const user = ref("");
const password = ref("");

// const { login, loading } = useAuth();

const loading = ref(false)

const { success, error } = useToast()

async function loginRequest(usern: string, passw: string) {
	const response = await fetch(`/api/login`, {
		method: "POST",
		headers: {
			"Content-Type": "application/json"
		},
		body: JSON.stringify({ usern, passw })
	})

	const data = await response.json()

	if (!response.ok) {
		throw new Error(data.message || "Login falhou")
	}

	return data
}
async function login(user: string, password: string) {

	if (!user || !password) {
		error("login ou password vazios")
		return
	}

	loading.value = true

	try {
		const data = await loginRequest(user, password)

		success("Login bem sucedido!")

		window.location.assign(data.rota)

	} catch (err: any) {

		error(err.message)

	} finally {

		loading.value = false

	}
}


// Submit handler
function submit() {
	login(user.value, password.value);
}
</script>

<template>
	<section>
		<!-- Button to open modal -->
		<div class="buttons">
			<b-button type="is-light" @click="isModalActive = true">Login</b-button>
		</div>

		<!-- Modal component -->
		<b-modal v-model="isModalActive" has-modal-card trap-focus custom-class="custom-class custom-class-2">
			<form @submit.prevent="submit">
				<div class="modal-card" style="width:auto">

					<header class="modal-card-head">
						<p class="modal-card-title">Login</p>
						<button type="button" class="delete" @click="isModalActive = false"></button>
					</header>

					<section class="modal-card-body">
						<b-field label="Usuário">
							<b-input type="text" v-model="user" placeholder="Seu nome de usuário" required />
						</b-field>

						<b-field label="Password">
							<b-input type="password" v-model="password" password-reveal placeholder="Seu password"
								required />
						</b-field>

						<b-checkbox>Remember me</b-checkbox>
					</section>

					<footer class="modal-card-foot">
						<b-button @click="isModalActive = false">Fechar</b-button>
						<b-button class="move-right" type="is-primary" native-type="submit"
							:loading="loading">Login</b-button>
					</footer>

				</div>
			</form>
		</b-modal>
	</section>
</template>

<style scoped>
.move-right {
	margin-left: auto;
}
</style>