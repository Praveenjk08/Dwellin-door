<template>
    <!-- Banner -->
    <section class="relative mb-5 overflow-hidden">

        <div class="w-full lg:h-[360px]">
            <img :src="getFileUrl('Contact-Us-Banner.jpeg')" alt="Contact Banner"
                class="w-full aspect-[10/5] md:h-[360px] lg:h-[360px] object-cover object-center" />
        </div>

    </section>

    <!-- Contact Section -->
    <section class="my-10 mx-4 md:mx-10">
        <div class="max-w-[1400px] mx-auto ">

            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">

                <!-- Contact Card -->
                <div class="lg:col-span-4 bg-white rounded-xl p-6 md:py-4 px-8 shadow-md">

                    <h2 class="text-[22px] md:text-[22px] font-serif font-semibold leading-tight">
                        Get In
                        <span class="text-[#0D5C63]">Touch</span>
                    </h2>

                    <p class="text-gray-600 mt-1 text-sm md:text-base leading-5">
                        Have questions? We'd love to hear from you.
                        Our team is here to help you.
                    </p>

                    <!-- Phone -->
                    <div class="flex gap-4 mt-4">

                        <div class="w-12 h-12 rounded-full bg-[#E8F4F5] flex items-center justify-center shrink-0">
                            <span class="material-symbols-outlined text-[#0D5C63]">
                                call
                            </span>
                        </div>


                        <div>
                            <h4 class="font-semibold">Call Us</h4>
                            <p class="text-gray-600 text-[13px]">+91 98765 43210</p>
                            <p class="text-gray-500  text-[12px]">Mon - Sat, 9:00 AM - 6:00 PM</p>
                        </div>
                    </div>

                    <!-- Email -->
                    <div class="flex gap-4 mt-4">

                        <div class="w-12 h-12 rounded-full bg-[#E8F4F5] flex items-center justify-center shrink-0">
                            <span class="material-symbols-outlined text-[#0D5C63]">
                                mail
                            </span>
                        </div>

                        <div>
                            <h4 class="font-semibold">Email Us</h4>
                            <p class="text-gray-600 text-[13px]">info@dwellindoors.com</p>
                            <p class="text-gray-500 text-[12px]">We reply within 24 hours</p>
                        </div>
                    </div>

                    <!-- Location -->
                    <div class="flex gap-4 mt-4">
                        <div class="w-12 h-12 rounded-full bg-[#E8F4F5] flex items-center justify-center shrink-0">
                            <span class="material-symbols-outlined text-[#0D5C63]">
                                location_on
                            </span>
                        </div>

                        <div>
                            <h4 class="font-semibold ">Visit Our Office</h4>
                            <p class="text-gray-600 text-[12px] ">
                                BTM Layout, Bangalore - 560076,
                                Karnataka, India
                            </p>
                        </div>
                    </div>

                    <!-- Social -->
                    <div class="mt-4">
                        <h4 class="font-semibold mb-4">Follow Us</h4>

                        <div class="flex gap-3">

                            <div class="w-10 h-10 rounded-full bg-[#E8F4F5] flex items-center justify-center">
                                <i class="fa-brands fa-facebook-f text-[#0D5C63]"></i>
                            </div>

                            <div class="w-10 h-10 rounded-full bg-[#E8F4F5] flex items-center justify-center">
                                <i class="fa-brands fa-linkedin-in text-[#0D5C63]"></i>
                            </div>

                            <div class="w-10 h-10 rounded-full bg-[#E8F4F5] flex items-center justify-center">
                                <i class="fa-brands fa-instagram text-[#0D5C63]"></i>
                            </div>

                            <div class="w-10 h-10 rounded-full bg-[#E8F4F5] flex items-center justify-center">
                                <i class="fa-brands fa-youtube text-[#0D5C63]"></i>
                            </div>

                        </div>
                    </div>

                </div>

                <!-- Form -->
                <div class="lg:col-span-5 bg-white rounded-xl p-4 md:py-4 px-8 shadow-md">

                    <h2 class="text-[22px] md:text-[22px] font-serif font-semibold leading-tight">
                        Send Us a
                        <span class="text-[#0D5C63]">Message</span>
                    </h2>

                    <p class="text-gray-600 mt-3 text-sm md:text-base">
                        Fill out the form below and our team will get back to you soon.
                    </p>
                    <div v-if="successMessage"
                        class="mb-4 p-1 rounded-lg bg-green-100 text-green-700 border border-green-200">
                        {{ successMessage }}
                    </div>

                    <div v-if="errorMessage" class="mb-4 p-1 rounded-lg bg-red-100 text-red-700 border border-red-200">
                        {{ errorMessage }}
                    </div>

                    <form class="mt-6 space-y-4" @submit.prevent="submitForm">

                        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">

                            <input type="text" placeholder="Your Name" v-model="form.name"
                                class="border border-gray-200 rounded-xl px-4 py-2 w-full" required />

                            <input type="email" placeholder="Your Email" v-model="form.email"
                                class="border border-gray-200 rounded-xl px-4 py-2 w-full" required />

                        </div>

                        <input type="text" placeholder="Your Phone Number" v-model="form.phone"
                            class="border border-gray-200 rounded-xl px-4 py-2 w-full" required />

                        <select v-model="form.service" class="border border-gray-200 rounded-xl px-4 py-2 w-full">
                            <option value="Others">Others</option>
                            <option value="Interested In">Interested In</option>
                            <option value="Real Estate">Real Estate</option>
                            <option value="Constrcution">Constrcution</option>
                        </select>

                        <textarea rows="3" placeholder="Your Message"
                            class="border border-gray-200 rounded-xl px-4 py-2 w-full"></textarea>

                        <button type="submit" class="w-full bg-[#D4AF37] text-white py-2 rounded-xl font-semibold">
                            Send Message →
                        </button>

                    </form>

                </div>

                <!-- Map -->
                <div class="lg:col-span-3 overflow-hidden rounded-xl shadow-md h-full">

                    <iframe src="https://www.google.com/maps?q=BTM%20Layout%20Bangalore&output=embed"
                        class="w-full h-full min-h-[400px] border-0" loading="lazy">
                    </iframe>

                </div>

            </div>

        </div>
    </section>


    <section class="my-10">

        <div class="mx-4 md:mx-10 lg:mx-20">

            <div
                class="bg-white rounded-[24px] shadow-sm border border-[#F3EEE4] grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 overflow-hidden">

                <!-- Item 1 -->
                <div class="flex items-center gap-4 px-6 py-6 border-b lg:border-b-0 lg:border-r border-[#E9DFCF]">


                    <div class="w-14 h-14 rounded-full bg-[#E8F4F5] flex items-center justify-center shrink-0">

                        <span class="material-symbols-outlined text-[#0D5C63]">
                            handshake
                        </span>

                    </div>


                    <div>

                        <h4 class="font-semibold text-[18px] text-gray-900">
                            Trusted by 1000+ Clients
                        </h4>

                        <p class="text-gray-500 text-sm">
                            Building lasting relationships
                        </p>

                    </div>

                </div>

                <!-- Item 2 -->
                <div class="flex items-center gap-4 px-6 py-6 border-b lg:border-b-0 lg:border-r border-[#E9DFCF]">


                    <div class="w-14 h-14 rounded-full bg-[#E8F4F5] flex items-center justify-center shrink-0">

                        <span class="material-symbols-outlined text-[#0D5C63]">
                            home
                        </span>

                    </div>

                    <div>

                        <h4 class="font-semibold text-[18px] text-gray-900">
                            Wide Range of Properties
                        </h4>

                        <p class="text-gray-500 text-sm">
                            Find your perfect space
                        </p>

                    </div>

                </div>

                <!-- Item 3 -->
                <div class="flex items-center gap-4 px-6 py-6 border-b lg:border-b-0 lg:border-r border-[#E9DFCF]">

                    <div class="w-14 h-14 rounded-full bg-[#E8F4F5] flex items-center justify-center shrink-0">

                        <span class="material-symbols-outlined text-[#0D5C63]">
                            verified_user
                        </span>

                    </div>

                    <div>

                        <h4 class="font-semibold text-[18px] text-gray-900">
                            100% Transparent Deals
                        </h4>

                        <p class="text-gray-500 text-sm">
                            No hidden charges
                        </p>

                    </div>

                </div>

                <!-- Item 4 -->
                <div class="flex items-center gap-4 px-6 py-6">

                    <div class="w-14 h-14 rounded-full bg-[#E8F4F5] flex items-center justify-center shrink-0">
                        <span class="material-symbols-outlined text-[#0D5C63]">
                            support_agent
                        </span>
                    </div>

                    <div>

                        <h4 class="font-semibold text-[18px] text-gray-900">
                            Dedicated Support
                        </h4>

                        <p class="text-gray-500 text-sm">
                            Always here for you
                        </p>

                    </div>

                </div>

            </div>

        </div>

    </section>
</template>
<script setup>
import { reactive, ref } from "vue";
import axios from "axios";

const form = reactive({
    name: "",
    phone: "",
    email: "",
    service: "Others",

});

const successMessage = ref("");
const errorMessage = ref("");

const submitForm = async () => {
    successMessage.value = "";
    errorMessage.value = "";

    // Phone number validation
    if (!/^\d{10}$/.test(form.phone)) {
        errorMessage.value = "Please enter a valid 10-digit mobile number.";

        setTimeout(() => {
            errorMessage.value = "";
        }, 5000);

        return;
    }

    try {
        await axios.post(
            "/api/method/dwell_in_door.api.crmlead.lead_add_api",
            {
                name: form.name,
                phone: form.phone,
                email: form.email,
                service: form.service
            }
        );

        successMessage.value =
            "Thank you! Your enquiry has been submitted successfully.";

        form.name = "";
        form.phone = "";
        form.email = "";
        form.service = "";

        setTimeout(() => {
            successMessage.value = "";
        }, 5000);

    } catch (error) {
        console.error(error);

        errorMessage.value =
            "Failed to submit your enquiry. Please try again.";

        setTimeout(() => {
            errorMessage.value = "";
        }, 5000);
    }
};

const getFileUrl = (file) => {
    return `${window.location.origin}/files/${file}`;
};
</script>