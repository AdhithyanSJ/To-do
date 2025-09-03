import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../home-page.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePage,
    },
    {
       path: '/login', name: 'Login', component: () => import('../login-page.vue') 
    },
    {
      path: '/signup' , name: 'Signup', component: () => import('../signup-page.vue')
    },
    {
      path: '/todoslist', name: 'Todos', component: () => import('../todos-page.vue')
    },
   
   

  ],
})

export default router
