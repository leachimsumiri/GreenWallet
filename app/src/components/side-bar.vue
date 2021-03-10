<template>
  <nav id="sidebarMenu" class="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse">
    <div class="position-sticky pt-3">
      <ul class="nav flex-column">
          <router-link active-class="nav-link active" class="nav-link" to="/home"><li class="nav-item"><span data-feather="home"></span>Home</li></router-link>
          <router-link active-class="nav-link active" class="nav-link" to="/greendashboard"><li class="nav-item"><span data-feather="activity"></span>Green Dashboard</li></router-link>
          <router-link active-class="nav-link active" class="nav-link" to="/accountdetails"><li class="nav-item"><span data-feather="info"></span>Account details</li></router-link>
          <router-link active-class="nav-link active" class="nav-link" to="/newtransaction"><li class="nav-item"><span data-feather="plus-circle"></span>New transaction</li></router-link>
          <router-link active-class="nav-link active" class="nav-link" to="/signout"><li class="nav item"><span data-feather="log-out"></span>Sign out</li></router-link>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {
name: "side-bar.vue"
}
</script>

<style scoped>
.nav-link.active{
  color: #27cc00;
}
</style>