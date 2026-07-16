<template>
    <section class="bg-white mb-10 mt-4 ">
        <div class="max-w-[1400px]  mx-auto px-4">

            <div class="grid grid-cols-1 lg:grid-cols-12 gap-2 ">

                <!-- LEFT SIDE -->
                <!-- <div class="ml-20"> -->
                <div class="lg:col-span-7">
                    <!-- Main Image -->
                    <div class="relative">
                        <!-- <img :src="project.image" class="w-full h-[250px] md:h-[400px] object-cover rounded-[5px]" /> -->
                        <Carousel :items-to-show="1" :wrap-around="true" :autoplay="5000"
                            :pause-autoplay-on-hover="true">
                            <!-- Main Image -->
                            <Slide>
                                <img :src="project.image"
                                    class="w-full h-[250px] md:h-[400px] object-cover rounded-[5px]" />
                            </Slide>

                            <!-- Gallery Images -->
                            <Slide v-for="(item, index) in project.cursol_project_images" :key="index">
                                <img :src="item.cusrol_images"
                                    class="w-full h-[250px] md:h-[400px] object-cover rounded-[5px]" />
                            </Slide>

                            <template #addons>
                                <Navigation />
                                <Pagination />
                            </template>
                        </Carousel>
                    </div>

                    <!-- gallery -->
                    <!-- <div class=" grid grid-cols-6 gap-3 mt-4"> -->
                    <div class="mt-1 w-full" v-if="project.gallery_images?.length">


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

                        <button @click="visiteButton = true"
                            class="bg-[#0D5C63] hover:bg-[#084950] text-white px-6 py-2 text-[14px] rounded-xl font-medium transition">
                            Schedule Video Visit
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

        <!-- <div v-if="visiteButton" class="h-full w-full">



        </div> -->


        <!-- Schedule Visit Modal -->
        <!-- Schedule Visit Modal -->
        <div v-if="visiteButton" @click="visiteButton = false"
            class="fixed inset-0 bg-black/60 backdrop-blur-sm z-[9999] flex items-center justify-center p-3 md:p-4">

            <div @click.stop
                class="bg-white rounded-2xl w-full max-w-2xl shadow-2xl overflow-hidden max-h-[90vh] overflow-y-auto md:max-h-none ">
                <!-- Header -->
                <div class="bg-gradient-to-r from-[#0D5C63] to-[#084950] px-6 py-3 text-white">

                    <div class="flex items-center justify-between">

                        <div>
                            <h2 class="text-2xl font-bold">
                                Schedule Your Virtual Tour
                            </h2>

                            <p class="text-sm text-white/80 ">
                                Connect with our property expert through a video call.
                            </p>
                        </div>

                        <button @click="visiteButton = false"
                            class="w-10 h-10 rounded-full bg-white/10 hover:bg-white/20 flex items-center justify-center transition">

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
                                    class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-gray-400">
                                    person
                                </span>

                                <input v-model="form.first_name" type="text" placeholder="Enter your full name"
                                    @blur="validateName"
                                    @input="form.first_name = form.first_name.replace(/[^a-zA-Z\s]/g, '')"
                                    class="w-full border border-gray-200 rounded-xl pl-11 pr-4 py-2 outline-none focus:border-[#0D5C63] focus:ring-2 focus:ring-[#0D5C63]/10" />

                            </div>

                            <p v-if="errors.first_name" class="text-red-500 text-sm mt-2">
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
                                    class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-gray-400">
                                    call
                                </span>

                                <input v-model="form.mobile_no" type="tel" placeholder="+91 9876543210" maxlength="10"
                                    @blur="validateMobile" @input="form.mobile_no = form.mobile_no.replace(/\D/g, '')"
                                    class="w-full border border-gray-200 rounded-xl pl-11 pr-4 py-2 outline-none focus:border-[#0D5C63] focus:ring-2 focus:ring-[#0D5C63]/10" />

                            </div>

                            <p v-if="errors.mobile_no" class="text-red-500 text-sm mt-2">
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
                                class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-gray-400">
                                mail
                            </span>

                            <input v-model="form.email" type="email" placeholder="yourname@example.com"
                                @blur="validateEmail"
                                class="w-full border border-gray-200 rounded-xl pl-11 pr-4 py-2 outline-none focus:border-[#0D5C63] focus:ring-2 focus:ring-[#0D5C63]/10" />

                        </div>

                        <p v-if="errors.email" class="text-red-500 text-sm mt-2">
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
                                class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-gray-400">
                                videocam
                            </span>

                            <select required v-model="form.visist_type"
                                class="w-full border border-gray-200 rounded-xl pl-11 pr-4 py-2 outline-none focus:border-[#0D5C63] focus:ring-2 focus:ring-[#0D5C63]/10">

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

                            <input ref="dateInput" type="datetime-local" v-model="form.visiting_time"
                                :min="new Date().toISOString().slice(0, 16)" @click="dateInput?.showPicker?.()"
                                @focus="dateInput?.showPicker?.()" @blur="validateDateTime"
                                class="w-full border border-gray-200 rounded-xl px-4 py-2 outline-none focus:border-[#0D5C63] focus:ring-2 focus:ring-[#0D5C63]/10" />

                        </div>

                        <p v-if="errors.visiting_time" class="text-red-500 text-sm mt-2">
                            {{ errors.visiting_time }}
                        </p>

                    </div>
                    <!-- Property Info -->
                    <!-- <div class="mt-5 bg-[#F4F8F8] border border-[#DCECEC] rounded-xl px-4 py-2">

                        <div class="flex items-start gap-3">

                            <div
                                class="w-10 h-10 rounded-full bg-[#0D5C63] text-white flex items-center justify-center shrink-0">

                                <span class="material-symbols-outlined">
                                    apartment
                                </span>

                            </div>

                            <div>

                                <h4 class="font-semibold text-gray-800">
                                    Property Visit Request
                                </h4>

                                <p class="text-sm text-gray-500 mt-1">
                                    Schedule a personalized virtual tour and explore the property from the comfort of
                                    your home.
                                </p>

                            </div>

                        </div>

                    </div> -->

                </div>

                <!-- Footer -->
                <div class="border-t bg-gray-50 px-6 py-3 flex gap-3">

                    <button @click="visiteButton = false"
                        class="flex-1 border border-gray-300 py-2 rounded-xl font-medium hover:bg-white transition">
                        Cancel
                    </button>
                    <!-- 
                    <button @click="submitForm"
                        class="flex-1 bg-gradient-to-r from-[#0D5C63] to-[#084950] text-white py-2 rounded-xl font-medium shadow-lg hover:scale-[1.02] transition">
                        Schedule Visit
                    </button> -->
                    <button @click="submitForm" :disabled="loading"
                        class="flex-1 bg-gradient-to-r from-[#0D5C63] to-[#084950] text-white py-2 rounded-xl font-medium shadow-lg hover:scale-[1.02] transition disabled:opacity-50">
                        {{ loading ? "Scheduling..." : "Schedule Visit" }}
                    </button>

                </div>
                <div v-if="successMessage" class="mb-4 p-3 rounded-xl   px-4 py-2 text-green-500">
                    {{ successMessage }}
                </div>

                <div v-if="errorMessage" class="mb-4 p-3 rounded-xl bg-red-100 border border-red-300 text-red-700">
                    {{ errorMessage }}
                </div>

            </div>

        </div>
    </section>
    <!--------------Next SEction -2--------------->
    <!-- <section class="py-2 bg-white mx-auto md:mx-10">
        <div class="max-w-[1400px] mx-auto px-4">

            <div class="grid lg:grid-cols-12 gap-10">

                LEFT
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

                RIGHT
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

                               
                                <p class="text-gray-500 text-[12px] mt-1 leading-4 h-8 overflow-hidden">
                                    {{ item.project_descrption_high }}
                                </p>
                            </div>

                        </div>

                    </div>

                </div>

            </div>

        </div>
    </section> -->
    <!-- <ProjectOverviewHighlights /> -->
    <!--Price and Animites-->
    <PriceAndConfiguarion :project="project" />
    <!--Project overview-->
    <ProjectOverviewHighlights :project="project" />


    <!-----Section-3----->
    <!-- <section class="py-8 bg-white mx-auto md:mx-10 ">
        <div class="max-w-[1400px] mx-auto px-4">

            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 lg:gap-10">

                LEFT SIDE


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
    </section> -->
    <FloorPlanAndForm :project="project" />


    <!--Next section-4-->
    <!-- <section class="mb-10 md:mx-10 bg-white">
        <div class="max-w-[1400px] mx-auto px-4">

            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-stretch">

                Floor Plan Slider
                <div class="lg:col-span-7 h-[400px]">

                    <div class="border border-gray-200 rounded-2xl overflow-hidden bg-white h-full flex flex-col">

                        <div class="text-center py-3">
                            <h2 class="text-[22px] font-bold text-[#1B1B1B]">
                                Floor Plans
                            </h2>
                            <div class="w-16 h-[2px] bg-[#D4AF37] mx-auto mt-2 rounded-full"></div>
                        </div>

                        <div class="flex-1">
                            <Carousel :items-to-show="1" :wrap-around="true" :autoplay="3000"
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

                Enquiry Form
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
    </section> -->
    <!--Propety simailar cards bro-->
    <SimilarCradsIndetaiPage :properties="similarProjects" />
    <GoggleMap :project="project" />


    <!--Next section-5-->
    <!-- <section class="my-10 bg-white "
        v-if="project.property_loaction_detail_descr?.length && project.property_location_details?.length && project.property_loaction_link?.length">
        <div class="max-w-[1400px] mx-auto px-4">

            <div class="max-w-5xl mx-auto">

                <div class="grid grid-cols-1 md:grid-cols-2 overflow-hidden rounded-2xl shadow-lg ">

                    Left Content
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

                                    <span>{{ item.location_name }}</span>
                                </div>
                                <span>{{ item.distance }}</span>
                            </div>



                        </div>

                    </div>

                    Right Side Map
                    <div class="h-[300px] md:h-full">


                        <iframe :src="project.property_loaction_link" class="w-full h-full" loading="lazy">
                        </iframe>


                    </div>

                </div>

            </div>

        </div>
    </section> -->


</template>

<script setup>
import axios from "axios";
import { onMounted, provide, reactive, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import { Carousel, Slide, Navigation, Pagination } from "vue3-carousel";
import "vue3-carousel/dist/carousel.css";
import SimilarCradsIndetaiPage from "./SimilarCradsIndetaiPage.vue";
import { watch } from "vue";
import ProjectOverviewHighlights from "../projects/ProjectOverviewHighlights.vue";
import PriceAndConfiguarion from "../projects/PriceAndConfiguarion.vue";
import FloorPlanAndForm from "../projects/FloorPlanAndForm.vue";
import GoggleMap from "../projects/GoggleMap.vue";

const router = useRouter()


const showFullDescription = ref(false);
const route = useRoute();

const project = ref({});
const selectedImage = ref(null);
const currentIndex = ref(0)

// const visiteButton = ref(false)
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




///// Post api intigartion bro


const successMessage = ref("");
const errorMessage = ref("");
const loading = ref(false);
const dateInput = ref(null);
const visiteButton = ref(false);

const form = reactive({
    first_name: "",
    mobile_no: "",
    email: "",
    visist_type: "WhatsApp Video Call",
    visiting_time: ""
});

const errors = reactive({
    first_name: "",
    mobile_no: "",
    email: "",
    visiting_time: ""
});

const validateName = () => {
    if (!form.first_name.trim()) {
        errors.first_name = "Name is required.";
    } else if (!/^[A-Za-z\s]+$/.test(form.first_name)) {
        errors.first_name = "Name should contain only letters.";
    } else {
        errors.first_name = "";
    }
};

const validateMobile = () => {
    if (!form.mobile_no.trim()) {
        errors.mobile_no = "Mobile number is required.";
    } else if (!/^[0-9]{10}$/.test(form.mobile_no)) {
        errors.mobile_no = "Mobile number must be exactly 10 digits.";
    } else {
        errors.mobile_no = "";
    }
};

const validateEmail = () => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!form.email.trim()) {
        errors.email = "Email is required.";
    } else if (!emailRegex.test(form.email)) {
        errors.email = "Please enter a valid email address.";
    } else {
        errors.email = "";
    }
};

const validateDateTime = () => {
    if (!form.visiting_time) {
        errors.visiting_time = "Please select your preferred date and time.";
    } else {
        errors.visiting_time = "";
    }
};

const submitForm = async () => {

    successMessage.value = "";
    errorMessage.value = "";

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

        const response = await axios.post(
            "/api/method/dwell_in_door.api.crmlead.video_meeting_shedule",
            {
                name: form.first_name,
                phone: form.mobile_no,
                email: form.email,
                visist_type: form.visist_type,
                visiting_time: form.visiting_time,
                project_name: project.value.project_name
            }
        );

        successMessage.value =
            response?.data?.message?.message ||
            response?.data?.message ||
            "Your virtual tour request has been submitted successfully.";

        form.first_name = "";
        form.mobile_no = "";
        form.email = "";
        form.visist_type = "WhatsApp Video Call";
        form.visiting_time = "";

        errors.first_name = "";
        errors.mobile_no = "";
        errors.email = "";
        errors.visiting_time = "";

        setTimeout(() => {
            visiteButton.value = false;
            successMessage.value = "";
        }, 8000);

    } catch (error) {

        console.error(error);

        errorMessage.value =
            error?.response?.data?.message ||
            "Something went wrong. Please try again.";

    } finally {

        loading.value = false;

    }
};
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