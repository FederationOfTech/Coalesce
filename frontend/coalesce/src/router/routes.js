
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: 'login', component: () => import('pages/LogIn.vue') },
      { path: 'opportunities', component: () => import('pages/OpportunitiesSearchPage.vue') },
      { path: 'opportunity/:id', component: () => import('pages/OpportunityDetailsPage.vue') },
      { path: 'volunteer/:id', component: () => import('pages/VolunteerDetailPage.vue') },
      { path: '/create-organiser', component: () => import('pages/CreateOrganiser.vue') },
      { path: '', component: () => import('pages/Index.vue') }
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
