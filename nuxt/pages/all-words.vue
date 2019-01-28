<template lang="pug">
section
  h1 Все слова
  span Все слова
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
      url: 'http://127.0.0.1:3001/api/word/get-all'
    })
    .then((response) => {
      return {
        allWords: response.data
      }
    })
  },
  computed: {

  },
  beforeCreate () {},
  created () {},
  beforeMount () {},
  mounted () {},
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
