<template>
<div id="container" @submit.prevent="signIn" class="py-5">
    <div id="loginBox">
      <div id="loginBoxTitle">Login</div>
      <div id="inputBox">
        <div class="input-form-box">
          <label for="username">Username:</label>
          <input type="text" v-model.trim="username" id="username" class="form-control">
        </div>
        <div class="input-form-box">
          <label for="password">Password:</label>
          <input type="password" v-model.trim="password" id="password" class="form-control">
        </div>
        <div class="button-login-box">
          <button type="button" class="btn btn-xs col" style="width: 100%;" @click="signIn">로그인</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useArticleStore } from '../stores/articles';

const store = useArticleStore()

const username = ref(null)
const password = ref(null)

const signIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.signIn(payload)
}
</script>

<style scoped>
template {
  height: 100%;
  margin: 0;
  display: flex;
  justify-content: center;
  align-items: center;
}
#container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  width: 100%;
}
#loginBox {
  width: 400px; /* 크기 키우기 */
  padding: 20px; /* 내부 여백 추가 */
  text-align: center;
  background-color: #ffffff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 그림자 추가 */
  border-radius: 8px; /* 모서리 둥글게 */
}
.input-form-box {
  display: flex;
  margin-bottom: 10px;
}
.input-form-box > label {
  min-width: 100px; /* 라벨의 최소 너비 */
  padding-top: 10px;
  text-align: right;
  margin-right: 10px;
}
.input-form-box > input {
  flex: 1;
}
.button-login-box {
  margin: 20px 0;
}
#loginBoxTitle {
  color: #000000;
  font-weight: bold;
  font-size: 32px;
  text-transform: uppercase;
  padding: 10px;
  margin-bottom: 20px;
  background: linear-gradient(to right, #270a09, #8ca6ce);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
#inputBox {
  margin: 10px;
}
#inputBox button {
  padding: 10px 20px;
}
.col {
  background-color: skyblue;
}
</style>
