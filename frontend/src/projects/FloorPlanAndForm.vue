<template>
    <!--Next section-4-->
    <section class="mb-10 md:mx-10 bg-white" v-if="project.floor_plan?.length">
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

                <!-- Enquiry Form -->
                <div class="lg:col-span-5 h-full md:h-[400px]">

                    <div class="border border-gray-200 rounded-[10px] p-6 shadow-2xl h-full flex flex-col">

                        <h2 class="text-[22px] font-bold mb-3 text-[#1B1B1B]">
                            Interested in this project?
                        </h2>

                        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">

                            <!-- Name -->
                            <div>
                                <input v-model="enquiryForm.name" type="text" placeholder="Full Name"
                                    @blur="validateEnquiryName"
                                    @input="enquiryForm.name = enquiryForm.name.replace(/[^a-zA-Z\s]/g, '')"
                                    class="border border-gray-300 rounded-lg px-4 py-2 outline-none focus:border-[#0D5C63] w-full" />

                                <p v-if="enquiryErrors.name" class="text-red-500 text-sm mt-1">
                                    {{ enquiryErrors.name }}
                                </p>
                            </div>

                            <!-- Phone -->
                            <div>
                                <input v-model="enquiryForm.phone" type="text" maxlength="10" placeholder="Phone Number"
                                    @blur="validateEnquiryPhone"
                                    @input="enquiryForm.phone = enquiryForm.phone.replace(/\D/g, '')"
                                    class="border border-gray-300 rounded-lg px-4 py-2 outline-none focus:border-[#0D5C63] w-full" />

                                <p v-if="enquiryErrors.phone" class="text-red-500 text-sm mt-1">
                                    {{ enquiryErrors.phone }}
                                </p>
                            </div>

                            <!-- Email -->
                            <div>
                                <input v-model="enquiryForm.email" type="email" placeholder="Email Address"
                                    @blur="validateEnquiryEmail"
                                    class="border border-gray-300 rounded-lg px-4 py-2 outline-none focus:border-[#0D5C63] w-full" />

                                <p v-if="enquiryErrors.email" class="text-red-500 text-sm mt-1">
                                    {{ enquiryErrors.email }}
                                </p>
                            </div>

                            <!-- Date -->
                            <div>
                                <input v-model="enquiryForm.visiting_time" type="date"
                                    :min="new Date().toISOString().split('T')[0]" @blur="validateEnquiryDate"
                                    class="border border-gray-300 rounded-lg px-4 py-2 outline-none focus:border-[#0D5C63] w-full" />

                                <p v-if="enquiryErrors.visiting_time" class="text-red-500 text-sm mt-1">
                                    {{ enquiryErrors.visiting_time }}
                                </p>
                            </div>

                        </div>

                        <textarea v-model="enquiryForm.message" placeholder="Your Message"
                            class="w-full h-[100px] md:h-[150px] border border-gray-300 rounded-lg px-4 py-2 mt-4 outline-none resize-none focus:border-[#0D5C63]">
        </textarea>

                        <div class="mt-auto">

                            <button @click="submitEnquiry" :disabled="enquiryLoading"
                                class="w-full mt-4 bg-gradient-to-r from-[#0D5C63] to-[#1D3B2A] text-white py-2 rounded-lg font-medium hover:opacity-90 transition disabled:opacity-50">

                                {{ enquiryLoading ? "Submitting..." : "Send Enquiry" }}

                            </button>

                            <p v-if="enquirySuccess" class="text-green-600 text-sm mt-3">
                                {{ enquirySuccess }}
                            </p>

                            <p v-if="enquiryError" class="text-red-600 text-sm mt-3">
                                {{ enquiryError }}
                            </p>

                        </div>

                    </div>

                </div>

            </div>

        </div>
    </section>



</template>

<script setup>
import axios from "axios";
import { reactive, ref } from "vue";

const props = defineProps({
    project: {
        type: Object,
        required: true
    }
});

const enquiryLoading = ref(false);
const enquirySuccess = ref("");
const enquiryError = ref("");

const enquiryForm = reactive({
    name: "",
    phone: "",
    email: "",
    visiting_time: "",
    message: ""
});

const enquiryErrors = reactive({
    name: "",
    phone: "",
    email: "",
    visiting_time: ""
});

const validateEnquiryName = () => {
    if (!enquiryForm.name.trim()) {
        enquiryErrors.name = "Name is required.";
    } else if (!/^[A-Za-z\s]+$/.test(enquiryForm.name)) {
        enquiryErrors.name = "Name should contain only letters.";
    } else {
        enquiryErrors.name = "";
    }
};

const validateEnquiryPhone = () => {
    if (!enquiryForm.phone.trim()) {
        enquiryErrors.phone = "Mobile number is required.";
    } else if (!/^[0-9]{10}$/.test(enquiryForm.phone)) {
        enquiryErrors.phone = "Mobile number must be exactly 10 digits.";
    } else {
        enquiryErrors.phone = "";
    }
};

const validateEnquiryEmail = () => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!enquiryForm.email.trim()) {
        enquiryErrors.email = "Email is required.";
    } else if (!emailRegex.test(enquiryForm.email)) {
        enquiryErrors.email = "Please enter a valid email address.";
    } else {
        enquiryErrors.email = "";
    }
};

const validateEnquiryDate = () => {
    if (!enquiryForm.visiting_time) {
        enquiryErrors.visiting_time = "Please select a date.";
    } else {
        enquiryErrors.visiting_time = "";
    }
};

const submitEnquiry = async () => {

    enquirySuccess.value = "";
    enquiryError.value = "";

    validateEnquiryName();
    validateEnquiryPhone();
    validateEnquiryEmail();
    validateEnquiryDate();

    if (
        enquiryErrors.name ||
        enquiryErrors.phone ||
        enquiryErrors.email ||
        enquiryErrors.visiting_time
    ) {
        return;
    }

    try {

        enquiryLoading.value = true;

        const response = await axios.post(
            "/api/method/dwell_in_door.api.crmlead.detaip_page_coatct",
            {
                name: enquiryForm.name,
                phone: enquiryForm.phone,
                email: enquiryForm.email,
                visiting_time: enquiryForm.visiting_time,
                project_name: props.project.project_name
            }
        );
        console.log(response.data);

        enquirySuccess.value =
            response?.data?.message?.message ||
            response?.data?.message ||
            "Thank you for your interest.";

        setTimeout(() => {
            enquirySuccess.value = ""
        }, 6000);
        enquiryForm.name = "";
        enquiryForm.phone = "";
        enquiryForm.email = "";
        enquiryForm.visiting_time = "";
        enquiryForm.message = "";

        enquiryErrors.name = "";
        enquiryErrors.phone = "";
        enquiryErrors.email = "";
        enquiryErrors.visiting_time = "";

    } catch (error) {

        enquiryError.value =
            error?.response?.data?.message ||
            "Something went wrong. Please try again.";

    } finally {

        enquiryLoading.value = false;

    }
};
</script>