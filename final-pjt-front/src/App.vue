<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-light bg-beige" style="background-color: beige">
      <div class="container-fluid">
        <a class="navbar-brand" @click="router.push({name: 'main'})">
          <img src="@/assets/logo.png" alt="" style="height: 60px; width: 65px;">
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button> 
        <div class="collapse navbar-collapse" id="navbarNavDropdown">
          <ul class="navbar-nav w-100 d-flex justify-content-between">
            <div class="navbar-left d-flex">
              <li class="nav-item">
                <RouterLink :to="{name: 'product'}" class="nav-link" href="#">예금 비교</RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink :to="{name: 'ratecal'}" class="nav-link" href="#">환율계산기</RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink :to="{name: 'board'}" class="nav-link" href="#">게시판</RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink :to="{name: 'map'}" class="nav-link" href="#">Map</RouterLink>
              </li>
            </div>
            <div class="navbar-right d-flex">
              <li class="nav-item" v-if="store.isLogin">
                <RouterLink :to="{name: 'profile'}" class="nav-link">마이페이지</RouterLink>
              </li>
              <li class="nav-item" v-if="store.isLogin">
                <a @click="store.logOut" class="nav-link">LogOut</a>
              </li>
              <li class="nav-item" v-if="!store.isLogin">
                <RouterLink to="/signup" class="nav-link">SignUp</RouterLink>
              </li>
              <li class="nav-item" v-if="!store.isLogin">
                <RouterLink to="/signin" class="nav-link">SignIn</RouterLink>
              </li>
            </div>
          </ul>
        </div>
      </div>
    </nav>
    <br>
    &nbsp;
    <button class="btn" @click="router.go(-1)">⬅ 뒤로가기</button>
  
    <RouterView />
    <ChatbotView />
  </div>
</template>


<script setup>

import { useArticleStore } from './stores/articles';
import { RouterLink, RouterView, useRouter } from 'vue-router'
import ChatbotView from './views/ChatbotView.vue';

const router = useRouter()
const store = useArticleStore()

</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  margin-top: 60px;
}
.navbar {
  font-size: 1.3rem; /* 텍스트 크기 키우기 */
  padding: 1rem 1.5rem; /* 상하/좌우 패딩 추가 */
}
.navbar-brand img {
  width: 90px; /* 이미지 너비 키우기 */
  height: auto; /* 이미지 높이를 비율에 맞게 조정 */
}
.nav-link {
  padding: 0.5rem 1rem; /* 링크 패딩 키우기 */
}
.navbar-toggler {
  font-size: 1.5em; /* 토글러 아이콘 크기 키우기 */
}

</style>