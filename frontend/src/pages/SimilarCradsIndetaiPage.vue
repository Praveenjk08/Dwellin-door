<template>
    <section class="my-10 px-4 md:px-10" v-if="properties && properties.length > 0">
        <div class="max-w-[1400px] mx-auto px-4">

            <!-- Heading -->
            <div class="flex items-center justify-between mb-8">

                <div>
                    <h2 class="text-[28px] font-bold text-[#1B1B1B]">
                        Similar Properties
                    </h2>

                    <div class="w-16 h-[2px] bg-[#D4AF37] mt-2 rounded-full"></div>
                </div>

               <button
    class="hidden md:flex items-center gap-2 text-[#0D5C63] font-semibold"
    @click="router.push({
        path: '/properties',
        query: {
            location_type: properties[0]?.property_location_type
        }
    })"
>
    View All

    <span class="material-symbols-outlined text-[18px]">
        arrow_forward
    </span>
</button>

            </div>

          <Carousel
    :items-to-show="5"
    :wrap-around="showNavigation"
    :autoplay="showNavigation ? 3000 : 0"
    class="pb-8"
    snapAlign="start"
    :breakpoints="{
        0: {
            itemsToShow: 1
        },
        640: {
            itemsToShow: 2
        },
        1024: {
            itemsToShow: 3
        },
        1280: {
            itemsToShow: 4.2
        }
    }"
>

    <Slide
        v-for="item in properties"
        :key="item.url"
        @click="router.push(`/properties/${item.url}`)"
    >

        <div class="px-3 pb-4">

            <div class="rounded-[16px] shadow-lg bg-white overflow-hidden cursor-pointer min-h-[370px]">

                <!-- Image -->
                <img
                    :src="item.image"
                    alt=""
                    class="w-full h-[190px] object-cover"
                >

                <!-- Content -->
                <div class="p-4">

                    <div class="flex justify-between items-start gap-2">

                        <div>
                            <h3 class="text-lg font-semibold text-gray-800 line-clamp-1">
                                {{ item.project_name }}
                            </h3>

                            <p class="text-sm text-gray-500 mt-1 line-clamp-1">
                                {{ item.location }}
                            </p>
                        </div>

                        <span class="bg-[#07BE8A1A]/10 text-[#07BE8A] px-3 py-1 rounded-full text-xs whitespace-nowrap">
                            ₹{{ item.price }}
                        </span>

                    </div>

                    <!-- Features -->
                    <div class="grid grid-cols-3 pt-4 mt-4 border-t border-gray-200">

                        <div class="text-center">
                            <span class="material-symbols-outlined text-gray-600">
                                bed
                            </span>

                            <p class="text-xs mt-1">
                                {{ item.bedrooms }}
                            </p>
                        </div>

                        <div class="text-center border-x border-gray-200">
                            <span class="material-symbols-outlined text-gray-600">
                                bathtub
                            </span>

                            <p class="text-xs mt-1">
                                {{ item.bathrooms }}
                            </p>
                        </div>

                        <div class="text-center">
                            <span class="material-symbols-outlined text-gray-600">
                                open_with
                            </span>

                            <p class="text-xs mt-1">
                                {{ item.area }}
                            </p>
                        </div>

                    </div>

                </div>

            </div>

        </div>

    </Slide>

    <template v-if="showNavigation" #addons>
    <Navigation />
</template>

</Carousel>
        </div>
    </section>
</template>

<script setup>
import { computed } from "vue";
import { Carousel, Slide, Navigation } from "vue3-carousel";
import "vue3-carousel/dist/carousel.css";
import router from "../router";

const props = defineProps({
    properties: {
        type: Array,
        default: () => []
    }
});

const showNavigation = computed(() => {
    if (window.innerWidth < 768) {
        return props.properties.length > 1; // Mobile
    }
    return props.properties.length > 4; // Desktop
});
</script>

<style>
.carousel__viewport {
    overflow: hidden !important;
}
</style>