<template>
  <div id="align">
    <h1>금융 게시판</h1>
    <br>
    <button type="button" class="btn btn-outline-primary m" @click="router.push({ name:'create' })">새 글 작성</button>
    <button type="button" class="btn btn-outline-info" @click="router.push({ name:'myboard' })">내가 쓴 글</button>
    <br>
    <br>
  <BoardList class="m-auto p-3 border border-secondary"/>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import BoardList from '@/components/BoardList.vue'

const router = useRouter()
</script>

<style scoped>
.m {
  margin-right: 10px;
}

#align {
  justify-content: center;
  text-align: center;
  margin-inline: 10%;
}

</style>