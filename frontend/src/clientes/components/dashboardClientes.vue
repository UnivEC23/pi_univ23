<script setup lang="ts">
import { computed, onMounted, ref, watch } from 'vue'
import {
  Chart,
  BarController,
  BarElement,
  CategoryScale,
  LinearScale,
  PieController,
  ArcElement,
  Tooltip,
  Legend
} from 'chart.js'
import ChartDataLabels from 'chartjs-plugin-datalabels'
import {
  estados_str,
  setor_str,
  genero_str,
  idade_str
} from '@/clientes/types'

Chart.register(
  BarController,
  BarElement,
  CategoryScale,
  LinearScale,
  PieController,
  ArcElement,
    Tooltip,
  Legend,
  ChartDataLabels
)

const graficoGenero = ref<HTMLCanvasElement | null>(null)
const graficoSetor = ref<HTMLCanvasElement | null>(null)
const graficoIdade = ref<HTMLCanvasElement | null>(null)

const clientes = ref<any[]>([])

const estadoSelecionado = ref<number | 'brasil'>('brasil')

const estadosDisponiveis = [
  { codigo: 'brasil', nome: 'Brasil' },
  ...Array.from({ length: 27 }, (_, indice) => ({
    codigo: indice + 1,
    nome: estados_str(indice + 1)
  }))
]

const clientesExpostos = computed(() => {
  if (estadoSelecionado.value === 'brasil') {
    return clientes.value
  }

  return clientes.value.filter(
    cliente => Number(cliente.estados) === estadoSelecionado.value
  )
})

/* =========================
   CLIENTE PADRÃO
========================= */

const clientePadrao = computed(() => {
  const dados = clientesExpostos.value

  if (!dados.length) {
    return null
  }

 const maisFrequente = (valores: number[]) => {
  const contagem: Record<number, number> = {}

  valores.forEach(valor => {
    contagem[valor] = (contagem[valor] || 0) + 1
  })

  // NOVA VERSÃO:
  const chaves = Object.keys(contagem)
  let codigoMaisFrequente = Number(chaves[0] ?? 0)

  for (const chave of chaves) {
    const quantidadeAtual = contagem[Number(chave)] ?? 0
    const quantidadeMaior = contagem[codigoMaisFrequente] ?? 0

    if (quantidadeAtual > quantidadeMaior) {
      codigoMaisFrequente = Number(chave)
    }
  }

  return codigoMaisFrequente
}

return {
  genero: maisFrequente(dados.map(cliente => Number(cliente.genero))),
  setor: maisFrequente(dados.map(cliente => Number(cliente.setor))),
  idade: maisFrequente(dados.map(cliente => Number(cliente.idade))),

  // VERSÃO ANTERIOR:
  // estado: maisFrequente(dados.map(cliente => Number(cliente.estados)))

  // NOVA VERSÃO:
  estado: estadoSelecionado.value === 'brasil'
    ? 0
    : estadoSelecionado.value
}
})

const filtroAtivo = ref('')
const clientesFiltrados = ref<any[]>([])

let chartGenero: Chart | null = null
let chartSetor: Chart | null = null
let chartIdade: Chart | null = null

onMounted(async () => {
  try {
    const response = await fetch('/api/clientes')

    if (!response.ok) {
      throw new Error('Erro ao buscar clientes')
    }

    const data = await response.json()

    clientes.value = Array.isArray(data)
      ? data
      : data.clientes || []

    criarGraficoGenero()
    criarGraficoSetor()
    criarGraficoIdade()

  } catch (error) {
    console.error('Erro ao carregar dados dos gráficos:', error)
  }
})


/* =========================
   GRÁFICO DE GÊNERO
========================= */

function criarGraficoGenero() {
  if (!graficoGenero.value) return

  const categorias = [1, 2, 3]

// VERSÃO ANTERIOR:
// const categoriasAtivas = categorias.filter(codigo =>
//   clientes.value.some(
//     cliente => Number(cliente.genero) === codigo
//   )
// )

const categoriasAtivas = categorias.filter(codigo =>
  clientesExpostos.value.some(
    cliente => Number(cliente.genero) === codigo
  )
)

  const dados = categoriasAtivas.map(codigo =>
  clientesExpostos.value.filter(
    cliente => Number(cliente.genero) === codigo
  ).length
)

  const labels = categoriasAtivas.map(codigo =>
    genero_str(codigo as any)
  )

  if (chartGenero) {
    chartGenero.destroy()
  }

  chartGenero = new Chart(graficoGenero.value, {
    type: 'pie',

    data: {
      labels,

      datasets: [
        {
          data: dados,
          backgroundColor: ['#4A90E2', '#E91E63']
        }
      ]
    },

    options: {
      responsive: true,

      maintainAspectRatio: false,

      plugins: {
  legend: {
    position: 'bottom'
  },
  datalabels: {
    color: '#ffffff',
    font: {
      weight: 'bold',
      size: 16
    },
    formatter: (valor, contexto) => {
      const dados = (contexto.chart.data.datasets[0]?.data ?? []) as number[]
      const total = dados.reduce(
        (soma, atual) => soma + Number(atual),
        0
      )

      const percentual = total
        ? ((Number(valor) / total) * 100).toFixed(0)
        : '0'

      return `${valor} (${percentual}%)`
    }
  }
},

      onClick: (_event, elementos) => {
        if (!elementos.length) return

        const elemento = elementos[0]
        if (!elemento) return

        const indice = elemento.index
        const codigo = categoriasAtivas[indice]

  if (codigo === undefined) return

        aplicarFiltro(
          'Gênero',
          codigo,
          genero_str(codigo as any)
        )
      }
    }
  })
}


/* =========================
   GRÁFICO DE SETOR
========================= */

function criarGraficoSetor() {
  if (!graficoSetor.value) return

  const categorias = [1, 2, 3, 4]

// VERSÃO ANTERIOR:
// const dados = categorias.map(codigo =>
//   clientes.value.filter(
//     cliente => Number(cliente.setor) === codigo
//   ).length
// )

const dados = categorias.map(codigo =>
  clientesExpostos.value.filter(
    cliente => Number(cliente.setor) === codigo
  ).length
)

  const labels = categorias.map(codigo =>
    setor_str(codigo as any)
  )

  if (chartSetor) {
    chartSetor.destroy()
  }

  chartSetor = new Chart(graficoSetor.value, {
    type: 'bar',

    data: {
      labels,

      datasets: [
        {
          label: 'Quantidade de clientes',
          data: dados,
          backgroundColor: [
            '#4A90E2',
            '#50B87B',
            '#F5A623',
            '#8E6BBE'
          ]
        }
      ]
    },

    options: {
      responsive: true,

      maintainAspectRatio: false,

      scales: {
        y: {
          beginAtZero: true,

          ticks: {
            precision: 0
          }
        }
      },

      plugins: {
        legend: {
          display: false
        }
      },

      onClick: (_event, elementos) => {
        if (!elementos.length) return

        const elemento = elementos[0]
if (!elemento) return

const indice = elemento.index
const codigo = categorias[indice]

if (codigo === undefined) return

        aplicarFiltro(
          'Setor',
          codigo,
          setor_str(codigo as any)
        )
      }
    }
  })
}


/* =========================
   GRÁFICO DE IDADE
========================= */

function criarGraficoIdade() {
  if (!graficoIdade.value) return

  const categorias = [1, 2, 3, 4]

// VERSÃO ANTERIOR:
// const dados = categorias.map(codigo =>
//   clientes.value.filter(
//     cliente => Number(cliente.idade) === codigo
//   ).length
// )

const dados = categorias.map(codigo =>
  clientesExpostos.value.filter(
    cliente => Number(cliente.idade) === codigo
  ).length
)

  const labels = categorias.map(codigo =>
    idade_str(codigo as any)
  )

  if (chartIdade) {
    chartIdade.destroy()
  }

  chartIdade = new Chart(graficoIdade.value, {
    type: 'bar',

    data: {
      labels,

      datasets: [
        {
          label: 'Quantidade de clientes',
          data: dados,
          backgroundColor: [
            '#4A90E2',
            '#50B87B',
            '#F5A623',
            '#8E6BBE'
         ]
        }
      ]
    },

    options: {
      responsive: true,

      maintainAspectRatio: false,

      scales: {
        y: {
          beginAtZero: true,

          ticks: {
            precision: 0
          }
        }
      },

      plugins: {
        legend: {
          display: false
        }
      },

      onClick: (_event, elementos) => {
        if (!elementos.length) return

        const elemento = elementos[0]
if (!elemento) return

const indice = elemento.index
const codigo = categorias[indice]

if (codigo === undefined) return

        aplicarFiltro(
          'Faixa etária',
          codigo,
          idade_str(codigo as any)
        )
      }
    }
  })
}

/* =========================
   ATUALIZAÇÃO DOS GRÁFICOS
========================= */

function atualizarGraficos() {
  criarGraficoGenero()
  criarGraficoSetor()
  criarGraficoIdade()
}

watch(estadoSelecionado, () => {
  atualizarGraficos()
})


/* =========================
   FILTRO
========================= */

function aplicarFiltro(
  tipo: string,
  codigo: number,
  nome: string
) {
  filtroAtivo.value = `${tipo}: ${nome}`

  if (tipo === 'Gênero') {

    // VERSÃO ANTERIOR:
    // clientesFiltrados.value = clientes.value.filter(
    //   cliente => Number(cliente.genero) === codigo
    // )

    // NOVA VERSÃO:
    clientesFiltrados.value = clientesExpostos.value.filter(
      cliente => Number(cliente.genero) === codigo
    )
  }

  if (tipo === 'Setor') {

    // VERSÃO ANTERIOR:
    // clientesFiltrados.value = clientes.value.filter(
    //   cliente => Number(cliente.setor) === codigo
    // )

    // NOVA VERSÃO:
    clientesFiltrados.value = clientesExpostos.value.filter(
      cliente => Number(cliente.setor) === codigo
    )
  }

  if (tipo === 'Idade') {

    // VERSÃO ANTERIOR:
    // clientesFiltrados.value = clientes.value.filter(
    //   cliente => Number(cliente.idade) === codigo
    // )

    // NOVA VERSÃO:
    clientesFiltrados.value = clientesExpostos.value.filter(
      cliente => Number(cliente.idade) === codigo
    )
  }
}

/* =========================
   LIMPAR FILTRO
========================= */

function limparFiltro() {
  filtroAtivo.value = ''
  clientesFiltrados.value = []
}


/* =========================
   ESTADOS
========================= */

function contarEstados() {
  const contagem: Record<string, number> = {}

  clientesFiltrados.value.forEach(cliente => {
    const estado = estados_str(cliente.estados)

    contagem[estado] = (contagem[estado] || 0) + 1
  })

  return Object.entries(contagem)
}
</script>


<template>

  <div class="dashboard">

    <div class="cabecalho-dashboard">

      <h2 class="title is-4">
        Visualização dos dados
      </h2>

      <!-- FILTRO POR ESTADO -->
<div class="campo-estado">
  <label class="label">Estado</label>

  <div class="select">
    <select v-model="estadoSelecionado">
      <option
        v-for="estado in estadosDisponiveis"
        :key="estado.codigo"
        :value="estado.codigo"
      >
        {{ estado.nome }}
      </option>
    </select>
  </div>
</div>

      <button
        v-if="filtroAtivo"
        class="button is-light"
        @click="limparFiltro"
      >
        Limpar seleção
      </button>

    </div>

    <!-- CLIENTE PADRÃO -->
    <div v-if="clientePadrao" class="box cliente-padrao">
      <h3 class="title is-5">
        Cliente padrão
      </h3>

      <p>
        <strong>Gênero:</strong>
        {{ clientePadrao.genero === 1 ? 'Masculino' :
           clientePadrao.genero === 2 ? 'Feminino' : 'Outro' }}
      </p>

      <p>
        <strong>Setor:</strong>
        {{ clientePadrao.setor === 1 ? 'Comércio' :
           clientePadrao.setor === 2 ? 'Serviços' :
           clientePadrao.setor === 3 ? 'Indústria' : 'Outros' }}
      </p>

      <p>
        <strong>Faixa etária:</strong>
        {{ clientePadrao.idade === 1 ? 'Até 20' :
           clientePadrao.idade === 2 ? '21–39' :
           clientePadrao.idade === 3 ? '40–59' : '60+' }}
      </p>

      <p>
        <strong>Estado:</strong>
        {{ estados_str(clientePadrao.estado) }}
      </p>
    </div>

    <!-- GRÁFICOS -->

    <div class="columns is-multiline">


      <!-- GÊNERO -->

      <div class="column is-4">

        <div class="box grafico-box">

          <h3 class="title is-5">
            Clientes por gênero
          </h3>

          <p class="instrucao">
            Clique em uma categoria para filtrar
          </p>

          <div class="grafico">
            <canvas ref="graficoGenero"></canvas>
          </div>

        </div>

      </div>


      <!-- SETOR -->

      <div class="column is-4">

        <div class="box grafico-box">

          <h3 class="title is-5">
            Clientes por setor
          </h3>

          <p class="instrucao">
            Clique em uma categoria para filtrar
          </p>

          <div class="grafico">
            <canvas ref="graficoSetor"></canvas>
          </div>

        </div>

      </div>


      <!-- IDADE -->

      <div class="column is-4">

        <div class="box grafico-box">

          <h3 class="title is-5">
            Clientes por idade
          </h3>

          <p class="instrucao">
            Clique em uma faixa etária para filtrar
          </p>

          <div class="grafico">
            <canvas ref="graficoIdade"></canvas>
          </div>

        </div>

      </div>

    </div>


    <!-- RESULTADO DO FILTRO -->

    <div
      v-if="filtroAtivo"
      class="box resultado-filtro"
    >

      <div class="resultado-cabecalho">

        <div>

          <h3 class="title is-4">
            {{ filtroAtivo }}
          </h3>

          <p class="subtitulo">
            {{ clientesFiltrados.length }}
            cliente(s) encontrado(s)
          </p>

        </div>

        <button
          class="button is-light"
          @click="limparFiltro"
        >
          Limpar seleção
        </button>

      </div>


      <!-- ESTADOS -->

      <div
        v-if="clientesFiltrados.length"
        class="estado-resumo"
      >

        <h4 class="title is-5">
          Distribuição por estado
        </h4>

        <div class="estado-lista">

          <div
            v-for="[estado, quantidade] in contarEstados()"
            :key="estado"
            class="estado-item"
          >

            <span>
              {{ estado }}
            </span>

            <strong>
              {{ quantidade }}
            </strong>

          </div>

        </div>

      </div>


      <!-- CLIENTES -->

      <div class="clientes-detalhes">

        <h4 class="title is-5">
          Clientes encontrados
        </h4>

        <div class="table-container">

          <table class="table is-fullwidth">

            <thead>

              <tr>
                <th>Nome</th>
                <th>Estado</th>
                <th>Email</th>
              </tr>

            </thead>

            <tbody>

              <tr
                v-for="cliente in clientesFiltrados"
                :key="cliente.id"
              >

                <td>
                  {{ cliente.nome }}
                </td>

                <td>
                  {{ estados_str(cliente.estados) }}
                </td>

                <td>
                  {{ cliente.email }}
                </td>

              </tr>

            </tbody>

          </table>

        </div>

      </div>

    </div>

  </div>

</template>


<style scoped>

.dashboard {
  width: 100%;
}

.cabecalho-dashboard {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.cabecalho-dashboard .title {
  color: white;
  margin-bottom: 0;
}

.cliente-padrao .title {
  color: #363636;
}

.grafico-box {
  height: 100%;
  background: white;
}

.grafico-box .title {
  color: #363636;
}

.instrucao {
  color: #777;
  font-size: 0.85rem;
  margin-bottom: 0.75rem;
}

.grafico {
  position: relative;
  height: 280px;
  width: 100%;
}

canvas {
  max-width: 100%;
  max-height: 100%;
}

.resultado-filtro {
  margin-top: 1rem;
  background: white;
}

.resultado-cabecalho {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 1rem;
}

.resultado-filtro .title {
  color: #363636;
}

.subtitulo {
  color: #777;
  margin-top: -0.75rem;
  margin-bottom: 1.5rem;
}

.estado-resumo {
  margin-bottom: 2rem;
}

.estado-lista {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
}

.estado-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;

  min-width: 180px;

  padding: 0.75rem 1rem;

  border: 1px solid #ddd;
  border-radius: 6px;

  background: #f7f7f7;
}

.estado-item strong {
  font-size: 1.1rem;
}

.clientes-detalhes {
  margin-top: 1rem;
}

.table-container {
  overflow-x: auto;
}

.clientes-detalhes table {
  background: white;
}

.clientes-detalhes th {
  color: #363636;
}

.clientes-detalhes td {
  color: #363636;
}

@media (max-width: 768px) {

  .cabecalho-dashboard {
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
  }

  .resultado-cabecalho {
    flex-direction: column;
  }

}

</style>