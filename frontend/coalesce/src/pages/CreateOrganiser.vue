<template>
<q-page class="bg-white">
    <div class="col-12 page-banner bg-grey">
        <div class="banner-content">
            <div class="q-pa-md breadcrumbs">
                <q-breadcrumbs class="q-gutter-none">
                    <q-breadcrumbs-el label="Homepage" to="/" />
                    <q-breadcrumbs-el label="Register as an organisation" />
                </q-breadcrumbs>
            </div>
            <h1 class="text-weight-bolder text-h2">Register as an Organisation</h1>
            <p class="text-weight-medium text-body-1">Try our out volunteer recruitment platform that is under developemt. You can register here and play with the features on offer.</p>
            <p class="text-weight-bold text-subtitle-2">
                Not an organisation?
                <q-btn flat no-caps label="Register as a volunteer instead" class="volunteer-link" to="/" />
            </p>
            <q-btn unelevated no-caps class="submit-button q-mt-xl" style="" padding="8px 16px" text-color="white" label="Submit Profile" />
        </div>
    </div>
    <create-organiser-form />
  </q-page>
</template>

<script>
import CreateOrganiserForm from '../components/create-organiser/create-organiser-form'
import Banner from '../components/Banner.vue'
export default {
  name: 'CreateOrganiser',
  components: {
    CreateOrganiserForm,
    Banner
  }
}
</script>
