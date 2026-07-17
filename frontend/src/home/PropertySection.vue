<template>
  <section class="py-12 md:py-12 bg-white px-4 md:px-6 lg:px-0 lg:mx-40">
    <div class="max-w-[1400px] mx-auto">

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 lg:gap-8">

        <!-- Left Content -->
        <div class="lg:col-span-5">

          <div class="flex items-center gap-2 mb-4">
            <div class="w-3 h-3 bg-[#35CAA0] rounded-sm"></div>
            <span class="text-sm text-gray-500 font-medium">
              Categories
            </span>
          </div>

          <h2 class="text-[28px] md:text-[36px] lg:text-[30px] leading-[110%] font-semibold text-[#111827]">
            Explore best properties
            <br />
            with expert services.
          </h2>

          <p class="mt-5 text-gray-500 text-base leading-6 max-w-full lg:max-w-[400px]">
            Discover a diverse range of premium properties, from luxurious
            apartments to spacious villas, tailored to your needs.
          </p>

          <!-- <button class="mt-5 bg-[#35CAA0] hover:bg-[#084950] text-white px-5 py-3 rounded-full font-medium transition">
            View Properties
          </button> -->
          <button @click="router.push('/properties')"
            class="mt-4 bg-[#35CAA0] hover:bg-[#084950] text-white px-4 py-2 rounded-full  font-medium transition">
            <span class="text-[12px] py-2 px-2">View Properties</span>
          </button>

        </div>

        <!-- Top Image -->
        <div class="lg:col-span-7 relative cursor-pointer overflow-hidden rounded-[20px]" @click="router.push({
          path: '/properties',
          query: {
            location: proprty_type[3]?.location_type
          }
        })">
          <img :src="proprty_type[3]?.images"
            class="w-full h-[180px] sm:h-[220px] md:h-[260px] object-cover rounded-[20px] transition-all duration-500 md:hover:scale-110" />

          <span
            class="absolute top-3 left-3 bg-white/20 backdrop-blur-md text-white px-3 py-1 rounded-full text-xs md:text-sm font-medium">
            {{ proprty_type[3]?.location_type }}
          </span>
        </div>

        <!-- Large Card -->
        <div class="lg:col-span-6">

          <div class="relative overflow-hidden rounded-[20px] group cursor-pointer" @click="router.push({
            path: '/properties',
            query: {
              location: proprty_type[2]?.location_type
            }
          })">

            <img :src="proprty_type[2]?.images"
              class="w-full h-[260px] object-cover transition-transform duration-700 group-hover:scale-110" />

            <span
              class="absolute top-4 left-4 bg-white/20 backdrop-blur-md text-white px-4 py-1 rounded-full text-sm font-medium">
              {{ proprty_type[2]?.location_type }}
            </span>

            <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-black/20 to-transparent"></div>

            <button class="absolute top-4 right-4 w-8 h-8 bg-white rounded-full flex items-center justify-center">
              →
            </button>

            <div class="absolute bottom-5 left-5 right-5 text-white">
              <h3 class="text-xl md:text-3xl font-semibold">
                Luxury Villas
              </h3>

              <p class="mt-2 text-sm md:text-base text-white/80 max-w-full md:max-w-[400px]">
                Experience elegance and comfort with our exclusive luxury villas,
                designed for sophisticated living.
              </p>
            </div>

          </div>

        </div>

        <!-- Bottom Images -->
        <!-- <div class="lg:col-span-6">

          <div class="grid grid-cols-2 gap-4 md:gap-5">

            <img src="/files/image (5).png" class="w-full h-[180px] md:h-[260px] object-cover rounded-[20px]" />

            <img src="/files/image (4).png" class="w-full h-[180px] md:h-[260px] object-cover rounded-[20px]" />

          </div>

        </div> -->
        <div class="lg:col-span-6">

          <div class="grid grid-cols-2 gap-4 md:gap-5">

            <!-- First Image -->
            <div class="relative cursor-pointer" @click="router.push({
              path: '/properties',
              query: {
                location: proprty_type[1]?.location_type
              }
            })">
              <img :src="proprty_type[1]?.images"
                class="w-full h-[180px] md:h-[260px] object-cover rounded-[20px] transition-all duration-500 hover:scale-110" />

              <span
                class="absolute top-3 left-3 bg-white/20 backdrop-blur-md text-white px-3 py-1 rounded-full text-xs md:text-sm font-medium border border-white/30">
                {{ proprty_type[1]?.location_type }}
              </span>
            </div>

            <!-- Second Image -->
            <div class="relative cursor-pointer" @click="router.push({
              path: '/properties',
              query: {
                location: proprty_type[0]?.location_type
              }
            })">
              <img :src="proprty_type[0]?.images"
                class="w-full h-[180px] md:h-[260px] object-cover rounded-[20px] transition-all duration-500 hover:scale-110 " />

              <span
                class="absolute top-3 left-3 bg-white/20 backdrop-blur-md text-white px-3 py-1 rounded-full text-xs md:text-sm font-medium border border-white/30">
                {{ proprty_type[0]?.location_type }} </span>
            </div>

          </div>

        </div>

      </div>

    </div>
  </section>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import axios from 'axios'
import router from '../router';

const proprty_type = ref([])

const get_all_propertype = async () => {
  try {

    const response = await axios.get("/api/method/dwell_in_door.api.property.get_property_type")

    proprty_type.value = response.data.message
    // console.log(property_type.value)
  }
  catch (error) {
    console.log(error);

  }
}

onMounted(() => {
  get_all_propertype()
})

</script>