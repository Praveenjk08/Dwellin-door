<template>

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
                    <!-- <div class="h-[300px] md:h-full">


                        <iframe :src="project.property_loaction_link" class="w-full h-full" loading="lazy">
                        </iframe>


                    </div> -->
                    <div class="relative h-[300px] md:h-full">

                        <iframe :src="project.property_loaction_link" class="w-full h-full pointer-events-none"
                            loading="lazy">
                        </iframe>

                        <!-- Overlay -->
                        <div @click="visiteButton = true"
                            class="absolute inset-0 bg-black/10 cursor-pointer flex items-center justify-center">

                            <div class="bg-white px-6 py-3 rounded-xl shadow-lg text-center">

                                <span class="material-symbols-outlined text-[#0D5C63] text-3xl">
                                    location_on
                                </span>

                                <p class="font-medium text-[#0D5C63]">
                                    Click to View Exact Location
                                </p>

                            </div>

                        </div>

                    </div>

                </div>

            </div>

        </div>

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

</template>


<!-- <script setup>
import axios from 'axios';
import { reactive, ref } from 'vue';

const successMessage = ref("");
const errorMessage = ref("");
const loading = ref(false);

const form = reactive({
    first_name: "",
    mobile_no: "",
    email: "",
    visist_type: "WhatsApp Video Call",
    visiting_time: ""
});

const submitForm = async () => {

    successMessage.value = "";
    errorMessage.value = "";

    if (!form.first_name.trim()) {
        errorMessage.value = "Please enter your name";
        return;
    }

    const mobileRegex = /^[0-9]{10}$/;

    if (!mobileRegex.test(form.mobile_no)) {
        errorMessage.value = "Mobile number must be exactly 10 digits";
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
                project_name: props.project.project_name
            }
        );

        successMessage.value = response.data.message || "Meeting scheduled successfully";
        setTimeout(() => {
            window.open(props.project.property_loaction_link, "_blank");
        }, 1000);

        form.first_name = "";
        form.mobile_no = "";
        form.email = "";
        form.visist_type = "WhatsApp Video Call";
        form.visiting_time = "";

        setTimeout(() => {
            visiteButton.value = false;
            successMessage.value = "";
        }, 4000);

    } catch (error) {

        errorMessage.value =
            error?.response?.data?.message ||
            "Something went wrong. Please try again.";

    } finally {
        loading.value = false;
    }
};
// defineProps({
//     project: {
//         type: Object,
//         required: true
//     }
// });
const props = defineProps({
    project: {
        type: Object,
        required: true
    }
});
const visiteButton = ref(false)
</script> -->


<script setup>
import axios from "axios";
import { reactive, ref } from "vue";

const successMessage = ref("");
const errorMessage = ref("");
const loading = ref(false);
const dateInput = ref(null);

const props = defineProps({
    project: {
        type: Object,
        required: true
    }
});

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
                project_name: props.project.project_name
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