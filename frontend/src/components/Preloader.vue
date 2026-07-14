<template>
    <div class="fixed inset-0 z-[9999] bg-white flex items-center justify-center overflow-hidden">

        <!-- Glow Effect -->
        <div class="absolute w-80 h-80 rounded-full bg-yellow-400/20 blur-3xl transition-all duration-[2500ms]"
            :class="{ 'opacity-0 scale-150': startOpen }">
        </div>

        <!-- Left Logo Half -->
        <div class="logo-half left-half" :class="{ 'open-left': startOpen }">
            <img :src="getFileUrl('dwellin-door-logo.png')" alt="Dwellin Door" class="logo-img" />
        </div>

        <!-- Right Logo Half -->
        <div class="logo-half right-half" :class="{ 'open-right': startOpen }">
            <img :src="getFileUrl('dwellin-door-logo.png')" alt="Dwellin Door" class="logo-img" />
        </div>

    </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const startOpen = ref(false);

const getFileUrl = (file) => {
    return `${window.location.origin}/files/${file}`;
};

onMounted(() => {
    setTimeout(() => {
        startOpen.value = true;
    }, 1200);
});
</script>

<style scoped>
.logo-half {
    position: absolute;
    width: min(90vw, 700px);

    left: 50%;
    top: 50%;

    overflow: hidden;

    transform: translate(-50%, -50%);

    transition: all 4.5s cubic-bezier(0.22, 1, 0.36, 1);

    backface-visibility: hidden;
    transform-style: preserve-3d;
}

.logo-img {
    width: 100%;
    height: auto;
    display: block;
}

/* Left Half */
.left-half {
    clip-path: inset(0 50% 0 0);
    transform-origin: left center;
}

/* Right Half */
.right-half {
    clip-path: inset(0 0 0 50%);
    transform-origin: right center;
}

/* Desktop Animation */
.open-left {
    transform:
        translate(-50%, -50%) translateX(-600px) rotateY(-90deg);

    opacity: 0;
}

.open-right {
    transform:
        translate(-50%, -50%) translateX(600px) rotateY(90deg);

    opacity: 0;
}

/* Mobile Responsive */
@media (max-width: 768px) {

    .logo-half {
        width: 90vw;
    }

    .open-left {
        transform:
            translate(-50%, -50%) translateX(-250px) rotateY(-90deg);
    }

    .open-right {
        transform:
            translate(-50%, -50%) translateX(250px) rotateY(90deg);
    }
}
</style>
