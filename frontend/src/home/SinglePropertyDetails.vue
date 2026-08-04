

<template>
    <section class="mx-4 md:mx-40 lg:mx-40 pb-10">
        <div class="max-w-[1400px] mx-auto px-4">



            <div class="grid grid-cols-1 lg:grid-cols-[60%_40%] gap-8 lg:gap-10 items-center">

          
                <div class="h-f rounded-3xl">
                    <Carousel :items-to-show="1" :wrap-around="true" autoplay="3000">
                        <Slide v-for="(image, index) in images" :key="index">
                            <img :src="image"  alt="Featured luxury villa in Bangalore by Dwell In Door" class="w-full md:h-[500px] rounded-[10px] object-cover" />
                        </Slide>

                        <template #addons>
                            <Navigation />
                        </template>
                    </Carousel>
                </div>

                <!-- Right Content -->
                <div class="w-full">

                    <div class="flex items-center gap-2 mb-2">

                        <span class="material-symbols-outlined text-[#17C08E]">
                            home
                        </span>

                        <span class="font-medium text-[#435768] text-[14px]">
                           Featured Property in Bangalore
                        </span>

                    </div>

                    <h2 class="text-[24px] md:text-[28px] lg:text-[30px] font-semibold leading-[1.05] text-[#1E252B]">
                       Luxury Villas & Premium Homes in Bangalore
                    </h2>

                    <div class="flex items-center gap-2 mt-2 text-gray-500">

                        <span class="material-symbols-outlined text-[16px]">
                            location_on
                        </span>

                        <span class="text-[14px] md:text-[16px]">
                            Bangalore, Karnataka
                        </span>

                    </div>

                    <p class="mt-4 text-[12px] leading-6 text-gray-700">
                        Discover premium apartments, 
                        luxury villas and residential plots in
                         Bangalore with Dwell In Door. Our verified
                          real estate properties feature spacious bedrooms, 
                          modern bathrooms, premium amenities and prime
                           locations to help you find your dream home.
                    </p>

                    <div class="mt-5 space-y-3">

                        <div class="flex gap-5">

                            <span class="material-symbols-outlined text-[20px]">
                                pool
                            </span>

                            <div>

                                <h4 class="text-[16px] font-medium">
                                    Premium Amenities
                                </h4>

                                <p class="text-gray-500 text-[14px]">
                                    Enjoy landscaped gardens, clubhouse, swimming pool and premium lifestyle amenities.
                                </p>

                            </div>

                        </div>

                        <div class="flex gap-5">

                            <span class="material-symbols-outlined text-[20px]">
                                smartphone
                            </span>

                            <div>

                                <h4 class="text-[16px] font-medium">
                                    Smart home access
                                </h4>

                                <p class="text-gray-500 text-[14px]">
                                    Easily check yourself in with a modern keypad system.
                                </p>

                            </div>

                        </div>

                        <div class="flex gap-5">

                            <span class="material-symbols-outlined text-[20px]">
                                lightbulb
                            </span>

                            <div>

                                <h4 class="text-[16px] font-medium">
                                    Verified Properties
                                </h4>

                                <p class="text-gray-500 text-[14px]">
                                    Browse verified apartments, villas and plots with transparent pricing and trusted guidance.
                                </p>

                            </div>

                        </div>

                    </div>

                    <div class="flex items-center gap-6 mt-5">

                        <button class="bg-[#17C08E] text-white px-4 py-2 rounded-full font-medium"
                            @click="router.push('/contact-us')">

                            <span class="text-sm">
                                Get in touch
                            </span>

                        </button>

                        <div>

                            <h3 class="text-[26px] font-semibold text-[#1E252B]">
                                $1,650,500
                            </h3>

                            <p class="text-gray-400 text-[14px]">
                                Discounted price
                            </p>

                        </div>

                    </div>

                </div>

            </div>
        </div>

    </section>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from "vue";
import { Carousel, Slide, Navigation } from 'vue3-carousel'
import 'vue3-carousel/dist/carousel.css'
import router from "../router";

const images = [
    "/files/singleimage.jpeg",
    "/files/image (4).png",
    "/files/image (5).png",
];

const currentIndex = ref(0);

const nextSlide = () => {
    currentIndex.value =
        (currentIndex.value + 1) % images.length;
};

const prevSlide = () => {
    currentIndex.value =
        (currentIndex.value - 1 + images.length) % images.length;
};

let interval;

onMounted(() => {
    interval = setInterval(() => {
        nextSlide();
    }, 3000);
});

onUnmounted(() => {
    clearInterval(interval);
});
</script>