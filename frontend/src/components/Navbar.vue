<template>
    <!-- <nav class="absolute top-0 left-0 w-full z-50 flex items-center h-[70px]"> -->
    <nav :class="route.path === '/'
        ? 'absolute top-0 left-0 w-full z-50'
        : 'sticky top-0 left-0 w-full z-50 bg-white shadow-sm'">
        <div class="max-w-[1440px] mx-auto w-full px-6 lg:px-12">

            <div class="flex items-center justify-between">

                <!-- Logo -->
                <RouterLink to="/" class="flex-shrink-0">
                    <img :src="getFileUrl('dwellin-door-logo.png')" alt="Dwellin Door"
                        class="h-[70px] w-auto object-contain" />
                </RouterLink>

                <!-- Desktop Menu -->
                <div class="hidden lg:flex items-center gap-8 text-[15px] font-medium text-white hover:text-#0D5C63">

                    <RouterLink to="/" :class="[
                        'font-medium hover:text-[#0D5C63]',
                        $route.path === '/' ? 'text-white' : 'text-black'
                    ]">
                        Dwell In Door
                    </RouterLink>


                    <RouterLink to="/about-us" class="font-medium text-[#1B1B1B] hover:text-[#0D5C63]">About Us
                    </RouterLink>
                    <RouterLink to="/properties"
                        class="flex items-center gap-1 font-medium text-[#1B1B1B] hover:text-[#0D5C63] transition-colors">
                        <span>Properties</span>
                        <span class="material-symbols-outlined text-[18px]">
                            keyboard_arrow_down
                        </span>
                    </RouterLink>
                    <RouterLink to="/properties"
                        class="flex items-center gap-1 font-medium text-[#1B1B1B] hover:text-[#0D5C63] transition-colors">
                        <span>Services</span>
                        <span class="material-symbols-outlined text-[18px]">
                            keyboard_arrow_down
                        </span>
                    </RouterLink>

                    <RouterLink to="/blogs" class="font-medium text-[#1B1B1B] hover:text-[#0D5C63]">Blogs
                    </RouterLink>
                    <RouterLink to="/gallery" class="font-medium text-[#1B1B1B] hover:text-[#0D5C63]">Gallery
                    </RouterLink>
                    <RouterLink to="/contact-us" class="font-medium text-[#1B1B1B] hover:text-[#0D5C63]">Contact
                    </RouterLink>
                </div>

                <!-- Desktop Button -->
                <div class="hidden lg:flex items-center">
                    <button
                        class="bg-[#0D5C63] text-white text-sm px-5 py-2 rounded-xl font-medium shadow-sm hover:bg-[#084950] transition">
                        <!-- Enquire Now -->Login
                    </button>
                </div>

                <!-- Mobile Menu Button -->
                <!-- <button @click="mobileMenu = !mobileMenu" class="lg:hidden text-red-900 relative">

                    <span class="material-symbols-outlined text-[32px] text-[#0D5C63]">
                        {{ mobileMenu ? 'close' : 'menu' }}
                    </span>

                </button> -->
                <!-- Mobile Menu Button -->
                <button @click="mobileMenu = !mobileMenu" class="lg:hidden relative z-[10000]">
                    <span class="material-symbols-outlined text-[32px] text-[#0D5C63]">
                        {{ mobileMenu ? 'close' : 'menu' }}
                    </span>
                </button>

            </div>

            <!-- Mobile Menu -->
            <div v-if="mobileMenu" class="lg:hidden absolute left-0 top-[70px] w-full bg-white  shadow-lg z-50">

                <div class="flex flex-col p-5 space-y-4 text-[#1B1B1B] font-medium">

                    <RouterLink to="/" @click="mobileMenu = false"
                        class="font-medium text-[#1B1B1B] hover:text-[#0D5C63]">
                        Dwell In Door
                    </RouterLink>


                    <RouterLink to="/about-us" class="font-medium text-[#1B1B1B] hover:text-[#0D5C63]"
                        @click="mobileMenu = false">
                        About Us
                    </RouterLink>
                    <!-- <RouterLink to="/projects" @click="mobileMenu = false">
                        Projects
                    </RouterLink> -->
                    <RouterLink to="/properties" @click="mobileMenu = false"
                        class="flex items-center gap-1 font-medium text-[#1B1B1B] hover:text-[#0D5C63] transition-colors">
                        <span>Properties</span>
                        <span class="material-symbols-outlined text-[18px]">
                            keyboard_arrow_down
                        </span>
                    </RouterLink>
                    <RouterLink to="/services" @click="mobileMenu = false"
                        class="flex items-center gap-1 font-medium text-[#1B1B1B] hover:text-[#0D5C63] transition-colors">
                        <span>Services</span>
                        <span class="material-symbols-outlined text-[18px]">
                            keyboard_arrow_down
                        </span>
                    </RouterLink>





                    <RouterLink to="/blogs" class="font-medium text-[#1B1B1B] hover:text-[#0D5C63]"
                        @click="mobileMenu = false">
                        Blogs
                    </RouterLink>

                    <RouterLink to="/gallery" class="font-medium text-[#1B1B1B] hover:text-[#0D5C63]"
                        @click="mobileMenu = false">
                        Gallery
                    </RouterLink>

                    <RouterLink to="/contact-us" class="font-medium text-[#1B1B1B] hover:text-[#0D5C63]"
                        @click="mobileMenu = false">
                        Contact
                    </RouterLink>

                    <button class="bg-[#0D5C63] text-white py-3 rounded-xl font-medium">
                        Enquire Now
                    </button>

                </div>

            </div>

        </div>
    </nav>
</template>

<script setup>
import { ref } from "vue";
import { RouterLink, useRoute } from "vue-router";
const route = useRoute()

const mobileMenu = ref(false);
const getFileUrl = (file) => {
    return `${window.location.origin}/files/${file}`;
};
</script>