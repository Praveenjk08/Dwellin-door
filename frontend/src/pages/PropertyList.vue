<template>


    <!-- <main class="grid grid-cols-1 lg:grid-cols-12 gap-6 ">
        ...
    </main> -->

    <main class="grid grid-cols-1 lg:grid-cols-12 gap-6 min-h-screen">


        <aside class="lg:col-span-3 bg-white rounded-2xl  p-4 md:p-5
           mb-0  lg:mb-0
           lg:sticky lg:top-24
           lg:h-[calc(100vh-120px)]
           lg:overflow-y-auto">

            <h2 class="font-bold text-xl md:text-2xl mb-6">
                Filters
            </h2>

            <!-- Location -->
            <div class="mb-6 md:mb-8">
                <h3 class="font-semibold mb-3">
                    Location
                </h3>

                <div class="flex flex-wrap gap-2">
                    <button v-for="location in locations" :key="location" @click="selectLocation(location)" :class="[
                        'px-3 md:px-4 py-2 border rounded-full text-xs md:text-sm transition',
                        selectedLocation.includes(location)
                            ? 'bg-[#0D5C63] text-white'
                            : 'bg-white'
                    ]">

                        {{ location }}

                    </button>
                </div>
            </div>

            <!-- BHK -->
            <div class="mb-6 md:mb-8">
                <h3 class="font-semibold mb-3">
                    Bath Type
                </h3>

                <div class="flex flex-wrap gap-2">
                    <button v-for="type in propertyTypes" :key="type" @click="selectBhk(type)" :class="[
                        'px-3 md:px-4 py-2 border rounded-full text-xs md:text-sm transition',
                        selectedBhk.includes(type)
                            ? 'bg-[#0D5C63] text-white'
                            : 'bg-white'
                    ]">

                        {{ type }}

                    </button>
                </div>
            </div>

            <!-- Bedrooms -->
            <div class="mb-6 md:mb-8">
                <h3 class="font-semibold mb-3">
                    Bedrooms Type
                </h3>

                <div class="flex flex-wrap gap-2">
                    <button v-for="type in bedroomsType" :key="type" @click="selectBedroom(type)" :class="[
                        'px-3 md:px-4 py-2 border rounded-full text-xs md:text-sm transition',
                        selectedBedroom.includes(type)
                            ? 'bg-[#0D5C63] text-white border-[#0D5C63]'
                            : 'bg-white'
                    ]">

                        {{ type }}

                    </button>
                </div>
            </div>

            <div class="flex flex-col sm:flex-row gap-3 sm:gap-4">

                <!-- <button @click="applyFilters" class="w-full bg-[#0D5C63] text-white py-2.5 rounded-lg font-medium">

                    Apply Filters

                </button> -->

                <button @click="clearFilters"
                    class="w-full border border-[#0D5C63] text-[#0D5C63] py-2.5 rounded-lg font-medium">

                    Clear Filters

                </button>

            </div>

        </aside>
        <!-- Property Cards -->
        <section class="lg:col-span-9 bg-white">
            <div class="px-4 mt-0 md:mt-4 flex justify-center mb-2">
                <div class="relative w-full max-w-xl">

                    <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-gray-400">
                        search
                    </span>

                    <input v-model="searchProject" type="text" placeholder="Search by project name..."
                        class="w-full pl-10 pr-4 py-3 bg-white border border-gray-300 rounded-xl shadow-md outline-none focus:border-[#0D5C63]" />

                </div>
            </div>

            <section class="p-4">

                <div v-if="filteredProjects.length > 0" class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4">

                    <div v-for="(item, index) in filteredProjects" :key="index"
                        @click="router.push(`/properties/${item.url}`)"
                        class="bg-white rounded-lg shadow-lg border border-gray-200 overflow-hidden cursor-pointer">

                        <!-- Property Image -->
                        <div class="p-2">
                            <img :src="item.image" :alt="item.property_name"
                                class="w-full h-[220px] rounded-lg object-cover" />
                        </div>

                        <div class="p-4">

                            <!-- Property Name & Price -->
                            <div class="flex justify-between items-start gap-2">

                                <div>
                                    <h3 class="text-[18px] font-semibold text-[#1F2937]">
                                        {{ item.project_name }} </h3>

                                    <p class="text-gray-600 mt-1 text-[14px] flex items-center gap-1">

                                        <span class="material-symbols-outlined text-[18px]">
                                            location_on
                                        </span>

                                        {{ item.location }}
                                    </p>
                                </div>

                                <span
                                    class="bg-[#E8F8F3] text-[#35CAA0] px-3 py-2 rounded-full text-sm font-medium whitespace-nowrap">

                                    ₹ {{ item.price }}

                                </span>

                            </div>

                            <!-- Property Details -->
                            <div class="grid grid-cols-3 mt-5 pt-5 border-t border-gray-200">

                                <div class="text-center">

                                    <span class="material-symbols-outlined">
                                        bed
                                    </span>

                                    <p class="mt-2 text-sm">
                                        {{ item.bedrooms }}
                                    </p>

                                </div>

                                <div class="text-center border-x border-gray-200">

                                    <span class="material-symbols-outlined">
                                        bathtub
                                    </span>

                                    <p class="mt-2 text-sm">
                                        {{ item.bathrooms }}
                                    </p>

                                </div>

                                <div class="text-center">

                                    <span class="material-symbols-outlined">
                                        crop_free
                                    </span>

                                    <p class="mt-2 text-sm">
                                        {{ item.area }} Sq.ft
                                    </p>

                                </div>

                            </div>



                        </div>

                    </div>
                </div>
                <div v-else-if="filterApplied" class="text-center py-20">

                    <h2 class="text-2xl font-bold text-red-500">
                        Property Not Found
                    </h2>

                    <p class="text-gray-500 mt-2">
                        No properties available for selected filters.
                    </p>

                </div>

            </section>

        </section>

    </main>
</template>

<script setup>
import axios from 'axios'
import { computed, onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const router = useRouter()
const goToDetailPage = () => {
    router.push(`/properties/${url}`)
}

const selectedLocation = ref([])
const selectedBhk = ref([])
const selectedBedroom = ref([])

const locations = [
    'East',
    'West',
    'North',
    'South'
]

const propertyTypes = [
    '1 Bathrooms',
    '2 Bathrooms',
    '3 Bathrooms',
    '4 Bathrooms',
    '5 Bathrooms'
]

const bedroomsType = [
    '1 Bedroom',
    '2 Bedroom',
    '3 Bedroom',
    '4 Bedroom',
    '5 Bedroom',
    '6 Bedroom'
]

// const selectLocation = (location) => {
//     selectedLocation.value = location
//     selectedLocation.value === location ? '' : location
// }

const selectLocation = (location) => {
    const index = selectedLocation.value.indexOf(location)

    if (index > -1) {
        selectedLocation.value.splice(index, 1)
    } else {
        selectedLocation.value.push(location)
    }
    applyFilters()
}
// const selectBhk = (bhk) => {
//     selectedBhk.value = bhk
//     selectedBhk.value === bhk ? '' : bhk
// }
const selectBhk = (bhk) => {
    const index = selectedBhk.value.indexOf(bhk)

    if (index > -1) {
        selectedBhk.value.splice(index, 1)
    } else {
        selectedBhk.value.push(bhk)
    }
    applyFilters()
}

// const selectBedroom = (bedroom) => {
//     selectedBedroom.value = bedroom

// }
const selectBedroom = (bedroom) => {
    const index = selectedBedroom.value.indexOf(bedroom)

    if (index > -1) {
        selectedBedroom.value.splice(index, 1)
    } else {
        selectedBedroom.value.push(bedroom)
    }
    applyFilters()
}

const applyFilters1 = () => {
    const filters = {
        location: selectedLocation.value,
        bhk: selectedBhk.value,
        bedroom: selectedBedroom.value
    }

    console.log(filters)
}
// const clearFilters = () => {
//     selectedLocation.value = ''
//     selectedBhk.value = ''
//     selectedBedroom.value = ''
// }
const clearFilters = () => {
    selectedLocation.value = []
    selectedBhk.value = []
    selectedBedroom.value = []
    get_all_property_detils_api()
}





const api_propertydetils = ref([])
const get_all_property_detils_api = async () => {
    try {

        const response = await axios.get("api/method/dwell_in_door.api.propertdetail.get_property_detils_for_cards")

        api_propertydetils.value = response.data.message
        console.log(api_propertydetils.value.message);

    }
    catch (error) {
        console.log(error);

    }

}
const filterApplied = ref(false)

const applyFilters = async () => {
    try {
        console.log("Location:", selectedLocation.value)
        console.log("Bathrooms:", selectedBhk.value)
        console.log("Bedrooms:", selectedBedroom.value)

        filterApplied.value = true
        const response = await axios.get(
            "/api/method/dwell_in_door.api.propertdetail.list_get_property_detils_for_cards",
            {
                params: {
                    property_location_type: JSON.stringify(selectedLocation.value),
                    bathrooms: JSON.stringify(selectedBhk.value),
                    bedroom: JSON.stringify(selectedBedroom.value)
                }
            }
        )

        console.log(response.data)

        api_propertydetils.value = response.data.message

        console.log(api_propertydetils.value)

    } catch (error) {
        console.log(error)
    }
}

const searchProject = ref('')
const filteredProjects = computed(() => {
    return api_propertydetils.value.filter(item =>
        item.project_name
            ?.toLowerCase()
            .includes(searchProject.value.toLowerCase())
    )
})
// onMounted(() => {
//     get_all_property_detils_api()

// })
const route = useRoute()

onMounted(() => {

    if (route.query.location) {

        selectedLocation.value = [route.query.location]

        applyFilters()

    } else {

        get_all_property_detils_api()

    }

})

</script>

<style scoped>
aside::-webkit-scrollbar {
    width: 4px;
}

aside::-webkit-scrollbar-thumb {
    background: #cbd5e1;
    border-radius: 10px;
}
</style>