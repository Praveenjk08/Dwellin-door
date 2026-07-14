import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/home/Home.vue'),
  },
  // {
  //   path: "/detailpage",
  //   name: "detailpage",
  //   component: () => import('@/pages/DetailPage.vue')

  // },
  {
    path: "/properties",
    name: "properties",
    component: () => import('@/pages/PropertyList.vue'),
  },
  {
    path: "/properties/:url",
    name: "PropertyDetail",
    component: () => import('@/pages/DetailPage.vue'),
    props: true
  },
  {
    path: "/about-us",
    name: "About-Us",
    component: () => import('@/pages/About-Us.vue')

  },
  {
    path: "/about-us",
    name: "About-Us",
    component: () => import('@/About-us/About.vue')

  },

]

let router = createRouter({
  history: createWebHistory('/'),
  routes,
  scrollBehavior() {
    return {
      top: 0,
      behavior: "smooth",
    };
  },
})

export default router
