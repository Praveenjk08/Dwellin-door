<template>
    <footer class="bg-[#07161D] text-white">
        <div class="w-full max-w-[1600px] mx-auto px-5 md:px-8 lg:px-12">

            <!-- Newsletter Section -->
            <div
                class="mx-0 md:mx-10 lg:mx-[135px] pt-10 pb-5 lg:pt-16 lg:pb-10 border-b border-white/10 flex flex-col lg:flex-row items-start lg:items-center justify-between gap-6">

                <div class="w-full md:w-[450px] ">
                    <p class="text-[12px] leading-[20px] text-gray-300 font-semibold">
                        Stay updated with the latest news,
                        promotions, and exclusive offers.
                    </p>
                </div>

                <div class="flex flex-col sm:flex-row w-full lg:w-auto gap-3 sm:items-center">
                    <input type="email" v-model="email" placeholder="Enter your email" class="w-full lg:w-[220px]
  h-9
  bg-[#29333A]
  rounded-full
  px-4
  text-sm
  text-white
  border-0
  shadow-none
  outline-none
  ring-0
  focus:ring-0
  focus:outline-none
  appearance-none
  placeholder:text-gray-400" />

                    <button @click="subscribe" class="h-9
                        px-4
                        rounded-full
                        bg-white
                        text-black
                        text-sm
                        font-medium">
                        Subscribe
                    </button>

                    <p v-if="successMessage" class="text-green-600">
  {{ successMessage }}
</p>

<p v-if="errorMessage" class="text-red-600">
  {{ errorMessage }}
</p>
                </div>

                <div class="w-full md:w-[400px] lg:w-auto">
                    <p class="text-[11px] leading-4 text-gray-600">
                        By subscribing, you agree to receive our
                        promotional emails. You can unsubscribe
                        at any time.
                    </p>
                </div>

                <div class="relative lg:top-[20px] top-0 flex items-center gap-5">
                    <a href="#" class="text-2xl hover:text-[#16D6A4]">𝕏</a>
                    <a href="#" class="text-2xl hover:text-[#16D6A4]">f</a>
                    <a href="#" class="text-2xl hover:text-[#16D6A4]">◎</a>
                </div>

            </div>

            <!-- Main Footer -->
            <div
                class="py-6 lg:pt-12 pb-16 flex flex-col lg:flex-row justify-between gap-8 mx-0 md:mx-10 lg:mx-[135px]">

                <div>
                    <h2 class="text-[22px]
                        md:text-[28px]
                        lg:text-[32px]
                        leading-tight
                        font-medium">
                        Begin your path to
                        <br />
                        success—contact us today.
                    </h2>

                    <button @click="router.push('/contact-us')" class="mt-4
                        bg-[#16D6A4]
                        hover:bg-[#14c397] 
                        px-5 py-2
                        rounded-full
                        text-xs
                        font-medium">
                        Get in touch
                    </button>
                </div>

                <div class="grid grid-cols-2 gap-10 lg:gap-16 mr-0 lg:mr-20">

                    <div class="space-y-3 text-sm">
    <RouterLink
        to="/"
        class="block text-gray-600 hover:text-white"
    >
        Home
    </RouterLink>

    <RouterLink
        to="/properties"
        class="block text-gray-600 hover:text-white"
    >
        Properties
    </RouterLink>

    <RouterLink
        to="/gallery"
        class="block text-gray-600 hover:text-white"
    >
        Gallery
    </RouterLink>
</div>

                   <div class="space-y-3 text-sm">
    <RouterLink to="/about-us" class="block text-gray-600 hover:text-white">
        Testimonials
    </RouterLink>

    <RouterLink to="/blogs" class="block text-gray-600 hover:text-white">
        Blog
    </RouterLink>

    <RouterLink to="/contact-us" class="block text-gray-600 hover:text-white">
        Contact Us
    </RouterLink>
</div>
                </div>

            </div>

            <!-- Bottom -->
<div
    class="border-t border-white/10 py-5
           flex flex-col md:flex-row
           items-center justify-between
           gap-4
           text-center md:text-left
           mx-5 md:mx-10 lg:mx-[135px]">

    <!-- Copyright -->
    <p class="text-xs text-gray-500">
        ©2026 Dwell In Door
    </p>

    <!-- Links -->
    <div
        class="flex flex-col sm:flex-row
               items-center
               gap-3 sm:gap-6">

        <a href="#" class="text-xs text-gray-500 hover:text-white transition">
            Terms of Service
        </a>

        <a href="#" class="text-xs text-gray-500 hover:text-white transition">
            Privacy Policy
        </a>

        <a
            href="https://quantumberg.com"
            target="_blank"
            rel="noopener noreferrer"
            class="text-xs text-gray-500 hover:text-white transition"
        >
            Powered By:
            <span class="font-semibold text-[#0D5C63]">
                QuantumBerg Technologies
            </span>
        </a>

    </div>

</div>

        </div>
    </footer>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import router from '../router.js';

const email = ref("");
const successMessage = ref("");
const errorMessage = ref("");

const subscribe = async () => {
  successMessage.value = "";
  errorMessage.value = "";

   // Empty email validation
  if (!email.value.trim()) {
    errorMessage.value = "Please enter your email address.";
    return;
  }

  // Email format validation
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  if (!emailRegex.test(email.value)) {
    errorMessage.value = "Please enter a valid email address.";
    return;
  }
  try {
    const response = await axios.post(
      "/api/method/dwell_in_door.api.newsletter.add_email",
      {
        email: email.value,
      }
    );

   const result = response.data.message;

if (result.status === "success") {
  successMessage.value = result.message;
  errorMessage.value = "";
  email.value = "";

  setTimeout(() => {
    successMessage.value = "";
  }, 3000);

} else if (result.status === "exists") {
  errorMessage.value = result.message;

  setTimeout(() => {
    errorMessage.value = "";
  }, 3000);
}
  } catch (error) {
    if (error.response) {
      errorMessage.value =
        error.response.data.message || "Something went wrong!";
    } else {
      errorMessage.value = "Server connection failed.";
    }
  }
};
</script>