<template>
    <section class="pb-20 pt-2 lg:mx-40">

        <div class="max-w-[1400px] mx-auto px-4">

            <div class="grid grid-cols-1 lg:grid-cols-2 gap-10 lg:gap-16 items-center">

                <!-- Left Images -->
                <div class="grid grid-cols-1 md:grid-cols-[45%_55%] gap-5">

                    <div class="flex flex-col gap-5">

                        <img :src="getFileurl('cta-1.png')" alt="Luxury apartment interior by Dwell In Door"
                            class="w-full h-[220px] md:h-[220px] object-cover rounded-[10px]" />

                        <img :src="getFileurl('cta-2.png')"   alt="Premium villa exterior by Dwell In Door"
                            class="w-full h-[220px] md:h-[220px] object-cover rounded-[10px]" />

                    </div>

                    <div>

                        <img :src="getFileurl('cta-3.png')" alt="Modern real estate property in Bangalore by Dwell In Door"
                            class="w-full h-[300px] md:h-[460px] object-cover rounded-[10px]" />

                    </div>

                </div>

                <!-- Right Content -->
                <div>

                    <div class="flex items-center gap-2 mb-3">

                        <span class="material-symbols-outlined text-[#17C08E] text-[18px]">
                            home
                        </span>

                        <span class="text-[15px] font-medium text-[#435768]">
                             Real Estate FAQs
                        </span>

                    </div>

                    <h2 class="text-[28px] md:text-[33px] font-semibold leading-tight text-[#131A20]">
                        Frequently Asked Questions About Buying Property in Bangalore
                    </h2>

                    <p class="text-[#8B8B8B] text-[12px] leading-6 mt-3 mb-4">
                        Find answers to common questions about buying apartments, 
                        villas and residential plots in Bangalore. Dwell In Door
                         helps you choose verified real estate properties with 
                         confidence.
                    </p>

                    <!-- FAQ List -->
                    <div class="space-y-4">

                        <div v-for="(faq, index) in faqs" :key="index"
                            class="bg-[#F4F4F4] rounded-[18px] overflow-hidden" @mouseenter="activeIndex = index"
                            @mouseleave="activeIndex = null">

                            <div class="w-full flex justify-between items-center px-4 py-4 text-left">

                                <span class="text-[14px] font-medium text-[#222]">
                                    {{ index + 1 }}. {{ faq.question }}
                                </span>

                                <span class="material-symbols-outlined">
                                    {{ activeIndex === index ? 'remove' : 'expand_more' }}
                                </span>

                            </div>

                            <div class="overflow-hidden transition-all duration-500 ease-in-out" :class="activeIndex === index
                                ? 'max-h-40 opacity-100 pb-4'
                                : 'max-h-0 opacity-0'">
                                <div class="px-4 text-[#777] text-[14px] leading-7">
                                    {{ faq.answer }}
                                </div>
                            </div>
                        </div>

                    </div>

                    <p class="text-[#8B8B8B] text-[12px] leading-6 mt-4">
                        Discover a diverse range of premium properties through Dwell In Door,
                        from luxurious apartments to spacious villas tailored to your lifestyle.
                    </p>

                </div>

            </div>

        </div>

    </section>
</template>

<script setup>
import { ref } from "vue";

const activeIndex = ref(null);

// const toggleFaq = (index) => {
//     activeIndex.value =
//         activeIndex.value === index ? null : index;
// };

const faqs = [
    {
        question: "Can I customize my apartment or villa?",
        answer:
            "Yes. Many apartments and villas offer customization options based on the builder, project stage and availability."
    },
    {
        question: "How can I find properties through Dwell In Door?",
        answer:
            "You can browse apartments, villas, plots, and premium real estate projects listed on Dwell In Door."
    },
    {
        question: "What are the steps to buy a property?",
        answer:
            "Select a property, schedule a visit, verify documents, arrange financing, and complete the registration process."
    }
];

const getFileurl = (file) => {

    return `${window.location.origin}/files/${file}`
}
</script>