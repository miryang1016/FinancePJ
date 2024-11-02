<template>
  <div>
    <label for="bank">은행&nbsp;:&nbsp;</label>
    <select id="bank" v-model="selectedBank">
      <option value="">전체</option>
      <option v-for="bank in banks" :key="bank" :value="bank">{{ bank }}</option>
    </select>
    <br>
    <br>
    <label for="attribute">정렬 속성&nbsp;:&nbsp;</label>
    <select id="attribute" v-model="sortAttribute" :disabled="isSpecificBankSelected">
      <option value="kor_co_nm">은행 이름</option>
      <option value="fin_prdt_nm">상품 이름</option>
    </select>
    &nbsp; &nbsp;
    <label for="sort">정렬&nbsp;:&nbsp;</label>
    <select id="sort" v-model="sortOrder">
      <option value="asc">오름차순</option>
      <option value="desc">내림차순</option>
    </select>
    <div class="d-flex justify-content-center">
      <div class="container d-flex row justify-content-left">
        <div class="col-md-6 col-lg-4" v-for="product in sortedAndFilteredProducts" :key="product.pk">
          <div class="card m-3 justify-content-center" style="width: 100%;" id="mouseover">
            <div class="card-body">
              <h5 class="card-title">{{ product.kor_co_nm }}</h5>
              <p class="card-text">{{ product.fin_prdt_nm }}</p>
              <a @click="redirectToDetail(product, productStore.prdtstate)" class="btn">상세보기</a>
            </div>
          </div>
        </div>
      </div>
    </div> 
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useProductStore } from '@/stores/products';
import { useArticleStore } from '@/stores/articles';

const router = useRouter();
const productStore = useProductStore();
const store = useArticleStore();

const props = defineProps({
  products: Array // products를 Array로 정의
});

const banks = [
  '농협은행주식회사', '하나은행', '신한은행', '국민은행', '토스뱅크 주식회사',
  '주식회사 카카오뱅크', '우리은행', '주식회사 케이뱅크', '한국스탠다드차타드은행',
  '대구은행', '부산은행', '광주은행', '제주은행', '전북은행', '경남은행',
  '중소기업은행', '한국산업은행', '수협은행'
];
const selectedBank = ref('');
const sortOrder = ref('asc'); // 정렬 순서를 저장할 상태
const sortAttribute = ref('kor_co_nm'); // 정렬 속성을 저장할 상태

const isSpecificBankSelected = computed(() => selectedBank.value !== '');

const sortedAndFilteredProducts = computed(() => {
  let filtered = props.products;

  if (selectedBank.value) {
    filtered = filtered.filter(product => product.kor_co_nm === selectedBank.value);
    sortAttribute.value = 'fin_prdt_nm'; // 필터 이름 상품 이름으로 변경
  }

  return filtered.slice().sort((a, b) => {
    const aValue = a[sortAttribute.value];
    const bValue = b[sortAttribute.value];

    if (typeof aValue === 'string' && typeof bValue === 'string') {
      if (sortOrder.value === 'asc') {
        return aValue.localeCompare(bValue);
      } else {
        return bValue.localeCompare(aValue);
      }
    } else if (typeof aValue === 'number' && typeof bValue === 'number') {
      if (sortOrder.value === 'asc') {
        return aValue - bValue;
      } else {
        return bValue - aValue;
      }
    } else {
      return 0;
    }
  });
});

const redirectToDetail = function (product, state) {
  // 해당 제품의 click_deposit 값을 1 증가시킵니다.
  if (state === 'deposit') {
    product.click_deposit += 1
    updateDeposit(product)
  }
  else {
    product.click_saving += 1
    updateSaving(product)
  }
  router.push({name: 'prdtdetail', params: {pk: product.id}})
}

const updateDeposit = (product) => {
  console.log('성공')
  axios({
    method: 'put',
    url: `http://127.0.0.1:8000/products/update-click-deposit/${product.id}/`,
    data: {
      click_deposit: product.click_deposit,
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then((response) => {
    console.log(response)
  })
  .catch((error) => {
    console.log(error)
  })
}

const updateSaving = (product) => {
  console.log('성공')
  axios({
    method: 'put',
    url: `http://127.0.0.1:8000/products/update-click-saving/${product.id}/`,
    data: {
      click_saving: product.click_saving,
    },
    headers: {
      Authorization: `Token ${store.token}`
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
.card {
  /* background-color: ivory; */
  display: flex;
  flex-direction: column;
  justify-content: center; /* 수직 가운데 정렬 */
  align-items: center; /* 수평 가운데 정렬 */
  width: 18rem;
  height: 15rem;
  text-align: center; /* 카드 내용을 가로로 가운데 정렬 */
  padding-top: 40px;
}
.btn {
  background-color: skyblue;
}

#mouseover:hover {
  background-color: beige;
  border: 1px solid black;
}
</style>