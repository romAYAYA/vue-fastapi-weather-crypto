<template>
  <div class="flex justify-center items-center mt-20">
    <table class="table-auto">
      <thead>
        <tr>
          <th>Currency</th>
          <th>Buy ₸</th>
          <th>Sell ₸</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="currency in currencies" :key="currency.id">
          <td>{{ currency.currency }}</td>
          <td>{{ currency.buy_value }}</td>
          <td>{{ currency.sell_value }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'

const currencies = ref([])

onMounted(async () => {
  try {
    await getCurrencies()
  } catch (error) {
    console.error('An error occurred:', error.message)
  }
})

async function getCurrencies() {
  try {
    const res = await axios.get(`http://127.0.0.1:8000/api/get_currency`)
    currencies.value = res.data.currency
  } catch (err) {
    console.error(err)
  }
}
</script>
