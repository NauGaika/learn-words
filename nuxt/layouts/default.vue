<template lang="pug">
div
  section
    h1 Learn Words
  word-menu
  nuxt
</template>
<script>
import WordMenu from '~/components/header/WordMenu'
export default {
  components: {
    'word-menu': WordMenu
  }
}
</script>
<style>
h1 {
  display: block;
  font-size: 3em;
  text-align: center;
}
h2 {
  display: block;
  font-size: 2em;
  text-align: center;
}
button {
  background: silver;
  height: 2em;
  border: 1px solid black;
  border-radius: .3em;
  margin: 0 .5em;
  text-align: center;
  font-size: 1em;
  margin-top: .5em;
}
button:hover {
  cursor: pointer;
  background: SlateGrey;
}
</style>
