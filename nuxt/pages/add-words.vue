<template lang="pug">
section
  h2 Добавление новых слов в словарь
  div 
    select(v-if="myDicts.length > 0" v-model="currentDict" @change="show_word_in_dict()")
      option(v-for="dict in myDicts" :value="dict.id" :key="'dict_' + dict.id") {{dict.name}}
  .GeneralContainer
    span {{lang_1}}
    input(type="text"
          placeholder="Слово"
          v-model="word"
          @blur="get_word_translates"
          list="wordDatalist")
    span {{lang_2}}
    input(type="text"
          placeholder="Перевод слова"
          v-model="translate"
          list="translateDatalist")
    datalist#translateDatalist
      option(v-for="(trans, key) in translates") {{trans}}
  .ButtonContainer
    button(@click="addWord") Добавить слово
  div
    table
      tbody
        tr(v-for="(transArray, word) in currentWords" :key="'curWord_'+word")
          td(width="30%") {{word}}
          td
            span(v-for="(trans, key) in transArray"
            :key="'curWord' + word + '_' + key") {{key == transArray.length - 1 ? trans.translate : trans.translate + ','}} 
</template>
<!-- is, v-for, v-if, v-else-if, v-else, v-show, v-cloak, v-pre, v-once, id, ref, key, slot, v-model, другие атрибуты, v-on, v-html, v-text -->
<script>
import axios from 'axios'
export default {
  components: {},
  asyncData () {
    return {
      word: "",
      translate: "",
      lang_1: '',
      lang_2: '',
      currentWords: {},
      translates:[],
      myDicts: [],
      currentDict: 0
    }
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
          }
        })
      }
    }
  },
  computed: {
    currentRusWord: {
      set(val) {
        this.$data._currentRusWord = val
      },
      get() {
        return this.$data.SysCurrentRusWord.toLowerCase().trim().replace(/[.,\/#!$%\^&\*;:{}=\-_`~()\\]/g,"")
      }
    },
    currentEngWord: {
      set(val) {
        this.$data._currentRusWord = val
      },
      get() {
        return this.$data.SysCurrentEngWord.toLowerCase().trim().replace(/[.,\/#!$%\^&\*;:{}=\-_`~()\\]/g,"")
      }
    },
  },
  methods: {
    get_word_translates() {
      if (this.word.length > 0) {
        axios({
          method: 'post',
          url: '/api/word/get-word-translates/',
          data: {
            word: this.word,
            lang: this.lang_1
          }
        })
        .then((response) => {
          this.translates = response.data
        })
      }
    },
    show_word_in_dict () {
      if (process.client) {
        let dict_id = this.currentDict
        if (dict_id > 0) {
          axios({
            method: 'post',
            url: '/api/word/get-all-from-dict/',
            data: {
              userId: localStorage.userId,
              dictId: dict_id
            },
          })
          .then((response) => {
            this.lang_1 = response.data.lang
            this.lang_2 = response.data.trans_lang
            this.currentWords = response.data.words
          })
        }
      }
    },
    checkWord () {
      let word = this.word
      let translate = this.translate
      if (word.length > 0 && translate.length > 0) {
        if (this.currentDict>0){
          return true
        }
      }
    },
    word_in_translates (arr, word) {
      for (let i of arr){
        if (i.translate == word){
          return true
        }
      }
    },
    addWord () {
      if (this.checkWord()) {
        let word = this.word
        let translate = this.translate
        axios({
          method: 'post',
          url: '/api/word/add',
          data: {
            userId: localStorage.userId,
            dictId: this.currentDict,
            word: word,
            translate: translate
          },
        })
        .then((response) => {
          let res = response.data
          if (!(res.word in this.currentWords)){
            this.$set(this.currentWords, res.word, [])
          }
          if (!this.word_in_translates(this.currentWords[res.word], res.translate)){
            this.currentWords[res.word].push({
              translate: res.translate,
              associate_id: res.associate_id,
            })
          }
        })
      }

      
    }
  }
}
</script>
<style scope>
  .MenuContainer {
    text-align: center;
  }
  .MenuContainer select {
    height: 2em;
    color: black;
    border: 1px solid black;
    border-radius: .3em;
    margin: 0 .5em;
    background: silver;
  }
  .GeneralContainer, .ButtonContainer {
    margin-top: 1em;
    text-align: center;
  }
  .ButtonContainer button {
    cursor: pointer;
  }
  .ButtonContainer button:hover {
    background: SlateGrey;
  }
  table {
    margin-top: 2em; 
    width: 100%;
  }
  td {
    text-align: center;
    border: 1px solid black;
  }
</style>
