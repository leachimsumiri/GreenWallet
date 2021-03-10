<template>
  <div id="app">
    <HeaderBar />
    <div class="container-fluid">
      <div class="row">
        <SideBar />
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
import feather from 'feather-icons'
import HeaderBar from '@/components/header-bar';
import SideBar from '@/components/side-bar';

export default {
  data(){
    return {
      name: 'GreenWallet'
    }
  },
  components:{
    HeaderBar,
    SideBar
  },
  mounted() {
    feather.replace();
  }
}
</script>

<style>

</style>
