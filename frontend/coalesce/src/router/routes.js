
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: 'login', component: () => import('pages/LogIn.vue') },
      { path: 'opportunities', component: () => import('pages/OpportunitiesSearch.vue') },
      { path: 'opportunities/create', component: () => import('pages/CreateOpportunity.vue') },
      { path: 'opportunities/:id', component: () => import('pages/OpportunityDetails.vue') },
      { path: 'organisers', component: () => import('pages/OrganiserDashboard.vue') },
      { path: 'organisers/create', component: () => import('pages/CreateOrganiser.vue') },
      { path: 'volunteers/:id', component: () => import('pages/VolunteerDetail.vue') },
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
