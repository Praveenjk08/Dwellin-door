<template>
    <section class="pb-20 pt-5 lg:mx-40">

        <div class="max-w-[1400px] mx-auto px-4">

            <div class="grid grid-cols-1 lg:grid-cols-2 gap-10 lg:gap-16 items-center">

                <!-- Left Images -->
                <div class="grid grid-cols-1 md:grid-cols-[45%_55%] gap-5">

                    <div class="flex flex-col gap-5">

                        <img :src="getFileurl('abouask-image-1.png')"
                            class="w-full h-[220px] md:h-[220px] object-cover rounded-[10px]" />

                        <img :src="getFileurl('abouask-image-2.png')"
                            class="w-full h-[220px] md:h-[220px] object-cover rounded-[10px]" />

                    </div>

                    <div>

                        <img :src="getFileurl('abouask-image-3.png')"
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
                            FAQs
                        </span>

                    </div>

                    <h2 class="text-[28px] md:text-[33px] font-semibold leading-tight text-[#131A20]">
                        Everything about Dwell In Door
                    </h2>

                    <p class="text-[#8B8B8B] text-[12px] leading-6 mt-3 mb-4">
                        We know that buying, selling, or investing in real estate can be overwhelming.
                        Here are some frequently asked questions about Dwell In Door to help guide
                        you through the process.
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
        question: "Can I personalize my property?",
        answer:
            "Yes, many properties offer customization options depending on the builder and project stage."
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