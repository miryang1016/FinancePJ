<template>
  <div class="container mt-4">
    <div class="form-group row align-items-center">
      <label for="from" class="col-sm-1 col-form-label">From:</label>
      <div class="col-sm-3">
        <select id="from" v-model="fromCurrency" class="form-control">
          <option v-for="rate in rateStore.rates" :key="rate.cur_unit" :value="rate.cur_unit">
            {{ rate.cur_nm }}
          </option>
        </select>
      </div>

      <label for="to" class="col-sm-1 col-form-label">To:</label>
      <div class="col-sm-3">
        <select id="to" v-model="toCurrency" class="form-control">
          <option v-for="rate in rateStore.rates" :key="rate.cur_unit" :value="rate.cur_unit">
            {{ rate.cur_nm }}
          </option>
        </select>
      </div>

      <label for="amount" class="col-sm-1 col-form-label">Amount:</label>
      <div class="col-sm-3">
        <input type="number" id="amount" v-model="amount" class="form-control" />
      </div>
    </div>
    
    <div class="card mt-3">
      <div class="card-body">
        <h5 class="card-title">결과</h5>
        <p class="card-text">{{ amount }} {{ fromCurrencyName }} = {{ result }} {{ toCurrencyName }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, computed } from 'vue';
import { useRateStore } from '@/stores/rates';

const fromCurrency = ref('NOK');
const toCurrency = ref('NOK');
const amount = ref(1);
const result = ref(null);
const rateStore = useRateStore();

// const parseRate = (rate) => {
//   return parseFloat(rate.replace(/,/g, ''));  
// };

const calculateRate = () => {
  const fromRate = rateStore.rates.find(rate => rate.cur_unit === fromCurrency.value);
  const toRate = rateStore.rates.find(rate => rate.cur_unit === toCurrency.value);

  if (fromRate && toRate && amount.value > 0) {
    const fromTTS = parseFloat(fromRate.tts);
    const toTTB = parseFloat(toRate.ttb);


    if (!isNaN(fromTTS) && !isNaN(toTTB)) {
      const fromToBase = amount.value * fromTTS;
      result.value = (fromToBase / toTTB).toFixed(2)
      if (fromTTS === 0 && toTTB !== 0) {
        result.value = (amount.value / toTTB).toFixed(2)
      } else if (toTTB === 0 && fromTTS !== 0) {
        result.value = (amount.value * fromTTS).toFixed(2)
      } else {
        result.value = ''; // 이 외의 경우
    }
  } else {
    result.value = '';
  }
  }
};

watch([fromCurrency, toCurrency, amount], calculateRate);

const fromCurrencyName = computed(() => {
  const fromRate = rateStore.rates.find(rate => rate.cur_unit === fromCurrency.value);
  return fromRate ? fromRate.cur_nm : '';
});
const toCurrencyName = computed(() => {
  const toRate = rateStore.rates.find(rate => rate.cur_unit === toCurrency.value);
  return toRate ? toRate.cur_nm : '';
});
</script>

<style scoped>
</style>