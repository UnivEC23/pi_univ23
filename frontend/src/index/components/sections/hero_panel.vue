<script setup lang="ts">
import { ref } from "vue";
// import "@/assets/index/css/tema.css"
import icone from "@/assets/index/img/apple-touch-icon.png"

</script>

<template>
	<section class="hero-panel section">
		<div class="container">
			<div class="columns is-vcentered is-variable is-8">
				<div class="column is-5-desktop">
					<span class="eyebrow">Conheça</span>
					<h1 class="hero-title">ED 360° Soluções Digitais</h1>
					<h3 class="hero-subtitle">Transformamos sua presença digital em resultados reais.</h3>
					<p class="hero-subtitle">
						No cenário digital atual, não basta apenas estar online, é preciso se destacar. A ED 360°
						Soluções Digitais te ajuda a fortalecer sua presença digital através de <span>estratégias
							inteligentes, design profissional e soluções tecnológicas</span> que atraem, engajam e
						convertem clientes.
					</p>
					<!-- <div class="hero-actions"> -->
					<!-- <button class="button is-dark action-primary" onclick="abrirModal('modalOrcamento')">Solicite um
							Orçamento</button> -->
					<!-- <a class="button is-light action-secondary" href="#sobre">Sobre Nós</a> -->
					<!-- </div> -->
				</div>

				<div class="column is-7-desktop">
					<div class="hero-visual">
						<div class="hero-scene"></div>
						<div class="floating-card">
							<img :src=icone alt="ED 360° Soluções Digitais">
							<div>
								<strong>ED 360° Soluções Digitais</strong>
								<p>estratégias inteligentes, design profissional e soluções tecnológicas</p>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</section>
</template>

<style scoped>
/* .hero-panel {
	padding-top: 1.5rem;
	padding-bottom: 5rem;
}

.hero-title {
	margin: 1rem 0 1.25rem;
	color: var(--ink);
	font-size: clamp(2.8rem, 5vw, 4.25rem);
	line-height: 0.96;
	font-weight: 800;
	letter-spacing: -0.05em;
	max-width: 9ch;
}

.hero-subtitle,
.section-copy,
.immersive-copy p,
.footer-copy {
	color: var(--muted);
	font-size: 1.4rem;
	line-height: 1.75;
	margin-bottom: 20px;
}

.hero-subtitle {
	font-size: 1.16rem;
	line-height: 1.8;
	max-width: 56ch;
}

h3.hero-subtitle {
	font-size: 2.2rem;
	line-height: 1.4;
	margin-bottom: 20px;
}

.hero-subtitle span {
	color: var(--ink);
	font-weight: 600;
}

.hero-actions {
	display: flex;
	align-items: center;
	gap: 0.9rem;
	margin-top: 2rem;
	flex-wrap: wrap;
} */
</style>

<style></style>