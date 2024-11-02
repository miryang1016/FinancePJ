<template>
  <div class="container m-auto p-3">
    <h1>근처 은행 찾기</h1>
    <br>
    <div class="form-container">
      <label for="region" class="form-item">시/도:</label>
      <select id="region" v-model="selectedRegion" class="form-select size form-item" aria-label="Default select example">
        <option v-for="region in regionData.regions" :value="region">{{ region }}</option>
      </select>
      <label for="city" class="form-item">시/군/구:</label>
      <select id="city" v-model="selectedCity" class="form-select size form-item" aria-label="Default select example">
        <option v-for="city in regionData.cities[selectedRegion]" :value="city">{{ city }}</option>
      </select>
      <label for="loc" class="form-item">동:</label>
      <input type="text" v-model.trim="selectedloc" id="loc" class="form-control size" placeholder="ex) 분평동">
      <label for="bank" class="form-item">은행:</label>
      <select id="bank" v-model="selectedBank" class="form-select size form-item" aria-label="Default select example">
        <option v-for="bank in banks" :value="bank">{{ bank }}</option>
      </select>
      <button type="button" class="btn btn-outline-secondary form-item" @click="initMap()">찾기</button>
    </div>
    <div><button type="button" class="btn btn-outline-secondary form-item" @click="getCurrentLocation()">현재 위치 보기</button></div>
    <div id="map" style="width:1000px;height:700px;"></div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

// Kakao Maps API 스크립트를 로드하고 initMap 함수를 호출합니다.

onMounted(() => {
  const script = document.createElement('script')
  script.type = 'text/javascript'
  script.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=${import.meta.env.VITE_KAKAO_API_KEY_JS}&autoload=false&libraries=services,clusterer,drawing`
  document.body.appendChild(script)

  initMap()

});

function initMap() {
  // 카카오 지도 API가 로드되면 kakao 객체가 전역으로 사용 가능하게 됩니다.
  // 따라서 이곳에서 kakao 객체를 사용할 수 있습니다.
  function checkAndAddDong() {
        // selectedloc 값이 '동'으로 끝나지 않는다면 '동'을 붙여줌
        if (!selectedloc.value.endsWith('동')) {
            selectedloc.value += '동';
        }
        if (selectedBank.value === '은행') {
          selectedBank.value = '은행'
        }
    }

    // 입력 폼에서 포커스를 벗어날 때 이벤트 리스너 등록
    document.getElementById('loc').addEventListener('blur', checkAndAddDong);
  if (navigator.geolocation) {
      
      // GeoLocation을 이용해서 접속 위치를 얻어옵니다
      navigator.geolocation.getCurrentPosition(function(position) {

        var lat = position.coords.latitude, // 위도
            lon = position.coords.longitude; // 경도

  // 마커를 클릭하면 장소명을 표출할 인포윈도우입니다.
  const infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });

  const mapContainer = document.getElementById('map'); // 지도를 표시할 div 
  const mapOption = {
    center: new kakao.maps.LatLng(lat, lon), // 지도의 중심좌표
    level: 3 // 지도의 확대 레벨
  };  

  // 지도를 생성합니다    
  const map = new kakao.maps.Map(mapContainer, mapOption); 

  // 장소 검색 객체를 생성합니다
  const ps = new kakao.maps.services.Places(); 
  
  // 키워드로 장소를 검색합니다
  ps.keywordSearch(`${selectedRegion.value} ${selectedCity.value} ${selectedloc.value} ${selectedBank.value}`, placesSearchCB); 
  
  // 키워드 검색 완료 시 호출되는 콜백함수입니다
  function placesSearchCB(data, status, pagination) {
    if (status === kakao.maps.services.Status.OK) {
      // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
      // LatLngBounds 객체에 좌표를 추가합니다
      const bounds = new kakao.maps.LatLngBounds();
      
      for (let i = 0; i < data.length; i++) {
        displayMarker(data[i]);    
        bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
      }       
      
      // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
      map.setBounds(bounds);
    } else if (status !== kakao.maps.services.Status.OK) {
      window.alert('입력하신 주소에 선택한 은행이 없습니다.')
    }
    
  }

  // 지도에 마커를 표시하는 함수입니다
  function displayMarker(place) {
      // 마커를 생성하고 지도에 표시합니다
      const marker = new kakao.maps.Marker({
        map: map,
        position: new kakao.maps.LatLng(place.y, place.x) 
      });

      // 마커에 클릭이벤트를 등록합니다
      kakao.maps.event.addListener(marker, 'click', function() {
        // 마커를 클릭하면 장소명
        // 마커를 클릭하면 장소명이 인포윈도우에 표시됩니다.
      infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>');
      infowindow.open(map, marker);
    });
  }
}
)}
}

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
const banks = ['은행', '농협은행주식회사', '하나은행', '신한은행', '국민은행', '우리은행', '한국스탠다드차타드은행', '대구은행', '부산은행', '광주은행', '제주은행', '전북은행', '경남은행', '중소기업은행', '한국산업은행', '수협은행']

const selectedRegion = ref('서울특별시')
const selectedCity = ref('중구')
const selectedloc = ref('명동')
const selectedBank = ref('은행')

function getCurrentLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      const lat = position.coords.latitude; // 위도
      const lon = position.coords.longitude; // 경도
      
      const mapContainer = document.getElementById('map'); // 지도를 표시할 div 
      const mapOption = {
        center: new kakao.maps.LatLng(lat, lon), // 지도의 중심좌표를 현재 위치로 설정
        level: 5 // 지도의 확대 레벨
      };  

      // 지도를 생성합니다    
      const map = new kakao.maps.Map(mapContainer, mapOption); 
    });
  } else {
    window.alert('현재 위치를 가져올 수 없습니다.');
  }
}




</script>

<style scoped>
/* 필요한 경우 스타일을 추가할 수 있습니다. */
template {
      height: 100%;
      margin: 0;
      display: flex;
      justify-content: center;
      align-items: center;
    }
    .container {
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .form-container {
      display: flex;
      flex-direction: row;
      align-items: center;
      gap: 10px; /* 요소 간의 간격 */
    }
    .form-item {
      margin: 5px;
    }
    .size {
      width: 150px; /* select 요소의 너비 설정 */
    }
    #map {
      margin-top: 10px; /* 맵과 폼 사이의 간격 */
    }
    
</style>