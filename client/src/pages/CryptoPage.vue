<template>
  <div class="flex justify-center items-center mt-20">
    <table class="table-auto">
      <thead>
        <tr>
          <th>Coin</th>
          <th>Price</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="crypto in cryptos" :key="crypto.symbol">
          <td>{{ crypto.symbol }}</td>
          <td>{{ crypto.price }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'

const cryptos = ref([])

onMounted(async () => {
  try {
    await getCryptoCurrencies()
    startPolling()
  } catch (error) {
    console.error('An error occurred:', error.message)
  }
})

async function getCryptoCurrencies() {
  try {
    const res = await axios.get(
      `http://127.0.0.1:8000/api/get_cyrypto_currency`
    )
    cryptos.value = res.data.crypto_price
  } catch (err) {
    console.error(err)
  }
}

function startPolling() {
  setInterval(() => {
    getCryptoCurrencies()
  }, 5000)
}
</script>
