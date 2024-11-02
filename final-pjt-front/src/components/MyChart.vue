<template>
    <div>
      <h3>가입한 상품들</h3>
      <br>
    </div>
      <div class="chart-container">
        <b>예금 금리 정보</b>
        <canvas id="myChart"></canvas>
      </div>
      <div class="chart-container">
        <b>적금 금리 정보</b>
        <canvas id="Chart"></canvas>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useProductStore } from '@/stores/products';
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, BarController } from 'chart.js'

const store = useProductStore()

// 예금
// Chart.js에 필요한 컴포넌트 등록
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, BarController)

const labels = ref([]);
const interests = ref([]);

onMounted(() => {
  // for 문을 사용하여 savedProducts 배열을 순회
  for (let i = 0; i < store.savedProducts.length; i++) {
    if (store.savedProducts[i].click_deposit !== undefined) {
      labels.value.push(store.savedProducts[i].fin_prdt_nm)
      // 현재 제품의 optionId를 가져옴
      const targetOptionId = store.savedProducts[i].optionId
      // 현재 제품의 options 배열을 필터링하여 optionId가 targetOptionId와 일치하는 항목만 추출
      let filteredOptions = store.savedProducts[i].options.filter(option => option.id === targetOptionId)
      
      // 필터링된 옵션이 존재하는 경우, 각 옵션의 intr_rate를 interests 배열에 추가
      if (filteredOptions.length > 0) {
        filteredOptions.forEach(option => {
          interests.value.push(option.intr_rate)
        })
      }
    }
  }

  const ctx = document.getElementById('myChart').getContext('2d')
  new ChartJS(ctx, {
    type: 'bar',
    data: {
      labels: labels.value,
      datasets: [
        {
          label: '금리 정보',
          data: interests.value,
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)',
          ],
          borderColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)',
            'rgba(255, 159, 64, 1)',
          ],
          borderWidth: 1,
        },
      ],
    },
    options: {
      maintainAspectRatio: true,
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  })
})

// 적금

const label = ref([]);
const interest = ref([]);

onMounted(() => {
  // for 문을 사용하여 savedProducts 배열을 순회
  for (let i = 0; i < store.savedProducts.length; i++) {
    if (store.savedProducts[i].click_saving !== undefined) {
      label.value.push(store.savedProducts[i].fin_prdt_nm)
      // 현재 제품의 optionId를 가져옴
      const targetOptionId = store.savedProducts[i].optionId
      // 현재 제품의 options 배열을 필터링하여 optionId가 targetOptionId와 일치하는 항목만 추출
      let filteredOptions = store.savedProducts[i].options.filter(option => option.id === targetOptionId)
      
      // 필터링된 옵션이 존재하는 경우, 각 옵션의 intr_rate를 interests 배열에 추가
      if (filteredOptions.length > 0) {
        filteredOptions.forEach(option => {
          interest.value.push(option.intr_rate)
        })
      }
    }
  }

  const ctxs = document.getElementById('Chart').getContext('2d')
  new ChartJS(ctxs, {
    type: 'bar',
    data: {
      labels: label.value,
      datasets: [
        {
          label: '금리 정보',
          data: interest.value,
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)',
          ],
          borderColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)',
            'rgba(255, 159, 64, 1)',
          ],
          borderWidth: 1,
        },
      ],
    },
    options: {
      maintainAspectRatio: true,
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  })
})

</script>

<style scoped>.container {
  width: 100%;
}

.chart-container {
  margin-bottom: 20px;
}

.chart-container b {
  display: block;
  margin-bottom: 10px;
}

.container h3 {
  margin: 0; /* 제목 위의 여백 제거 */
}
</style>