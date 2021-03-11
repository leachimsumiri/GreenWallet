<template>
  <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
    <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
      <h1 class="h2">AccountDetails</h1>
      <div class="btn-toolbar mb-2 mb-md-0">
        <div class="btn-group me-2">
          <button type="button" class="btn btn-sm btn-outline-secondary" disabled>Share</button>
          <button type="button" class="btn btn-sm btn-outline-secondary" disabled>Export</button>
        </div>
      </div>
    </div>
    <div class="row row-cols-1 row-cols-md-3 mb-3 text-center">
      <div class="col">
        <div class="card mb-4 shadow-sm">
          <div class="card-header">
            <h4 class="my-0 fw-normal">Financial Overview</h4>
          </div>
          <div class="card-body">
            <h1 class="card-title pricing-card-title" style="color: #27cc00">632,19<small class="text-muted">€</small></h1>
            <ul class="list-unstyled mt-3 mb-4">
              <li><span style="color: #27cc00">413,89</span>€ - checking account</li>
              <li><span style="color: #27cc00">0,01</span>€- savings others</li>
              <li><span style="color: #27cc00">100,01</span>€ - savings car</li>
              <li><span style="color: #27cc00">100,01</span>€ - savings household</li>
            </ul>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card mb-4 shadow-sm">
          <div class="card-header">
            <h4 class="my-0 fw-normal">My Supervisor</h4>
          </div>
          <div class="card-body">
            <h1 class="card-title pricing-card-title" style="color: #27cc00">Moser <small class="text-muted">Diana</small></h1>
            <ul class="list-unstyled mt-3 mb-4">
              <li><span data-feather="phone" style="color: #27cc00"> </span><span> +43 2 1987 65432</span></li>
              <li><span data-feather="headphones" style="color: #27cc00"></span><span style="color: #27cc00"> Hotline: </span><span>+43 2 1987 654433</span></li>
              <li><span data-feather="clock" style="color: #27cc00"></span><span style="color: #27cc00"> Opening hours:</span></li>
              <li><span class="fw-bold">Mon:</span><span> 08:00 - 18:00</span></li>
              <li><span class="fw-bold">Tue:</span><span> 08:00 - 18:00</span></li>
              <li><span class="fw-bold">Wed:</span><span> 08:00 - 18:00</span></li>
              <li><span class="fw-bold">Thu:</span><span> 08:00 - 18:00</span></li>
              <li><span class="fw-bold">Fri:</span><span> 08:00 - 18:00</span></li>
            </ul>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card mb-4 shadow-sm">
          <div class="card-header">
            <h4 class="my-0 fw-normal">Green Credit Card</h4>
          </div>
          <div class="card-body">
            <h1 class="card-title pricing-card-title" style="color: #27cc00">29 € <small class="text-muted">/ year</small></h1>
            <ul class="list-unstyled mt-3 mb-4">
              <li>+ gold card</li>
              <li>+ Accepted world wide</li>
              <li>+ pay online safely</li>
              <li>+ insurance included</li>
            </ul>
            <button type="button" class="w-100 btn btn-lg btn-outline-dark">Contact us</button>
          </div>
        </div>
      </div>
    </div>


  </main>
</template>

<script>
export default {
  name: "AccountDetails.vue"
}
</script>

<style scoped>

</style>