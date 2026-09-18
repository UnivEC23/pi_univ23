<script setup lang="ts">
import { onMounted, onBeforeUnmount, ref } from 'vue';
import { Chart, registerables } from 'chart.js';

Chart.register(...registerables);

interface Visita {
    id: number;
    data_hora: string | null;
}

const visitas = ref<Visita[]>([]);
const mesSelecionado = ref<number | null>(null);
const anoSelecionado = ref<number | null>(null);
const grafico = ref<Chart | null>(null);
const canvas = ref<HTMLCanvasElement | null>(null);

const nomesMeses = [
    'Janeiro',
    'Fevereiro',
    'Março',
    'Abril',
    'Maio',
    'Junho',
    'Julho',
    'Agosto',
    'Setembro',
    'Outubro',
    'Novembro',
    'Dezembro'
];

async function carregarVisitas() {
    try {
        const resposta = await fetch('/api/visitas');

        if (!resposta.ok) {
            throw new Error('Erro ao buscar visitas');
        }

        visitas.value = await resposta.json();

        criarGrafico();
    } catch (erro) {
        console.error('Erro ao carregar visitas:', erro);
    }
}

function quantidadePorMes() {
    const quantidades = Array(12).fill(0);

    visitas.value.forEach((visita) => {
        if (!visita.data_hora) {
            return;
        }

        const data = new Date(visita.data_hora);

        if (!isNaN(data.getTime())) {
            quantidades[data.getMonth()]++;
        }
    });

    return quantidades;
}

function criarGrafico() {
    if (!canvas.value) {
        return;
    }

    if (grafico.value) {
        grafico.value.destroy();
    }

    grafico.value = new Chart(canvas.value, {
        type: 'bar',
        data: {
            labels: nomesMeses,
            datasets: [
                {
                    label: 'Acessos',
                    data: quantidadePorMes(),
                    borderWidth: 1
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,

            onClick: (_evento, elementos) => {
                if (elementos.length === 0) {
                    return;
                }

                const indice = elementos[0]?.index;

                if (indice === undefined) {
                return;
                }   
            
                mesSelecionado.value = indice;
                anoSelecionado.value = new Date().getFullYear();
            },

            plugins: {
                legend: {
                    display: false
                }
            },

            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        precision: 0
                    }
                }
            }
        }
    });
}

function visitasDoMesSelecionado() {
    if (mesSelecionado.value === null) {
        return [];
    }

    return visitas.value
        .filter((visita) => {
            if (!visita.data_hora) {
                return false;
            }

            const data = new Date(visita.data_hora);

            return (
                data.getMonth() === mesSelecionado.value &&
                data.getFullYear() === anoSelecionado.value
            );
        })
        .sort((a, b) => {
            return (
                new Date(b.data_hora!).getTime() -
                new Date(a.data_hora!).getTime()
            );
        });
}

function formatarData(dataHora: string | null) {
    if (!dataHora) {
        return '-';
    }

    const data = new Date(dataHora);

    return data.toLocaleString('pt-BR', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
}

function fecharDetalhes() {
    mesSelecionado.value = null;
    anoSelecionado.value = null;
}

onMounted(() => {
    carregarVisitas();
});

onBeforeUnmount(() => {
    if (grafico.value) {
        grafico.value.destroy();
    }
});
</script>

<template>
    <section class="box">
        <h2 class="title is-4">
            👁 Dashboard de Visitantes
        </h2>

        <p class="subtitle is-6">
            Acessos por mês
        </p>

        <div class="grafico-container">
            <canvas ref="canvas"></canvas>
        </div>

        <div v-if="mesSelecionado !== null" class="mt-5">
            <div class="is-flex is-justify-content-space-between is-align-items-center">
                <h3 class="title is-5 mb-0">
                    Acessos em {{ nomesMeses[mesSelecionado] }} {{ anoSelecionado }}
                </h3>

                <button
                    class="button is-small"
                    @click="fecharDetalhes"
                >
                    Fechar
                </button>
            </div>

            <br>

            <div v-if="visitasDoMesSelecionado().length > 0" class="table-container">
                <table class="table is-fullwidth is-striped is-hoverable">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Data/Hora</th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr
                            v-for="visita in visitasDoMesSelecionado()"
                            :key="visita.id"
                        >
                            <td>{{ visita.id }}</td>
                            <td>{{ formatarData(visita.data_hora) }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <p v-else>
                Nenhum acesso registrado neste mês.
            </p>
        </div>
    </section>
</template>

<style scoped>
.grafico-container {
    position: relative;
    width: 100%;
    height: 350px;
}
</style>