<template>
  <div>
    <ProjectMenu />
    <div>
      <h2>Login</h2>
      <form @submit.prevent="login">
        <input v-model="username" type="text" placeholder="Username" name="login"/>
        <input v-model="password" type="password" placeholder="Password" name="password"/>
        <button type="submit">Login</button>
        <p>{{ errorMessage }}</p>
      </form>
    </div>

    <div>
      <h2>Create User</h2>
      <form @submit.prevent="userCreate">
        <input v-model="username_new" type="text" placeholder="New Username" name="new_username"/>
        <input v-model="password_new" type="text" placeholder="New Password" name="new_password"/>
        <button type="submit">Create</button>
        <p>{{ errorMessage }}</p>
      </form>
    </div>

  </div>
</template>

<script>
import { ref } from 'vue';
import axios from '../axios';
import router from '../router'; // Импортировать объект router
import ProjectMenu from '../components/ProjectMenu.vue';



export default {
  components: {
    ProjectMenu
  },

  setup() {

    const username = ref('');
    const password = ref('');
    const errorMessage = ref('');

    const username_new = ref('');
    const password_new = ref('');

    const userCreate = () => {
        let u = username_new.value
        let p = password_new.value
        let obj = {
          username: u,
          password: p,
        }
        if (u && p) {
          axios.post('/user/', obj).then(response => {
            if (response.data.status === 'success') {
              // Use the router from the composition API
              alert('The user has been created.');
            } else {
              alert('User creation failed.');
            }
          }).catch(error => {
            if (error.response.status === 400) {
              errorMessage.value = 'The user with this name has already been created.'
            } else {
              console.error('Error during Create User:', error);
              alert('An error occurred during Create User. Please fix software');
            }
          })
        }
    };

    const login = () => {
      let u = username.value
      let p = password.value
      if (u && p) {
        axios.post('/login/', {
          username: u,
          password: p
        }).then(response => {
          if (response.data.status === 'success') {
            localStorage.setItem('token', response.data.token);
            router.push({name: 'Tasks'});
          } else {
            alert('Login failed');
          }
        }).catch(error => {
          if (error.response.status === 401) {
            errorMessage.value = 'Unauthorized: Check your username and password.';
          } else {
            console.error('Error during login:', error);
            alert('An error occurred during login. Please try again later.');
          }
        });
      }

    }

    return { errorMessage, username, password, login, userCreate, password_new, username_new };
  }
};
</script>
