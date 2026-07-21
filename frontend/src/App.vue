<!-- <script setup>

import Footer from './components/Footer.vue';
import Navbar from './components/Navbar.vue';

</script>

<template>

  <Navbar />
  <router-view />

  <Footer />

</template> -->
<!-- <template>
  <Navbar />
  <FooterBarForMobile />

  <router-view />

  <Footer />

  Desktop WhatsApp
  <a href="https://wa.me/918123619994" target="_blank"
    class="hidden md:flex fixed bottom-6 right-6 z-40 w-12 h-12 bg-green-500 text-white rounded-full items-center justify-center shadow-lg hover:scale-110 transition-all duration-300">
    <i class="bi bi-whatsapp text-3xl"></i>
  </a>


  Scroll To Top
  <button v-show="showScrollTop" @click="scrollToTop"
    class="fixed bottom-24 right-6 z-30 w-12 h-12 bg-[#0D5C63] text-white rounded-full flex items-center justify-center shadow-lg">
    <i class="bi bi-chevron-up text-xl"></i>
  </button>
</template>

<script setup>
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'
import FooterBarForMobile from './FooterBarForMobile.vue';
import { onMounted, onUnmounted, ref } from 'vue';

const showScrollTop = ref(false);

const handleScroll = () => {
  showScrollTop.value = window.scrollY > 300;
};

const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: "smooth",
  });
};

onMounted(() => {
  window.addEventListener("scroll", handleScroll);
});

onUnmounted(() => {
  window.removeEventListener("scroll", handleScroll);
});
</script>

<style>
* {
  font-family: "Bricolage Grotesque", sans-serif;
  
}
</style> -->

<template>
  <!-- Preloader -->
  <Preloader v-if="loading" />

  <!-- Website Content -->
  <template v-else>
    <Navbar />

    <!-- <FooterBarForMobile />

    <router-view />

    <Footer /> -->
    <div class="pb-20 md:pb-0">
    <router-view />
    <Footer />
  </div>

  <FooterBarForMobile />

    <!-- Desktop WhatsApp -->
    <a href="https://wa.me/918123619994" target="_blank"
      class="hidden md:flex fixed bottom-6 right-6 z-40 w-12 h-12 bg-green-500 text-white rounded-full items-center justify-center shadow-lg hover:scale-110 transition-all duration-300">
      <i class="bi bi-whatsapp text-3xl"></i>
    </a>
<RouterLink
  v-if="$route.path !== '/'"
  to="/contact-us"
  class="fixed right-0 top-1/2 -translate-y-1/2 z-50
         hidden lg:flex
         flex-col items-center gap-3
         bg-[#0D5C63]
         text-white
         px-2 py-5
         rounded-l-2xl
         shadow-2xl
         hover:bg-[#09464B]
         transition-all duration-300"
>
  <i class="bi bi-chat-dots-fill text-xl"></i>

  <span
    class="text-xs font-semibold tracking-widest"
    style="writing-mode: vertical-rl;"
  >
    ENQUIRY
  </span>
</RouterLink>

    

    <!-- Scroll To Top -->
    <button v-show="showScrollTop" @click="scrollToTop"
      class="fixed bottom-24 right-6 z-30 w-12 h-12 bg-[#0D5C63] text-white rounded-full flex items-center justify-center shadow-lg">
      <i class="bi bi-chevron-up text-xl"></i>
    </button>
  </template>
</template>

<script setup>
import Navbar from "./components/Navbar.vue";
import Footer from "./components/Footer.vue";
import FooterBarForMobile from "./FooterBarForMobile.vue";
import Preloader from "./components/Preloader.vue";

import { onMounted, onUnmounted, ref } from "vue";

const loading = ref(true);
const showScrollTop = ref(false);

const handleScroll = () => {
  showScrollTop.value = window.scrollY > 300;
};

const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: "smooth",
  });
};

onMounted(() => {
  window.addEventListener("scroll", handleScroll);

  setTimeout(() => {
    loading.value = false;
  }, 1800);
});

onUnmounted(() => {
  window.removeEventListener("scroll", handleScroll);
});
</script>

<style>
* {
  font-family: "Bricolage Grotesque", sans-serif;
}
</style>