<template>
    <!--------------Next SEction -2--------------->
    <section class="my-10 bg-white mx-auto md:mx-10">
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


</template>

<script setup>
import { ref } from "vue";

const props = defineProps({
    project: {
        type: Object,
        required: true
    }
});

const showFullDescription = ref(false);

const downloadBrochure = () => {
    if (props.project?.brochure) {
        const link = document.createElement("a");
        link.href = window.location.origin + props.project.brochure;
        link.download = "";
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }
};
</script>