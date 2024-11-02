<template>
  <div id="align" class="container">
    <h1>금융 게시글 작성</h1>
    <form @submit.prevent="submitData" class="form">
      <div class="mb-3">
        <label for="title" class="form-label"><b>Title</b></label>
        <input type="text" id="title" v-model="title" class="form-control">
      </div>

      <div class="mb-3">
        <label for="content" class="form-label"><b>Content</b></label>
        <textarea id="content" v-model="content" class="form-control"></textarea>
      </div>
      <div class="button-login-box">
          <button type="submit" class="btn btn-xs col" style="width: 100%;">Create</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useArticleStore } from '@/stores/articles'

const store = useArticleStore()

const title = ref('')
const content = ref('')

const submitData = function () {
  const article = {
    title: title.value,
    content: content.value
  }
  store.createArticle(article)
  title.value = ''
  content.value = ''
}

</script>

<style scoped>
#align {
  justify-content: center;
  text-align: center;
}

.form {
  max-width: 500px;
  margin: auto;
}

.button-login-box {
  margin: 20px 0;
}

.col {
  background-color: skyblue;
}
</style>