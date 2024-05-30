import { createRouter, createWebHistory } from 'vue-router';
import LoginForm from '../components/LoginForm.vue';
import TasksList from '../components/TasksList.vue';
import IndexPage from '../components/IndexPage.vue';

const routes = [
  { path: '/', name:"Home", component: IndexPage},
  { path: '/tasks', name: 'Tasks', component: TasksList },
  { path: '/login', name: 'Login', component: LoginForm }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
