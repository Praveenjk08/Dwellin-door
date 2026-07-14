<template>
    <section class="bg-white overflow-hidden mb-10">

        <div class="grid grid-cols-1 md:grid-cols-2 md:h-[400px]">

            <!-- Left Content -->
            <div class="relative bg-[#FAF8F2] flex items-center">

                <!-- Curved Shape -->
                <div
                    class="hidden md:block absolute top-0 right-[-120px] w-[350px] h-full bg-[#F3EEE3] rounded-l-[250px]">
                </div>

                <div class="relative z-10 px-6 py-12 md:px-12">

                    <p class="uppercase tracking-[3px] text-[#0D5C63] font-semibold mb-3">
                        About Us
                    </p>

                    <h1 class="text-3xl sm:text-4xl md:text-5xl font-bold leading-tight mb-4 text-black">
                        Crafting Spaces,
                        <br>
                        <span class="text-[#0D5C63]">
                            Creating Lifestyles
                        </span>
                    </h1>

                    <p class="text-gray-600 text-base md:text-lg leading-7 mb-6 max-w-[500px]">
                        At Dwellin Door, we believe a home is more than just a
                        place—it's where life happens. We help families discover
                        exceptional properties that inspire comfort, growth,
                        and lasting memories.
                    </p>

                    <div class="flex flex-wrap gap-3">

                        <button
                            class="bg-[#0D5C63] text-white px-4 py-2 rounded-xl font-semibold hover:bg-[#08474d] transition">
                            Explore Properties
                        </button>

                        <button
                            class="border border-[#0D5C63] text-[#0D5C63] px-4 py-2 rounded-xl font-semibold hover:bg-[#0D5C63] hover:text-white transition">
                            Contact Us
                        </button>

                    </div>

                </div>

            </div>

            <!-- Right Image -->
            <div class="h-[280px] sm:h-[350px] md:h-[400px] overflow-hidden">

                <img :src="getFileUrl('About-us-page-banner.jpeg')" alt="Luxury Villa"
                    class="w-full h-full object-cover" />

            </div>

        </div>

    </section>
    <!--Section-2-->
    <WhoWEAre />
    <!--Section-3-->
    <StatsCrads />
    <!--Section-4-->
    <OurExprience />

    <!--Section-5-->
    <CustomerReview />



</template>
<script setup>

import CustomerReview from './CustomerReview.vue';
import OurExprience from './OurExprience.vue';
import StatsCrads from './StatsCrads.vue';
import WhoWEAre from './WhoWEAre.vue';
const getFileUrl = (file) => {
    return `${window.location.origin}/files/${file}`;
};

</script>