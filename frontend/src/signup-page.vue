<template>
  <div class="signup">
    <h2>Signup</h2>
    <form @submit.prevent="handleSignup">
    <label for="email">Email</label>
      <input v-model="email" type="email" placeholder="you@example.com" required />
    <label for="fullname">Fullname</label>
      <input v-model="fullname" type="fullname" placeholder="Fullname" required />
    <label for="password">Password</label>
      <input v-model="password" type="password" placeholder="Password" required />
      <button type="submit">Signup</button>
    </form>
    <p>{{ message }}</p>
    <p>Already have an account?</p>
    <router-link to="/login">Login</router-link>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      fullname: '',
      password: '',
      message: ''
    };
  },
  methods: {
    async handleSignup() {
      try {
        console.log('Signing up with:', this.email, this.fullname, this.password);
       const post_data = {'email': this.email, 'fullname':this.fullname,'password': this.password}
        const response = await fetch('http://127.0.0.1:5000/api/signup', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(post_data)
        });
        const result = await response.json();
        console.log('Response from backend:', result);

        if (response.ok) {
        alert('Registered successfully. Please login.');
        this.$router.push('/login');

        } else {
          this.message = result.message;
        }
      } catch (err) {
        this.message = 'Server error';
        console.error(err);
      }
    }
  }
};
</script>

<style scoped>
.signup {
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