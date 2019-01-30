<template lang="pug">
div
  h2 Все слова пользователя {{myName}}
  table
    tbody
      tr(v-for="word in allWords")
        td {{word.value}}
        td 
          span(v-for="trans in word.trans") {{trans.value}}, 
        td удалить
</template>
<!-- is, v-for, v-if, v-else-if, v-else, v-show, v-cloak, v-pre, v-once, id, ref, key, slot, v-model, другие атрибуты, v-on, v-html, v-text -->
<script>
import axios from 'axios' 
export default {
  components: {},
  mixins: [],
  model: [],
  props: [],
  asyncData () {
    return axios({
      method: 'get',
      url: 'http://127.0.0.1:3001/api/word/get-all/en-ru'
    })
    .then((response) => {
      return {
        allWords: response.data,
        myName: ""
      }
    })
  },
  computed: {

  },
  beforeCreate () {},
  created () {},
  beforeMount () {},
  mounted () {
    if (process.client) {
      if(localStorage.myName){
        this.myName = localStorage.myName
      }
    }
  },
  beforeUpdate () {},
  updated () {},
  activated () {},
  deactivated () {},
  beforeDestroy () {},
  destroyed () {},
  methods: {

  },
}
</script>
<style>
table {
  width: 100%;
}
td {
  border: 1px solid black;
}
</style>
