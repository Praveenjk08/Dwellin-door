<template>
    <!-----Section-3----->
    <section class="my-10 bg-white mx-auto md:mx-10 ">
        <div class="max-w-[1400px] mx-auto px-4">

            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 lg:gap-10">

                <!-- LEFT SIDE -->


                <div class="lg:col-span-5">

                    <div class="flex items-center justify-between">
                        <h2 class="text-[22px] font-bold">
                            Price & Configuration
                        </h2>
                    </div>

                    <div class="w-16 h-[2px] bg-[#D4AF37] mb-4 rounded-full"></div>

                    <div class="border border-gray-200 rounded-2xl overflow-x-auto">

                        <table class="w-full">

                            <thead class="bg-[#F8FAFA]">
                                <tr>
                                    <th class="p-3 md:p-4 text-left">Type</th>
                                    <th class="p-3 md:p-4 text-left">Area</th>
                                    <th class="p-3 md:p-4 text-left">Price</th>
                                    <th class="p-3 md:p-4 text-center">Action</th>
                                </tr>
                            </thead>

                            <tbody>

                                <tr v-for="(item, index) in project.property_configuartion" :key="index"
                                    class="border-t">
                                    <td class="p-3 md:px-6 md:py-4 font-medium">
                                        {{ item.bhktype }}
                                    </td>

                                    <td class="p-3 md:px-6 md:py-4">
                                        {{ item.area }}
                                    </td>

                                    <td class="p-3 md:px-6 md:py-4 font-semibold">
                                        ₹ {{ item.price }}
                                    </td>

                                    <td class="p-3 md:px-6 md:py-4 text-center">
                                        <button class="bg-[#0D5C63] text-white px-3 md:px-4 py-2 rounded-lg text-sm">
                                            Enquire
                                        </button>
                                    </td>
                                </tr>

                                <tr
                                    v-if="!project.property_configuartion || project.property_configuartion.length === 0">
                                    <td colspan="4" class="text-center py-6 text-gray-500">
                                        No Configuration Available
                                    </td>
                                </tr>

                            </tbody>

                        </table>

                    </div>

                </div>



                <div class="lg:col-span-7">

                    <div class="text-center mb-6">
                        <h2 class="text-[22px] font-bold text-[#1B1B1B]">
                            Top Amenities
                        </h2>

                        <div class="w-16 h-[2px] bg-[#D4AF37] mx-auto rounded-full"></div>
                    </div>

                    <div class="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-5">

                        <div v-for="(item, index) in project.property_amenities" :key="index" class="text-center">
                            <div
                                class="w-16 h-16 md:w-20 md:h-20 mx-auto border border-gray-200 rounded-xl flex items-center justify-center">
                                <span class="material-symbols-outlined text-[#0D5C63] text-[24px] md:text-[32px]">
                                    {{ item.amenity_icon }}
                                </span>
                            </div>

                            <p class="text-xs md:text-sm mt-2">
                                {{ item.amenity_name }}
                            </p>
                        </div>

                    </div>

                </div>

            </div>

        </div>
    </section>


</template>







<script setup>
defineProps({
    project: {
        type: Object,
        required: true
    }
});
</script>