import { ref, computed } from 'vue';
import { defineStore } from 'pinia';
import { useRouter } from 'vue-router';
import axios from 'axios';

export const useProductStore = defineStore('product', () => {
  const products = ref([]);
  const savedProducts = ref([]);
  const prdtstate = ref('deposit');
  const router = useRouter();

  const isStore = computed(() => {
    return savedProducts.value.length !== 0;
  });

  const sortedProducts = (order, attribute) => {
    return products.value.slice().sort((a, b) => {
      const aValue = a[attribute];
      const bValue = b[attribute];
  
      if (typeof aValue === 'string' && typeof bValue === 'string') {
        if (order === 'asc') {
          return aValue.localeCompare(bValue);
        } else {
          return bValue.localeCompare(aValue);
        }
      } else if (typeof aValue === 'number' && typeof bValue === 'number') {
        if (order === 'asc') {
          return aValue - bValue;
        } else {
          return bValue - aValue;
        }
      } else {
        return 0;
      }
    });
  };

  const fetchProducts = (type) => {
    const url = `http://127.0.0.1:8000/products/${type}_list/`;

    axios.get(url)
      .then(response => products.value = response.data)
      .catch(error => console.log(error));
  };

  const setPrdtState = (state) => {
    prdtstate.value = state;
    console.log(prdtstate.value);
    fetchProducts(state);
  };

  const findById = (pk) => {
    return products.value.find(product => product.pk === pk);
  };

  function saveProduct(product) {
    savedProducts.value.push(product);
    localStorage.setItem('savedProducts', JSON.stringify(savedProducts.value));
  }

  function removeSavedProduct(pk) {
    savedProducts.value = savedProducts.value.filter(product => product.optionId !== pk);
    localStorage.setItem('savedProducts', JSON.stringify(savedProducts.value));
  }

  function isSaved(pk) {
    console.log(products);
    return savedProducts.value.some(product => product.optionId === pk);
  }

  return { products, savedProducts, isStore, fetchProducts, setPrdtState, findById, isSaved, saveProduct, removeSavedProduct, prdtstate, sortedProducts };
}, { persist: true });