    <template>



        <!-- Gallery Hero -->
        <section class=" mx-auto px-6 lg:px-10 pt-5 pb-6">

            <div class="flex flex-col lg:flex-row justify-between gap-10">

                <div>
                    <p class="uppercase tracking-[0.2em] text-[#0D5C63] text-sm font-medium">
                        Gallery
                    </p>

                    <h1 class="text-5xl md:text-6xl lg:text-7xl font-bold text-gray-900 mt-2 leading-tight">
                        Explore Every
                        <br>
                        Beautiful Space
                    </h1>

                    <p class="text-gray-500 mt-2 text-lg max-w-xl leading-relaxed">
                        Discover premium apartments, villas, interiors, and thoughtfully
                        designed living spaces curated for modern lifestyles.
                    </p>
                </div>

                <div class="flex lg:justify-end">
                    <div class="w-40 h-40 rounded-[32px] bg-[#E8F4F5] flex flex-col items-center justify-center">
                        <h3 class="text-5xl font-bold text-[#0D5C63]">
                            <!-- 250+ -->{{ galleryCount }}
                        </h3>
                        <p class="text-gray-500 mt-2">
                            {{ tagsname }} Images
                        </p>

                    </div>
                </div>

            </div>

        </section>

        <section class="max-w-[1400px] mx-auto px-6 lg:px-10 pb-7">

            <div class="flex justify-center">

                <div
                    class="inline-flex flex-wrap justify-center gap-3 bg-[#F8FBFB] p-3 rounded-full shadow-sm border border-gray-100">

                    <button v-for="(tag, index) in tags" :key="index" @click="getGalleryByTag(tag.name)"
                        class="px-6 py-3 rounded-full bg-white text-gray-700 font-medium shadow-sm hover:bg-[#0D5C63] hover:text-white transition-all duration-300">
                        {{ tag.name }}
                    </button>

                </div>

            </div>

        </section>

        <!-- Gallery Grid -->
        <section class="md:mx-10    mx-auto px-6 lg:px-10 pb-24">

            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">

                <div v-for="(item, index) in paginatedGallery" :key="index"
                    class="relative group overflow-hidden rounded-[24px]">

                    <img :src="item.iamge"
                        class="w-full h-[240px] object-cover rounded-[24px] group-hover:scale-105 transition duration-500" />

                    <div
                        class="absolute top-3 right-3 w-10 h-10 bg-white rounded-full flex items-center justify-center shadow-md">
                        <span class="material-symbols-outlined text-gray-500">
                            favorite
                        </span>
                    </div>

                </div>

            </div>
         <div class="flex justify-center mt-10">

  <VueAwesomePaginate
    v-model="currentPage"
    :total-items="gallery.length"
    :items-per-page="itemsPerPage"
    :max-pages-shown="5"
    :show-ending-buttons="true"
    :show-breakpoint-buttons="true"
    back-button-text="Previous"
    next-button-text="Next"
/>

</div>

        </section>



    </template>

<!-- <script setup>
import axios from 'axios';
import { onMounted, ref, computed } from 'vue';
import Paginate from "vuejs-paginate-next"

const tags = ref([])

const currentPage = ref(1)
const itemsPerPage = 12
const paginatedGallery = computed(() => {
    const start = (currentPage.value - 1) * itemsPerPage
    const end = start + itemsPerPage
    return gallery.value.slice(start, end)
})

const totalPages = computed(() => {
    return Math.ceil(gallery.value.length / itemsPerPage)
})

const get_all_tags = async () => {
    try {

        const response = await axios.get("/api/method/dwell_in_door.api.gallery.get_all_tags")

        tags.value = response.data.message




    } catch (error) {

        console.log(error);

    }
}


const gallery = ref([])
const tagsname = ref("")

const galleryCount = ref(0)
const changePage = (page) => {
   
    currentPage.value = page
}

const getGalleryByTag = async (tag) => {
    try {

        const response = await axios.get(
            `/api/method/dwell_in_door.api.gallery.get_gallery_by_tag?tag=${tag}`
        )
        console.log(tag);

        tagsname.value = tag
        gallery.value = response.data.message
        galleryCount.value = response.data.message.length
        // Reset to first page whenever a new tag is selected
        currentPage.value = 1

    } catch (error) {
        console.log(error)
    }
}


onMounted(() => {
    get_all_tags()
    getGalleryByTag("All")
})



</script> -->

<script setup>
import axios from "axios";
// import "vue-awesome-paginate/dist/style.css";
import { ref, computed, onMounted } from "vue";
// import VueAwesomePaginate from "vue-awesome-paginate";

const tags = ref([]);
const gallery = ref([]);
const tagsname = ref("");
const galleryCount = ref(0);

// Pagination
const currentPage = ref(1);
const itemsPerPage = 12;

const paginatedGallery = computed(() => {
    const start = (currentPage.value - 1) * itemsPerPage;
    const end = start + itemsPerPage;
    return gallery.value.slice(start, end);
});

const totalPages = computed(() => {
    return Math.ceil(gallery.value.length / itemsPerPage);
});

// Get All Tags
const get_all_tags = async () => {
    try {
        const response = await axios.get(
            "/api/method/dwell_in_door.api.gallery.get_all_tags"
        );

        tags.value = response.data.message;

    } catch (error) {
        console.log(error);
    }
};

// Get Gallery By Tag
const getGalleryByTag = async (tag) => {
    try {

        const response = await axios.get(
            `/api/method/dwell_in_door.api.gallery.get_gallery_by_tag?tag=${tag}`
        );

        tagsname.value = tag;
        gallery.value = response.data.message;
        galleryCount.value = response.data.message.length;

        // Reset to first page
        currentPage.value = 1;

    } catch (error) {
        console.log(error);
    }
};

onMounted(() => {
    get_all_tags();
    getGalleryByTag("All");
});
</script>
<style scoped>
:deep(.pagination-container) {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
    margin-top: 40px;
    flex-wrap: wrap;
}

:deep(.paginate-buttons) {
    min-width: 42px;
    height: 42px;
    border: 1px solid #d1d5db;
    border-radius: 12px;
    background: #fff;
    color: #374151;
    font-size: 15px;
    font-weight: 600;
    transition: all 0.3s ease;
    cursor: pointer;
}

:deep(.paginate-buttons:hover) {
    background: #0D5C63;
    color: #fff;
    border-color: #0D5C63;
}

:deep(.active-page) {
    background: #0D5C63 !important;
    color: #fff !important;
    border-color: #0D5C63 !important;
}

:deep(.back-button),
:deep(.next-button) {
    width: 42px !important;
    min-width: 42px !important;
    height: 42px !important;
    padding: 0 !important;

    display: flex;
    align-items: center;
    justify-content: center;

    border-radius: 12px;
}

:deep(.back-button:disabled),
:deep(.next-button:disabled) {
    opacity: 0.45;
    cursor: not-allowed;
}

:deep(.ellipse) {
    padding: 0 6px;
    color: #6b7280;
    font-weight: 600;
}
</style>