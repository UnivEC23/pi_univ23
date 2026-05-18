<script setup lang="ts">
import { ref, onMounted } from "vue";
import "@/assets/index/css/tema.css"
import comentarios from "../components/comentarios.vue"
import form_cliente from "@/components/form_cliente.vue";
import hero_panel from "../components/sections/hero_panel.vue";
import servicos from "../components/sections/servicos.vue";
import sobre from "../components/sections/sobre.vue";
import tour360 from "../components/sections/tour360.vue";
// import depoimentos from "../components/sections/depoimentos.vue";
import comentarios2 from "../components/sections/comentarios.vue";

let email = ""
let password = ""
let abrir = ref<boolean>(false)


function atualizarBotaoTopo() {
    const botao = document.getElementById('backToTop');

    if (!botao) {
        return;
    }

    if (window.scrollY > 320) {
        botao.classList.add('is-visible');
    } else {
        botao.classList.remove('is-visible');
    }
}

function voltarAoTopo() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

onMounted(() => {
    window.addEventListener('scroll', atualizarBotaoTopo);
    window.addEventListener('load', atualizarBotaoTopo);
})


</script>

<template>
    <main id="topo">
        <hero_panel />
        <servicos />
        <sobre />
        <tour360 />
        <!-- <depoimentos /> -->
        <comentarios2 />
        <!-- <comentarios /> -->

        <section class="section cta-section" id="contato">
            <div class="container">
                <div class="cta-panel">
                    <h2>Pronto para crescer?</h2>
                    <p class="section-copy">Vamos conversar sobre como fortalecer sua presença digital e gerar mais
                        oportunidades para o seu negócio.</p>
                    <div class="columns is-centered">
                        <div class="column is-half">
                            <form_cliente class="form-bg modal-box" v-model:abrir="abrir" v-if="abrir" />
                        </div>
                    </div>
                    <div v-if="!abrir">
                        <button class="button is-info m-3" @click="abrir = true">Solicite um
                            Orçamento!</button>
                    </div>
                    <!-- <button class="button is-light cta-button" onclick="abrirModal('modalOrcamento')">Solicite um
                        Orçamento</button> -->
                    <p class="section-copy">Entre em contato e receba uma proposta personalizada.</p>

                </div>
            </div>
        </section>

    </main>
    <!-- <div class="modal" id="modalOrcamento">
        <div class="modal-background"></div>
        <div class="modal-content"> -->
    <!-- <form_cliente class="form-bg modal-box" v-model:abrir="abrir" v-if="abrir" /> -->
    <!-- </div>
    </div> -->

    <button class="back-to-top" id="backToTop" type="button" aria-label="Voltar ao topo" @click="voltarAoTopo()">
        <span aria-hidden="true">^</span>
    </button>

    <footer class="site-footer">
        <div class="container">
            <div class="footer-shell">
                <div>
                    <p class="footer-brand">ED 360° Soluções Digitais</p>
                </div>
                <div class="footer-links">
                    <a href="#servicos">Nossos Serviços</a>
                    <a href="#sobre">Sobre Nós</a>
                    <a href="#depoimentos">Depoimentos</a>
                </div>
            </div>
        </div>
    </footer>
</template>

<style scoped></style>

<style>
/* .form-bg {
    background-color: rgb(65, 118, 136);
} */
</style>
