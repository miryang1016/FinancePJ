<template>
  <div id="align" class="container">
    <h1>Update Page</h1>
    <form v-if="article" class="form">
      <div class="mb-3">
        <label for="title" class="form-label"><b>Title</b></label>
        <input type="text" id="title" v-model="article.title" class="form-control">
      </div>
      <div class="mb-3">
        <label for="content" class="form-label"><b>Content</b></label>
        <textarea id="content" v-model="article.content" class="form-control"></textarea>
      </div>
      <div class="button-login-box">
          <button type="submit" class="btn btn-xs col" style="width: 100%;" @click.prevent="updateArticle">Update</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useArticleStore } from '@/stores/articles'

const store = useArticleStore()
const route = useRoute()
const router = useRouter()
const article = ref(null)
const pk = route.params.pk

onMounted(() => {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/api/v1/articles/${pk}`,
      headers: {
      Authorization: `Token ${store.token}`
      }
    })
    .then((response) => {
      article.value = response.data
    })
    .catch((error) => {
      console.error('에러 발생:', error)
    })
  })
  
  const updateArticle = () => {
    axios({
      method: 'put',
      url: `http://127.0.0.1:8000/api/v1/articles/${pk}/`,
      data: {
        title: article.value.title,
        content: article.value.content
      },
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    .then((response) => {
      router.push({ name: 'detail', params: { pk: pk } })
    })
    .catch((error) => {
      window.alert('작성자가 아닙니다!')
    })
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