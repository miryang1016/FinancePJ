<template>
  <div id="align">
    <h1>예적금 비교</h1>
    <br>
    <span class="btn" @click="showPrdt('deposit')" :class="{ active: productStore.prdtstate === 'deposit'}">예금 </span> |
    <span class="btn" @click="showPrdt('saving')" :class="{ active: productStore.prdtstate === 'saving' }">적금</span>
    <br><br>
    <Product :products="productStore.products"/>
  </div>
</template>

<script setup>
import Product from '@/components/Product.vue'
import { useProductStore } from '@/stores/products'

const productStore = useProductStore()

const showPrdt = (type) => {
  productStore.setPrdtState(type)
}

// Fetch initial products
productStore.setPrdtState(productStore.prdtstate)

</script>

<style scoped>
#align {
  justify-content: center;
  text-align: center;
  margin-inline: 10%;
}

.active {
  font-weight: bold;
}
</style>