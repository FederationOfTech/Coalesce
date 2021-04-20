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
                <div class="text-body2">{{ opportunity.number_of_volenteers_needed }}</div>
                <div class="text-subtitle1 text-weight-bold
">Commitment</div>
                <div class="text-body2">{{ opportunity.commitment }} hours</div>
                <div class="text-subtitle1 text-weight-bold
">Estimated completion date</div>
                <div class="text-body2">{{ opportunity.completion_date }}</div>
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

          <q-btn label="APPLY NOW" @click="clearDateFilter" class="full-width q-mt-lg" color="primary" />
        </q-card>
      </div>
    </div>

  </q-page>
</template>

<script>
const opportunity = {
  id: 123,
  date: '2020/12/25',
  title: 'My opportunity 1',
  description: 'Description of the opportunity',
  accepting_applications: true,
  preparing_onboarding: false,
  skills_required: [
    'skill1', 'skill2'
  ],
  organiser_photo: '',
  number_of_volenteers_needed: 4,
  commitment: 20,
  completion_date: '2020/01/14',
  location: 'virtual',
  completed: false
}

export default {
  name: 'OpportunityDetailsPage',
  data () {
    return {
      opportunity: opportunity
    }
  }
}
</script>
