<template>
  <div id="app">
    <div v-if="logginstate === 0">
      <SignIn />
    </div>
    <div v-else>
      <HeaderBar />
      <div class="container-fluid">
        <div class="row">
          <SideBar />
          <router-view></router-view>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import feather from 'feather-icons';
import HeaderBar from '@/components/header-bar';
import SideBar from '@/components/side-bar';
import SignIn from '@/views/SignIn';

export default {
  data(){
    return {
      name: 'GreenWallet'
    }
  },
  methods:{
    logginstate: function(){
      if (window.loggedin === 1){return 1;}
      else{return 0;}
    }
  },
  components:{
    HeaderBar,
    SideBar,
    SignIn
  },
  mounted() {
    feather.replace();
  }
}
</script>

<style>

</style>
