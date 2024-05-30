// plugins/TasksPlugin.js
import Tasks from '../modules/Tasks';

export default {
    install(app) {
        app.config.globalProperties.$tasks = Tasks;
    }
};
