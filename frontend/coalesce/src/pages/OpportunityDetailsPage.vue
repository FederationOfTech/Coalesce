<template>
  <q-page>
    <div class="row">
      <div class="col-8 q-pa-md">
        <q-card class="q-mb-md">
          <q-card-section class="bg-primary text-white">
            <div class="text-h5 q-pt-lg">{{ opportunity.title }}</div>
          </q-card-section>
          <q-card-section>
            <!-- -->
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
                <div class="text-body1">Contribute to your local community through applying for volunteering opportunities near you..</div>
              </q-card-section>
            </div>
          </div>
        </q-card>
      </div>

      <!-- filtering -->
      <div class="col-4">
        <q-card class="q-pa-md q-ma-md">
          <div class="text-h5 text-weight-bold q-pb-md">Progress</div>
          <div class="row">
            <div class="col" style="display:block">
              <q-icon class="centre-icon large-icon" name="remove_red_eye" />
              <div class="text-body2" style="text-align: center">Accepting Applications</div>
            </div>
            <div class="col">
              <q-icon class="centre-icon small-icon" name="arrow_forward" />
            </div>
            <div class="col">
              <q-icon class="centre-icon large-icon" name="refresh" />
              <div class="text-body2">Preparing Onboarding</div>
            </div>
            <div class="col">
              <q-icon class="centre-icon small-icon" name="arrow_forward" />
            </div>
            <div class="col">
              <q-icon class="centre-icon large-icon" name="check" />
              <div class="text-body2">Complete</div>
            </div>
          </div>

          <q-btn label="APPLY NOW" @click="clearDateFilter" color="primary" />
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
  description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
  accepting_applications: true,
  skills_required: [
    'skill1', 'skill2'
  ],
  organiser_photo: '',
  number_of_volenteers_needed: 4,
  commitment: 20,
  completion_date: '2020/01/14',
  location: 'virtual'
}

export default {
  name: 'OpportunitiesSearchPage',
  data () {
    return {
      opportunity: opportunity,
      filter: '',
      filterDate: ''
    }
  },
  computed: {
    filterOpportunity: function () {
      if (!this.filter && !this.filterDate) {
        return this.opportunities
      }

      let results = this.opportunities.filter(o => {
        return o.title.toLowerCase().indexOf(this.filter.toLowerCase()) > -1
      })

      results = results.filter(o => {
        return o.date.toLowerCase().indexOf(this.filterDate.toLowerCase()) > -1
      })
      return results
    }
  },
  methods: {
    clearDateFilter () {
      this.filterDate = ''
    }
  }
}
</script>
