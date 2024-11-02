<template>
  <div>
    <h4>환율 리스트</h4>
    <div class="rate-header">
      <span>화폐 단위</span>
      <span>나라</span>
      <span>송금 받을 때</span>
      <span>송금 보낼 때</span>
    </div>
    <hr>
    <div class="rate-row" v-for="rate in filteredRates" :key="rate.id" id="mouseover">
      <span>{{ rate.cur_unit }}</span>
      <span>{{ rate.cur_nm }}</span>
      <span>{{ rate.ttb }}</span>
      <span>{{ rate.tts }}</span>
      <hr>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { useRateStore } from '@/stores/rates';

const rateStore = useRateStore();

const filteredRates = computed(() => {
  return rateStore.sortedRates.filter(rate => rate.cur_unit !== 'KRW')
});
</script>

<style scoped>
.rate-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
  font-weight: bold;
  margin-right: 20px;
}
.rate-header span {
  flex: 1;
}
.rate-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
  /* margin-left: 10px; */
}
.rate-row span {
  flex: 1;
}
</style>