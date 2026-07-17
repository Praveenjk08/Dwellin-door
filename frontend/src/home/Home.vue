<template>
  <section class="">

    <!-- Hero Banner -->
    <div class="relative h-[400px] md:h-[500px] overflow-hidden">

      <!-- Image -->
      <img :src="getFileUrl('home-banner-image-desktopece40f.png')" alt="Banner"
        class="hidden md:block w-full h-ful md:h-full md:object-cover" />

      <img :src="getFileUrl('mobile-home-banner.png')" alt="Banner"
        class="md:hidden w-full h-ful md:h-full md:object-cover" />

      <!-- Overlay -->
      <div class=" absolute inset-0 bg-gradient-to-r from-[#8DB8E3]/80 via-[#8DB8E3]/40 to-transparent">
      </div>

      <!-- Content -->
      <div class="absolute left-6 md:left-12 lg:left-[140px] top-20 md:top-36 z-10">

        <p class="text-white text-xs md:text-sm mb-4">
          Palm Springs, CA
        </p>

        <h1 class="text-[38px] md:text-[50px] lg:text-[60px]
          leading-[100%]
          tracking-[-0.02em]
          font-semibold
          text-white">
          Nature At <br />
          It's Best
        </h1>

        <div class="flex flex-wrap items-center gap-3 md:gap-4 mt-6">

          <button class="bg-white text-black px-4 py-2 rounded-full font-medium" @click="router.push('/contact-us')">
            Get in touch
          </button>

          <button class="border border-white text-white px-4 py-2 rounded-full" @click="router.push('/properties')">
            View Details
          </button>

        </div>

      </div>

      <div class="hidden lg:flex absolute top-[300px] right-[80px] z-20
         bg-white/25  rounded-xl shadow-xl p-3 items-center gap-3 w-[700px]">

        <input type="text" placeholder="Location"
          class="w-[180px] bg-white/65 hover:bg-white border rounded-xl px-4 py-2 outline-none">

        <select class="w-[150px] border bg-white/65 hover:bg-white  rounded-xl px-4 py-2 outline-none">
          <option>Type</option>
          <option>Apartment</option>
          <option>Villa</option>
          <option>Plot</option>
        </select>

        <select class="w-[150px] bg-white/65 hover:bg-white border rounded-xl px-4 py-2 outline-none">
          <option>Budget</option>
          <option>₹20L - ₹50L</option>
          <option>₹50L - ₹1Cr</option>
        </select>

        <button class="bg-[#0F5C63]/75 hover:bg-[#0F5C63]  text-white px-8 py-2 rounded-xl whitespace-nowrap">
          Search
        </button>

      </div>

      <!-- Floating Card -->
      <div class="hidden md:flex absolute bottom-0 right-0
        bg-white
        w-[95%] md:w-[700px] lg:w-[750px]
        min-h-[90px]
        rounded-tl-[10px]
         flex-wrap md:flex-nowrap items-center">


        <!-- Bedroom -->
        <div class="flex-1 min-w-[120px] text-center border-r border-gray-200 py-3">
          <span class="material-symbols-outlined text-2xl">
            bed
          </span>
          <p class="text-xs md:text-sm mt-1">
            4 Bedrooms
          </p>
        </div>

        <!-- Bathroom -->
        <div class="flex-1 min-w-[120px] text-center border-r border-gray-200 py-3">
          <span class="material-symbols-outlined text-2xl">
            bathtub
          </span>
          <p class="text-xs md:text-sm mt-1">
            4 Bathrooms
          </p>
        </div>

        <!-- Parking -->
        <div class="flex-1 min-w-[120px] text-center border-r border-gray-200 py-3">
          <span class="material-symbols-outlined text-2xl">
            garage_home
          </span>
          <p class="text-xs md:text-sm mt-1">
            Parking Space
          </p>
        </div>

        <!-- Price -->
        <div class="flex-1 min-w-[150px] text-center md:text-left p-3 md:pl-6">
          <h3 class="text-lg md:text-2xl lg:text-3xl font-semibold">
            $4,750,000
          </h3>
          <p class="text-gray-500 text-xs md:text-sm">
            For selling price
          </p>
        </div>

      </div>

    </div>


  </section>
  <!-- Mobile Search Bar -->
  <div class="lg:hidden px-4 -mt-8 relative bottom-10 z-20">

    <div class="bg-white rounded-2xl shadow-xl p-4">

      <input type="text" placeholder="Location" class="w-full border rounded-xl px-4 py-3 mb-3 outline-none">

      <div class="grid grid-cols-2 gap-3">

        <select class="border rounded-xl px-4 py-3 outline-none">
          <option>Type</option>
          <option>Apartment</option>
          <option>Villa</option>
          <option>Plot</option>
        </select>

        <select class="border rounded-xl px-4 py-3 outline-none">
          <option>Budget</option>
          <option>₹20L - ₹50L</option>
          <option>₹50L - ₹1Cr</option>
        </select>

      </div>

      <button class="w-full mt-3 bg-[#0F5C63]/75 hover:bg-[#0F5C63] text-white py-3 rounded-xl">
        Search
      </button>

    </div>
  </div>


  <!-- <PropertySections/> -->
  <PropertyCards class="block md:hidden" />
  <PropertySection />

  <section>
    <!-- Mobile Property Info Card -->
    <div class="block md:hidden px-4 py-6 bg-[#F8F8F8]">

      <!-- Bedroom -->
      <div class="flex items-center gap-4 bg-white rounded-2xl shadow-md px-5 py-5 mb-4">
        <span class="material-symbols-outlined text-3xl">
          bed
        </span>
        <div>
          <p class="font-semibold">4 Bedrooms</p>
          <p class="text-sm text-gray-500">Spacious Rooms</p>
        </div>
      </div>

      <!-- Bathroom -->
      <div class="flex items-center gap-4 bg-white rounded-2xl shadow-md px-5 py-5 mb-4">
        <span class="material-symbols-outlined text-3xl">
          bathtub
        </span>
        <div>
          <p class="font-semibold">4 Bathrooms</p>
          <p class="text-sm text-gray-500">Modern Design</p>
        </div>
      </div>

      <!-- Parking -->
      <div class="flex items-center gap-4 bg-white rounded-2xl shadow-md px-5 py-5 mb-4">
        <span class="material-symbols-outlined text-3xl">
          garage_home
        </span>
        <div>
          <p class="font-semibold">Parking Space</p>
          <p class="text-sm text-gray-500">2 Vehicle Capacity</p>
        </div>
      </div>

      <!-- Price -->
      <div class="bg-white rounded-2xl shadow-md px-5 py-5">
        <h3 class="text-3xl font-bold">
          $4,750,000
        </h3>
        <p class="text-gray-500 mt-1">
          For Selling Price
        </p>
      </div>

    </div>


  </section>
  <!-- <PropertyCards /> -->
  <PropertyCards class="hidden md:block" />
  <SinglePropertyDetails />
  <Testimonials />
  <HomeBlog />
  <CTA />
  <AboutTheDwellin />

</template>

<script setup>

import router from '../router.js';
import AboutTheDwellin from './AboutTheDwellin.vue';
import CTA from './CTA.vue';
import HomeBlog from './HomeBlog.vue';
import PropertyCards from './PropertyCards.vue';
import PropertySection from './PropertySection.vue';
import SinglePropertyDetails from './SinglePropertyDetails.vue';
import Testimonials from './Testimonials.vue';


const getFileUrl = (file) => {
  return `${window.location.origin}/files/${file}`;
};


// import PropertySections from '@/home/PropertySections.vue'
</script>