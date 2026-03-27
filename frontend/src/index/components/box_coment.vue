<script setup lang="ts">
defineProps<{ autor: string; texto: string }>()

</script>

<template>
	<div class="container">
		<p class="has-text-success">{{ autor }}</p>
		<p class="has-text-grey-light">{{ texto }}</p>
	</div>
	<br>
</template>