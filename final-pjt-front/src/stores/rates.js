import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useRateStore = defineStore('rate', () => {
  const rates = ref([])
  const API_URL = 'http://127.0.0.1:8000'

  const getrate = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/interest_rate/calculate/',
    })
    .then(res => {
        rates.value = res.data
        console.log(rates.value)
    })
    .catch(error => console.log(error))
  }

  const sortedRates = computed(() => {
    return rates.value.sort((a, b) => a.cur_nm.localeCompare(b.cur_nm))
  })

  return { API_URL, getrate, rates, sortedRates }
}, { persist: true })