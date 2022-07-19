import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../components/HomePage.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../components/LoginView.vue')
  },
  {
    path: '/playground',
    name: 'Playground',
    component: () => import('../views/PlaygroundView.vue')
  },
  {
    path: '/crear-ejercicio',
    name: 'Crear ejercicio',
    component: () => import('../views/CreateTaskView.vue')
  },
  {
    path: '/crear-clase',
    name: 'Crear clase',
    component: () => import('../views/CreateClassView.vue')
  },
  {
    path: '/alumnos',
    name: 'Estudiantes',
    component: () => import('../views/StudentsView.vue')
  },
  {
    path: '/usuarios/:id',
    name: 'Estudiante',
    component: () => import('../views/StudentView.vue')
  },
  {
    path: '/agregar-tecnologia',
    name: 'Agregar tecnologia',
    component: () => import('../views/AddTechnologyView.vue')
  },
  {
    path: '/clases/:id',
    name: 'Clases',
    component: () => import('../views/ClassesView.vue')
  },
  {
    path: '/tecnologias-clases',
    name: 'Tecnologias Clases',
    component: () => import('../views/TechnologyClassView.vue')
  },
  {
    path: '/clases/:id',
    name: 'Clase',
    component: () => import('../views/ClassView.vue')
  },
  {
    path: '/ejercicios/:id',
    name: 'Ejercicios',
    component: () => import('../views/TasksView.vue')
  },
  {
    path: '/tecnologias-ejercicios',
    name: 'Tecnologias Ejercicios',
    component: () => import('../views/TechnologyTaskView.vue')
  },
  {
    path: '/ejercicios/:id',
    name: 'Ejercicio',
    component: () => import('../views/TaskView.vue')
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  document.title = to.name;
  next();
});

export default router
