<template>
  <div id="align">
    <div v-if="product">
      <h1 class="p-3">상품 상세 정보</h1>
      <div class="card-container" id="align">
    <div v-for="option in product.options" :key="option.id">
      <div class="card" style="width: 18rem;" id="mouseover">
        <div class="card-body">
          <h5 class="card-title">상품명: {{ product.fin_prdt_nm }}</h5>
          <p class="card-text">회사명: {{ product.kor_co_nm }}</p>
          <p class="card-text">이자율 타입: {{ option.intr_rate_type_nm }}</p>
          <p class="card-text">이자율: {{ option.intr_rate }}</p>
          <p class="card-text">저축 기간: {{ option.save_trm }}</p>
          <button class="btn" @click="SavedStatus(option.id, userName)">
          {{ isSaved(option.id) ? '이미 가입된 상품입니다.' : '가입하기' }}
        </button>
        </div>
      </div>
    </div>
  </div>
  </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'
import { useProductStore } from '@/stores/products'
import { useArticleStore } from '@/stores/articles'

const route = useRoute()
const store = useArticleStore()
const productStore = useProductStore()
const product = ref(null)
const pk = ref(route.params.pk)

// 유저 이름을 가져오는 로직을 추가합니다. 예를 들어, 로그인된 사용자의 이름을 가져오는 방법.
const userName = store.name

const fetchProduct = () => {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/products/${productStore.prdtstate}_list/${pk.value}/`
  })
  .then((response) => {
    product.value = response.data
    console.log(product)
  })
  .catch((error) => {
    console.log(error)
  })
}

onMounted(() => {
  product.value = productStore.findById(Number(pk))
  fetchProduct()
})

const isSaved = (optionId) => {
  return productStore.isSaved(optionId)
}

function SavedStatus(optionId, userName) {
  const productData = { ...product.value, optionId, userName }
  if (!isSaved(optionId)) {
    productStore.saveProduct(productData)
  }
}
</script>



<style scoped>
#align {
justify-content: center;
text-align: center;
margin-inline: 10%;
}

.card-container {
display: flex;
flex-wrap: wrap;
gap: 20px; /* 카드 사이의 간격 */
}

.card {
/* background-color: ivory; */
display: flex;
flex-direction: column;
justify-content: center; /* 수직 가운데 정렬 */
align-items: center; /* 수평 가운데 정렬 */
width: 18rem;
height: 20rem;
text-align: center; /* 카드 내용을 가로로 가운데 정렬 */
padding-top: 30px;
}
.btn {
background-color: skyblue;
}

#mouseover:hover {
background-color: beige;
border: 1px solid black;
}
</style>