<template lang="pug">
div
  h2 Словари {{myName}}
  input(type="text"
    v-model="newDictName"
    placeholder="Новый словарь")
  button(@click="addDict") Добавить словарь
  br
  select(v-if="myDicts.length > 0")
    option(v-for="dict in myDicts" :value="dict.id" :key="'dict_' + dict.id") {{dict.name}}
  button(@click="showDictWord") Показать слова в словаре
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
    return {
      myName: "",
      myDicts: [],
      currentDict: 0,
      newDictName: "",
      lang: "en",
      transLang: "ru"
    }
  },
  computed: {

  },
  mounted () {
    if (process.client) {
      if(localStorage.userName){
        this.myName = localStorage.userName
        axios({
          method: 'post',
          url: 'api/dictionary/get-all-dicts-name',
          data: {
            userId: localStorage.userId
          }
        }).then((req) => {
          if (req.data) {
            this.myDicts = req.data
            console.log(req.data)
          }
        })
      }
    }
  },
  methods: {
    showDictWord(){
      console.log('test')
    },
    addDict () {
      if (this.newDictName.length > 0 && localStorage.userId)
      {
        axios({
          method: 'post',
          url: 'api/dictionary/new',
          data: {
            userId: localStorage.userId,
            dictName: this.newDictName,
            lang: this.lang,
            transLang: this.transLang
          }
        })
        .then((req) => {
          if (req.data.id) {
            this.myDicts.push(req.data)
          }
        })
      }
    }
  }
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
