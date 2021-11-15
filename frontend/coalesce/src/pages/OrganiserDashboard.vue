<template>
  <q-page>
    <div class="row q-pt-lg">
      <div class="col-8 q-pa-md">
        <h2 class="text-weight-bolder">My Dashboard</h2>
        <div class="text-body-1">Magni nulla doloremque cupiditate ratione placeat hic tenetur praesentium. Quidem harum dolores odit quae explicabo. Quo nihil dignissimos aut quasi. Qui dolorem eius nemo. Et ut eum aliquam fuga.</div>

        <div class="row">
          <q-input
            label="Search current opportunities..."
            rounded
            outlined
            class="col-grow"
            v-model="filter"
            debounce="500"
            v-on:input="search"
            type="text"
            :loading="loading"
          >
            <template v-slot:append>
              <q-icon name="search" />
            </template>
          </q-input>

          <q-btn to="/opportunities/create" class="q-ma-md" color="primary" label="Create an opportunity" size="lg" />
        </div>

        <!-- search results list -->
        <div class="col-md-6 q-pa-md">
          <div class="text-weight-bolder text-h2">Opportunities</div>
        </div>
        <div class="row" >
          <div class="col-md-6 q-pa-md" v-for="o in opportunities" v-bind:key="o.id">
            <q-card class="opportunity-card card">
              <q-card-section class="bg-primary text-white">
                <div class="text-h6">{{ o.title }}</div>
              </q-card-section>

              <q-card-section>
                <div class="text-h7 ellipsis-2-lines">{{ o.description }}</div>
              </q-card-section>

              <q-separator />

              <q-card-actions align="left" class="text-blue">
                <q-btn flat>Open</q-btn>
              </q-card-actions>
            </q-card>
          </div>
        </div>
      </div>
    </div>

  </q-page>
</template>

<script>
export default {
  name: 'OrganiserDashboardPage',
  data () {
    return {
      // The search input textbox value
      filter: '',

      // True while waiting for a REST API call
      loading: true,

      // Search results
      opportunities: []
    }
  },

  methods: {
    search () {
      this.loading = true

      // TODO if this.filter != "", add it as a search parameter for full-text
      // search of opportunities
      this.$axios.get('/api/v1/opportunities/',
        {
          headers: {
            Authorization: 'Bearer ' + this.$store.state.auth.jwt.access
          }
        })
        .then(response => {
          this.loading = false

          // TODO pagination via response.data.next and previous fields
          this.opportunities = response.data.results
        })
        .catch(e => {
          console.log(e)
        })
    }
  },

  created () {
    this.search()
  }
}
</script>
