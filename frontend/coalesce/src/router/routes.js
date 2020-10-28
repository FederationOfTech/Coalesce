
const routes = [
  {
    path: '/opportunities',
    component: () => import('layouts/BasicLayout.vue'),
    children: [
      { path: '', component: () => import('pages/OpportunitiesSearchPage.vue') }
    ]
  },

  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: 'login', component: () => import('pages/LogIn.vue') },
      { path: 'account', component: () => import('pages/Account.vue') }
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
