<script setup lang="ts">
import { ref } from "vue";
import comentarios from "../components/comentarios.vue"
import form_cliente from "@/components/form_cliente.vue";

let email = ""
let password = ""
let abrir = ref<boolean>(false)
</script>

<template>
    <main class="bg-leve">
        <section class="hero is-fullheight">
            <div class="hero-body ">
                <div class="container has-text-centered py-3">
                    <img src="/apple-touch-icon.png" alt="imagem pequena" style="width: 100px; height: auto;"
                        class="mb-3">
                    <h1 class="title is-2 has-text-info"> ED 360° SOLUÇOES DIGITAIS </h1>
                    <p class="subtitle is-4  has-text-dark">Transforme sua presença digital e conquiste mais
                        clientes.
                    </p>
                    <div class="columns is-centered">
                        <div class="column is-half">
                            <p class="has-text-justified has-text-grey-dark">
                                No mundo digital de hoje, ter um site profissional e uma forte presença no Instagram é
                                essencial para o sucesso.
                                Nós te ajudamos a criar a estratégia perfeita, desde o design do seu site até o conteúdo
                                que
                                engaja seu público,
                                para que você possa focar no que realmente importa: o crescimento do seu negócio.
                            </p>
                        </div>
                    </div>
                    <br>
                    <div class="columns is-centered">
                        <div class="column is-half">
                            <div class="container has-text-grey-dark">
                                <h2 class="title is-4 has-text-info mb-3">Nossos Serviços</h2>
                                <p class="has-text-justified">
                                    Projetamos e desenvolvemos serviços de alta qualidade para ajudar sua empresa a se
                                    destacar no mercado digital, conforme as necessidades de seu negocio.
                                </p>
                                <br>
                                <h3 class="title-light is-6 mb-2"> Serviços oferecidos:</h3>
                                <p>• Criação de Tour Virtual 360º</p>
                                <p>• Google Meu Negócio</p>
                                <p>• Criação de Sites Profissionais</p>
                                <p>• Criação de Chatbots</p>
                                <p>• Criação de Landing Pages</p>
                                <p>• Marketing Digital</p>
                                <p>• Gestão de Redes Sociais </p>
                                <p>• SEO (Otimização para Motores de Busca)</p>
                                <p>• Campanhas Publicitárias Online </p>

                            </div>
                        </div>
                    </div>
                    <div class="columns is-centered">
                        <div class="column is-half">
                            <comentarios />
                        </div>
                    </div>
                    <div class="columns is-centered">
                        <div class="column is-half">
                            <form_cliente class="form-bg" v-model:abrir="abrir" v-if="abrir" />
                        </div>
                    </div>
                    <div v-if="!abrir">
                        <button class="button is-info m-3" @click="abrir = true">Solicite um
                            Orçamento!</button>
                    </div>
                </div>

            </div>

        </section>


    </main>
</template>

<style scoped></style>

<style>
.form-bg {
    background-color: rgb(65, 118, 136);
}
</style>
