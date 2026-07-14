<!-- <template>
    <section class="px-8 md:px-8 lg:mx-40 py-10">

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-20 items-center">

            Left Image
            <div class="relative">

                <img :src="images[currentIndex]"
                    class="w-full lg:w-[900px] h-[250px] md:h-[350px] lg:h-[420px] object-cover rounded-[10px] transition-all duration-500" />

                Left Arrow
                <button @click="prevSlide"
                    class="absolute left-2 lg:-left-4 top-1/2 -translate-y-1/2 w-8 h-8 lg:w-10 lg:h-10 rounded-full bg-[#162028] text-white flex items-center justify-center">
                    <span class="material-symbols-outlined text-[14px]">
                        arrow_back
                    </span>
                </button>

                Right Arrow
                <button @click="nextSlide"
                    class="absolute right-2 lg:-right-4 top-1/2 -translate-y-1/2 w-8 h-8 lg:w-10 lg:h-10 rounded-full bg-[#162028] text-white flex items-center justify-center">
                    <span class="material-symbols-outlined text-[14px]">
                        arrow_forward
                    </span>
                </button>

                Dots
                <div class="absolute bottom-4 left-1/2 -translate-x-1/2 flex gap-2">
                    <div v-for="(img, index) in images" :key="index" @click="currentIndex = index"
                        class="w-2 h-2 rounded-full cursor-pointer"
                        :class="currentIndex === index ? 'bg-white' : 'bg-white/50'"></div>
                </div>

            </div>

            Right Content
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

                <div class="mt-5 space-y-2">

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

                <div class="flex  sm:flex-row items-start sm:items-center gap-4 sm:gap-8 mt-3">

                    <button class="bg-[#17C08E] text-white px-4 py-2 rounded-full font-medium">
                        <span class="text-sm text-center">
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

    </section>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from "vue";

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
    }, 3000); // 3 seconds
});

onUnmounted(() => {
    clearInterval(interval);
});
</script> -->

<template>
    <section class="mx-4 md:mx-40 lg:mx-40 pb-10">
        <div class="max-w-[1400px] mx-auto px-4">



            <div class="grid grid-cols-1 lg:grid-cols-[60%_40%] gap-8 lg:gap-10 items-center">

                <!-- Left Image -->
                <!-- <div class="relative">

                    <img :src="images[currentIndex]"
                        class="w-full h-[250px] md:h-[350px] lg:h-[420px] object-cover rounded-[10px] transition-all duration-500" />

                    Left Arrow
                    <button @click="prevSlide"
                        class="absolute left-2 lg:-left-4 top-1/2 -translate-y-1/2 w-8 h-8 lg:w-10 lg:h-10 rounded-full bg-[#162028] text-white flex items-center justify-center">

                        <span class="material-symbols-outlined text-[14px]">
                            arrow_back
                        </span>

                    </button>

                    Right Arrow
                    <button @click="nextSlide"
                        class="absolute right-2 lg:-right-4 top-1/2 -translate-y-1/2 w-8 h-8 lg:w-10 lg:h-10 rounded-full bg-[#162028] text-white flex items-center justify-center">

                        <span class="material-symbols-outlined text-[14px]">
                            arrow_forward
                        </span>

                    </button>

                    Dots
                    <div class="absolute bottom-4 left-1/2 -translate-x-1/2 flex gap-2">

                        <div v-for="(img, index) in images" :key="index" @click="currentIndex = index"
                            class="w-2 h-2 rounded-full cursor-pointer"
                            :class="currentIndex === index ? 'bg-white' : 'bg-white/50'">
                        </div>

                    </div>

                </div> -->
                <div class="h-f rounded-3xl">
                    <Carousel :items-to-show="1" :wrap-around="true" autoplay="4000">
                        <Slide v-for="(image, index) in images" :key="index">
                            <img :src="image" class="w-full md:h-[500px] rounded-[10px] object-cover" />
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

                        <button class="bg-[#17C08E] text-white px-4 py-2 rounded-full font-medium">

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