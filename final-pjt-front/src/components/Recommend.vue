<template>
  <div class="m-auto p-3" id="align">
    <h4>상품 추천</h4>
    <hr>
    <span class="btn" @click="showPrdt('deposit')" :class="{ active: productStore.prdtstate === 'deposit'}">예금 </span> |
    <span class="btn" @click="showPrdt('saving')" :class="{ active: productStore.prdtstate === 'saving' }">적금</span>
    <br><br>
    <div>
      <label for="bank">은행&nbsp;:&nbsp;</label>
      <select id="bank" v-model="selectedBank">
        <option value="">전체</option>
        <option v-for="bank in banks" :key="bank" :value="bank">{{ bank }}</option>
      </select>
      <br>
      <p class="op"><b>[클릭 수 기준]</b></p>
    </div>
    <div class="d-flex flex-column align-items-center mar">
      <div v-if="visibleProducts.length > 0" class="col-3" v-for="product in visibleProducts" :key="product.pk">
        <div class="card m-3 option" style="width: 18rem;" id="mouseover">
          <div class="card-body">
            <h5 class="card-title">{{ product.kor_co_nm }}</h5>
            <p class="card-text">{{ product.fin_prdt_nm }}</p>
            <a @click="() => router.push({ name: 'prdtdetail', params: { pk: product.id }})" class="btn" style="background-color: skyblue;">상세보기</a>
          </div>
        </div>
      </div>
      <div v-else>
        <p>Loading...</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useProductStore } from '@/stores/products'

const productStore = useProductStore()
const router = useRouter()

const finProducts = ref([])

// for 문을 사용하여 savedProducts 배열을 순회
for (let i = 0; i < productStore.savedProducts.length; i++) {
  finProducts.value.push(productStore.savedProducts[i].fin_prdt_nm);
}

const showPrdt = (type) => {
  productStore.setPrdtState(type)
}

productStore.setPrdtState(productStore.prdtstate)

const banks = [
  '농협은행주식회사', '하나은행', '신한은행', '국민은행', '토스뱅크 주식회사',
  '주식회사 카카오뱅크', '우리은행', '주식회사 케이뱅크', '한국스탠다드차타드은행',
  '대구은행', '부산은행', '광주은행', '제주은행', '전북은행', '경남은행',
  '중소기업은행', '한국산업은행', '수협은행'
];

const selectedBank = ref('');

const sortedProducts = computed(() => {
  let filteredProducts = productStore.products;
    
  if (selectedBank.value) {
    filteredProducts = filteredProducts.filter(product => product.kor_co_nm === selectedBank.value);
  }
    
  return filteredProducts.sort((a, b) => b.click_deposit - a.click_deposit);
});

const visibleProducts = computed(() => {
  const filteredProducts = sortedProducts.value.filter(product => !finProducts.value.includes(product.fin_prdt_nm));
  if (filteredProducts.length >= 5) {
    return filteredProducts.slice(0, 5);
  } else {
    // 필요한 수량을 채우기 위해 반복 추가
    let additionalProducts = [];
    let index = 0;
    while (additionalProducts.length + filteredProducts.length < 5 && index < sortedProducts.value.length) {
      const product = sortedProducts.value[index];
      if (!filteredProducts.includes(product) && !finProducts.value.includes(product.fin_prdt_nm)) {
        additionalProducts.push(product);
      }
      index++;
    }
    return filteredProducts.concat(additionalProducts).slice(0, 5);
  }
});

</script>

<style scoped>
#align {
  justify-content: center;
  text-align: center;
}

.active {
  font-weight: bold;
}

.op {
  margin-top: 30px;
}

#mouseover:hover {
  background-color: beige;
  border: 1px solid black;
}

.mar {
  margin-left: 50px;
}
</style>