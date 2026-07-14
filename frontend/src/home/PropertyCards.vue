<template>
    <section class="py-2 md:py-6 lg:mx-20 px-4 lg:px-0 bg-white">
        <div class="max-w-[1400px] mx-auto px-4">

            <!-- Heading -->
            <div class="text-center mb-7">
                <div class="flex justify-center items-center gap-2 mb-3">
                    <div class="w-3 h-3 bg-[#35CAA0] rounded-sm"></div>

                    <span class="text-gray-500 font-medium text-sm">
                        Properties
                    </span>
                </div>

                <h2 class="text-3xl md:text-[32px] font-semibold text-[#1F2937]">
                    Discover inspiring designed homes.
                </h2>

                <p class="text-gray-500 mt-1 text-[12px]">
                    Curated homes where elegance, style, and comfort unite.
                </p>
            </div>


            <Carousel :items-to-show="3" :wrap-around="true" :autoplay="3000" class="pb-8" snapAlign="start"
                :breakpoints="{
                    0: {
                        itemsToShow: 1
                    },
                    640: {
                        itemsToShow: 2
                    },
                    1024: {
                        itemsToShow: 3.6
                    },
                    1280: {
                        itemsToShow: 3.4
                    }
                }">

                <Slide v-for="item in propertydetils" @click="router.push(`/properties/${item.url}`)" :key="item.name">

                    <div class="px-3 pb-4">

                        <div class="rounded-[16px] shadow-lg bg-white overflow-hidden cursor-pointer min-h-[370px]">

                            <!-- Image -->
                            <img :src="item.image" alt="" class="w-full h-[190px] object-cover">

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

                                    <span
                                        class="bg-[#07BE8A1A]/10 text-[#07BE8A] px-3 py-1 rounded-full text-xs whitespace-nowrap">
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

                <template #addons>
                    <Navigation />
                </template>

            </Carousel>
        </div>
    </section>
</template>
<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { Carousel, Slide, Navigation } from "vue3-carousel";
import "vue3-carousel/dist/carousel.css";


const router = useRouter()
const propertydetils = ref([])
const get_all_property_detils = async () => {
    try {

        const response = axios.get("api/method/dwell_in_door.api.propertdetail.get_property_detils_for_cards")

        propertydetils.value = (await response).data.message
    }
    catch (error) {
        console.log(error);

    }

}
onMounted(() => {
    get_all_property_detils()
})

</script>
<style>
.carousel__viewport {
    overflow: hidden !important;
}
</style>