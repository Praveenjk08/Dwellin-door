<template>
    <!-----Section-3----->
    <section
        class="my-10 bg-white mx-auto md:mx-10"
        v-if="
            project.property_configuartion?.length ||
            project.property_amenities?.length
        "
    >
        <div class="max-w-[1400px] mx-auto px-4">

            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 lg:gap-10">

                <!-- ================= LEFT : PRICE ================= -->

                <div
                    v-if="project.property_configuartion?.length"
                    :class="
                        project.property_amenities?.length
                            ? 'lg:col-span-5'
                            : 'lg:col-span-12'
                    "
                >

                    <div class="text-center mb-6">

                        <h2 class="text-[22px] font-bold text-[#1B1B1B]">
                            Price & Configuration
                        </h2>

                        <div
                            class="w-16 h-[2px] bg-[#D4AF37] mx-auto rounded-full"
                        ></div>

                    </div>


                    <!-- PRICE TABLE -->

                    <div
                        class="border border-gray-200 rounded-2xl overflow-x-auto"
                    >

                        <table class="w-full">

                            <thead class="bg-[#F8FAFA]">

                                <tr>

                                    <th class="p-3 md:p-4 text-left">
                                        Type
                                    </th>

                                    <th class="p-3 md:p-4 text-left">
                                        Area
                                    </th>

                                    <th class="p-3 md:p-4 text-left">
                                        Price
                                    </th>

                                    <th class="p-3 md:p-4 text-center">
                                        Action
                                    </th>

                                </tr>

                            </thead>


                            <tbody>

                                <template
                                    v-for="(item, index) in project.property_configuartion"
                                    :key="index"
                                >

                                    <!--
                                        First 3 rows are always visible.
                                        Remaining rows appear after See More.
                                    -->
                                    <tr
                                        v-if="
                                            (item.bhktype ||
                                            item.area ||
                                            item.price) &&
                                            (index < 2 || showAllConfigurations)
                                        "
                                        class="border-t"
                                    >

                                        <!-- TYPE -->

                                        <td
                                            class="p-3 md:px-6 md:py-4 font-medium"
                                        >
                                            {{ item.bhktype }}
                                        </td>


                                        <!-- AREA -->

                                        <td
                                            class="p-3 md:px-6 md:py-4"
                                        >
                                            {{ item.area }}
                                        </td>


                                        <!-- PRICE -->

                                        <td
                                            class="p-3 md:px-6 md:py-4 font-semibold"
                                        >
                                            <span v-if="item.price">
                                                ₹ {{ item.price }}
                                            </span>
                                        </td>


                                        <!-- ACTION -->

                                        <td
                                            class="p-3 md:px-6 md:py-4 text-center"
                                        >

                                            <button
                                                @click="
                                                    router.push('/contact-us')
                                                "
                                                class="bg-[#0D5C63] text-white text-sm px-5 py-2 rounded-xl font-sm shadow-sm hover:bg-[#084950] transition"
                                            >
                                                Enquire
                                            </button>

                                        </td>

                                    </tr>

                                </template>

                            </tbody>

                        </table>

                    </div>


                    <!-- ================= SEE MORE / SEE LESS ================= -->

                    <div
                        v-if="project.property_configuartion.length > 2"
                        class="flex justify-center mt-4"
                    >

                        <button
                            @click="
                                showAllConfigurations =
                                    !showAllConfigurations
                            "
                            class="text-[#0D5C63] font-medium text-sm hover:text-[#084950] transition"
                        >

                            {{
                                showAllConfigurations
                                    ? "See Less"
                                    : "See More"
                            }}

                        </button>

                    </div>

                </div>


                <!-- ================= RIGHT : AMENITIES ================= -->

                <div
                    v-if="project.property_amenities?.length"
                    :class="
                        project.property_configuartion?.length
                            ? 'lg:col-span-7'
                            : 'lg:col-span-12'
                    "
                >

                    <div class="text-center mb-6">

                        <h2 class="text-[22px] font-bold text-[#1B1B1B]">
                            Top Amenities
                        </h2>

                        <div
                            class="w-16 h-[2px] bg-[#D4AF37] mx-auto rounded-full"
                        ></div>

                    </div>


                    <div
                        class="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-5"
                    >

                        <template
                            v-for="(item, index) in project.property_amenities"
                            :key="index"
                        >

                            <div
                                v-if="item.amenity_name"
                                class="text-center"
                            >

                                <!-- AMENITY IMAGE -->

                                <div
                                    class="w-16 h-16 md:w-20 md:h-20 mx-auto border border-gray-200 rounded-xl flex items-center justify-center bg-white overflow-hidden"
                                >

                                    <img
                                        v-if="item.custom_amenity_image"
                                        :src="
                                            getImageUrl(
                                                item.custom_amenity_image
                                            )
                                        "
                                        :alt="
                                            item.amenity_name || 'Amenity'
                                        "
                                        class="w-8 h-8 md:w-10 md:h-10 object-contain"
                                    />


                                    <span
                                        v-else
                                        class="text-gray-300 text-xs"
                                    >
                                        No Icon
                                    </span>

                                </div>


                                <!-- AMENITY NAME -->

                                <p class="text-xs md:text-sm mt-2">
                                    {{ item.amenity_name }}
                                </p>

                            </div>

                        </template>

                    </div>

                </div>

            </div>

        </div>
    </section>
</template>


<script setup>
import { ref } from 'vue'
import router from '../router.js'


defineProps({
    project: {
        type: Object,
        required: true
    }
})


/*
|--------------------------------------------------------------------------
| See More / See Less
|--------------------------------------------------------------------------
*/

const showAllConfigurations = ref(false)


/*
|--------------------------------------------------------------------------
| Frappe Image URL
|--------------------------------------------------------------------------
| Handles:
| /files/image.png
| and
| https://your-site.com/files/image.png
*/

const getImageUrl = (image) => {

    if (!image) {
        return ''
    }

    // Already a complete URL
    if (
        image.startsWith('http://') ||
        image.startsWith('https://')
    ) {
        return image
    }

    // Frappe relative file path
    if (image.startsWith('/')) {
        return `${window.location.origin}${image}`
    }

    // Frappe path without /
    return `${window.location.origin}/${image}`
}
</script>