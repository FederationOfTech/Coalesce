
const routes = [
  {
    path: '/opportunities',
    component: () => import('layouts/BasicLayout.vue'),
    children: [
      { path: '', component: () => import('pages/OpportunitiesSearchPage.vue') }
    ]
  },

  {
    path: '/opportunity/:id',
    component: () => import('layouts/BasicLayout.vue'),
    children: [
      { path: '', component: () => import('pages/OpportunityDetailsPage.vue') }
    ]
  },

  {
    path: '/volunteer/:id',
    component: () => import('layouts/BasicLayout.vue'),
    children: [
      { path: '', component: () => import('pages/VolunteerDetailPage.vue') }
    ]
  },

  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: 'login', component: () => import('pages/LogIn.vue') }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
