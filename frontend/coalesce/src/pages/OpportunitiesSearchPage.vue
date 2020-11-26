<template>
  <q-page>
    <div class="row">
      <div class="col-8 q-pa-md">
        <!-- search for an opportunity -->
        <q-card class="q-mb-md">
          <q-card-section>
            <div class="text-h3">Search for opportunities</div>
            <div class="text-body1">Gain experience with hands-on training, share your expertise and work with others across the government.</div>
          </q-card-section>
        </q-card>

        <!-- list all opportunities -->
        <div class="row" >
          <div class="col-md-6 q-pa-md" v-for="o in opportunities" v-bind:key="o.id">
            <q-card class="opportunity-card card">
              <q-card-section class="bg-primary text-white">
                <div class="text-h6">{{ o.title }}</div>
              </q-card-section>

              <q-card-section>
                <div class="text-h6">{{ o.description }}</div>
              </q-card-section>

              <q-separator />

              <q-card-actions align="left">
                <q-btn flat>Open</q-btn>
              </q-card-actions>
            </q-card>
          </div>
        </div>

      </div>
      <div class="col-4">
        <q-card class="q-pa-md q-ma-md">
          Filter
        </q-card>
      </div>
    </div>

  </q-page>
</template>

<script>
const opportunities = [
  {
    id: 123,
    title: 'Opportunity 1',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
  },
  {
    id: 234,
    title: 'Opportunity 2',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
  },
  {
    id: 345,
    title: 'Opportunity 3',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
  },
  {
    id: 456,
    title: 'Opportunity 4',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
  }
]

export default {
  name: 'OpportunitiesSearchPage',
  data () {
    return {
      opportunities: opportunities
    }
  }
}
</script>
