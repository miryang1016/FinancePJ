<template>
  <div class="container-fluid">
    <div class="row align-items-start">
      <div class="col-lg-6 left-pane">
        <h3 class="text-center pad">가입된 상품 목록</h3>
        <br>
        <div v-if="store.isStore">
          <div v-for="product in store.savedProducts" :key="product.id" class="product-item">
            <div v-if="product.userName === articleStore.name">
              <p><strong>회사명:</strong> {{ product.kor_co_nm }}</p>
              <p><strong>상품명:</strong> {{ product.fin_prdt_nm }}</p>
              <div v-for="option in product.options" :key="option.id" class="option-item">
                <div v-if="option.id === product.optionId">
                  <p><strong>저축 금리 유형명:</strong> {{ option.intr_rate_type_nm }}</p>
                  <p><strong>저축 기간:</strong> {{ option.save_trm }}</p>
                  <p><strong>저축 금리:</strong> {{ option.intr_rate }}</p>
                  <button class="btn btn-danger btn-sm" @click="store.removeSavedProduct(option.id); updateUser()">가입 취소</button>
                  <hr>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-lg-6 right-pane">
        <div class="chart-container">
          <MyChart />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useProductStore } from '@/stores/products';
import { useArticleStore } from '@/stores/articles';
import MyChart from './MyChart.vue';

const articleStore = useArticleStore()
const store = useProductStore()
const user = ref([])

const fetchUser = () => {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/accounts/api/user/`,
    headers: {
      Authorization: `Token ${articleStore.token}`
    }
  })
  .then((response) => {
    user.value = response.data
  })
  .catch((error) => {
    console.error('유저 정보를 불러오는 중 에러가 발생했습니다:', error)
    window.alert('유저 정보를 불러오는 중 에러가 발생했습니다.')
  })
}

onMounted(() => {
  fetchUser()
  updateUser()
})

const updateUser = () => {
  let financialProducts = [];

  // for 문을 사용하여 savedProducts 배열을 순회
  for (let i = 0; i < store.savedProducts.length; i++) {
    financialProducts.push(store.savedProducts[i].fin_prdt_nm);
  }

  // 쉼표로 구분된 문자열로 변환
  const financialProductsString = financialProducts.join(',')

  axios({
    method: 'put',
    url: `http://127.0.0.1:8000/accounts/api/update-user/`,
    data: {
      financial_products: financialProductsString,
    },
    headers: {
      Authorization: `Token ${articleStore.token}`
    }
  })
  .then((response) => {
    console.log(response)
  })
  .catch((error) => {
    console.log(error)
  })
}


</script>

<style scoped>
.container-fluid {
  padding: 20px;
}

.left-pane {
  background-color: #f8f9fa;
  padding: 20px;
  border-right: 1px solid #ddd;
}

.right-pane {
  padding: 20px;
}

.chart-container {
  width: 100%;
  padding: 20px;
}

.product-item, .option-item {
  margin-bottom: 15px;
}

hr {
  margin: 10px 0;
}

.text-center {
  text-align: center;
}

.btn-danger {
  background-color: #dc3545;
  color: white;
  margin: 10px;
}

.pad {
  margin-top: 20px;
}
</style>