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
            <p class="text-weight-medium text-body-1">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor <br> incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.</p>
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
export default {
  name: 'CreateOrganiser',
  components: {
    CreateOrganiserForm
  }
}
</script>

<style lang="scss">
    .page-banner {
        padding: 36px;

        .banner-content {
            max-width: 1280px;
            margin: 0 auto;

            .breadcrumbs {
                font-weight: bold;
                letter-spacing: 2px;
                text-transform: uppercase;
            }

            h1 {
                color: $font-primary;
            }

            .submit-button {
                margin-top: 24px;
                font-weight: bold;
                color: white;
                background: $accent;
                border-radius: 8px;
                min-width: 200px;
            }

            .volunteer-link {
                color: $accent;
            }
        }
    }
</style>
