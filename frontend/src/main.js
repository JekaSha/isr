import { createApp } from 'vue';
import App from './App.vue';
import axios from 'axios';
import router from './router';
import TasksPlugin from './plugins/TasksPlugin';

const app = createApp(App);

app.use(router);
app.config.globalProperties.$axios = axios;
app.use(TasksPlugin)
app.mount('#app');
