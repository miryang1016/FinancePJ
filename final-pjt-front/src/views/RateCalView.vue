<template>
  <div id="align">
    <h1>환율 계산기</h1>
    <RateCal />
    <br><br>
    <RateList class="m-auto p-3 border border-secondary"/>
  </div>
</template>

<script setup>
import RateList from '@/components/RateList.vue';
import RateCal from '@/components/RateCal.vue';
import { onMounted,ref } from 'vue';
import { useRateStore } from '@/stores/rates'

const store = useRateStore()
const rates = ref([])


store.getrate()


</script>

<style scoped>
#align {
  justify-content: center;
  text-align: center;
  margin-inline: 10%;
}
</style>