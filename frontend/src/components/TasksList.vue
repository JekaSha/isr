<template>
  <div>
    <h2>Tasks</h2>
    <ProjectMenu />
    <form @submit.prevent="addTask">
      <input
          v-model="caption" type="text" placeholder="Caption"
          :style="{ backgroundColor: captionEmpty && captionTouched  ? '#FD7279' : 'initial' }"
          @input="captionTouched = true"
          @focus="captionTouched = true"
          @blur="captionTouched = !!caption.trim()"
      />
      <textarea
          v-model="body" placeholder="Body"
          :style="{ backgroundColor: bodyEmpty && bodyTouched ? '#FD7279' : 'initial' }"
          @input="bodyTouched = true"
          @focus="bodyTouched = true"
          @blur="bodyTouched = !!body.trim()"
      ></textarea>
      <button type="submit">Add Task</button>
      <button @click="logout">Logout</button>
    </form>
    <ul>
      <li v-for="task in tasks" :key="task.id">
        <h3 id="caption">{{ task.caption }}</h3>
        <p id="body">{{ task.body }}</p>
        <p>Owner: {{ task.user.username }}</p>
        <p>Created at: {{ task.created_at }}</p>
      </li>
    </ul>
  </div>
</template>

<script>
import ProjectMenu from '../components/ProjectMenu.vue';

export default {

  components: {
    ProjectMenu
  },

  data() {
    return {
      tasks: [],
      caption: '',
      body: '',
      captionTouched: false,
      bodyTouched: false
    };
  },

  computed: {
    captionEmpty() {
      return !this.caption.trim();
    },
    bodyEmpty() {
      return !this.body.trim();
    }
  },

  methods: {
    logout() {

      localStorage.removeItem('token');
      this.$router.push('/login');

    },

    fetchTasks() {

      this.$tasks.get()
        .then(response => {
          this.tasks = response.data;
        }) .catch(error => {
        if (error.response && (error.response.status === 403 || error.response.status === 401)) {
          // Redirect to login page if user is not authenticated
          this.$router.push('/login');
        } else {
          console.error(error);
        }
      });
    },
    addTask() {
      if (!this.caption) {

        return false
      }

      this.$tasks.add({
        caption: this.caption,
        body: this.body
      }).then(response => {
        this.tasks.unshift(response.data);
        this.caption = '';
        this.body = '';
      });
    }
  },
  mounted() {
    this.fetchTasks();
  }
};
</script>

<style>

li:nth-child(even) {
  background-color: white;
}

li:nth-child(odd) {
  background-color: #f2f2f2;
}

</style>
