import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useArticleStore = defineStore('article', () => {
  const articles = ref([])
  const comments = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const router = useRouter()
  const userInfo = ref([])
  const name = ref(null)

  const getArticles = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/articles/',
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(res => articles.value = res.data)
  }

  const createArticle = function ({ title, content }) {
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/api/v1/articles/',
      data: {
        title,
        content
      },
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(res => {
      console.log(res)
      router.push('/board')
    })
  }

  const getComments = (article_id) => {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/api/v1/articles/${article_id}/comments/`,
    })
    .then(res => comments.value = res.data)
    .catch(err => console.error(err))
  }

  const createComment = function (payload) {
    const { comment, article_id } = payload
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/api/v1/comments/',
      data: {
        comment: comment,
        article: article_id
      },
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(res => {
      console.log(res)
    })
  }

  const signUp = function (payload) {
    const { username, password1, password2, email, salary, mainbank, register, work, money, financial_products} = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2, email, salary, mainbank, register, work, money, financial_products
      }
    })
      .then((res) => {
        console.log('회원가입 성공!')
        userInfo.value = res.config.data
        const password = password1
        signIn({ username, password })
        router.push({ name: 'main' })
      })
      .catch((err) => console.log(err.response))
  }

  const signIn = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        console.log('로그인 성공!')
        name.value = username
        token.value = res.data.key
        window.alert(`${username}님 환영합니다.`)
        router.push({ name: 'main' })
      })
      .catch((err) => console.log(err))
  }

  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const findById = (pk) => {
    return articles.value.find(article => article.pk === pk)
  }

  const logOut = function () {
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/accounts/logout/',
      headers: { Authorization: `Token ${token.value}`}
    })
      .then(res => {
        console.log(res.data)
        token.value = null  // token 초기화
        router.push({ name: 'signin' })
      })
      .catch(err => {
        console.log(err)
      })
  }

  const deleteArticle = function (pk) {
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/api/v1/${pk}/delete/`,
      headers: { Authorization: `Token ${token.value}`}
    })
      .then(res => {
        const index = articles.value.findIndex((article) => article.pk === Number(pk))
        articles.value.splice(index, 1);
        // router.push({name: 'board'})
        console.log(index)
      })
      .catch(err => {
        console.log(err)
      })
  }

  return { articles, comments, userInfo, name, API_URL, token, getArticles, getComments, createArticle, createComment, signUp, signIn, logOut, isLogin, findById,
    deleteArticle
   }
}, { persist: true })
