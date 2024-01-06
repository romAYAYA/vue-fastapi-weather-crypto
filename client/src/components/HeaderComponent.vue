<template>
  <header>
    <nav class="bg-white border-gray-200 px-4 lg:px-6 py-2.5 dark:bg-gray-800">
      <div
        class="flex flex-wrap justify-between items-center mx-auto max-w-screen-xl"
      >
        <router-link to="/" class="flex items-center">
          <img
            src="https://flowbite.com/docs/images/logo.svg"
            class="mr-3 h-6 sm:h-9"
            alt="Flowbite Logo"
          />
          <span
            class="self-center text-xl font-semibold whitespace-nowrap dark:text-white"
            >Flowbite</span
          >
        </router-link>
        <div class="flex items-center lg:order-2">
          <p
            class="text-gray-800 dark:text-white font-medium text-sm px-4 lg:px-5 py-2 lg:py-2.5 mr-2"
          >
            {{ userCity }}:
          </p>
          <p
            class="text-gray-800 dark:text-white font-medium text-sm px-4 lg:px-5 py-2 lg:py-2.5 mr-2"
          >
            {{ temperature }}
          </p>
        </div>
        <div
          class="justify-between items-center w-full lg:flex lg:w-auto lg:order-1"
        >
          <ul
            class="flex flex-col mt-4 font-medium lg:flex-row lg:space-x-8 lg:mt-0"
          >
            <li>
              <router-link
                to="/"
                class="block py-2 pr-4 pl-3 text-white rounded bg-primary-700 lg:bg-transparent lg:text-primary-700 lg:p-0 dark:text-white"
                aria-current="page"
                >Currencies
              </router-link>
            </li>
            <li>
              <router-link
                to="/crypto"
                class="block py-2 pr-4 pl-3 text-gray-700 border-b border-gray-100 hover:bg-gray-50 lg:hover:bg-transparent lg:border-0 lg:hover:text-primary-700 lg:p-0 dark:text-gray-400 lg:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white lg:dark:hover:bg-transparent dark:border-gray-700"
                >Crypto
              </router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
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
