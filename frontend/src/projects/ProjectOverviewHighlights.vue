<template>
    <!-------------- Next Section - 2 --------------->
    <section class="my-10 bg-white mx-auto md:mx-10">
        <div class="max-w-[1400px] mx-auto px-4">

            <div class="grid grid-cols-1 lg:grid-cols-12 gap-10">

                <!-- ================= LEFT : PROJECT OVERVIEW ================= -->

                <div
                    :class="
                        project.project_highlights?.length
                            ? 'lg:col-span-4'
                            : 'lg:col-span-12'
                    "
                >

                    <!-- HEADING -->
                    <div class="text-center mb-6">

                        <h2 class="text-[22px] font-bold text-[#1B1B1B]">
                            Project Overview
                        </h2>

                        <div
                            class="w-16 h-[2px] bg-[#D4AF37] mx-auto rounded-full"
                        ></div>

                    </div>


                    <!-- ================= DESCRIPTION ================= -->

                    <div
                        v-if="project.long__descrption"
                        class="text-gray-600 text-[14px] leading-6"
                    >

                        <!-- FULL DESCRIPTION -->
                        <template v-if="showFullDescription">

                            <div
                                v-html="project.long__descrption"
                            ></div>

                        </template>


                        <!-- SHORT DESCRIPTION -->
                        <template v-else>

                            {{
                                stripHtml(project.long__descrption).slice(
                                    0,
                                    150
                                )
                            }}

                            <span
                                v-if="
                                    stripHtml(project.long__descrption)
                                        .length > 150
                                "
                            >
                                ...
                            </span>

                        </template>

                    </div>


                    <!-- DESCRIPTION READ MORE -->
                    <button
                        v-if="
                            project.long__descrption &&
                            stripHtml(project.long__descrption).length > 150
                        "
                        @click="
                            showFullDescription =
                                !showFullDescription
                        "
                        class="text-[#0D5C63] font-medium mt-2"
                    >
                        {{
                            showFullDescription
                                ? "Read Less"
                                : "Read More"
                        }}
                    </button>


                    <!-- ================= PROJECT INFORMATION ================= -->

                    <div class="mt-4 space-y-2">

                        <!-- LAND AREA -->
                        <div
                            v-if="project.total_area"
                            class="flex justify-between border-b pb-3"
                        >

                            <span class="font-medium text-[14px]">
                                Land Area
                            </span>

                            <span class="text-gray-600 text-[14px]">
                                {{ project.total_area }}
                            </span>

                        </div>


                        <!-- CONFIGURATION -->
                        <div
                            v-if="project.configuration"
                            class="flex justify-between border-b pb-3"
                        >

                            <span class="font-medium text-[14px]">
                                Configuration
                            </span>

                            <span class="text-gray-600 text-[14px]">
                                {{ project.configuration }}
                            </span>

                        </div>


                        <!-- ================= KNOW MORE CONTENT ================= -->

                        <template v-if="showOverviewDetails">

                            <!-- FLOORS -->
                            <div
                                v-if="project.floors"
                                class="flex justify-between border-b pb-3"
                            >

                                <span class="font-medium text-[14px]">
                                    Floors
                                </span>

                                <span class="text-gray-600 text-[14px]">
                                    {{ project.floors }}
                                </span>

                            </div>


                            <!-- POSSESSION -->
                            <div
                                v-if="project.possession"
                                class="flex justify-between border-b pb-3"
                            >

                                <span class="font-medium text-[14px]">
                                    Possession
                                </span>

                                <span class="text-gray-600 text-[14px]">
                                    {{ project.possession }}
                                </span>

                            </div>

                        </template>

                    </div>


                    <!-- ================= KNOW MORE BUTTON ================= -->

                    <button
                        v-if="
                            project.floors ||
                            project.possession ||
                            project.brochure
                        "
                        @click="
                            showOverviewDetails =
                                !showOverviewDetails
                        "
                        class="text-[#0D5C63] font-medium mt-3"
                    >

                        {{
                            showOverviewDetails
                                ? "Know Less"
                                : "Know More"
                        }}

                    </button>


                    <!-- ================= BROCHURE ================= -->

                    <!-- Brochure will show only after Know More -->

                    <button
                        v-if="
                            showOverviewDetails &&
                            project.brochure
                        "
                        @click="downloadBrochure"
                        class="mt-4 bg-[#0D5C63] text-white px-4 py-2 rounded-xl font-medium flex items-center gap-2"
                    >

                        Download Brochure

                        <span class="material-symbols-outlined">
                            download
                        </span>

                    </button>

                </div>


                <!-- ================= RIGHT : PROJECT HIGHLIGHTS ================= -->

                <div
                    v-if="project.project_highlights?.length"
                    class="lg:col-span-8"
                >

                    <!-- HEADING -->
                    <div class="text-center mb-6">

                        <h2 class="text-[22px] font-bold text-[#1B1B1B]">
                            Project Highlights
                        </h2>

                        <div
                            class="w-16 h-[2px] bg-[#D4AF37] mx-auto rounded-full"
                        ></div>

                    </div>


                    <!-- ================= HIGHLIGHTS GRID ================= -->

                    <div
                        class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 items-start"
                    >

                        <template
                            v-for="(item, index) in project.project_highlights"
                            :key="index"
                        >

                            <!-- HIGHLIGHT CARD -->

                            <div
                                v-if="
                                    item.highlight_title ||
                                    item.project_descrption_high
                                "
                                class="border border-gray-200 rounded-xl p-3 flex items-start gap-3 bg-white min-h-[95px]"
                            >

                                <!-- ================= SAME ICON FOR EVERY HIGHLIGHT ================= -->

                                <div
                                    class="w-10 h-10 rounded-lg bg-[#F4F8F8] flex items-center justify-center flex-shrink-0"
                                >

                                    <span
                                        class="material-symbols-outlined text-[#0D5C63] text-[18px]"
                                    >
                                        star
                                    </span>

                                </div>


                                <!-- ================= HIGHLIGHT CONTENT ================= -->

                                <div>

                                    <!-- TITLE -->
                                    <h3
                                        v-if="item.highlight_title"
                                        class="font-semibold text-[14px] leading-4"
                                    >
                                        {{ item.highlight_title }}
                                    </h3>


                                    <!-- DESCRIPTION -->
                                    <p
                                        v-if="item.project_descrption_high"
                                        class="text-gray-500 text-[12px] mt-1 leading-4"
                                    >
                                        {{ item.project_descrption_high }}
                                    </p>

                                </div>

                            </div>

                        </template>

                    </div>

                </div>

            </div>

        </div>
    </section>
</template>


<script setup>
import { ref } from "vue";


// ============================================================
// PROPS
// ============================================================

const props = defineProps({
    project: {
        type: Object,
        required: true
    }
});


// ============================================================
// DESCRIPTION READ MORE / READ LESS
// ============================================================

const showFullDescription = ref(false);


// ============================================================
// PROJECT OVERVIEW KNOW MORE / KNOW LESS
// ============================================================

const showOverviewDetails = ref(false);


// ============================================================
// STRIP HTML TAGS
// ============================================================

const stripHtml = (html) => {

    if (!html) {
        return '';
    }

    const tmp = document.createElement("div");

    tmp.innerHTML = html;

    return tmp.textContent || tmp.innerText || '';
};


// ============================================================
// DOWNLOAD BROCHURE
// ============================================================

const downloadBrochure = () => {

    if (props.project?.brochure) {

        const link = document.createElement("a");

        link.href =
            window.location.origin +
            props.project.brochure;

        link.download = "";

        document.body.appendChild(link);

        link.click();

        document.body.removeChild(link);
    }
};
</script>