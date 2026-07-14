<template>
    <section class="bg-white mb-10 mt-4 ">
        <div class="max-w-[1400px]  mx-auto px-4">

            <div class="grid grid-cols-1 lg:grid-cols-12 gap-2 ">

                <!-- LEFT SIDE -->
                <!-- <div class="ml-20"> -->
                <div class="lg:col-span-7">
                    <!-- Main Image -->
                    <div class="relative">
                        <img :src="project.image" class="w-full h-[250px] md:h-[400px] object-cover rounded-[5px]" />

                    </div>

                    <!-- gallery -->
                    <!-- <div class=" grid grid-cols-6 gap-3 mt-4"> -->
                    <div class="mt-1 w-full">


                        <Carousel :items-to-show="7" :wrap-around="true" :autoplay="2000" :key="project.project_name"
                            :pause-autoplay-on-hover="true" :breakpoints="{
                                0: {
                                    itemsToShow: 2.8
                                },
                                640: {
                                    itemsToShow: 6.4
                                },
                                1024: {
                                    itemsToShow: 6.4
                                }
                            }">
                            <Slide v-for="(item, index) in project.gallery_images" :key="index">
                                <div class="px-[2px]">
                                    <img :src="item.images" @click="openImage(item.images, index)"
                                        class="w-full h-[80px] md:h-[80px] object-cover rounded-[5px] cursor-pointer" />
                                </div>
                            </Slide>

                            <template #addons>
                                <Navigation />
                            </template>
                        </Carousel>
                    </div>
                </div>


                <!-- RIGHT SIDE -->
                <!-- RIGHT SIDE -->
                <!-- <div class="flex flex-col justify-center h-full bg-white rounded-[24px] px-8 shadow-lg"> -->
                <div class="lg:col-span-5 flex flex-col  h-full bg-white rounded-[24px] px-auto md:px-8  ">

                    <!-- Breadcrumb -->
                    <div class="flex items-center gap-1 text-gray-500 mb-4 text-[16px]">

                        <router-link to="/" class="hover:text-[#0D5C63]">
                            Home
                        </router-link>

                        <span class="material-symbols-outlined text-[16px]">
                            chevron_right
                        </span>

                        <router-link to="/properties" class="hover:text-[#0D5C63]">
                            Properties
                        </router-link>

                        <span class="material-symbols-outlined text-[16px]">
                            chevron_right
                        </span>

                        <span class="text-[#0D5C63] font-medium">
                            {{ project.project_name }}
                        </span>

                    </div>

                    <!-- Premium Badge -->
                    <div class="mb-2">
                        <span
                            class="inline-flex items-center gap-2 bg-[#FFF8E1] text-[#C9A227] px-3 py-1 rounded-full text-sm font-medium border border-[#F3D46B]">

                            <span class="material-symbols-outlined text-[14px]">
                                star
                            </span>

                            Premium Project
                        </span>
                    </div>

                    <!-- Project Name -->
                    <h1 class="text-[22px] lg:text-[22px] font-bold text-[#1B1B1B] leading-tight">
                        <!-- Azure Heights -->{{ project.project_name }}
                    </h1>

                    <!-- Subtitle -->
                    <h3 class="text-[15px] text-gray-600 mt-2">
                        <!-- Luxury 3 & 4 BHK Apartments -->{{ project.varints }}
                    </h3>

                    <!-- Location -->
                    <div class="flex items-center gap-2 mt-2 text-[14px] text-gray-700">
                        <span class="material-symbols-outlined text-[#0D5C63]">
                            location_on
                        </span>
                        {{ project.location }}
                    </div>

                    <!-- Description -->
                    <p class="mt-3 text-gray-600 leading-6 text-[15px]">
                        <!-- Experience elevated living surrounded by greenery and modern amenities.
                        Designed for contemporary families seeking comfort, convenience,
                        and luxury in one destination. -->
                        {{ project.descrption }}
                    </p>

                    <hr class="my-4">

                    <!-- Stats -->
                    <div class="grid grid-cols-2 md:grid-cols-4 gap-5">

                        <!-- Total Area -->
                        <div class="text-center">
                            <div
                                class="w-12 h-12 rounded-full bg-[#F8FAFA] shadow flex items-center justify-center mx-auto">
                                <span class="material-symbols-outlined text-[#0D5C63]">
                                    landscape
                                </span>
                            </div>

                            <h4 class="font-semibold mt-3">
                                <!-- 2.5 Acres -->{{ project.total_area }}
                            </h4>

                            <p class="text-xs text-gray-500">
                                Total Area
                            </p>
                        </div>

                        <!-- Configuration -->
                        <div class="text-center">
                            <div
                                class="w-12 h-12 rounded-full bg-[#F8FAFA] shadow flex items-center justify-center mx-auto">
                                <span class="material-symbols-outlined text-[#0D5C63]">
                                    apartment
                                </span>
                            </div>

                            <h4 class="font-semibold mt-3">
                                <!-- 3 & 4 BHK -->{{ project.configuration }}
                            </h4>

                            <p class="text-xs text-gray-500">
                                Configuration
                            </p>
                        </div>

                        <!-- Floors -->
                        <div class="text-center">
                            <div
                                class="w-12 h-12 rounded-full bg-[#F8FAFA] shadow flex items-center justify-center mx-auto">
                                <span class="material-symbols-outlined text-[#0D5C63]">
                                    business
                                </span>
                            </div>

                            <h4 class="font-semibold mt-3">
                                <!-- G+14 -->{{ project.floors }}
                            </h4>

                            <p class="text-xs text-gray-500">
                                Floors
                            </p>
                        </div>

                        <!-- Possession -->
                        <div class="text-center">
                            <div
                                class="w-12 h-12 rounded-full bg-[#F8FAFA] shadow flex items-center justify-center mx-auto">
                                <span class="material-symbols-outlined text-[#0D5C63]">
                                    calendar_month
                                </span>
                            </div>

                            <h4 class="font-semibold mt-3">
                                <!-- Dec 2026 -->{{ project.possession }}
                            </h4>

                            <p class="text-xs text-gray-500">
                                Possession
                            </p>
                        </div>

                    </div>

                    <!-- Price Card -->
                    <div
                        class="mt-8 border border-gray-200 rounded-[10px] py-2  flex flex-col md:flex-row justify-around items-center gap-2">

                        <div>
                            <p class="text-gray-500 text-sm">
                                Starting From
                            </p>

                            <h2 class="text-[20px] font-bold text-[#0D5C63]">
                                <!-- ₹ 1.25 Cr* -->{{ project.price }}
                            </h2>
                        </div>

                        <button
                            class="bg-[#0D5C63] hover:bg-[#084950] text-white px-6 py-2 text-[14px] rounded-xl font-medium transition">
                            Schedule Visit
                        </button>

                    </div>

                </div>

            </div>

        </div>
        <!-- <div v-if="selectedImage" class="fixed inset-0 bg-black/90 z-[9999] flex items-center justify-center"
            @click="closeImage">
            <img :src="selectedImage" class="max-w-[90%] max-h-[90vh] object-contain" @click.stop />

            <button @click="closeImage"
                class="absolute top-5 right-5 w-10 h-10 bg-white rounded-full flex items-center justify-center shadow-lg">
                <span class="material-symbols-outlined text-black">
                    close
                </span>
            </button>
        </div> -->
        <div v-if="selectedImage" class="fixed inset-0 bg-black/90 z-[9999] flex items-center justify-center"
            @click="closeImage">
            <img :src="selectedImage" class="max-w-[90%] max-h-[90vh] object-contain" @click.stop />

            <!-- Close -->
            <button @click.stop="closeImage"
                class="absolute top-5 right-5 w-10 h-10 bg-white rounded-full flex items-center justify-center shadow-lg">
                <span class="material-symbols-outlined">close</span>
            </button>

            <!-- Previous -->
            <button @click.stop="prevImage"
                class="absolute left-4 md:left-10 top-1/2 -translate-y-1/2 w-12 h-12 bg-white rounded-full flex items-center justify-center shadow-lg">
                <span class="material-symbols-outlined">chevron_left</span>
            </button>

            <!-- Next -->
            <button @click.stop="nextImage"
                class="absolute right-4 md:right-10 top-1/2 -translate-y-1/2 w-12 h-12 bg-white rounded-full flex items-center justify-center shadow-lg">
                <span class="material-symbols-outlined">chevron_right</span>
            </button>
        </div>
    </section>
    <!--------------Next SEction -2--------------->
    <section class="py-2 bg-white mx-auto md:mx-10">
        <div class="max-w-[1400px] mx-auto px-4">

            <div class="grid lg:grid-cols-12 gap-10">

                <!-- LEFT -->
                <div class="lg:col-span-4">

                    <h2 class="text-[22px] font-bold ">
                        Project Overview
                    </h2>
                    <div class="w-16 h-[2px] bg-[#D4AF37] mb-4  rounded-full"></div>

                    <p class="text-gray-600 text-[14px] leading-6">
                        {{
                            showFullDescription
                                ? project.long__descrption
                                : project.long__descrption?.slice(0, 150) + "..."
                        }}
                    </p>

                    <button v-if="project.long__descrption?.length > 150"
                        @click="showFullDescription = !showFullDescription" class="text-[#0D5C63] font-medium mt-2">
                        {{ showFullDescription ? "Read Less" : "Read More" }}
                    </button>

                    <div class="mt-4 space-y-2">

                        <!-- <div class="flex justify-between border-b pb-3">
                            <span class="font-medium text-[14px]">RERA Approved</span>
                            <span class="text-gray-600 text-[14px]">
                                PRM/KA/RERA/1251/446
                            </span>
                        </div> -->

                        <div class="flex justify-between border-b pb-3">
                            <span class="font-medium text-[14px] ">Land Area</span>
                            <span class="text-gray-600 text-[14px] ">
                                {{ project.total_area }}
                            </span>
                        </div>

                        <div class="flex justify-between border-b pb-3">
                            <span class="font-medium text-[14px] ">Configuration</span>
                            <span class="text-gray-600 text-[14px] ">
                                {{ project.configuration }}
                            </span>
                        </div>

                        <div class="flex justify-between border-b pb-3">
                            <span class="font-medium text-[14px] ">Floors</span>
                            <span class="text-gray-600 text-[14px] ">
                                {{ project.floors }}
                            </span>
                        </div>

                        <div class="flex justify-between border-b pb-3">
                            <span class="font-medium text-[14px] ">Possession</span>
                            <span class="text-gray-600 text-[14px] ">
                                {{ project.possession }}
                            </span>
                        </div>

                    </div>

                    <button v-if="project.brochure" @click="downloadBrochure"
                        class="mt-4 bg-[#0D5C63] text-white px-4 py-2 rounded-xl font-medium flex items-center gap-2">
                        Download Brochure
                        <span class="material-symbols-outlined">download</span>
                    </button>

                </div>

                <!-- RIGHT -->
                <div class="lg:col-span-8 ">
                    <div class="text-center mb-4">
                        <h2 class="text-[22px] font-bold text-[#1B1B1B]">
                            Project Highlights
                        </h2>

                        <div class="w-16 h-[2px] bg-[#D4AF37] mx-auto  rounded-full"></div>
                    </div>


                    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 items-start ">

                        <div v-for="(item, index) in project.project_highlights" :key="index"
                            class="border border-gray-200 rounded-xl p-3 flex items-start gap-3 bg-white h-[95px]">

                            <div
                                class="w-10 h-10 rounded-lg shadow-[30px] bg-[#F4F8F8] flex items-center justify-center flex-shrink-0">

                                <span class="material-symbols-outlined text-[#0D5C63] text-[18px]">
                                    {{ item.icon }}
                                </span>

                            </div>

                            <div>
                                <h3 class="font-semibold text-[14px] leading-4">
                                    {{ item.highlight_title }}
                                </h3>

                                <!-- <p class="text-gray-500 text-[12px] mt-1 leading-4 line-clamp-2">
                                    {{ item.project_descrption_high }}
                                </p> -->
                                <p class="text-gray-500 text-[12px] mt-1 leading-4 h-8 overflow-hidden">
                                    {{ item.project_descrption_high }}
                                </p>
                            </div>

                        </div>

                    </div>

                </div>

            </div>

        </div>
    </section>


    <!-----Section-3----->
    <section class="py-8 bg-white mx-auto md:mx-10 ">
        <div class="max-w-[1400px] mx-auto px-4">

            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 lg:gap-10">

                <!-- LEFT SIDE -->


                <div class="lg:col-span-5">

                    <div class="flex items-center justify-between">
                        <h2 class="text-[22px] font-bold">
                            Price & Configuration
                        </h2>
                    </div>

                    <div class="w-16 h-[2px] bg-[#D4AF37] mb-4 rounded-full"></div>

                    <div class="border border-gray-200 rounded-2xl overflow-x-auto">

                        <table class="w-full">

                            <thead class="bg-[#F8FAFA]">
                                <tr>
                                    <th class="p-3 md:p-4 text-left">Type</th>
                                    <th class="p-3 md:p-4 text-left">Area</th>
                                    <th class="p-3 md:p-4 text-left">Price</th>
                                    <th class="p-3 md:p-4 text-center">Action</th>
                                </tr>
                            </thead>

                            <tbody>

                                <tr v-for="(item, index) in project.property_configuartion" :key="index"
                                    class="border-t">
                                    <td class="p-3 md:px-6 md:py-4 font-medium">
                                        {{ item.bhktype }}
                                    </td>

                                    <td class="p-3 md:px-6 md:py-4">
                                        {{ item.area }}
                                    </td>

                                    <td class="p-3 md:px-6 md:py-4 font-semibold">
                                        ₹ {{ item.price }}
                                    </td>

                                    <td class="p-3 md:px-6 md:py-4 text-center">
                                        <button class="bg-[#0D5C63] text-white px-3 md:px-4 py-2 rounded-lg text-sm">
                                            Enquire
                                        </button>
                                    </td>
                                </tr>

                                <tr
                                    v-if="!project.property_configuartion || project.property_configuartion.length === 0">
                                    <td colspan="4" class="text-center py-6 text-gray-500">
                                        No Configuration Available
                                    </td>
                                </tr>

                            </tbody>

                        </table>

                    </div>

                </div>



                <div class="lg:col-span-7">

                    <div class="text-center mb-6">
                        <h2 class="text-[22px] font-bold text-[#1B1B1B]">
                            Top Amenities
                        </h2>

                        <div class="w-16 h-[2px] bg-[#D4AF37] mx-auto rounded-full"></div>
                    </div>

                    <div class="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-5">

                        <div v-for="(item, index) in project.property_amenities" :key="index" class="text-center">
                            <div
                                class="w-16 h-16 md:w-20 md:h-20 mx-auto border border-gray-200 rounded-xl flex items-center justify-center">
                                <span class="material-symbols-outlined text-[#0D5C63] text-[24px] md:text-[32px]">
                                    {{ item.amenity_icon }}
                                </span>
                            </div>

                            <p class="text-xs md:text-sm mt-2">
                                {{ item.amenity_name }}
                            </p>
                        </div>

                    </div>

                </div>

            </div>

        </div>
    </section>


    <!--Next section-4-->
    <section class="mb-10 md:mx-10 bg-white">
        <div class="max-w-[1400px] mx-auto px-4">

            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-stretch">

                <!-- Floor Plan Slider -->
                <div class="lg:col-span-7 h-[400px]">

                    <div class="border border-gray-200 rounded-2xl overflow-hidden bg-white h-full flex flex-col">

                        <div class="text-center py-3">
                            <h2 class="text-[22px] font-bold text-[#1B1B1B]">
                                Floor Plans
                            </h2>
                            <div class="w-16 h-[2px] bg-[#D4AF37] mx-auto mt-2 rounded-full"></div>
                        </div>

                        <div class="flex-1">
                            <Carousel :items-to-show="1" :wrap-around="true" :autoplay="1000"
                                :key="project.project_name" :pause-autoplay-on-hover="true">

                                <Slide v-for="(item, index) in project.floor_plan" :key="index">
                                    <img :src="item.images" alt="Floor Plan"
                                        class="w-full h-[300px] md:h-[400px] object-cover bg-white" />
                                </Slide>

                                <template #addons>
                                    <Navigation />
                                </template>

                            </Carousel>
                        </div>

                    </div>

                </div>

                <!-- Enquiry Form -->
                <div class="lg:col-span-5 h-full md:h-[400px]">

                    <div class="border border-gray-200 rounded-[10px] p-6 shadow-2xl h-full flex flex-col">

                        <h2 class="text-[22px] font-bold mb-3 text-[#1B1B1B]">
                            Interested in this project?
                        </h2>

                        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">

                            <input type="text" placeholder="Full Name"
                                class="border border-gray-300 rounded-lg px-4 py-2 outline-none focus:border-[#0D5C63]" />

                            <input type="text" placeholder="Phone Number"
                                class="border border-gray-300 rounded-lg px-4 py-2 outline-none focus:border-[#0D5C63]" />

                            <input type="email" placeholder="Email Address"
                                class="border border-gray-300 rounded-lg px-4 py-2 outline-none focus:border-[#0D5C63]" />

                            <input type="date" :value="new Date().toISOString().split('T')[0]"
                                class="border border-gray-300 rounded-lg px-4 py-2 outline-none focus:border-[#0D5C63]" />

                        </div>

                        <!-- <textarea rows="6" placeholder="Your Message"
                            class="w-full border border-gray-300 rounded-lg px-4 py-2 mt-4 outline-none resize-none focus:border-[#0D5C63]"></textarea> -->
                        <textarea placeholder="Your Message"
                            class="w-full h-[100px] md:h-[150px] border border-gray-300 rounded-lg px-4 py-2 mt-4 outline-none resize-none focus:border-[#0D5C63]"></textarea>
                        <div class="mt-auto">
                            <button
                                class="w-full mt-4 bg-gradient-to-r from-[#0D5C63] to-[#1D3B2A] text-white py-2 rounded-lg font-medium hover:opacity-90 transition">
                                Send Enquiry
                            </button>
                        </div>

                    </div>

                </div>

            </div>

        </div>
    </section>
    <!--Propety simailar cards bro-->
    <SimilarCradsIndetaiPage :properties="similarProjects" />


    <!--Next section-5-->
    <section class="my-10 bg-white "
        v-if="project.property_loaction_detail_descr?.length && project.property_location_details?.length && project.property_loaction_link?.length">
        <div class="max-w-[1400px] mx-auto px-4">

            <div class="max-w-5xl mx-auto">

                <div class="grid grid-cols-1 md:grid-cols-2 overflow-hidden rounded-2xl shadow-lg ">

                    <!-- Left Content -->
                    <div
                        class="bg-gradient-to-r from-[#0D5C63] to-[#1D3B2A] text-white p-6 md:p-8 flex flex-col justify-start">

                        <h2 class="text-[24px] md:text-[28px] font-bold mb-6">
                            Prime Location
                        </h2>

                        <p class="text-[14px] md:text-[15px] leading-6 md:leading-7 text-gray-100 mb-8">

                            {{ project.property_loaction_detail_descr }}
                        </p>

                        <div class="space-y-4 md:space-y-5">

                            <div class="flex items-center justify-between text-[14px] md:text-[15px]"
                                v-for="(item, index) in project.property_location_details" :key="index">
                                <div class="flex items-center gap-3">
                                    <span class="material-symbols-outlined text-[18px]">
                                        location_on
                                    </span>
                                    <!-- <span>ITPL, Whitefield</span> -->
                                    <span>{{ item.location_name }}</span>
                                </div>
                                <span>{{ item.distance }}</span>
                            </div>



                        </div>

                    </div>

                    <!-- Right Side Map -->
                    <div class="h-[300px] md:h-full">


                        <iframe :src="project.property_loaction_link" class="w-full h-full" loading="lazy">
                        </iframe>


                    </div>

                </div>

            </div>

        </div>
    </section>


</template>

<script setup>
import axios from "axios";
import { onMounted, provide, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import { Carousel, Slide, Navigation } from "vue3-carousel";
import "vue3-carousel/dist/carousel.css";
import SimilarCradsIndetaiPage from "./SimilarCradsIndetaiPage.vue";
import { watch } from "vue";
const router = useRouter()


const showFullDescription = ref(false);
const route = useRoute();

const project = ref({});
const selectedImage = ref(null);
const currentIndex = ref(0)

// const openImage = (image) => {
//     selectedImage.value = image;
// };
const openImage = (image, index) => {
    selectedImage.value = image
    currentIndex.value = index
}

const closeImage = () => {
    selectedImage.value = null;
};
const nextImage = () => {
    currentIndex.value =
        (currentIndex.value + 1) % project.value.gallery_images.length

    selectedImage.value =
        project.value.gallery_images[currentIndex.value].images
}
const prevImage = () => {
    currentIndex.value =
        (currentIndex.value - 1 + project.value.gallery_images.length) %
        project.value.gallery_images.length

    selectedImage.value =
        project.value.gallery_images[currentIndex.value].images
}

const getFileUrl = (file) => {
    return `${window.location.origin}/files/${file}`;
};



const downloadBrochure = () => {
    if (project.value?.brochure) {
        const link = document.createElement("a");
        link.href = window.location.origin + project.value.brochure;
        link.download = "";
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }
};
const getProjectDetails = async () => {
    try {
        const response = await axios.get(
            "/api/method/dwell_in_door.api.propertdetail.get_property_details",

            {
                params: {
                    url: route.params.url,
                },
            }
        );

        project.value = response.data.message || {};
        await getSimilarProjects()
        console.log("URL Param:", route.params.url);
        console.log(project.gallery_images);
        console.log(project.value.brochure);
        console.log(project.value.property_configuartion);
        console.log(project.value.property_location_type);




    } catch (error) {
        console.log(error);
    }
};

const similarProjects = ref([])

const getSimilarProjects = async () => {
    try {

        const response = await axios.get(
            "/api/method/dwell_in_door.api.propertdetail.get_similar_projects",
            {
                params: {
                    location_type: project.value.property_location_type,
                    current_project: project.value.project_name
                }
            }
        )

        similarProjects.value = response.data.message


        console.log(similarProjects.value)

    } catch (error) {
        console.log(error)
    }
}

// const showAll = ref(false);

// const displayedImages = computed(() => {
//     if (showAll.value) {
//         return project.value.gallery_images || [];
//     }
//     return (project.value.gallery_images || []).slice(0, 6);
// });

onMounted(() => {
    getProjectDetails();

});



watch(
    () => route.params.url,
    () => {
        getProjectDetails();
    }
);
</script>

<style>
.carousel__prev,
.carousel__next {
    background: white !important;
    /* width: 40px !important;
    height: 40px !important; */
    border-radius: 9999px !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, .15);
    color: black !important;
}
</style>