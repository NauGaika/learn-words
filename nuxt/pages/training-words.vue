<template lang="pug">
section
  h2 Тренировка слов
  div
    span.currentWord {{currentWord ? currentWord.value : message}}
    span(v-if="stage==4") Правильный ответ </br> {{currentWord.trans}}
  div.controlPanel
    button(v-if="stage==0"
    @click="startTraining()") Начать тренировку
    button(v-if="stage==1"
    @click="nextWord(true)") Это я знаю!
    button(v-if="stage==1"
    @click="nextWord()") Не помню :(
    button(v-if="stage==3"
    @click="startTraining()") Мы еще не закончили!
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
      words: [],
      stage: 0,
      currentWord: false,
      message: "Начать тренировку"
    }
  },
  computed: {
    uncorrectWords () {
      let wordNotCorrect = []
      for (let i of this.words) {
        if(!i.correct) {
          wordNotCorrect.push(i)
        }
      }
      return wordNotCorrect
    }
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
    startTraining () {
      this.words = [
        {
          value: 'why',
          correct: false,
          translate: 'почему',
          showCount: 0
        },
        {
          value: 'where',
          correct: false,
          translate: 'где',
          showCount: 0
        },
        {
          value: 'any',
          correct: false,
          translate: 'ни одного',
          showCount: 0
        },
        {
          value: 'hello',
          correct: false,
          translate: 'привет',
          showCount: 0
        },
        {
          value: 'bue',
          correct: false,
          translate: 'пока',
          showCount: 0
        }
      ]
      this.stage = 1
      this.nextWord()
    },
    showRandomWord () {
      let wordNotCorrect = this.uncorrectWords
      let wordCount = wordNotCorrect.length - 1
      let randWord = wordNotCorrect[Math.round(Math.random()*wordCount)]
      if (randWord != undefined) {
        return randWord
      } else {
        this.message = "Ты знаешь все слова:)"
        this.stage = 3
      }
       
    },
    showTranslate() {
      
    },
    checkWord () {
      
    },
    nextWord (correct=false) {
      if (this.currentWord) {
        this.currentWord.correct = correct
        this.currentWord.showCount++ 
      }
      this.currentWord = this.showRandomWord()
    }
  },
}
</script>
<style>
.currentWord {
  display: block;
  text-align: center;
  font-size: 2em;
}
.controlPanel {
  margin-top: 1em;
  text-align: center;
  font-size: 1.5em;
}

</style>
