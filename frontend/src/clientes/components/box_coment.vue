<script setup lang="ts">
import { inject, ref } from 'vue';

defineProps<{ autor: string; texto: string }>()

let hover = ref(false)
const remover = inject<(_name: string) => Promise<void>>('remover')

</script>

<template>
	<div class="container has-background-dark" @mouseenter="hover = true" @mouseleave="hover = false">
		<div class="is-flex is-align-items-center is-justify-content-center">
			<div class="">
				<p class="has-text-success">{{ autor }}</p>
				<p class="has-text-white-ter">{{ texto }}</p>
			</div>
			<button v-if="hover" type="button" @click="remover?.(autor)"
				class="button is-hoverable is-danger list-item-controls ml-3">
				<span class="icon">
					<i class="fas fa-plus"></i>
				</span>
				<span>Remover</span>
			</button>
		</div>

	</div>
	<br>
</template>

<style scoped></style>