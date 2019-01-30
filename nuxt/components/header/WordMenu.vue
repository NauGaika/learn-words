<template lang="pug">
  nav
    ul
      li
        nuxt-link(to="/") Главная страница
      li
        nuxt-link(to="/add-words") Добавление слов
      li
        nuxt-link(to="/training-words") Тренировка слов
      li
        nuxt-link(to="/all-words") Все слова
</template>
<!-- is, v-for, v-if, v-else-if, v-else, v-show, v-cloak, v-pre, v-once, id, ref, key, slot, v-model, другие атрибуты, v-on, v-html, v-text -->
<script>
export default {
  components: {},
  mixins: [],
  model: [],
  props: [],
  data () {
    return {

    }
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
  nav ul {
    list-style: none;
    text-align: center;
  }
  nav ul li {
    display: inline;
    padding: 1em;
    
  }
  nav ul li a {
    color: black;
    transition: .5s;
  }
  nav ul li a:hover {
    color: blue;
  }
</style>
