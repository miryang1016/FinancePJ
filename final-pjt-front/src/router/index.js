import { createRouter, createWebHistory } from 'vue-router'
import MainPageView from '@/views/MainPageView.vue'
import CompareView from '@/views/CompareView.vue'
import RateCalView from '@/views/RateCalView.vue'
import ProfileView from '@/views/ProfileView.vue'
import BoardView from '@/views/BoardView.vue'
import BoardDetailView from '@/views/BoardDetailView.vue'
import BoardCreateView from '@/views/BoardCreateView.vue'
import SignUpView from '@/views/SignUpView.vue'
import SignInView from '@/views/SignInView.vue'
import { useArticleStore } from '@/stores/articles'
import MyBoardView from '@/views/MyBoardView.vue'
import BoardUpdateView from '@/views/BoardUpdateView.vue'
import ProductDetailView from '@/views/ProductDetailView.vue'
import MapView from '@/views/MapView.vue'
import ChatbotView from '@/views/ChatbotView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainPageView
    },
    {
      path: '/product',
      name: 'product',
      component: CompareView
    },
    {
      path: '/product/:pk',
      name: 'prdtdetail',
      component: ProductDetailView
    },
    {
      path: '/ratecal',
      name: 'ratecal',
      component: RateCalView,
    },
    {
      path: '/map',
      name: 'map',
      component: MapView,
    },
    {
      path: '/board',
      name: 'board',
      component: BoardView,
      beforeEnter: (to, from) => {
        const store = useArticleStore()
        if (store.isLogin === false) {
          window.alert('로그인이 필요합니다.')
          return { name: 'signin' }
        }
      }
    },
    {
      path: '/board/:pk',
      name: 'detail',
      component: BoardDetailView,
      beforeEnter: (to, from) => {
        const store = useArticleStore()
        if (store.isLogin === false) {
          window.alert('로그인이 필요합니다.')
          return { name: 'signin' }
        }
      }
    },
    {
      path: '/update/:pk',
      name: 'update',
      component: BoardUpdateView,
      beforeEnter: (to, from) => {
        const store = useArticleStore()
        if (store.isLogin === false) {
          window.alert('로그인이 필요합니다.')
          return { name: 'signin' }
        }
      }
    },
    {
      path: '/myboard',
      name: 'myboard',
      component: MyBoardView,
    },
    {
      path: '/create',
      name: 'create',
      component: BoardCreateView,
      beforeEnter: (to, from) => {
        const store = useArticleStore()
        if (store.isLogin === false) {
          window.alert('로그인이 필요합니다.')
          return { name: 'signin' }
        }
      }
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView,
      beforeEnter: (to, from) => {
        const store = useArticleStore()
        if (to.name === 'signup' && store.isLogin === true) {
          window.alert('이미 로그인된 계정입니다.')
          return { name: 'home' }
        }
      }
    },
    {
      path: '/signin',
      name: 'signin',
      component: SignInView,
      beforeEnter: (to, from) => {
        const store = useArticleStore()
        if (to.name === 'signin' && store.isLogin === true) {
          window.alert('이미 로그인된 계정입니다.')
          return { name: 'main' }
        }
      }
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView,
      beforeEnter: (to, from) => {
        const store = useArticleStore()
        if (store.isLogin === false) {
          window.alert('로그인이 필요합니다.')
          return { name: 'signin' }
        }
      }
    },
  ]
})

export default router
