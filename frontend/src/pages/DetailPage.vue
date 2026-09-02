<template>
    <section class="bg-white mb-10 mt-4">
        <div class="max-w-[1400px] mx-auto px-4">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-2">

                <!-- LEFT SIDE -->
                <div class="lg:col-span-7">

                    <!-- Main Image -->
                    <div class="relative">
                        <Carousel
                            :items-to-show="1"
                            :wrap-around="true"
                            :autoplay="5000"
                            :pause-autoplay-on-hover="true"
                        >
                            <!-- Main Project Image -->
                            <Slide v-if="project.image">
                                <img
                                    :src="project.image"
                                    :alt="project.project_name || 'Property'"
                                    class="w-full h-[250px] md:h-[400px] object-cover rounded-[5px]"
                                />
                            </Slide>

                            <!-- Gallery / Cursor Images -->
                            <Slide
                                v-for="(item, index) in project.cursol_project_images || []"
                                :key="index"
                            >
                                <img
                                    :src="item.cusrol_images"
                                    :alt="project.project_name || 'Property'"
                                    class="w-full h-[250px] md:h-[400px] object-cover rounded-[5px]"
                                />
                            </Slide>

                            <template #addons>
                                <Navigation />
                                <Pagination />
                            </template>
                        </Carousel>
                    </div>

                    <!-- Gallery -->
                    <div
                        class="mt-1 w-full"
                        v-if="project.gallery_images?.length"
                    >
                        <Carousel
                            :items-to-show="7"
                            :wrap-around="true"
                            :autoplay="2000"
                            :key="project.project_name"
                            :pause-autoplay-on-hover="true"
                            :breakpoints="{
                                0: {
                                    itemsToShow: 2.8
                                },
                                640: {
                                    itemsToShow: 6.4
                                },
                                1024: {
                                    itemsToShow: 6.4
                                }
                            }"
                        >
                            <Slide
                                v-for="(item, index) in project.gallery_images"
                                :key="index"
                            >
                                <div class="px-[2px]">
                                    <img
                                        :src="item.images"
                                        :alt="project.project_name || 'Property'"
                                        @click="openImage(item.images, index)"
                                        class="w-full h-[80px] md:h-[80px] object-cover rounded-[5px] cursor-pointer"
                                    />
                                </div>
                            </Slide>

                            <template #addons>
                                <Navigation />
                            </template>
                        </Carousel>
                    </div>
                </div>

                <!-- RIGHT SIDE -->
                <div
                    class="lg:col-span-5 flex flex-col h-full bg-white rounded-[24px] px-auto md:px-8"
                >

                    <!-- Breadcrumb -->
                    <div class="flex items-center gap-1 text-gray-500 mb-4 text-[16px]">
                        <router-link
                            to="/"
                            class="hover:text-[#0D5C63]"
                        >
                            Home
                        </router-link>

                        <span class="material-symbols-outlined text-[16px]">
                            chevron_right
                        </span>

                        <router-link
                            to="/properties"
                            class="hover:text-[#0D5C63]"
                        >
                            Properties
                        </router-link>

                        <span class="material-symbols-outlined text-[16px]">
                            chevron_right
                        </span>

                        <span class="text-[#0D5C63] font-medium">
                            {{ project.project_name }}
                        </span>
                    </div>

                    <!-- Premium Badge-->
                    <div class="mb-2">
                        <span
                            class="inline-flex items-center gap-2 bg-[#FFF8E1] text-[#C9A227] px-3 py-1 rounded-full text-sm font-medium border border-[#F3D46B]"
                        >
                            <span class="material-symbols-outlined text-[14px]">
                                star
                            </span>

                            Premium Project
                        </span>
                    </div> 

                    <!-- Project Name -->
                    <h1
                        class="text-[22px] lg:text-[22px] font-bold text-[#1B1B1B] leading-tight"
                    >
                        {{ project.project_name }}
                    </h1>
                    

                    <!-- Subtitle 
                    <h3 class="text-[15px] text-gray-600 mt-2">
                        {{ project.varints }}
                    </h3>-->

                    <!-- Location -->
                    <div class="flex items-center gap-2 mt-2 text-[14px] text-gray-700">
                        <span class="material-symbols-outlined text-[#0D5C63]">
                            location_on
                        </span>

                        {{ project.location }}
                    </div>

                    <!-- Description -->
                    <div
                        class="mt-3 text-gray-600 leading-6 text-[15px]"
                        v-html="project.descrption"
                    ></div>

                    <hr class="my-4" />

                    <!-- Stats -->
                    <div class="grid grid-cols-2 md:grid-cols-4 gap-5">

                        <!-- Total Area -->
                        <div class="text-center">
                            <div
                                class="w-12 h-12 rounded-full bg-[#F8FAFA] shadow flex items-center justify-center mx-auto"
                            >
                                <span class="material-symbols-outlined text-[#0D5C63]">
                                    landscape
                                </span>
                            </div>

                            <h4 class="font-semibold mt-3">
                                {{ project.total_area }}
                            </h4>

                            <p class="text-xs text-gray-500">
                                Total Area
                            </p>
                        </div>

                        <!-- Configuration -->
                        <div class="text-center">
                            <div
                                class="w-12 h-12 rounded-full bg-[#F8FAFA] shadow flex items-center justify-center mx-auto"
                            >
                                <span class="material-symbols-outlined text-[#0D5C63]">
                                    apartment
                                </span>
                            </div>

                            <h4 class="font-semibold mt-3">
                                {{ project.configuration }}
                            </h4>

                            <p class="text-xs text-gray-500">
                                Configuration
                            </p>
                        </div>

                        <!-- Floors -->
                        <div class="text-center">
                            <div
                                class="w-12 h-12 rounded-full bg-[#F8FAFA] shadow flex items-center justify-center mx-auto"
                            >
                                <span class="material-symbols-outlined text-[#0D5C63]">
                                    business
                                </span>
                            </div>

                            <h4 class="font-semibold mt-3">
                                {{ project.floors }}
                            </h4>

                            <p class="text-xs text-gray-500">
                                Floors
                            </p>
                        </div>

                        <!-- Possession -->
                        <div class="text-center">
                            <div
                                class="w-12 h-12 rounded-full bg-[#F8FAFA] shadow flex items-center justify-center mx-auto"
                            >
                                <span class="material-symbols-outlined text-[#0D5C63]">
                                    calendar_month
                                </span>
                            </div>

                            <h4 class="font-semibold mt-3">
                                {{ project.possession }}
                            </h4>

                            <p class="text-xs text-gray-500">
                                Possession
                            </p>
                        </div>
                    </div>

                    <!-- Price Card -->
                    <div
                        class="mt-8 border border-gray-200 rounded-[10px] py-2 flex flex-col md:flex-row justify-around items-center gap-2"
                    >
                        <div>
                            <p class="text-gray-500 text-sm">
                                Starting From
                            </p>

                            <h2 class="text-[20px] font-bold text-[#0D5C63]">
                                {{ project.price }}
                            </h2>
                        </div>

                        <button
                            @click="openVisitModal"
                            class="bg-[#0D5C63] hover:bg-[#084950] text-white px-6 py-2 text-[14px] rounded-xl font-medium transition"
                        >
                            Schedule Video Visit
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Image Preview Modal -->
        <div
            v-if="selectedImage"
            class="fixed inset-0 bg-black/90 z-[9999] flex items-center justify-center"
            @click="closeImage"
        >
            <img
                :src="selectedImage"
                :alt="project.project_name || 'Property'"
                class="max-w-[90%] max-h-[90vh] object-contain"
                @click.stop
            />

            <!-- Close -->
            <button
                @click.stop="closeImage"
                class="absolute top-5 right-5 w-10 h-10 bg-white rounded-full flex items-center justify-center shadow-lg"
            >
                <span class="material-symbols-outlined">
                    close
                </span>
            </button>

            <!-- Previous -->
            <button
                @click.stop="prevImage"
                class="absolute left-4 md:left-10 top-1/2 -translate-y-1/2 w-12 h-12 bg-white rounded-full flex items-center justify-center shadow-lg"
            >
                <span class="material-symbols-outlined">
                    chevron_left
                </span>
            </button>

            <!-- Next -->
            <button
                @click.stop="nextImage"
                class="absolute right-4 md:right-10 top-1/2 -translate-y-1/2 w-12 h-12 bg-white rounded-full flex items-center justify-center shadow-lg"
            >
                <span class="material-symbols-outlined">
                    chevron_right
                </span>
            </button>
        </div>

        <!-- Schedule Visit Modal -->
        <div
            v-if="visiteButton"
            @click="visiteButton = false"
            class="fixed inset-0 bg-black/60 backdrop-blur-sm z-[9999] flex items-center justify-center p-3 md:p-4"
        >
            <div
                @click.stop
                class="bg-white rounded-2xl w-full max-w-2xl shadow-2xl overflow-hidden max-h-[90vh] overflow-y-auto md:max-h-none"
            >

                <!-- Header -->
                <div
                    class="bg-gradient-to-r from-[#0D5C63] to-[#084950] px-6 py-3 text-white"
                >
                    <div class="flex items-center justify-between">
                        <div>
                            <h2 class="text-2xl font-bold">
                                Schedule Your Virtual Tour
                            </h2>

                            <p class="text-sm text-white/80">
                                Connect with our property expert through a video call.
                            </p>
                        </div>

                        <button
                            @click="visiteButton = false"
                            class="w-10 h-10 rounded-full bg-white/10 hover:bg-white/20 flex items-center justify-center transition"
                        >
                            <span class="material-symbols-outlined">
                                close
                            </span>
                        </button>
                    </div>
                </div>

                <!-- Form -->
                <div class="p-4">

                    <div class="grid md:grid-cols-2 gap-4">

                        <!-- Full Name -->
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-2">
                                Full Name
                            </label>

                            <div class="relative">
                                <span
                                    class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-gray-400"
                                >
                                    person
                                </span>

                                <input
                                    v-model="form.first_name"
                                    type="text"
                                    placeholder="Enter your full name"
                                    @blur="validateName"
                                    @input="form.first_name = form.first_name.replace(/[^a-zA-Z\s]/g, '')"
                                    class="w-full border border-gray-200 rounded-xl pl-11 pr-4 py-2 outline-none focus:border-[#0D5C63] focus:ring-2 focus:ring-[#0D5C63]/10"
                                />
                            </div>

                            <p
                                v-if="errors.first_name"
                                class="text-red-500 text-sm mt-2"
                            >
                                {{ errors.first_name }}
                            </p>
                        </div>

                        <!-- Phone -->
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-2">
                                Phone Number
                            </label>

                            <div class="relative">
                                <span
                                    class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-gray-400"
                                >
                                    call
                                </span>

                                <input
                                    v-model="form.mobile_no"
                                    type="tel"
                                    placeholder="9876543210"
                                    maxlength="10"
                                    @blur="validateMobile"
                                    @input="form.mobile_no = form.mobile_no.replace(/\D/g, '')"
                                    class="w-full border border-gray-200 rounded-xl pl-11 pr-4 py-2 outline-none focus:border-[#0D5C63] focus:ring-2 focus:ring-[#0D5C63]/10"
                                />
                            </div>

                            <p
                                v-if="errors.mobile_no"
                                class="text-red-500 text-sm mt-2"
                            >
                                {{ errors.mobile_no }}
                            </p>
                        </div>
                    </div>

                    <!-- Email -->
                    <div class="mt-4">
                        <label class="block text-sm font-medium text-gray-700 mb-2">
                            Email Address
                        </label>

                        <div class="relative">
                            <span
                                class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-gray-400"
                            >
                                mail
                            </span>

                            <input
                                v-model="form.email"
                                type="email"
                                placeholder="yourname@example.com"
                                @blur="validateEmail"
                                class="w-full border border-gray-200 rounded-xl pl-11 pr-4 py-2 outline-none focus:border-[#0D5C63] focus:ring-2 focus:ring-[#0D5C63]/10"
                            />
                        </div>

                        <p
                            v-if="errors.email"
                            class="text-red-500 text-sm mt-2"
                        >
                            {{ errors.email }}
                        </p>
                    </div>

                    <!-- Meeting Type -->
                    <div class="mt-4">
                        <label class="block text-sm font-medium text-gray-700 mb-2">
                            Meeting Type
                        </label>

                        <div class="relative">
                            <span
                                class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-gray-400"
                            >
                                videocam
                            </span>

                            <select
                                required
                                v-model="form.visist_type"
                                class="w-full border border-gray-200 rounded-xl pl-11 pr-4 py-2 outline-none focus:border-[#0D5C63] focus:ring-2 focus:ring-[#0D5C63]/10"
                            >
                                <option value="">
                                    Select Meeting Type
                                </option>

                                <option value="WhatsApp Video Call">
                                    WhatsApp Video Call
                                </option>

                                <option value="Google Meet">
                                    Google Meet
                                </option>

                                <option value="Zoom Meeting">
                                    Zoom Meeting
                                </option>
                            </select>
                        </div>
                    </div>

                    <!-- Date & Time -->
                    <div class="mt-4">
                        <label class="block text-sm font-medium text-gray-700 mb-2">
                            Preferred Date & Time
                        </label>

                        <div class="relative">
                            <input
                                ref="dateInput"
                                type="datetime-local"
                                v-model="form.visiting_time"
                                :min="minDateTime"
                                @click="openDatePicker"
                                @focus="openDatePicker"
                                @blur="validateDateTime"
                                class="w-full border border-gray-200 rounded-xl px-4 py-2 outline-none focus:border-[#0D5C63] focus:ring-2 focus:ring-[#0D5C63]/10"
                            />
                        </div>

                        <p
                            v-if="errors.visiting_time"
                            class="text-red-500 text-sm mt-2"
                        >
                            {{ errors.visiting_time }}
                        </p>
                    </div>
                </div>

                <!-- Footer -->
                <div class="border-t bg-gray-50 px-6 py-3 flex gap-3">

                    <button
                        @click="visiteButton = false"
                        class="flex-1 border border-gray-300 py-2 rounded-xl font-medium hover:bg-white transition"
                    >
                        Cancel
                    </button>

                    <button
                        @click="submitForm"
                        :disabled="loading"
                        class="flex-1 bg-gradient-to-r from-[#0D5C63] to-[#084950] text-white py-2 rounded-xl font-medium shadow-lg hover:scale-[1.02] transition disabled:opacity-50"
                    >
                        {{ loading ? "Scheduling..." : "Schedule" }}
                    </button>
                </div>

                <!-- Success Message -->
                <div
                    v-if="successMessage"
                    class="mx-4 mb-4 p-3 rounded-xl px-4 py-2 text-green-600 bg-green-50 border border-green-200"
                >
                    {{ successMessage }}
                </div>

                <!-- Error Message -->
                <div
                    v-if="errorMessage"
                    class="mx-4 mb-4 p-3 rounded-xl bg-red-100 border border-red-300 text-red-700"
                >
                    {{ errorMessage }}
                </div>
            </div>
        </div>
    </section>

    <!-- Price and Amenities -->
    <PriceAndConfiguarion :project="project" />

    <!-- Project Overview -->
    <ProjectOverviewHighlights :project="project" />

    <!-- Floor Plan -->
    <FloorPlanAndForm :project="project" />

    <!-- Similar Projects -->
    <SimilarCradsIndetaiPage
        :properties="similarProjects"
    />

    <!-- Google Map -->
    <GoggleMap :project="project" />
</template>


<script setup>
import axios from "axios";
import {
    onMounted,
    reactive,
    ref,
    computed,
    watch
} from "vue";

import {
    useRoute,
    useRouter
} from "vue-router";

import {
    Carousel,
    Slide,
    Navigation,
    Pagination
} from "vue3-carousel";

import "vue3-carousel/dist/carousel.css";

import SimilarCradsIndetaiPage from "./SimilarCradsIndetaiPage.vue";
import ProjectOverviewHighlights from "../projects/ProjectOverviewHighlights.vue";
import PriceAndConfiguarion from "../projects/PriceAndConfiguarion.vue";
import FloorPlanAndForm from "../projects/FloorPlanAndForm.vue";
import GoggleMap from "../projects/GoggleMap.vue";


const router = useRouter();
const route = useRoute();


// =====================================================
// PROJECT
// =====================================================

const project = ref({});
const similarProjects = ref([]);

const showFullDescription = ref(false);


// =====================================================
// IMAGE GALLERY
// =====================================================

const selectedImage = ref(null);
const currentIndex = ref(0);


const openImage = (image, index) => {
    selectedImage.value = image;
    currentIndex.value = index;
};


const closeImage = () => {
    selectedImage.value = null;
};


const nextImage = () => {
    const gallery = project.value?.gallery_images || [];

    if (!gallery.length) {
        return;
    }

    currentIndex.value =
        (currentIndex.value + 1) % gallery.length;

    selectedImage.value =
        gallery[currentIndex.value]?.images;
};


const prevImage = () => {
    const gallery = project.value?.gallery_images || [];

    if (!gallery.length) {
        return;
    }

    currentIndex.value =
        (currentIndex.value - 1 + gallery.length) %
        gallery.length;

    selectedImage.value =
        gallery[currentIndex.value]?.images;
};


// =====================================================
// BROCHURE
// =====================================================

const downloadBrochure = () => {

    if (!project.value?.brochure) {
        return;
    }

    const brochureUrl = project.value.brochure.startsWith("http")
        ? project.value.brochure
        : `${window.location.origin}${project.value.brochure}`;

    const link = document.createElement("a");

    link.href = brochureUrl;
    link.target = "_blank";
    link.download = "";

    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
};


// =====================================================
// SEO
// =====================================================

const stripHtml = (html) => {

    if (!html) {
        return "";
    }

    const tmp = document.createElement("div");

    tmp.innerHTML = html;

    return tmp.textContent ||
        tmp.innerText ||
        "";
};


const setProjectSeo = () => {

    const currentProject = project.value || {};

    const title =
        `${currentProject.project_name || "Premium Property"} in ${currentProject.location || "Bangalore"} | Dwell In Door`;

    const cleanDescription =
        stripHtml(currentProject.descrption);

    const description =
        (
            cleanDescription ||
            "Explore premium apartments, villas, plots, and luxury homes in Bangalore with Dwell In Door."
        ).slice(0, 160);

    const keywords =
        `${currentProject.project_name || "property"}, ${currentProject.location || "Bangalore"}, apartments, villas, plots, luxury homes, real estate, Dwell In Door`;

    const image =
        currentProject.image ||
        `${window.location.origin}/files/logo-with-some-changes.png`;

    const currentUrl =
        `${window.location.origin}${route.fullPath}`;

    document.title = title;


    const updateMetaByAttribute = (
        attribute,
        key,
        content
    ) => {

        let tag =
            document.querySelector(
                `meta[${attribute}="${key}"]`
            );

        if (!tag) {

            tag = document.createElement("meta");

            tag.setAttribute(
                attribute,
                key
            );

            document.head.appendChild(tag);
        }

        tag.setAttribute(
            "content",
            content || ""
        );
    };


    updateMetaByAttribute(
        "name",
        "description",
        description
    );

    updateMetaByAttribute(
        "name",
        "keywords",
        keywords
    );

    updateMetaByAttribute(
        "property",
        "og:title",
        title
    );

    updateMetaByAttribute(
        "property",
        "og:description",
        description
    );

    updateMetaByAttribute(
        "property",
        "og:type",
        "website"
    );

    updateMetaByAttribute(
        "property",
        "og:url",
        currentUrl
    );

    updateMetaByAttribute(
        "property",
        "og:image",
        image
    );

    updateMetaByAttribute(
        "name",
        "twitter:card",
        "summary_large_image"
    );

    updateMetaByAttribute(
        "name",
        "twitter:title",
        title
    );

    updateMetaByAttribute(
        "name",
        "twitter:description",
        description
    );

    updateMetaByAttribute(
        "name",
        "twitter:image",
        image
    );
};


// =====================================================
// STRUCTURED DATA
// =====================================================

const setProjectSchema = () => {

    const currentProject = project.value || {};

    const schema = {

        "@context": "https://schema.org",

        "@type": "Residence",

        name:
            currentProject.project_name ||
            "Premium Property",

        description:
            stripHtml(currentProject.descrption) ||
            "Premium real estate property in Bangalore",

        image:
            currentProject.image ||
            `${window.location.origin}/files/logo-with-some-changes.png`,

        url:
            `${window.location.origin}${route.fullPath}`,

        address: {

            "@type": "PostalAddress",

            addressLocality:
                currentProject.location ||
                "Bangalore",

            addressRegion:
                "Karnataka",

            addressCountry:
                "IN"
        },

        offers: {

            "@type": "Offer",

            price:
                currentProject.price ||
                "0",

            priceCurrency:
                "INR"
        }
    };


    let scriptTag =
        document.querySelector(
            "#property-schema"
        );


    if (!scriptTag) {

        scriptTag =
            document.createElement("script");

        scriptTag.id =
            "property-schema";

        scriptTag.type =
            "application/ld+json";

        document.head.appendChild(
            scriptTag
        );
    }


    scriptTag.textContent =
        JSON.stringify(schema);
};


// =====================================================
// GET PROJECT DETAILS
// =====================================================

const getProjectDetails = async () => {

    try {

        const response = await axios.get(
            "/api/method/dwell_in_door.api.propertdetail.get_property_details",
            {
                params: {
                    url: route.params.url
                }
            }
        );


        project.value =
            response?.data?.message || {};


        console.log(
            "Project Details:",
            project.value
        );


        // ============================================
        // GET SIMILAR PROJECTS AFTER PROJECT LOADS
        // ============================================

        await getSimilarProjects();


        // ============================================
        // SEO
        // ============================================

        setProjectSeo();
        setProjectSchema();


        // ============================================
        // DEBUG
        // ============================================

        console.log(
            "URL Param:",
            route.params.url
        );

        console.log(
            "Gallery Images:",
            project.value.gallery_images
        );

        console.log(
            "Brochure:",
            project.value.brochure
        );

        console.log(
            "Property Configuration:",
            project.value.property_configuartion
        );

        console.log(
            "Property Location Type:",
            project.value.property_location_type
        );

        console.log(
            "Similar Projects:",
            similarProjects.value
        );


    } catch (error) {

        console.error(
            "Error fetching project details:",
            error
        );

        project.value = {};

        similarProjects.value = [];
    }
};


// =====================================================
// GET SIMILAR PROJECTS
// =====================================================

const getSimilarProjects = async () => {

    try {

        /*
         * Do not call API if required values
         * are not available.
         */

        if (
            !project.value?.property_location_type ||
            !project.value?.project_name
        ) {

            console.warn(
                "Similar Projects API skipped:",
                "location_type or project_name missing"
            );

            similarProjects.value = [];

            return;
        }


        const response = await axios.get(
            "/api/method/dwell_in_door.api.propertdetail.get_similar_projects",
            {
                params: {

                    location_type:
                        project.value.property_location_type,

                    current_project:
                        project.value.project_name
                }
            }
        );


        /*
         * Frappe API response:
         *
         * response.data.message
         *
         * can be either array or object.
         */

        const result =
            response?.data?.message;


        if (Array.isArray(result)) {

            similarProjects.value =
                result;

        } else if (
            Array.isArray(result?.data)
        ) {

            similarProjects.value =
                result.data;

        } else {

            similarProjects.value =
                [];
        }


        /*
         * Extra frontend safety:
         * Remove current project from similar
         * projects if backend sends it.
         */

        similarProjects.value =
            similarProjects.value.filter(
                (item) =>
                    item?.project_name !==
                    project.value?.project_name
            );


        console.log(
            "Similar Projects API Response:",
            response?.data
        );

        console.log(
            "Final Similar Projects:",
            similarProjects.value
        );


    } catch (error) {

        console.error(
            "Error fetching similar projects:",
            error
        );

        /*
         * Do not break the complete
         * Detail Page if similar API fails.
         */

        similarProjects.value = [];
    }
};


// =====================================================
// VISIT FORM
// =====================================================

const successMessage = ref("");
const errorMessage = ref("");
const loading = ref(false);

const dateInput = ref(null);

const visiteButton = ref(false);


const form = reactive({

    first_name: "",

    mobile_no: "",

    email: "",

    visist_type:
        "WhatsApp Video Call",

    visiting_time: ""
});


const errors = reactive({

    first_name: "",

    mobile_no: "",

    email: "",

    visiting_time: ""
});


// =====================================================
// MIN DATE TIME
// =====================================================

const minDateTime = computed(() => {

    const now =
        new Date();

    const year =
        now.getFullYear();

    const month =
        String(
            now.getMonth() + 1
        ).padStart(2, "0");

    const day =
        String(
            now.getDate()
        ).padStart(2, "0");

    const hours =
        String(
            now.getHours()
        ).padStart(2, "0");

    const minutes =
        String(
            now.getMinutes()
        ).padStart(2, "0");


    return `${year}-${month}-${day}T${hours}:${minutes}`;
});


// =====================================================
// OPEN VISIT MODAL
// =====================================================

const openVisitModal = () => {

    visiteButton.value = true;

    successMessage.value = "";
    errorMessage.value = "";
};


// =====================================================
// DATE PICKER
// =====================================================

const openDatePicker = () => {

    if (
        dateInput.value &&
        typeof dateInput.value.showPicker ===
        "function"
    ) {

        dateInput.value.showPicker();
    }
};


// =====================================================
// VALIDATIONS
// =====================================================

const validateName = () => {

    if (!form.first_name.trim()) {

        errors.first_name =
            "Name is required.";

    } else if (
        !/^[A-Za-z\s]+$/.test(
            form.first_name
        )
    ) {

        errors.first_name =
            "Name should contain only letters.";

    } else {

        errors.first_name = "";
    }
};


const validateMobile = () => {

    if (!form.mobile_no.trim()) {

        errors.mobile_no =
            "Mobile number is required.";

    } else if (
        !/^[0-9]{10}$/.test(
            form.mobile_no
        )
    ) {

        errors.mobile_no =
            "Mobile number must be exactly 10 digits.";

    } else {

        errors.mobile_no = "";
    }
};


const validateEmail = () => {

    /*
     * FIXED REGEX
     *
     * Old:
     * /^[^\s@]+@[^\s@]+**\.**[^\s@]+$/
     *
     * Correct:
     */

    const emailRegex =
        /^[^\s@]+@[^\s@]+\.[^\s@]+$/;


    if (!form.email.trim()) {

        errors.email =
            "Email is required.";

    } else if (
        !emailRegex.test(
            form.email
        )
    ) {

        errors.email =
            "Please enter a valid email address.";

    } else {

        errors.email = "";
    }
};


const validateDateTime = () => {

    if (!form.visiting_time) {

        errors.visiting_time =
            "Please select your preferred date and time.";

    } else {

        errors.visiting_time = "";
    }
};


// =====================================================
// SUBMIT VIDEO VISIT FORM
// =====================================================

const submitForm = async () => {

    successMessage.value = "";
    errorMessage.value = "";


    // ============================================
    // VALIDATE
    // ============================================

    validateName();
    validateMobile();
    validateEmail();
    validateDateTime();


    if (
        errors.first_name ||
        errors.mobile_no ||
        errors.email ||
        errors.visiting_time
    ) {

        return;
    }


    try {

        loading.value = true;


        // ========================================
        // POST API
        // ========================================

        const response = await axios.post(
            "/api/method/dwell_in_door.api.crmlead.video_meeting_shedule",
            {

                name:
                    form.first_name,

                phone:
                    form.mobile_no,

                email:
                    form.email,

                visist_type:
                    form.visist_type,

                visiting_time:
                    form.visiting_time,

                project_name:
                    project.value.project_name
            }
        );


        console.log(
            "Video Meeting API Response:",
            response?.data
        );


        successMessage.value =
            response?.data?.message?.message ||
            response?.data?.message ||
            "Your virtual tour request has been submitted successfully.";


        // ========================================
        // RESET FORM
        // ========================================

        form.first_name = "";

        form.mobile_no = "";

        form.email = "";

        form.visist_type =
            "WhatsApp Video Call";

        form.visiting_time = "";


        // ========================================
        // RESET ERRORS
        // ========================================

        errors.first_name = "";

        errors.mobile_no = "";

        errors.email = "";

        errors.visiting_time = "";


        // ========================================
        // CLOSE AFTER 8 SECONDS
        // ========================================

        setTimeout(() => {

            visiteButton.value = false;

            successMessage.value = "";

        }, 8000);


    } catch (error) {

        console.error(
            "Video meeting API error:",
            error
        );


        errorMessage.value =
            error?.response?.data?.message?.message ||
            error?.response?.data?.message ||
            "Something went wrong. Please try again.";


    } finally {

        loading.value = false;
    }
};


// =====================================================
// INITIAL LOAD
// =====================================================

onMounted(() => {

    getProjectDetails();

});


// =====================================================
// ROUTE CHANGE
// =====================================================

watch(
    () => route.params.url,

    (newUrl, oldUrl) => {

        if (newUrl !== oldUrl) {

            /*
             * Reset old data first
             * so previous property's
             * similar projects don't remain.
             */

            project.value = {};

            similarProjects.value = [];

            selectedImage.value = null;

            currentIndex.value = 0;

            getProjectDetails();
        }
    }
);

</script>


<style>
.carousel__prev,
.carousel__next {
    background: white !important;
    border-radius: 9999px !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    color: black !important;
}
</style>