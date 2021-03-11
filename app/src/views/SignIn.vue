<template>
  <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
    <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
      <h1 class="h2">Sign In</h1>
    </div>

    <div>
      <button type="button" class="btn btn-outline-dark" @click="signin">Sign In</button>
    </div>

  </main>
</template>

<script>
export default {
  name: "SignIn.vue",
  methods:{
    signin: function(){
      window.loggedin = 1;
    }
  }
  }

</script>

<style scoped>

</style>