<template>
  <div>
    <h1>User City: {{ userCity }}</h1>
    <p>Temperature: {{ temperature }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const userCity = ref(null)
const temperature = ref(null)

onMounted(async () => {
  try {
    const position = await getUserLocation()
    const { latitude, longitude } = position.coords
    userCity.value = await reverseGeocode(latitude, longitude)
    await getWeather()
  } catch (error) {
    console.error('Error getting user city:', error.message)
  }
})

async function getUserLocation() {
  return new Promise((resolve, reject) => {
    navigator.geolocation.getCurrentPosition(resolve, reject)
  })
}

async function reverseGeocode(latitude, longitude) {
  try {
    const res = await axios.get(
      `https://nominatim.openstreetmap.org/reverse?format=json&lat=${latitude}&lon=${longitude}`
    )
    const data = res.data
    return (
      data.address.city ||
      data.address.town ||
      data.address.village ||
      data.address.county
    )
  } catch (err) {
    console.log(err)
    return null
  }
}

async function getWeather() {
  try {
    if (userCity.value) {
      const lowerCaseCity = userCity.value.toLowerCase()
      const res = await axios.get(
        `http://127.0.0.1:8000/api/get_weather?city=${lowerCaseCity}`
      )
      temperature.value = res.data.temperature
    }
  } catch (err) {
    console.error(err)
  }
}
</script>

<style scoped></style>
