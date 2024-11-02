<template>
  <div id="align">
    <h1>Profile</h1>
    <div>
      <span @click="State_b"> 기본 정보 |</span>
      <span @click="State_p"> 가입된 상품 목록 조회 |</span>
      <span @click="State_r"> 상품 추천 받기</span>
    </div>
    <br>
    <BasicInfo v-if="active_b"/>
    <Portfolio v-if="active_p" />
    <Recommend v-if="active_r" />
  </div>
</template>

<script setup>
import BasicInfo from '@/components/BasicInfo.vue'
import Portfolio from '@/components/Portfolio.vue'
import Recommend from '@/components/Recommend.vue'
import { ref } from 'vue'

const active_b = ref(true)
const active_p = ref(false)
const active_r = ref(false)

const State_b = function () {
  if (active_b === true) {
    active_b.value = false
  } else {
    active_b.value = true
    active_p.value = false
    active_r.value = false
  }
}

const State_p = function () {
  if (active_p === true) {
    active_p.value = false
  } else {
    active_b.value = false
    active_p.value = true
    active_r.value = false
  }
}

const State_r = function () {
  if (active_r === true) {
    active_r.value = false
  } else {
    active_b.value = false
    active_p.value = false
    active_r.value = true
  }
}

</script>

<style scoped>
#align {
  justify-content: center;
  text-align: center;
  margin-inline: 10%;
}
</style>