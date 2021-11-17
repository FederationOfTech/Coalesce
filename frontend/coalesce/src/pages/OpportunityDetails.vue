<template>
  <q-page>
    <div class="row">
      <div class="col-8 q-pa-md">
        <q-card class="q-mb-md">
          <q-card-section class="bg-primary text-white">
            <div class="text-h5 q-pt-lg">{{ opportunity.title }}</div>
          </q-card-section>
          <q-card-section>
            <q-chip v-if="this.opportunity.accepting_applications" size="lg" icon="circle" color="green">Accepting Applications</q-chip>
            <q-chip v-if="!this.opportunity.accepting_applications" size="lg" icon="circle" color="red">Accepting Applications</q-chip>
          </q-card-section>
          <q-card-section style="display: flow-root">
            <div v-for="s in opportunity.skills_required" v-bind:key="s">
              <q-chip size="md" style="float:right;">{{ s }}</q-chip>
            </div>
          </q-card-section>
        </q-card>
        <q-card class="q-mb-md">
          <div class="row">
            <div class="col-8 q-pa-md">
              <q-card-section>
                <div class="text-body1">{{ opportunity.description }}</div>
              </q-card-section>
            </div>
            <div class="col-4 q-pa-md">
              <q-card-section class="bg-primary text-white">
                <div class="text-subtitle1 text-weight-bold
">Personnel needed</div>
                <div class="text-body2">{{ opportunity.personnel_needed }}</div>
                <div class="text-subtitle1 text-weight-bold
">Commitment</div>
                <div class="text-body2">{{ opportunity.commitment_type }}</div>
                <div class="text-subtitle1 text-weight-bold
">Date</div>
                <div class="text-body2">{{ new Date(opportunity.datetime).toLocaleString() }}</div>
                <div class="text-subtitle1 text-weight-bold
">Location</div>
                <div class="text-body2">{{ opportunity.location }}</div>
              </q-card-section>
            </div>
          </div>
        </q-card>
      </div>

      <!-- filtering -->
      <div class="col-4">
        <q-card class="q-pa-md q-ma-md">
          <div class="text-h5 text-weight-bold q-pb-md">Progress</div>
          <div class="row q-pb-lg">
            <div class="col" style="display:block">
              <q-icon v-if="this.opportunity.accepting_applications" class="centre-icon large-icon" name="remove_red_eye" color="green" />
              <q-icon v-if="!this.opportunity.accepting_applications" class="centre-icon large-icon" name="remove_red_eye" color="grey" />
              <div class="text-body2" style="text-align: center">Accepting Applications</div>
            </div>
            <div class="col">
              <q-icon class="centre-icon small-icon" name="arrow_forward" color="grey" />
            </div>
            <div class="col">
              <q-icon v-if="this.opportunity.preparing_onboarding" class="centre-icon large-icon" name="refresh" color="green" />
              <q-icon v-if="!this.opportunity.preparing_onboarding" class="centre-icon large-icon" name="refresh" color="grey" />
              <div class="text-body2">Preparing Onboarding</div>
            </div>
            <div class="col">
              <q-icon class="centre-icon small-icon" name="arrow_forward" color="grey" />
            </div>
            <div class="col">
              <q-icon v-if="this.opportunity.completed" class="centre-icon large-icon" name="check" color="green" />
              <q-icon v-if="!this.opportunity.completed" class="centre-icon large-icon" name="check" color="grey" />
              <div class="text-body2">Complete</div>
            </div>
          </div>

          <q-btn label="APPLY NOW" class="full-width q-mt-lg" color="primary" />
        </q-card>
      </div>
    </div>

    <q-inner-loading :showing="loading">
      <q-spinner-gears size="50px" color="primary" />
    </q-inner-loading>
  </q-page>
</template>

<script>
// TODO The following fields are not yet available from the REST API:
// - accepting_applications (bool)
// - preparing_onboarding (bool)
// - completed (bool)

export default {
  name: 'OpportunityDetailsPage',
  data () {
    return {
      loading: true,
      opportunity: {}
    }
  },

  created () {
    this.$axios.get('/api/v1/opportunities/' + this.$route.params.id + '/',
      {
        headers: {
          Authorization: 'Bearer ' + this.$store.state.auth.jwt.access
        }
      })
      .then(response => {
        this.loading = false
        this.opportunity = response.data
      })
      .catch(e => {
        console.log(e)
      })
  }
}
</script>
