import axios from 'axios';

const instance = axios.create({
    baseURL: 'http://localhost:8000/api',
});

instance.interceptors.request.use(
    config => {
        const token = localStorage.getItem('token');
        if (token) {
            config.headers['Authorization'] = `Bearer ${token}`;
        }
        return config;
    },
    error => {
        return Promise.reject(error);
    }
);

instance.interceptors.response.use(
    response => response,
    error => {

        if (error.response && error.response.status === 401) {
            console.log('error')
        }
        return Promise.reject(error);
    }
);

export default instance;
