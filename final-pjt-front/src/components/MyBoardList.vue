<template>
    <br>
    <div class="article-header">
      <span>ID</span>
      <span>Title</span>
      <span>Created_Date</span>
    </div>
    <div v-for="article in store.articles" :key="article.pk" @click="router.push({ name: 'detail', params: { pk: article.pk } })" id="mouseover">
      <div v-if="article.author.username === store.name" class="article-row">
        <span>{{ article.pk }}</span>
        <span>{{ article.title }}</span>
        <span>{{ formatDate(article.created_at) }}</span>
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

const formatDate = (publishTime) => {
  // publishTime에서 년월일 부분만 추출하여 반환
  return publishTime.substring(0, 10);
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
  margin-right: 15px;
}
.article-row span {
  flex: 1;
}

#mouseover:hover {
  background-color: beige;
  border: 1px solid black;
}
</style>