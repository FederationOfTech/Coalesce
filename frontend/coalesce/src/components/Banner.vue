<template>
  <div class="col-12 page-banner bg-grey">
    <div class="banner-content">
      <div class="q-pa-md breadcrumbs">
        <q-breadcrumbs class="q-gutter-none">
          <q-breadcrumbs-el label="Homepage" to="/" />
          <q-breadcrumbs-el v-if="bannerTitle" :label="bannerTitle" />
        </q-breadcrumbs>
      </div>
      <h1 class="text-weight-bolder text-h2">{{ bannerTitle }}</h1>
      <p class="text-weight-medium text-body-1">{{ bannerDescription }}</p>
      <p class="text-weight-bold text-subtitle-2" v-if="registeringAs">
        Not {{ registeringAs }}?
        <q-btn
          flat
          no-caps
          label="Register as a volunteer instead"
          class="volunteer-link"
          to="/"
        />
      </p>
      <q-btn
        v-if="submitInBanner"
        unelevated
        no-caps
        class="submit-button q-mt-xl"
        style=""
        padding="8px 16px"
        text-color="white"
        label="Submit Profile"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: 'Banner',
  props: {
    bannerTitle: {
      type: String,
      default: ''
    },
    bannerDescription: {
      type: String,
      default: ''
    },
    registeringAs: {
      type: String,
      default: ''
    },
    submitInBanner: {
      type: Boolean,
      default: false
    }
  }
}
</script>

<style lang="scss">
.page-banner {
  padding: 36px;

  .banner-content {
    max-width: 1280px;
    margin: 0 auto;
    white-space: pre;

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
