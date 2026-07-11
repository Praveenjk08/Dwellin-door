<template>
    <div class="fixed bottom-0 left-0 w-full bg-white border-t shadow-lg z-50 md:hidden">
        <div class="grid grid-cols-4 py-3">

            <!-- Home -->
            <router-link to="/" class="flex flex-col items-center text-gray-700">
                <i class="bi bi-house-door text-xl"></i>
                <span class="text-xs mt-1">Home</span>
            </router-link>

            <!-- Call -->
            <a href="tel:+918123619994" class="flex flex-col items-center text-gray-700">
                <i class="bi bi-telephone text-xl"></i>
                <span class="text-xs mt-1">Call</span>
            </a>

            <!-- Contact -->
            <router-link to="/contact-us" class="flex flex-col items-center text-gray-700">
                <i class="bi bi-envelope text-xl"></i>
                <span class="text-xs mt-1">Contact</span>
            </router-link>

            <!-- WhatsApp -->
            <a href="https://wa.me/1234567123" target="_blank" class="flex flex-col items-center text-green-600">
                <i class="bi bi-whatsapp text-xl"></i>
                <span class="text-xs mt-1">WhatsApp</span>
            </a>

        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const deferredPrompt = ref(null);
const isInstalled = ref(false);
const isStandalone = ref(false);

// Detect if running as PWA
const detectStandalone = () => {
    isStandalone.value =
        window.matchMedia("(display-mode: standalone)").matches ||
        window.navigator.standalone === true;

    if (isStandalone.value) {
        isInstalled.value = true;
    }
};

onMounted(() => {

    detectStandalone();

    // Install available
    window.addEventListener("beforeinstallprompt", (e) => {
        e.preventDefault();
        deferredPrompt.value = e;
        isInstalled.value = false;
        console.log("Install available");
    });

    // App installed
    window.addEventListener("appinstalled", () => {
        isInstalled.value = true;
        deferredPrompt.value = null;
        console.log("App installed");
    });

    // Detect if already installed
    setTimeout(() => {
        if (!deferredPrompt.value) {
            isInstalled.value = true;
        }
    }, 1500);
});

// Button click handler
const handleAppButton = async () => {

    // Already running as PWA
    if (window.matchMedia("(display-mode: standalone)").matches) {
        return;
    }

    // Install available
    if (deferredPrompt.value) {
        deferredPrompt.value.prompt();
        const result = await deferredPrompt.value.userChoice;
        deferredPrompt.value = null;
        return;
    }

    // Already installed but in browser
    alert("Please open it from your device's app list.");
};

</script>
