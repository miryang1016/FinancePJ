<template>
  <div v-if="article">
    <div class="mt-5 px-5">
      <div class="border">
        <div class="card-body p-5">
          <h1 class="card-title" style="font-size: larger;"><b>{{ article.title }}</b></h1>
          &nbsp;
          <p class="card-text">글 번호: {{ pk }}</p>
          <p class="card-text">내용: {{ article.content }}</p>
          <p class="card-text">생성일자: {{ article.created_at.substring(0, 10) }}</p>
          <button v-if="data.author.username === store.name" @click="updateArticle" class="btn btn-outline-primary btn-sm">게시글 수정</button>
        </div>
      </div>
      <br>
      <form @submit="submitData" class="comment-form">
        <label for="comment" class="comment-label">댓글: </label>
        <input type="text" v-model.trim="comment" id="comment" class="comment-input">
        <button type="submit" class="comment-button">comment</button>
      </form>
        <h5><strong>댓글 목록</strong></h5>
        <div class="comments-container">
          <div
            v-for="comment in store.comments"
            :key="comment.id"
            class="comment-card"
          >
          <div v-if="comment.article === Number(pk)">
            <span class="comment-author">작성자: {{ comment.user }}</span>
            <span class="comment-content">{{ comment.comment }}</span>&nbsp;
            <span class="comment-date">{{ comment.created_at.substring(0, 10) }}</span>
            <button v-if="comment.user === store.name" @click="deleteComment(comment.id)" class="btn btn-outline-danger btn-sm">X</button>
          </div>
          </div>
        </div>
    </div>
  </div>


</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios'
import { useRoute, useRouter } from 'vue-router'
import { useArticleStore } from '@/stores/articles'
import { RouterLink } from 'vue-router';

const route = useRoute()
const router = useRouter()
const store = useArticleStore()
const pk = route.params.pk
const article = ref(null)

const data = ref(null)

onMounted(() => {
  data.value = store.findById(Number(pk))
})

onMounted(() => {
  fetchArticle()
})

const fetchArticle = () => {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/api/v1/articles/${pk}`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then((response) => {
    article.value = response.data
    // fetchComments()
  })
  .catch((error) => {
    console.error('게시글을 불러오는 중 에러가 발생했습니다:', error)
    window.alert('게시글을 불러오는 중 에러가 발생했습니다.')
  })
}

const comment = ref('')

const submitData = function () {
  const payload = {
    comment: comment.value,
    article_id: pk,
  }
  store.createComment(payload)
  comment.value = ''
}

const updateArticle = () => {
  if (article.value) {
    router.push({ name: 'update', params: { pk: article.value.pk } })
  }
}

onMounted(() => {
  store.getComments(pk)
})

const deleteComment = function (id) {
  axios({
    method: 'delete',
    url: `http://127.0.0.1:8000/api/v1/comments/${id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then(() => {
    window.alert('댓글이 성공적으로 삭제되었습니다.')
    store.comments = store.comments.filter(comment => comment.id !== id) // 새로고침 없이 댓글 목록 다시 불러오기
  })
  .catch((error) => {
    console.error('댓글 삭제 실패:', error)
    window.alert('댓글 삭제 중 에러가 발생했습니다.')
  })
}

</script>

<style scoped>
.comment-form {
  display: flex;
  align-items: center;
  gap: 10px; /* Adjust the gap as needed */
  margin-bottom: 20px; /* Add some space below the form */
}

.comment-label {
  margin-right: 10px; /* Adjust the margin as needed */
}

.comment-input {
  flex: 1;
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.comment-button {
  background-color: skyblue;
  border: none;
  padding: 5px 10px;
  border-radius: 5px;
  cursor: pointer;
  color: white;
}

.comment-button:hover {
  background-color: deepskyblue; /* Adjust the hover color as needed */
}

.comments-container {
  margin-top: 20px;
}

.comment-card {
  display: flex;
  align-items: center;
  gap: 10px; /* Adjust the gap as needed */
  padding: 10px;
  border-bottom: 1px solid #ddd;
}

.comment-author {
  font-weight: bold;
  margin-right: 10px; /* Add space between author and content */
}

.comment-content {
  flex: 1;
}

.comment-date {
  font-size: 0.9em;
  color: gray;
  margin-right: 10px; /* Add space between date and delete button */
}

.delete-button {
  background-color: transparent;
  border: none;
  color: red;
  cursor: pointer;
  font-size: 0.9em;
  transition: color 0.3s ease;
}

.delete-button:hover {
  color: darkred;
}

.border {
  border: 1px solid lightgray;
}
</style>