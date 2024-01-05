<template>
  <div>
    <h1>User City: {{ userCity }}</h1>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const userCity = ref(null)

onMounted(async () => {
  try {
    const position = await getUserLocation()
    const { latitude, longitude } = position.coords
    userCity.value = await reverseGeocode(latitude, longitude)
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
  const response = await fetch(
    `https://nominatim.openstreetmap.org/reverse?format=json&lat=${latitude}&lon=${longitude}`
  )
  const data = await response.json()
  return (
    data.address.city ||
    data.address.town ||
    data.address.village ||
    data.address.county
  )
}
</script>

<style scoped></style>
