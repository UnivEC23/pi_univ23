import { createRouter, createWebHistory } from 'vue-router'
// import HomeView from '../views/HomeView.vue'
import index from '../views/index2.vue'
import index2 from '../views/index.vue'
import sobre from '../views/sobre.vue'
import termos from '../views/termos.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'início',
      component: index,
    },
    {
      path: '/index2',
      name: 'index antigo',
      component: index2,
    },
    {
      path: '/sobre',
      name: 'sobre',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      // component: () => import('../views/sobre.vue'),
      component: sobre,
    },
    {
      path: '/termos',
      name: 'termos',
      component: termos,
    },
  ],
})

export default router
