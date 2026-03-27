<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import { defineComponent } from "vue";
import { ref } from "vue";
import { BBreadcrumb, BBreadcrumbItem } from "buefy";
import { BNavbar, BNavbarDropdown, BNavbarItem } from "buefy";
// import login from "@/components/outros/BotãoLogin.vue"
import login from "./botLogin.vue"

</script>

<template>
    <main>
        <section>
            <b-navbar class="nav-bg is-light">
                <template #brand>
                    <b-navbar-item tag="router-link" :to="{ path: '/' }">
                        <img src="/favicon-32x32.png" alt="EDS Marketing" />
                    </b-navbar-item>
                </template>
                <template #start>
                    <b-navbar-item tag="router-link" :to="{ path: '/' }">Início </b-navbar-item>
                    <!-- <RouterLink tag="b-navbar-item" to="/">Início</RouterLink> -->
                    <!-- <b-navbar-item href="#"> Documentation </b-navbar-item> -->
                    <b-navbar-item tag="router-link" :to="{ path: '/sobre' }">Sobre</b-navbar-item>
                    <b-navbar-dropdown label="Info" class="is-dark" hoverable>
                        <b-navbar-item tag="router-link" :to="{ path: '/termos' }">Termos & Política de Privacidade
                        </b-navbar-item>
                    </b-navbar-dropdown>
                </template>

                <template #end>
                    <b-navbar-item tag="div">
                        <div class="buttons">
                            <login />
                        </div>
                    </b-navbar-item>
                </template>
            </b-navbar>
        </section>
    </main>
</template>

<style scoped>
.nav-bg {
    background-color: rgb(116, 182, 218);
}
</style>