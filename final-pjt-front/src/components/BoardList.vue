<template>
  <div>
    <div class="article-header">
      <span>ID</span>
      <span>Title</span>
      <span>Username</span>
      <span>Created_Date</span>
    </div>
    <hr id="divider">
    <div v-for="article in store.articles" :key="article.pk">
      <div class="article-row" id="mouseover">
      <span @click="router.push({ name: 'detail', params: { pk: article.pk } })">{{ article.pk }}</span>
      <span @click="router.push({ name: 'detail', params: { pk: article.pk } })">{{ article.title }}</span>
      <span @click="router.push({ name: 'detail', params: { pk: article.pk } })">{{ article.author.username }}</span>
      <span @click="router.push({ name: 'detail', params: { pk: article.pk } })">{{ formatDate(article.created_at) }}</span>
      <button v-if="article.author.username === store.name" @click="store.deleteArticle(article.pk)" class="delete-button">X</button>
      <hr id="divider">
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router'
import { useArticleStore } from '@/stores/articles'

const store = useArticleStore()
const router = useRouter()

onMounted(() => {
  store.getArticles()
})

const formatDate = (dateString) => {
  const date = new Date(dateString);
  return `${date.getFullYear()}-${(date.getMonth() + 1).toString().padStart(2, '0')}-${date.getDate().toString().padStart(2, '0')}`;
}

</script>

<style scoped>
.article-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
  font-weight: bold;
  margin-right: 20px;
}
.article-header span {
  flex: 1;
}
.article-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
  /* margin-left: 10px; */
}
.article-row span {
  flex: 1;
}
.delete-button {
  color: white;
  background-color: skyblue;
  border: none;
  padding: 5px 10px;
  border-radius: 5px;
  cursor: pointer;
}

#mouseover:hover {
  background-color: beige;
  border: 1px solid black;
}
.divider {
  border: 0;
  height: 1px;
  background: #333;
  background-image: linear-gradient(to right, #ccc, #333, #ccc);
  margin: 10px 0;
}
</style>