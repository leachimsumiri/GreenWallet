<template>
  <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
    <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
      <h1 class="h2">GreenDashboard</h1>
      <div class="btn-toolbar mb-2 mb-md-0">
        <div class="btn-group me-2">
          <button type="button" class="btn btn-sm btn-outline-secondary" disabled>Share</button>
          <button type="button" class="btn btn-sm btn-outline-secondary" disabled>Export</button>
        </div>
      </div>
    </div>
    <div class="container">
      <canvas class="my-4 w-100" id="myChart" width="400" height="100"></canvas>
          <table class="table">
            <thead>
            <tr>
              <th scope="col">green index</th>
              <th scope="col">target name</th>
              <th scope="col">IBAN</th>
              <th scope="col">amount (€)</th>
              <th scope="col">purpose</th>
              <th scope="col">date</th>
            </tr>
            </thead>
            <tbody>
              <tr v-for="transaction in transactions" :key="transaction.buchungsDatum">
                <th scope="row">{{transaction.greenIndex}}</th>
                <td>{{transaction.targetName}}</td>
                <td>{{transaction.IBAN}}</td>
                <td>{{transaction.amount}}</td>
                <td>{{transaction.purpose}}</td>
                <td>{{transaction.buchungsDatum}}</td>
              </tr>
            </tbody>
          </table>
    </div>
  </main>
</template>

<script>
import * as axios from 'axios';
import Chart from 'chart.js';

const gettransactions = async function(returnobject){
  const response = await axios.get('api/getGreenTransactions.json');
  //const response = await axios.get('http://127.0.0.1:5000/getGreenTransactions');
  console.log(response);

  let result = response.data.map(transaction => {
    if (returnobject === "transaction"){
      return transaction
    }
    else {
      return transaction.greenIndex;
    }
  });

  if(returnobject === "dataset"){
    result = accumulateGreenIndizes(result);
  }

  return result;
};

const accumulateGreenIndizes = function(arr) {
  for(let i = 0; i < arr.length; i++){
    if(i) {
      arr[i] = arr[i] + arr[i-1];
    }
  }

  return arr;
}

export default {
  data() {
    return {
      transactions: [],
      message: '',
      dataset: []
    }
  },
  name: "Transactions",
  async created() {
    await this.loadData();
    let ctx = document.getElementById("myChart");
    new Chart(ctx, {
      type: 'line',
      data: {
        labels: ['January','February','March','April','May','June','July','August','September','October','November','December'],
        datasets: [{
          data: this.dataset,
          lineTension: 0,
          backgroundColor: 'transparent',
          borderColor: '#27cc00',
          borderWidth: 4,
          pointBackgroundColor: '#27cc00'
        }]
      },
      options: {
        scales: {
          yAxes: [{
            ticks: {
              beginAtZero: false
            }
          }]
        },
        legend: {
          display: false
        }
      }
    });

  },
  methods: {
    async loadData(){
      this.transactions = [];
      this.dataset = [];
      this.message = 'getting transactions, please be patient';
      this.transactions = await gettransactions("transaction");
      this.dataset = await gettransactions("dataset");
      this.message = '';
    }
  }
}
</script>