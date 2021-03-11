<template>
  <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
    <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
      <h1 class="h2">Sucessfully signed out</h1>
    </div>

    <canvas class="my-4 w-100" id="myChart" width="900" height="300"></canvas>

  </main>
</template>

<script>
export default {
  name: "SignOut.vue",
  mounted(){
    window.loggedin = 0;
    (document.getElementById("sidebarMenu")).remove();
    let elems = document.getElementsByClassName("navbar");
    for (let i = 0; i<=elems.length;i++){
      elems[i].remove();
    }
  }
}
</script>

<style scoped>

</style>