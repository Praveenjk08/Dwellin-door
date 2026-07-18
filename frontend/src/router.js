import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/home/Home.vue'),
    meta: {
      title: 'Dwell In Door | Premium Real Estate in Bangalore',
      description: 'Discover premium apartments, villas, plots, and luxury homes with Dwell In Door. Find your dream property today.',
      keywords: 'Dwell In Door, real estate, apartments, villas, plots, luxury homes, Bangalore properties,qb'
    }

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
  {
    path: "/blogs",
    name: "Blogs",
    component: () => import('@/blog/BlogList.vue')
  },
  {
    path: "/blogdetailpage/:route",
    name: "BlogDetailPage",
    component: () => import('@/blog/BlogDetailPage.vue'),
    props: true
  },
  {
    path: "/contact-us",
    name: "Contact-Us",
    component: () => import('@/pages/Contact-Us.vue')

  },
  {
    path: "/gallery",
    name: "Gallery",
    component: () => import('@/pages/Gallery.vue')
  }

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
