<template lang="pug">
  section
    h2 {{myNameSys.length == 0 ? "Зарегистрируйтесь или войдите": "Я " + myNameSys}}
    div.LoginContainer
      input(v-if="myNameSys.length == 0" v-model="myName" placeholder="мое имя")
    button(v-if="myNameSys.length == 0" @click="registrate") Зарегистрироваться
    button(v-if="myNameSys.length != 0" @click="exit") Выйти
</template>

<script>
import axios from 'axios'
export default {
  component: {
  },
  asyncData () {
    return {
      myNameSys: "",
      myName: ""
    }
  },
  methods: {
    registrate () {
      if (this.myName.length != 0) {
        let fd = new FormData()
        fd.append('name', this.myName)
        axios({
          method: 'post',
          url: '/api/user/registrate',
          data: fd,
          config: { headers: {'Content-Type': 'multipart/form-data' }},
        })
        .then((response) => {
          this.myNameSys = response.data['user_name']
          localStorage.userName = response.data['user_name']
          localStorage.userId = response.data['user_id']
        })
      }
    },
    exit () {
      localStorage.userName = '',
      this.myNameSys = ''
    }
  },
  mounted () {
    if (process.client) {
      if (localStorage.userName){
        this.myNameSys = localStorage.userName
      }
    }
  }
}
</script>

<style>
.LoginContainer {
  text-align: center;
}
section {
  text-align: center;
}
input {
  background: silver;
  height: 2em;
  border: 1px solid black;
  border-radius: .3em;
  margin: 0 .5em;
  text-align: center;
}
</style>
