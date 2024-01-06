import { createRouter, createWebHistory } from 'vue-router'
import CurrenciesPage from './pages/CurrenciesPage.vue'
import CryptoPage from './pages/CryptoPage.vue'

const routes = [
  {
    path: '/',
    component: CurrenciesPage,
    name: 'CurrenciesPage'
  },
  {
    path: '/crypto',
    component: CryptoPage,
    name: 'CryptoPage'
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
