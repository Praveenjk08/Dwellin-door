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
                    <input type="email" placeholder="Enter your email" class="w-full lg:w-[220px]
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

                    <button class="h-9
                        px-4
                        rounded-full
                        bg-white
                        text-black
                        text-sm
                        font-medium">
                        Subscribe
                    </button>
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

                    <button class="mt-4
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
                        <a href="#" class="block text-gray-600 hover:text-white">Home</a>
                        <a href="#" class="block text-gray-600 hover:text-white">Categories</a>
                        <a href="#" class="block text-gray-600 hover:text-white">Properties</a>
                        <a href="#" class="block text-gray-600 hover:text-white">Featured Property</a>
                    </div>

                    <div class="space-y-3 text-sm">
                        <a href="#" class="block text-gray-600 hover:text-white">Testimonials</a>
                        <a href="#" class="block text-gray-600 hover:text-white">Blog</a>
                        <a href="#" class="block text-gray-600 hover:text-white">FAQs</a>
                        <a href="#" class="block text-gray-600 hover:text-white">Contact Us</a>
                    </div>

                </div>

            </div>

            <!-- Bottom -->
            <div
                class="border-t border-white/10 py-4 flex flex-col md:flex-row items-center justify-between gap-4 mx-0 md:mx-10 lg:mx-[135px]">

                <p class="text-xs text-gray-500 text-center md:text-left">
                    ©2026 Dwell In Door
                </p>

                <div class="flex flex-wrap justify-center items-center gap-6">
                    <a href="#" class="text-xs text-gray-500 hover:text-white">
                        Terms of Service
                    </a>

                    <a href="#" class="text-xs text-gray-500 hover:text-white">
                        Privacy Policy
                    </a>
                </div>

            </div>

        </div>
    </footer>
</template>

<script setup>
import { ref } from 'vue';


const sucessMessage = ref("")
const errorMessage = ref("")



</script>