<template lang="pug">
section
  h2 Добавление новых слов в словарь
  .MenuContainer
    select(v-model="lang_1")
      option(value="en") Английский
      option(value="ru") Русский
    select(v-model="lang_2")
      option(value="en") Английский
      option(value="ru") Русский
  .GeneralContainer
    input(type="text"
          placeholder="Слово"
          v-model="SysCurrentEngWord")
    input(type="text"
          placeholder="Перевод слова"
          v-model="SysCurrentRusWord")
  .ButtonContainer
    button(@click="addWord") Добавить слово
  div
    table
      tbody
        tr(v-for="(word, key) in getWordWithTranslateByLang" :key="'curWord_'+key")
          td {{word.value}}
          td
            span(v-for="(word_1, key_1) in word.translate"
            :key="'curWord' + key + '_' + key_1"
            @click="delTranslate({key, RusKey})") {{word_1}}, 
</template>
<!-- is, v-for, v-if, v-else-if, v-else, v-show, v-cloak, v-pre, v-once, id, ref, key, slot, v-model, другие атрибуты, v-on, v-html, v-text -->
<script>
import axios from 'axios'
export default {
  components: {},
  asyncData () {
    return {
      SysCurrentRusWord: "",
      SysCurrentEngWord: "",
      lang_1: 'en',
      lang_2: 'ru',
      currentWords: []
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
    getWordWithTranslateByLang() {
      let arr = []
      let lang = this.lang_1
      let lang_trans = this.lang_2
      for (let word of this.currentWords) {
        if(word.lang == lang) {
          let trans_arr = []
          for(let trans of word.translate) {
            if (trans.lang == lang_trans) {
              trans_arr.push(trans.value)
            }
          }
          arr.push({value: word.value, translate: trans_arr})
        }
      }
      return arr
    }
  },
  methods: {
    delTranslate (obj) {
      let key = obj.key
      let RusKey = obj.RusKey
      if (this.currentWords[key].rus.length == 1) {
        this.delEngWord(key)
      }
      else {
        this.currentWords[key].rus.splice(RusKey, 1)
      }
    },
    delEngWord(key) {
      this.currentWords.splice(key, 1)
    },
    addWordsToData (words) {
      let word_0 = this.addWordToData(words[0])
      let word_1 = this.addWordToData(words[1])
      this.addTranslateIfNotExist(word_0, word_1)
      this.addTranslateIfNotExist(word_1, word_0)
    },
    addTranslateIfNotExist(w1, w2) {
      for (let i of this.currentWords) {
        if(i.lang == w1.lang) {
          if (i.value == w1.value) {
            w1.translate.push(w2)
          }
        }
      }
    },
    addWordToData (word) {
      for (let i of this.currentWords) {
        if(i.value == word.value) {
          return i
        }
      }
      let elem  = {id: word.id, value: word.value, translate: [], lang: word.lang}
      this.currentWords.push(elem)
      return elem
    },
    addWord () {
      let eng = this.currentEngWord
      let rus = this.currentRusWord
      let l_2 = this.lang_2
      let l_1 = this.lang_1
      let fd =  new FormData()
      fd.append('word_1', eng)
      fd.append('word_2', rus)
      fd.append('lang_1', l_1)
      fd.append('lang_2', l_2)
      axios({
        method: 'post',
        url: '/api/word/add',
        data: fd,
        config: { headers: {'Content-Type': 'multipart/form-data' }},
      })
      .then((response) => {
        this.addWordsToData(response.data.words)
      })
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
  .GeneralContainer input, .ButtonContainer button  {
    background: silver;
    height: 2em;
    border: 1px solid black;
    border-radius: .3em;
    margin: 0 .5em;
    text-align: center;
  }
  .ButtonContainer button {
    cursor: pointer;
  }
  .ButtonContainer button:hover {
    background: SlateGrey;
  }
</style>
