

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
                            Featured property
                        </span>

                    </div>

                    <h2 class="text-[24px] md:text-[28px] lg:text-[30px] font-semibold leading-[1.05] text-[#1E252B]">
                        Modern luxe villa
                    </h2>

                    <div class="flex items-center gap-2 mt-2 text-gray-500">

                        <span class="material-symbols-outlined text-[16px]">
                            location_on
                        </span>

                        <span class="text-[14px] md:text-[16px]">
                            20 S Aurora Ave, Miami
                        </span>

                    </div>

                    <p class="mt-4 text-[12px] leading-6 text-gray-700">
                        Experience luxury living at modern luxe villa, located at
                        20 S Aurora Ave, Miami. Priced at $1,650,500, this 560 ft²
                        smart home offers 4 bedrooms, 3 bathrooms, and spacious
                        living areas. Enjoy energy efficiency, natural light,
                        security systems, outdoor spaces, and 2 bar areas—
                        perfect for 8+ guests. Built in 2025.
                    </p>

                    <div class="mt-5 space-y-3">

                        <div class="flex gap-5">

                            <span class="material-symbols-outlined text-[20px]">
                                pool
                            </span>

                            <div>

                                <h4 class="text-[16px] font-medium">
                                    Poolside bliss
                                </h4>

                                <p class="text-gray-500 text-[14px]">
                                    One of the few homes in the area with a private pool.
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
                                    Energy efficient
                                </h4>

                                <p class="text-gray-500 text-[14px]">
                                    Built in 2025 with sustainable and smart-home features.
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