<template>
    <nav
        :class="
            route.path === '/'
                ? 'absolute top-0 left-0 w-full z-50'
                : 'sticky top-0 left-0 w-full z-50 bg-white shadow-sm'
        "
    >
        <div class="max-w-[1440px] mx-auto w-full px-6 lg:px-12">

            <div class="flex items-center justify-between">

                <!-- Logo -->
                <RouterLink to="/" class="flex-shrink-0">
                    <img
                        :src="getFileUrl('logo-with-some-changes.png')"
                        alt="Dwellin Door"
                        class="h-[70px] w-auto object-contain"
                    />
                </RouterLink>

                <!-- Desktop Menu -->
                <div
                    class="hidden lg:flex items-center gap-8 text-[15px] font-medium text-white"
                >

                    <RouterLink
                        to="/"
                        :class="[
                            'font-medium hover:text-[#0D5C63]',
                            route.path === '/' ? 'text-white' : 'text-black'
                        ]"
                    >
                        Dwell In Door
                    </RouterLink>

                    <RouterLink
                        to="/about-us"
                        class="font-medium text-[#1B1B1B] hover:text-[#0D5C63]"
                    >
                        About Us
                    </RouterLink>

                    <RouterLink
                        to="/properties"
                        class="flex items-center gap-1 font-medium text-[#1B1B1B] hover:text-[#0D5C63] transition-colors"
                    >
                        <span>Properties</span>
                    </RouterLink>

                    <RouterLink
                        to="/blogs"
                        class="font-medium text-[#1B1B1B] hover:text-[#0D5C63]"
                    >
                        Blogs
                    </RouterLink>

                    <RouterLink
                        to="/gallery"
                        class="font-medium text-[#1B1B1B] hover:text-[#0D5C63]"
                    >
                        Gallery
                    </RouterLink>

                    <RouterLink
                        to="/contact-us"
                        class="font-medium text-[#1B1B1B] hover:text-[#0D5C63]"
                    >
                        Contact
                    </RouterLink>
                </div>

                <!-- Desktop Call / Enquire Button -->
                <div class="hidden lg:flex items-center">

                    <a
                        href="tel:+919876543210"
                        class="bg-[#0D5C63] text-white text-sm px-5 py-2 rounded-xl font-medium shadow-sm hover:bg-[#084950] transition flex items-center gap-2"
                    >
                        <span class="material-symbols-outlined text-[18px]">
                            call
                        </span>

                        Enquire Now
                    </a>

                </div>

                <!-- Mobile Menu Button -->
                <button
                    @click="mobileMenu = !mobileMenu"
                    class="lg:hidden relative z-[10000]"
                >
                    <span
                        class="material-symbols-outlined text-[32px]"
                        :class="
                            route.path === '/'
                                ? 'text-white'
                                : 'text-[#0D5C63]'
                        "
                    >
                        {{ mobileMenu ? 'close' : 'menu' }}
                    </span>
                </button>

            </div>

            <!-- Mobile Menu -->
            <div
                v-if="mobileMenu"
                class="lg:hidden absolute left-0 top-[70px] w-full bg-white shadow-lg z-50"
            >

                <div
                    class="flex flex-col p-5 space-y-4 text-[#1B1B1B] font-medium"
                >

                    <RouterLink
                        to="/"
                        @click="mobileMenu = false"
                        class="font-medium text-[#1B1B1B] hover:text-[#0D5C63]"
                    >
                        Dwell In Door
                    </RouterLink>

                    <RouterLink
                        to="/about-us"
                        class="font-medium text-[#1B1B1B] hover:text-[#0D5C63]"
                        @click="mobileMenu = false"
                    >
                        About Us
                    </RouterLink>

                    <RouterLink
                        to="/properties"
                        @click="mobileMenu = false"
                        class="flex items-center gap-1 font-medium text-[#1B1B1B] hover:text-[#0D5C63] transition-colors"
                    >
                        <span>Properties</span>
                    </RouterLink>

                    <RouterLink
                        to="/blogs"
                        class="font-medium text-[#1B1B1B] hover:text-[#0D5C63]"
                        @click="mobileMenu = false"
                    >
                        Blogs
                    </RouterLink>

                    <RouterLink
                        to="/gallery"
                        class="font-medium text-[#1B1B1B] hover:text-[#0D5C63]"
                        @click="mobileMenu = false"
                    >
                        Gallery
                    </RouterLink>

                    <RouterLink
                        to="/contact-us"
                        class="font-medium text-[#1B1B1B] hover:text-[#0D5C63]"
                        @click="mobileMenu = false"
                    >
                        Contact
                    </RouterLink>

                    <!-- Mobile Call / Enquire Button -->
                    <a
                        href="tel:+919876543210"
                        @click="mobileMenu = false"
                        class="bg-[#0D5C63] text-white py-2 rounded-xl font-medium flex items-center justify-center gap-2"
                    >
                        <span class="material-symbols-outlined text-[18px]">
                            call
                        </span>

                        Enquire Now
                    </a>

                </div>

            </div>

        </div>
    </nav>
</template>

<script setup>
import { ref } from "vue";
import { RouterLink, useRoute } from "vue-router";
import router from "../router";

const route = useRoute();

const mobileMenu = ref(false);

const getFileUrl = (file) => {
    return `${window.location.origin}/files/${file}`;
};
</script>