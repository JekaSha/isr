// @modules/Tasks.js
import axios from '../axios';

const Tasks =  {
    get() {

        return axios.get('/tasks/', {
            headers: {
                'Content-Type': 'application/json'
            }
        });
    },

    add(task) {
        return axios.post('/tasks/', task, {
            headers: {
                'Content-Type': 'application/json'
            }
        });
    }
};

export default Tasks;
