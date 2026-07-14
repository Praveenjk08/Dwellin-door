<template>
    <section class="relative h-[300px] md:h-[520px] overflow-hidden mb-10">

        <!-- Background Image -->
        <img :src="getFileUrl('About-us-banner.jpeg')" alt="About Us Banner"
            class="w-full h-[300px] md:h-[520px] object-cover" />

        <!-- Dark Overlay -->
        <div class="absolute inset-0 bg-black/50"></div>

    </section>
    <section class="my-5 bg-white mx-4 md:mx-20">
        <div class="w-full mx-auto px-2 md:px-6">

            <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 md:gap-12 items-start">

                <!-- Left Content -->
                <div class="flex flex-col justify-center h-auto md:h-[350px]">

                    <span class="text-[#0D5C63] font-semibold uppercase text-[20px]">
                        Our Story
                    </span>

                    <h2 class="text-[18px] font-bold text-[#2f2f68] mt-2">
                        Opening Doors to New Possibilities
                    </h2>

                    <p class="text-gray-600 mt-4 leading-7">
                        Dwellin Door was founded with a simple belief that finding
                        the right property should be an exciting journey, not a
                        complicated process. We are passionate about helping
                        families, professionals, and investors discover spaces
                        that match their lifestyle and aspirations.
                    </p>

                    <p class="text-gray-600 mt-4 leading-7">
                        Through trusted partnerships, market expertise, and a
                        customer-first approach, we connect people with
                        opportunities that create lasting value. Every property
                        has a story, and we are here to help you find the one
                        that feels like home.
                    </p>

                </div>

                <!-- Right Image -->
                <div class="h-[250px] md:h-[350px]">
                    <img :src="getFileUrl('About-us-right-sid.jpeg')" alt="Our Story"
                        class="w-full h-full object-cover rounded-lg shadow-xl" />
                </div>

            </div>

        </div>
    </section>
    <section class="my-10 pt-6 pb-8 bg-gradient-to-br from-[#F1F8F8] to-[#F7FAFC] mx-4 md:mx-20 rounded-xl">
        <div class="px-4 md:px-6">

            <!-- Heading -->
            <div class="text-center mb-6 md:mb-8">
                <span class="text-[#0D5C63] font-semibold uppercase text-[16px] md:text-[20px]">
                    Our Values
                </span>

                <h2 class="text-[24px] md:text-[18px] font-bold text-[#2f2f68] mt-1">
                    What Drives Us Forward
                </h2>

                <p class="text-gray-600 mt-3 max-w-3xl mx-auto text-sm md:text-base">
                    Our commitment to excellence is built on a foundation of trust,
                    transparency, and customer satisfaction.
                </p>
            </div>

            <!-- Cards -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4 md:gap-6">

                <!-- Card 1 -->
                <div
                    class="bg-white p-6 md:p-8 rounded-xl shadow-md hover:shadow-2xl transition duration-300 hover:-translate-y-1">

                    <div class="w-14 h-14 bg-[#0D5C63]/10 rounded-full flex items-center justify-center mb-5">
                        <i class="bi bi-shield-check text-[#0D5C63] text-[25px]"></i>
                    </div>

                    <h3 class="text-lg md:text-xl font-semibold text-[#2f2f68] mb-3">
                        Trust & Transparency
                    </h3>

                    <p class="text-gray-600 leading-6 md:leading-7 text-sm md:text-base">
                        We believe every client deserves honest guidance and complete
                        transparency throughout their property journey.
                    </p>

                </div>

                <!-- Card 2 -->
                <div
                    class="bg-white p-6 md:p-8 rounded-xl shadow-md hover:shadow-2xl transition duration-300 hover:-translate-y-1">

                    <div class="w-14 h-14 bg-[#0D5C63]/10 rounded-full flex items-center justify-center mb-5">
                        <i class="bi bi-people text-[#0D5C63] text-[25px]"></i>
                    </div>

                    <h3 class="text-lg md:text-xl font-semibold text-[#2f2f68] mb-3">
                        Customer First
                    </h3>

                    <p class="text-gray-600 leading-6 md:leading-7 text-sm md:text-base">
                        Every recommendation we make is centered around the unique
                        needs and aspirations of our clients.
                    </p>

                </div>

                <!-- Card 3 -->
                <div
                    class="bg-white p-6 md:p-8 rounded-xl shadow-md hover:shadow-2xl transition duration-300 hover:-translate-y-1">

                    <div class="w-14 h-14 bg-[#0D5C63]/10 rounded-full flex items-center justify-center mb-5">
                        <i class="bi bi-award text-[#0D5C63] text-[25px]"></i>
                    </div>

                    <h3 class="text-lg md:text-xl font-semibold text-[#2f2f68] mb-3">
                        Excellence
                    </h3>

                    <p class="text-gray-600 leading-6 md:leading-7 text-sm md:text-base">
                        We continuously strive to provide exceptional service and
                        create lasting value for our customers.
                    </p>

                </div>

            </div>

        </div>
    </section>

    <section class="my-12 mx-4 md:mx-20">
        <div class="text-center mb-10">

            <span class="text-[#0D5C63] font-semibold uppercase text-[16px] md:text-[20px]">
                Our Team
            </span>

            <h2 class="text-[24px] md:text-[32px] font-bold text-[#2f2f68] mt-2">
                Meet The People Behind Dwellin Door
            </h2>

            <p class="text-gray-600 mt-3 max-w-3xl mx-auto">
                Our dedicated team combines industry expertise, local market knowledge,
                and a passion for helping clients find the perfect property.
            </p>

        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">

            <!-- Team Member 1 -->
            <div class="bg-white rounded-xl overflow-hidden shadow-md hover:shadow-xl transition duration-300">

                <img :src="getFileUrl('founder.jpg')" alt="Founder" class="w-full h-[300px] object-cover">

                <div class="p-5 text-center">
                    <h3 class="text-xl font-semibold text-[#2f2f68]">
                        Praveen JK
                    </h3>

                    <p class="text-[#0D5C63] mt-1">
                        Founder & CEO
                    </p>
                </div>

            </div>

            <!-- Team Member 2 -->
            <div class="bg-white rounded-xl overflow-hidden shadow-md hover:shadow-xl transition duration-300">

                <img :src="getFileUrl('team-1.jpg')" alt="Sales Head" class="w-full h-[300px] object-cover">

                <div class="p-5 text-center">
                    <h3 class="text-xl font-semibold text-[#2f2f68]">
                        Raj Kumar
                    </h3>

                    <p class="text-[#0D5C63] mt-1">
                        Sales Director
                    </p>
                </div>

            </div>

            <!-- Team Member 3 -->
            <div class="bg-white rounded-xl overflow-hidden shadow-md hover:shadow-xl transition duration-300">

                <img :src="getFileUrl('team-2.jpg')" alt="Consultant" class="w-full h-[300px] object-cover">

                <div class="p-5 text-center">
                    <h3 class="text-xl font-semibold text-[#2f2f68]">
                        Sneha R
                    </h3>

                    <p class="text-[#0D5C63] mt-1">
                        Property Consultant
                    </p>
                </div>

            </div>

            <!-- Team Member 4 -->
            <div class="bg-white rounded-xl overflow-hidden shadow-md hover:shadow-xl transition duration-300">

                <img :src="getFileUrl('team-3.jpg')" alt="Marketing Manager" class="w-full h-[300px] object-cover">

                <div class="p-5 text-center">
                    <h3 class="text-xl font-semibold text-[#2f2f68]">
                        Arjun S
                    </h3>

                    <p class="text-[#0D5C63] mt-1">
                        Marketing Manager
                    </p>
                </div>

            </div>

        </div>
    </section>


    <section class="my-16 mx-4 md:mx-20">

        <div class="text-center mb-5">
            <span class="text-[#0D5C63] font-semibold uppercase text-[16px] md:text-[20px]">
                Why Dwellin Door
            </span>

            <h2 class="text-[24px] md:text-[18px] mt-1 font-bold text-[#2f2f68] ">
                Designed Around Your Needs
            </h2>

            <p class="text-gray-600 mt-1 max-w-2xl mx-auto">
                We focus on creating a smooth, transparent, and personalized
                property journey for every customer.
            </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">

            <!-- Card 1 -->
            <div class="flex gap-5 bg-white border border-gray-100 p-6 rounded-xl shadow-sm">
                <div class="w-14 h-14 bg-[#0D5C63]/10 rounded-full flex items-center justify-center flex-shrink-0">
                    <i class="bi bi-search text-[#0D5C63] text-2xl"></i>
                </div>

                <div>
                    <h3 class="text-xl font-semibold text-[#2f2f68]">
                        Smart Property Discovery
                    </h3>

                    <p class="text-gray-600 mt-2">
                        Find properties that truly match your lifestyle,
                        preferences, and investment goals.
                    </p>
                </div>
            </div>

            <!-- Card 2 -->
            <div class="flex gap-5 bg-white border border-gray-100 p-6 rounded-xl shadow-sm">
                <div class="w-14 h-14 bg-[#0D5C63]/10 rounded-full flex items-center justify-center flex-shrink-0">
                    <i class="bi bi-shield-check text-[#0D5C63] text-2xl"></i>
                </div>

                <div>
                    <h3 class="text-xl font-semibold text-[#2f2f68]">
                        Trusted Guidance
                    </h3>

                    <p class="text-gray-600 mt-2">
                        Receive honest advice and expert support throughout
                        your property journey.
                    </p>
                </div>
            </div>

            <!-- Card 3 -->
            <div class="flex gap-5 bg-white border border-gray-100 p-6 rounded-xl shadow-sm">
                <div class="w-14 h-14 bg-[#0D5C63]/10 rounded-full flex items-center justify-center flex-shrink-0">
                    <i class="bi bi-building text-[#0D5C63] text-2xl"></i>
                </div>

                <div>
                    <h3 class="text-xl font-semibold text-[#2f2f68]">
                        Quality Listings
                    </h3>

                    <p class="text-gray-600 mt-2">
                        Explore carefully selected residential and commercial
                        properties from trusted sources.
                    </p>
                </div>
            </div>

            <!-- Card 4 -->
            <div class="flex gap-5 bg-white border border-gray-100 p-6 rounded-xl shadow-sm">
                <div class="w-14 h-14 bg-[#0D5C63]/10 rounded-full flex items-center justify-center flex-shrink-0">
                    <i class="bi bi-headset text-[#0D5C63] text-2xl"></i>
                </div>

                <div>
                    <h3 class="text-xl font-semibold text-[#2f2f68]">
                        Dedicated Support
                    </h3>

                    <p class="text-gray-600 mt-2">
                        Our team is always ready to assist and answer your
                        questions at every stage.
                    </p>
                </div>
            </div>

        </div>

    </section>

    <!-- Trust & Recognition Section -->
    <section class="my-16 mx-4 md:mx-20">

        <!-- Heading -->
        <div class="text-center mb-10">
            <span class="text-[#0D5C63] font-semibold uppercase text-[16px] md:text-[20px]">
                Trust & Recognition
            </span>

            <h2 class="text-[24px] md:text-[36px] font-bold text-[#2f2f68] mt-2">
                Recognized For Excellence
            </h2>

            <p class="text-gray-600 mt-3 max-w-3xl mx-auto">
                Our dedication to quality service and customer satisfaction has earned
                recognition from clients and industry partners.
            </p>
        </div>

        <!-- Certificate Carousel -->
        <div class="mb-6">

            <h3 class="text-[20px] md:text-[28px] font-bold text-[#2f2f68] text-center mb-6">
                Certificates & Achievements
            </h3>

            <Carousel :items-to-show="3" :wrap-around="true" :autoplay="4000" :pause-autoplay-on-hover="true"
                :breakpoints="{
                    0: {
                        itemsToShow: 1
                    },
                    768: {
                        itemsToShow: 2
                    },
                    1024: {
                        itemsToShow: 3
                    }
                }">

                <Slide v-for="(certificate, index) in certificates" :key="index">
                    <div class="mx-3">

                        <div class="bg-white rounded-xl overflow-hidden shadow-lg">
                            <img :src="getFileUrl(certificate.image)" :alt="certificate.title"
                                class="w-full h-[280px] object-cover" />

                            <div class="p-4">
                                <h4 class="font-semibold text-[#2f2f68] text-center">
                                    {{ certificate.title }}
                                </h4>
                            </div>
                        </div>

                    </div>
                </Slide>

            </Carousel>

        </div>

        <!-- Reviews Carousel -->
        <div>

            <h3 class="text-[20px] md:text-[28px] font-bold text-[#2f2f68] text-center mb-6">
                What Our Clients Say
            </h3>

            <Carousel :items-to-show="3" :wrap-around="true" :autoplay="1000" :pause-autoplay-on-hover="true"
                :breakpoints="{
                    0: {
                        itemsToShow: 1
                    },
                    1024: {
                        itemsToShow: 3
                    }
                }">

                <Slide v-for="(review, index) in reviews" :key="index">
                    <div
                        class="bg-white p-8 rounded-xl shadow-lg mx-3 h-[240px] flex flex-col justify-center border border-gray-100">

                        <div class="text-[#D4AF37] text-[24px] mb-3">
                            ★★★★★
                        </div>

                        <p class="text-gray-600 italic leading-7">
                            {{ review.review }}
                        </p>

                        <div class="mt-6">
                            <h4 class="font-semibold text-[#2f2f68] text-lg">
                                {{ review.name }}
                            </h4>

                            <p class="text-[#0D5C63] text-sm">
                                {{ review.role }}
                            </p>
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
import { Carousel, Slide, Navigation } from 'vue3-carousel'
import 'vue3-carousel/dist/carousel.css'

const getFileUrl = (file) => {
    return `${window.location.origin}/files/${file}`;
};

const reviews = [
    {
        name: "Rajesh Kumar",
        role: "Home Buyer",
        review: "Excellent service and professional guidance throughout the buying process."
    },
    {
        name: "Sneha R",
        role: "Property Investor",
        review: "Very transparent and supportive team. Highly recommended."
    },
    {
        name: "Arjun S",
        role: "First-Time Buyer",
        review: "The entire experience was smooth from property selection to closure."
    },
    {
        name: "Priya M",
        role: "Investor",
        review: "Their expertise helped us find the perfect investment opportunity."
    }
]

const certificates = [
    {
        image: "ChatGPT Image Jul 13, 2026, 02_17_54 PM.png",
        title: "Excellence Award 2025"
    },
    {
        image: "ChatGPT Image Jul 13, 2026, 02_15_14 PM.png",
        title: "Trusted Real Estate Partner"
    },
    {
        image: "ChatGPT Image Jul 13, 2026, 02_08_59 PM.png",
        title: "Customer Choice Award"
    },
    {
        image: "ChatGPT Image Jul 13, 2026, 02_05_03 PM.png",
        title: "Industry Recognition"
    },
    {
        image: "ChatGPT Image Jul 13, 2026, 02_05_03 PM.png",
        title: "Best Property Consultant"
    }
]

</script>

<style>
/* .carousel__viewport {
    overflow: visible !important;
} */

.carousel__track {
    padding-bottom: 20px;
}
</style>