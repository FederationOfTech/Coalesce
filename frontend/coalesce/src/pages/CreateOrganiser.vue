<template>
  <q-page class="bg-white">
    <banner
      banner-title="Register as an Organisation"
      banner-description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam."
      registering-as="an organisation"
      submit-in-banner="true"
    />
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
