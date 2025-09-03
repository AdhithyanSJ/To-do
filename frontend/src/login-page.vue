<template>
  <div class="login">
    <h2>Login</h2>
    <form @submit.prevent="handleLogin">
    <label for="email">Email</label>
      <input v-model="email" type="email" placeholder="you@example.com" required />
    <label for="password">Password</label>
      <input v-model="password" type="password" placeholder="Password" required />
      <button type="submit">Login</button>
    </form>
    <p>{{ message }}</p>
    <p>Don't have an account?</p>
    <router-link to="/signup">Signup</router-link>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      password: '',
      message: ''
    };
  },
  methods: {
    async handleLogin() {
      try {
        console.log('Logging in with:', this.email, this.password);
       const post_data = {'email': this.email, 'password': this.password}
        const response = await fetch('http://127.0.0.1:5000/api/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(post_data)
        });
        const result = await response.json();

        if (response.ok) {
          this.message = `Welcome, ${result.user}`;
          localStorage.setItem('token', result.token);
          localStorage.setItem('user_id', result.user.id);
      
          if (result.user.role === 'admin') {
            this.$router.push('/admin');
          } else {
            this.$router.push('/todoslist');
          }
        } else {
          this.message = result.message;
        }
      } catch (error) {
        console.error(error);
        this.message = 'Server error';
      }
    }
  }
};
</script>

<style scoped>
.login {
  max-width: 400px;
  margin: auto;
  text-align: center;
}
input {
  display: block;
  width: 100%;
  margin: 10px 0;
  padding: 10px;
}
button {
  padding: 10px 20px;
}
</style>
