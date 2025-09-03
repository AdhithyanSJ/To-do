<template>
  <div class="todos-page" :class="{ dark: isDark }">
    <h1>Todo List</h1>
    

<div class="d-grid gap-2 d-md-flex justify-content-md-end">
  <button @click="toggleDark()" class="btn btn-primary me-md-2" >
    Toggle {{ isDark ? 'Light':'Dark' }} MOde
</button>
  <button @click="signout" class="btn btn-primary" >signout</button>
</div>


    <div class="container-fluid">
      <form @submit.prevent="addTodo" class="d-flex gap-2">
        <input
          v-model="newTodoText"
          placeholder="Add a new todo"
          class="form-control"
        />
        <button type="submit" class="btn btn-primary">Add</button>
      </form>

      <table class="table table-striped mt-3">
        <thead>
          <tr>
            <th>#</th>
            <th>Task</th>
            <th>Status</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-if="todos.length === 0">
            <td colspan="4" class="text-center text-muted">
              No todos yet!
            </td>
          </tr>

          <tr v-for="todo in todos" :key="todo.tid">
            <td>{{ todo.tid }}</td>
            <td>
              <span
                :class="{ 'text-decoration-line-through text-muted': todo.status === 'completed' }"
              >
                {{ todo.name }}
              </span>
            </td>
            <td>
              <input
                type="checkbox"
                :checked="todo.status === 'completed'"
                :disabled="todo.status === 'completed'"
                @change="markTodo(todo)"
              />
            </td>
            <td>
              <button
                @click="removeTodo(todo)"
                class="btn btn-sm btn-danger"
              >
                Remove
              </button>
            </td>
          </tr>
        </tbody>
 </table>
    </div>
  </div>
</template>


<script setup>
import { ref, onMounted } from 'vue'
import {useToggle,useDark} from '@vueuse/core'

const isDark = useDark()
const toggleDark = useToggle(isDark)
const todos = ref([])
const newTodoText = ref('') 

const signout = () => {
  localStorage.removeItem('token')
  localStorage.removeItem('user_id')
this.$router.push('/login')

}
const fetchTodos = async () => {
    const token = localStorage.getItem('token')
  const res = await fetch(`https://to-do-t23j.onrender.com/api/todoslist/${localStorage.getItem('user_id')}`,{
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      }
 } )
  todos.value = await res.json()
  console.log(todos.value)

}
const addTodo = async () => {
    const token = localStorage.getItem('token')
  if (newTodoText.value.trim()=== '') return;
  const res = await fetch(`https://to-do-t23j.onrender.com/api/todoslist/${localStorage.getItem('user_id')}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify({ name: newTodoText.value, status: 'pending' })
  })
  const data = await res.json()
  alert(data.message)
  newTodoText.value = ""
  await fetchTodos()
}
const markTodo = async (todo) => {
    const token = localStorage.getItem('token')
  
  const res =  await fetch(`https://to-do-t23j.onrender.com/api/todoitem/${todo.tid}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify({ status: 'completed' })
  })
    const data = await res.json()
    alert(data.message)
  await fetchTodos()
}
const removeTodo = async (todo) => {
    const token = localStorage.getItem('token')
   const res = await fetch(`https://to-do-t23j.onrender.com/api/todoitem/${todo.tid}`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    }
})
  const data = await res.json()
  alert(data.message)
  await fetchTodos()
}
onMounted(() => {
  fetchTodos()
})
</script> 

<style scoped>
.todos-page {
  background: #fff;
  color: #000;
}

.todos-page.dark {
  background: #16171d;
  color: #fff;
}

    </style>
