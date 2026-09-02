<template>
    <section
        class="my-5 px-4 md:px-10"
        v-if="properties && properties.length > 0"
    >
        <div class="max-w-[1400px] mx-auto px-4">

            <!-- Heading -->
            <div class="flex items-center justify-between mb-8">

                <div>
                    <h2 class="text-[18px] md:text-[22px] font-bold text-[#1B1B1B]">
                        Similar Properties
                    </h2>

                    <div class="w-16 h-[2px] bg-[#D4AF37] mt-2 rounded-full"></div>
                </div>

                <!-- View All -->
                <button
                    v-if="properties[0]?.property_location_type"
                    class="flex items-center gap-2 text-[#0D5C63] font-semibold hover:text-[#084950] transition"
                    @click="viewAll"
                >
                    View All

                    <span class="material-symbols-outlined text-[14px] md:text-[18px] font-light">
                        arrow_forward
                    </span>
                </button>

            </div>

            <!-- Carousel -->
            <Carousel
                :items-to-show="1"
                :wrap-around="showNavigation"
                :autoplay="showNavigation ? 3000 : 0"
                :pause-autoplay-on-hover="true"
                class="pb-8"
                snap-align="start"
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

                <!-- Property Cards -->
                <Slide
                    v-for="(item, index) in properties"
                    :key="item.url || item.project_name || index"
                >

                    <div class="px-3 pb-4 w-full">

                        <div
                            class="rounded-[16px] shadow-lg bg-white overflow-hidden cursor-pointer min-h-[370px] hover:shadow-xl transition-shadow duration-300"
                            @click="openProperty(item)"
                        >

                            <!-- Image -->
                            <img
                                :src="item.image"
                                :alt="item.project_name || 'Property'"
                                class="w-full h-[190px] object-cover"
                                @error="handleImageError"
                            />

                            <!-- Content -->
                            <div class="p-4">

                                <!-- Name + Price -->
                                <div class="flex justify-between items-start gap-2">

                                    <div class="min-w-0">

                                        <h3
                                            class="text-lg font-semibold text-gray-800 line-clamp-1"
                                        >
                                            {{ item.project_name }}
                                        </h3>

                                        <p
                                            class="text-sm text-gray-500 mt-1 line-clamp-1"
                                        >
                                            {{ item.location }}
                                        </p>

                                    </div>

                                    <!-- Price -->
                                    <span
                                        v-if="item.price"
                                        class="bg-[#07BE8A1A] text-[#07BE8A] px-3 py-1 rounded-full text-xs whitespace-nowrap"
                                    >
                                        {{ item.price }}
                                    </span>

                                </div>

                                <!-- Features -->
                                <div
                                    class="grid grid-cols-3 pt-4 mt-4 border-t border-gray-200"
                                >

                                    <!-- Bedrooms -->
                                    <div class="text-center">

                                        <span class="material-symbols-outlined text-gray-600">
                                            bed
                                        </span>

                                        <p class="text-xs mt-1">
                                            {{ item.bedrooms || "-" }}
                                        </p>

                                    </div>

                                    <!-- Bathrooms -->
                                    <div
                                        class="text-center border-x border-gray-200"
                                    >

                                        <span class="material-symbols-outlined text-gray-600">
                                            bathtub
                                        </span>

                                        <p class="text-xs mt-1">
                                            {{ item.bathrooms || "-" }}
                                        </p>

                                    </div>

                                    <!-- Area -->
                                    <div class="text-center">

                                        <span class="material-symbols-outlined text-gray-600">
                                            open_with
                                        </span>

                                        <p class="text-xs mt-1">
                                            {{ item.area || "-" }}
                                        </p>

                                    </div>

                                </div>

                            </div>

                        </div>

                    </div>

                </Slide>

                <!-- Navigation -->
                <template v-if="showNavigation" #addons>
                    <Navigation />
                </template>

            </Carousel>

        </div>
    </section>
</template>


<script setup>
import { computed, onMounted, onBeforeUnmount, ref } from "vue";
import { Carousel, Slide, Navigation } from "vue3-carousel";
import "vue3-carousel/dist/carousel.css";
import router from "../router";


const props = defineProps({
    properties: {
        type: Array,
        default: () => []
    }
});


/*
|--------------------------------------------------------------------------
| Screen Width
|--------------------------------------------------------------------------
*/

const screenWidth = ref(
    typeof window !== "undefined"
        ? window.innerWidth
        : 1280
);


const updateScreenWidth = () => {
    screenWidth.value = window.innerWidth;
};


/*
|--------------------------------------------------------------------------
| Navigation
|--------------------------------------------------------------------------
|
| Mobile  : Show navigation if more than 1 property
| Tablet  : Show navigation if more than 2 properties
| Desktop : Show navigation if more than 4 properties
|
*/

const showNavigation = computed(() => {

    if (screenWidth.value < 640) {
        return props.properties.length > 1;
    }

    if (screenWidth.value < 1024) {
        return props.properties.length > 2;
    }

    return props.properties.length > 4;
});


/*
|--------------------------------------------------------------------------
| Open Property Detail
|--------------------------------------------------------------------------
*/

const openProperty = (item) => {

    if (!item?.url) {
        console.warn("Property URL is missing:", item);
        return;
    }

    router.push(`/properties/${item.url}`);
};


/*
|--------------------------------------------------------------------------
| View All
|--------------------------------------------------------------------------
*/

const viewAll = () => {

    const locationType =
        props.properties?.[0]?.property_location_type;

    if (!locationType) {
        router.push("/properties");
        return;
    }

    router.push({
        path: "/properties",
        query: {
            location_type: locationType
        }
    });
};


/*
|--------------------------------------------------------------------------
| Image Error
|--------------------------------------------------------------------------
*/

const handleImageError = (event) => {

    event.target.src =
        "/files/logo-with-some-changes.png";
};


/*
|--------------------------------------------------------------------------
| Lifecycle
|--------------------------------------------------------------------------
*/

onMounted(() => {
    window.addEventListener("resize", updateScreenWidth);
});


onBeforeUnmount(() => {
    window.removeEventListener("resize", updateScreenWidth);
});
</script>


<style>
.carousel__viewport {
    overflow: hidden !important;
}

.carousel__prev,
.carousel__next {
    background: white !important;
    border-radius: 9999px !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    color: black !important;
}
</style>