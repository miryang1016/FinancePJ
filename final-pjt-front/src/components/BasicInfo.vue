<template>
<div v-if="!update" class="container">
  <div class="basic-info">
    <br>
    <h3 class="text-center">기본 정보</h3>
    <br>
    <div>
      <p><strong>이름:</strong> {{ user.username }}</p>
      <p><strong>이메일:</strong> {{ user.email }}</p>
      <p><strong>주거래은행:</strong> {{ user.mainbank }}</p>
      <p><strong>연봉:</strong> {{ user.salary }}</p>
      <p><strong>자산:</strong> {{ user.money }}만원</p>
      <p><strong>거주지:</strong> {{ user.register }}</p>
      <p><strong>근무지:</strong> {{ user.work }}</p>
    </div>
    <div class="text-center"> <!-- 중앙 정렬 -->
      <button type="submit" class="btn button-login-box" @click="update = true">기본 정보 수정</button> <!-- btn 클래스 추가 -->
    </div>
  </div>
</div>
<div class="container" v-if="update">
    <div class="py-5">
      <div id="loginBox" class="card p-4">
        <h2 class="card-title text-center mb-4" id="loginBoxTitle">User Info</h2>
        <form @submit.prevent="signUp">
          <!-- <div class="mb-3">
            <label for="username" class="form-label">Username:</label>
            <input type="text" v-model.trim="user.username" id="username" class="form-control">
          </div> -->
          <div class="mb-3">
            <label for="email" class="form-label">Email:</label>
            <input type="email" v-model.trim="user.email" id="email" class="form-control">
          </div>
          <div class="mb-3">
            <label class="form-label op">주거래은행:&nbsp;
              <button @click="bankupdate" class="btn btn-outline-primary btn-xs my-3">은행 수정 완료</button>
</label><br>
            <div v-for="bank in banks" :key="bank" class="form-check form-check-inline box">
              <input type="checkbox" :value="bank" v-model="mainbank" class="form-check-input">
              <label class="form-check-label">{{ bank }}</label>
            </div>
          </div>
          <div class="mb-3">
            <div>
          거주지: &nbsp;<span v-if="info">{{ register }}&nbsp;</span>
          <button type="button" class="btn btn-outline-primary btn-xs" data-bs-toggle="modal" data-bs-target="#residenceModal" @click="handleRe">
            거주지 검색
          </button>
          <div class="modal fade" id="residenceModal" tabindex="-1" aria-labelledby="residenceModalLabel" aria-hidden="true">
            <div class="modal-dialog">
              <div class="modal-content">
                <div class="modal-header">
                  <h5 class="modal-title" id="residenceModalLabel">Address</h5>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                  <label for="residence-region">시/도: &nbsp;</label>
                  <select id="residence-region" v-model="selectedRegion">
                    <option v-for="region in regionData.regions" :key="region" :value="region">{{ region }}</option>
                  </select>
                  &nbsp;
                  <label for="residence-city">시/군/구: &nbsp;</label>
                  <select id="residence-city" v-model="selectedCity">
                    <option v-for="city in regionData.cities[selectedRegion]" :key="city" :value="city">{{ city }}</option>
                  </select>
                  <!-- <br>
                  <label for="residence-loc">동: </label>
                  <input type="text" v-model.trim="selectedloc" id="residence-loc"> -->
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn btn-secondary" data-bs-dismiss="modal" @click="handleSubmit">Submit</button>
                </div>
              </div>
          </div>
          </div>
          </div>
          </div>
          <div class="mb-3">
            <div>
      근무지: &nbsp;<span v-if="check">{{ work }}&nbsp;</span>
      <button type="button" class="btn btn-outline-primary btn-xs" data-bs-toggle="modal" data-bs-target="#workModal" @click="handleTurn">
        근무지 검색
      </button>
      <div class="modal fade" id="workModal" tabindex="-1" aria-labelledby="workModalLabel" aria-hidden="true">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="workModalLabel">Address</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <label for="work-region">시/도:  &nbsp;</label>
              <select id="work-region" v-model="workRegion">
                <option v-for="region in regionData.regions" :key="region" :value="region">{{ region }}</option>
              </select>
              &nbsp;
              <label for="work-city">시/군/구: &nbsp; </label>
              <select id="work-city" v-model="workCity">
                <option v-for="city in regionData.cities[workRegion]" :key="city" :value="city">{{ city }}</option>
              </select>
              <!-- <br>
              <label for="work-loc">동:</label>
              <input type="text" v-model.trim="workloc" id="work-loc"> -->
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary btn-xs" data-bs-dismiss="modal" @click="handlesubmit">Submit</button>
            </div>
          </div>
        </div>
      </div>
    </div>
    </div>
          <div class="mb-3">
            <label for="salary" class="form-label">연봉:</label>
            <select class="form-select form-select-sm" aria-label="Select your salary" v-model="user.salary" id="salary">
              <option value="" disabled>Select your salary</option>
              <option value="2500만원 미만">2500만원 미만</option>
              <option value="2500~3500만원">2500~3500만원</option>
              <option value="3500~4500만원">3500~4500만원</option>
              <option value="4500~5500만원">4500~5500만원</option>
              <option value="5500~6500만원">5500~6500만원</option>
              <option value="6500~7500만원">6500~7500만원</option>
              <option value="7500~8500만원">7500~8500만원</option>
              <option value="8500만원 초과">8500만원 초과</option>
            </select>
          </div>
          <div class="mb-3">
            <label for="money" class="form-label">자산:</label>
            <div class="input-group">
              <input type="text" v-model.trim="user.money" id="user.money" class="form-control">
              <span class="input-group-text">만원</span>
            </div>
          </div>
          <div class="d-grid">
            <button type="submit" class="btn col btn-lg" @click="updateUser">Update</button>
          </div>
        </form>
      </div>
      </div>
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useArticleStore } from '@/stores/articles'

const store = useArticleStore()
const update = ref(false)

const user = ref([])
const fetchUser = () => {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/accounts/api/user/`,
    headers: {
      Authorization: `Token ${store.token}`
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
})

const updateUser = () => {
  console.log('go')
  update.value = false
  axios({
    method: 'put',
    url: `http://127.0.0.1:8000/accounts/api/update-user/`,
    data: {
        email: user.value.email,
        financial_products: user.value.financial_products,
        mainbank: user.value.mainbank,
        money: user.value.money,
        register: user.value.register,
        salary: user.value.salary,
        username: user.value.username,
        work: user.value.work
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

const banks = ['농협은행주식회사', '하나은행', '신한은행', '국민은행', '토스뱅크 주식회사', '주식회사 카카오뱅크', '우리은행', '주식회사 케이뱅크', '한국스탠다드차타드은행', '대구은행', '부산은행', '광주은행', '제주은행', '전북은행', '경남은행', '중소기업은행', '한국산업은행', '수협은행']
const regionData = {
  regions: ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시', '세종특별자치시', '경기도', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주특별자치도'],
  cities: {
  '서울특별시': ['강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구', '동대문구', '동작구', '마포구', '서대문구', '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구'],
  '부산광역시': ['강서구', '금정구', '기장군', '남구', '동구', '동래구', '부산진구', '북구', '사상구', '사하구', '서구', '수영구', '연제구', '영도구', '중구', '해운대구'],
  '대구광역시': ['남구', '달서구', '달성군', '동구', '북구', '서구', '수성구'],
  '인천광역시': ['강화군', '계양구', '남동구', '동구', '미추홀구', '부평구', '서구', '연수구', '옹진군', '중구'],
  '광주광역시': ['광산구', '남구', '동구', '북구', '서구'],
  '대전광역시': ['대덕구', '동구', '서구', '유성구', '중구'],
  '울산광역시': ['남구', '동구', '북구', '울주군', '중구'],
  '세종특별자치시': ['세종특별자치시'],
  '경기도': ['가평군', '고양시 덕양구', '고양시 일산동구', '고양시 일산서구', '과천시', '광명시', '광주시', '구리시', '군포시', '김포시', '남양주시', '동두천시', '부천시 소사구', '부천시 오정구', '부천시 원미구', '성남시 분당구', '성남시 수정구', '성남시 중원구', '수원시 권선구', '수원시 영통구', '수원시 장안구', '수원시 팔달구', '시흥시', '안산시 단원구', '안산시 상록구', '안성시', '안양시 동안구', '안양시 만안구', '양주시', '양평군', '여주시', '연천군', '오산시', '용인시 기흥구', '용인시 수지구', '용인시 처인구', '의왕시', '의정부시', '이천시', '파주시', '평택시', '포천시', '하남시', '화성시'],
  '강원도': ['강릉시', '고성군', '동해시', '삼척시', '속초시', '양구군', '양양군', '영월군', '원주시', '인제군', '정선군', '철원군', '춘천시', '태백시', '평창군', '홍천군', '화천군', '횡성군'],
  '충청북도': ['괴산군', '단양군', '보은군', '영동군', '옥천군', '음성군', '제천시', '증평군', '진천군', '청주시 상당구', '청주시 서원구', '청주시 청원구', '청주시 흥덕구', '충주시'],
  '충청남도': ['계룡시', '공주시', '금산군', '논산시', '당진시', '보령시', '부여군', '서산시', '서천군', '아산시', '예산군', '천안시 동남구', '천안시 서북구', '청양군', '태안군', '홍성군'],
  '전라북도': ['고창군', '군산시', '김제시', '남원시', '무주군', '부안군', '순창군', '완주군', '익산시', '임실군', '장수군', '전주시 완산구', '전주시 덕진구', '정읍시', '진안군'],
  '전라남도': ['강진군', '고흥군', '곡성군', '광양시', '구례군', '나주시', '담양군', '목포시', '무안군', '보성군', '순천시', '신안군', '여수시', '영광군', '영암군', '완도군', '장성군', '장흥군', '진도군', '함평군', '해남군', '화순군'],
  '경상북도': ['경산시', '경주시', '고령군', '구미시', '군위군', '김천시', '문경시', '봉화군', '상주시', '성주군', '안동시', '영덕군', '영양군', '영주시', '영천시', '예천군', '울릉군', '울진군', '의성군', '청도군', '청송군', '칠곡군', '포항시 남구', '포항시 북구'],
  '경상남도': ['거제시', '거창군', '고성군', '김해시', '남해군', '밀양시', '사천시', '산청군', '양산시', '의령군', '진주시', '창녕군', '창원시 마산합포구', '창원시 마산회원구', '창원시 성산구', '창원시 의창구', '창원시 진해구', '통영시', '하동군', '함안군', '함양군', '합천군'],
  '제주특별자치도': ['서귀포시', '제주시'],
  },
}
const register = ref('');
const selectedRegion = ref('');
const selectedCity = ref('');
const selectedloc = ref('');

const info = ref(false);

const handleRe = () => {
  selectedRegion.value = '';
  selectedCity.value = '';
  selectedloc.value = '';
  info.value = false;
};

const handleSubmit = () => {
  register.value = `${selectedRegion.value} ${selectedCity.value} ${selectedloc.value}`;
  info.value = true;
  user.value.register = register.value
};

const work = ref('')
const workRegion = ref('');
const workCity = ref('');
const workloc = ref('');

const check = ref(false);

const handleTurn = () => {
  workRegion.value = '';
  workCity.value = '';
  workloc.value = '';
  check.value = false;
};

const handlesubmit = () => {
  work.value = `${workRegion.value} ${workCity.value} ${workloc.value}`;
  check.value = true;
  user.value.work = work.value
};

const mainbank = ref([])

const bankupdate = function () {
  const mainbankString = mainbank.value.join(', ')
  user.value.mainbank = mainbankString
}

</script>

<style scoped>
.basic-info {
  border: 1px solid #ccc;
  padding: 20px;
  margin-bottom: 20px;
}

.basic-info h3 {
  margin-bottom: 10px;
}

.update-btn {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
}

.update-btn:hover {
  background-color: #0056b3;
}

.button-login-box {
  width: 200px;
  margin: 20px 0;
  background-color: skyblue;
}

template {
  height: 100%;
  margin: 0;
  display: flex;
  justify-content: center;
  align-items: center;
}
#container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  width: 100%;
}
#loginBox {
  width: 400px; /* 크기 키우기 */
  padding: 20px; /* 내부 여백 추가 */
  text-align: center;
  background-color: #ffffff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 그림자 추가 */
  border-radius: 8px; /* 모서리 둥글게 */
}
.input-form-box {
  display: flex;
  margin-bottom: 10px;
}
.input-form-box > label {
  min-width: 100px; /* 라벨의 최소 너비 */
  padding-top: 10px;
  text-align: right;
  margin-right: 10px;
}
.input-form-box > input {
  flex: 1;
}
.button-login-box {
  margin: 20px 0;
}
#loginBoxTitle {
  color: #000000;
  font-weight: bold;
  font-size: 32px;
  text-transform: uppercase;
  padding: 10px;
  margin-bottom: 20px;
  background: linear-gradient(to right, #270a09, #8ca6ce);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
#inputBox {
  margin: 10px;
}
#inputBox button {
  padding: 10px 20px;
}
.col {
  background-color: skyblue;
}

#loginBox {
  max-width: 500px;
  margin: auto;
}

.input-form-box {
  margin-bottom: 1rem;
}

.btn-xs {
  font-size: 0.75rem;
}
</style>