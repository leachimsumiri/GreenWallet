import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home'
import GreenDashboard from '../views/GreenDashboard'
import AccountDetails from '../views/AccountDetails'
import NewTransaction from '../views/NewTransaction'
import SignOut from '../views/SignOut'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect: 'home'
  },
  {
  path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/greendashboard',
    name: 'Green dashboard',
    component: GreenDashboard
  },
  {
    path: '/accountdetails',
    name: 'Account details',
    component: AccountDetails
  },
  {
    path: '/newtransaction',
    name: 'New Transaction',
    component: NewTransaction
  },
  {
    path: '/signout',
    name: 'Sign out',
    component: SignOut
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
