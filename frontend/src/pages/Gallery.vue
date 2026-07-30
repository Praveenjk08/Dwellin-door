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

                    <img
    :src="item.iamge"
    @click="openViewer(index)"
    class="w-full h-[240px] object-cover rounded-[24px] group-hover:scale-105 transition duration-500 cursor-pointer"
/>

                    <div
    class="group absolute top-3 right-3 w-10 h-10 bg-white rounded-full flex items-center justify-center shadow-md cursor-pointer"
>
    <span
        class="material-symbols-outlined text-gray-500 group-hover:text-pink-500"
        style="font-variation-settings: 'FILL' 0;"
        onmouseover="this.style.fontVariationSettings=`'FILL' 1`"
        onmouseout="this.style.fontVariationSettings=`'FILL' 0`"
    >
        favorite
    </span>
</div>

                </div>

            </div>


    <div
    v-if="showViewer" @click.self="closeViewer"
    class="fixed inset-0 z-[9999] bg-black/90 flex items-center justify-center"
>
   <!-- Previous -->
<button
    @click="prevImage"
    class="absolute left-6 z-20 w-12 h-12 rounded-full bg-white/20 hover:bg-white/35 transition-all duration-300 flex items-center justify-center backdrop-blur-sm"
>
    <span class="material-symbols-outlined text-white text-[28px]">
        chevron_left
    </span>
</button>

    <!-- Image Wrapper -->
    <div class="relative inline-block">

        <img
            :src="gallery[selectedIndex]?.iamge"
            class="max-w-[90vw] max-h-[85vh] rounded-xl"
        />

        <!-- ✅ Close button -->
        <button
            @click="closeViewer"
            class="absolute top-0 right-0 w-10 h-10 rounded-full bg-black/50 hover:bg-black/70 flex items-center justify-center"
        >
            <span class="material-symbols-outlined text-white text-[24px]">
                close
            </span>
        </button>

    </div>

   <!-- Next -->
<button
    @click="nextImage"
    class="absolute right-6 z-20 w-12 h-12 rounded-full bg-white/20 hover:bg-white/35 transition-all duration-300 flex items-center justify-center backdrop-blur-sm"
>
    <span class="material-symbols-outlined text-white text-[28px]">
        chevron_right
    </span>
</button>
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



<script setup>
import axios from "axios";
import { ref, computed, onMounted, onUnmounted } from "vue";




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



//user clkiked on the gallery it will show full iamge
const showViewer = ref(false)
const selectedIndex = ref(0)

const openViewer = (index) => {
    selectedIndex.value = index
    showViewer.value = true
}

const closeViewer = () => {
    showViewer.value = false
}

const nextImage = () => {
    if (selectedIndex.value < gallery.value.length - 1) {
        selectedIndex.value++
    } else {
        selectedIndex.value = 0
    }
}

const prevImage = () => {
    if (selectedIndex.value > 0) {
        selectedIndex.value--
    } else {
        selectedIndex.value = gallery.value.length - 1
    }
}
const handleKeyDown = (event) => {
    if (!showViewer.value) return

    switch (event.key) {
        case "ArrowLeft":
            prevImage()
            break

        case "ArrowRight":
            nextImage()
            break

        case "Escape":
            closeViewer()
            break
    }
}
onMounted(() => {
    get_all_tags()
    getGalleryByTag("All")

    window.addEventListener("keydown", handleKeyDown)
})

onUnmounted(() => {
    window.removeEventListener("keydown", handleKeyDown)
})
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