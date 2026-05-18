<script setup lang="ts">
import { ref, onMounted, computed } from "vue"
import axios from "axios"
import box_comentario from "@/components/box_coment.vue"

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
    <section class="section testimonial-section" id="depoimentos">
        <div class="container">
            <div class="section-heading section-heading-centered">
                <h2 class="section-title">Depoimentos</h2>
                <p class="section-copy">Resultados reais, contados por quem já transformou sua presença digital conosco.
                </p>
            </div>

            <div class="columns is-multiline testimonial-grid">
                <div v-for="comenta in comentariosFixos" :key="'fixo-' + comenta.autor" class="column is-6-tablet"
                    :class="'is-6-desktop'">
                    <article class="testimonial-card">
                        <p class="testimonial-text">{{ comenta.texto }}</p>
                        <div class="testimonial-author">
                            <!-- <img class="avatar-chip" :src="testimonial.image" :alt="testimonial.author" /> -->
                            <div>
                                <strong>{{ comenta.autor }}</strong>
                                <!-- <p>{{ comenta.role }}</p> -->
                            </div>
                        </div>
                    </article>
                </div>

                <div v-if="fetchSuccess && comentariosValidos.length > 0" v-for="comenta in comentariosValidos"
                    :key="'dinamico-' + comenta.autor" class="column is-6-tablet" :class="'is-4-desktop'">
                    <article class="testimonial-card">
                        <p class="testimonial-text">{{ comenta.texto }}</p>
                        <div class="testimonial-author">
                            <!-- <img class="avatar-chip" :src="testimonial.image" :alt="testimonial.author" /> -->
                            <div>
                                <strong>{{ comenta.autor }}</strong>
                                <!-- <p>{{ comenta.role }}</p> -->
                            </div>
                        </div>
                    </article>
                </div>
            </div>

            <!-- <div class="columns is-multiline testimonial-grid">
                <div class="column is-6-tablet is-4-desktop">
                    <article class="testimonial-card">
                        <p class="testimonial-text">Serviço rápido e eficiente!</p>
                        <div class="testimonial-author">
                            <img class="avatar-chip" src="../static/person_1.webp" alt="Rose Alves">
                            <div>
                                <strong>Rose Alves</strong>
                                <p>Cabeleireira</p>
                            </div>
                        </div>
                    </article>
                </div>

                <div class="column is-6-tablet is-4-desktop">
                    <article class="testimonial-card">
                        <p class="testimonial-text">Meu caso era complicado, mas eles resolveram</p>
                        <div class="testimonial-author">
                            <img class="avatar-chip" src="../static/person_2.webp" alt="Aldo Marcus">
                            <div>
                                <strong>Aldo Marcus</strong>
                                <p>Marceneiro</p>
                            </div>
                        </div>
                    </article>
                </div>

                <div class="column is-6-tablet is-4-desktop">
                    <article class="testimonial-card">
                        <p class="testimonial-text">Depois do novo site e das campanhas digitais, começamos a
                            receber muito mais contatos diariamente.</p>
                        <div class="testimonial-author">
                            <img class="avatar-chip" src="../static/person_3.webp" alt="Carla Mendes">
                            <div>
                                <strong>Carla Mendes</strong>
                                <p>Clínica Estética (fictício)</p>
                            </div>
                        </div>
                    </article>
                </div>

                <div class="column is-6-tablet is-6-desktop">
                    <article class="testimonial-card">
                        <p class="testimonial-text">O tour virtual fez toda diferença nas apresentações dos
                            imóveis. Passou muito mais profissionalismo.</p>
                        <div class="testimonial-author">
                            <img class="avatar-chip" src="../static/person_4.webp" alt="Ricardo Nunes">
                            <div>
                                <strong>Ricardo Nunes</strong>
                                <p>Corretor Imobiliário (fictício)</p>
                            </div>
                        </div>
                    </article>
                </div>

                <div class="column is-6-tablet is-6-desktop">
                    <article class="testimonial-card">
                        <p class="testimonial-text">A presença digital da minha empresa mudou completamente. Hoje
                            meus clientes chegam já confiando no trabalho.</p>
                        <div class="testimonial-author">
                            <img class="avatar-chip" src="../static/person_5.webp" alt="Fernanda Lopes">
                            <div>
                                <strong>Fernanda Lopes</strong>
                                <p>Loja de Decoração (fictício)</p>
                            </div>
                        </div>
                    </article>
                </div>
            </div> -->
        </div>
    </section>
</template>

<style scoped></style>

<style></style>