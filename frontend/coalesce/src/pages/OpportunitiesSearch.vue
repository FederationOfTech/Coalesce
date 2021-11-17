<template>
  <q-page>
    <div class="row q-pt-lg">
      <div class="col-8 q-pa-md">
        <!-- search for an opportunity -->
        <q-card class="q-mb-md q-pa-md">
          <q-card-section>
            <div class="text-h3 text-weight-bold q-mb-md">Search for opportunities</div>
            <div class="text-subtitle1">Contribute to your local community through applying for volunteering opportunities near you..</div>
          </q-card-section>
          <!-- search bar -->
          <q-toolbar>
            <q-input rounded outlined class="search-bar" v-model="filter" type="text" >
              <template v-slot:append>
                <q-icon name="search" />
              </template>
            </q-input>
          </q-toolbar>
        </q-card>

        <!-- list all opportunities -->
        <div class="row" >
          <div class="col-md-6 q-pa-md" v-for="o in filterOpportunity" v-bind:key="o.id">
            <q-card class="opportunity-card card">
              <q-card-section class="bg-primary text-white">
                <div class="text-h6">{{ o.title }}</div>
              </q-card-section>

              <q-card-section>
                <div class="text-h7 ellipsis-2-lines">{{ o.description }}</div>
              </q-card-section>

              <q-separator />

              <q-card-actions align="left" class="text-blue">
                <q-btn @click="$router.replace('/opportunities/' + o.id )" flat>Open</q-btn>
              </q-card-actions>
            </q-card>
          </div>
        </div>
      </div>

      <!-- filtering -->
      <div class="col-4">
        <q-card class="q-pa-md q-ma-md">
          <div class="text-h5 text-weight-bold q-pl-md">Filter</div>

          <!-- Calender filter -->
          <div class="q-pa-md" >
            <q-input filled v-model="filterDate">
              <template v-slot:append>
                <q-icon name="event" class="cursor-pointer">
                  <q-popup-proxy ref="qDateProxy" transition-show="scale" transition-hide="scale">
                    <q-date v-model="filterDate" mask="YYYY-MM-DD">
                      <div class="row items-center justify-end">
                        <q-btn label="Clear" color="primary" @click="clearDateFilter" flat />
                        <q-btn v-close-popup label="Close" color="primary" flat />
                      </div>
                    </q-date>
                  </q-popup-proxy>
                </q-icon>
              </template>
            </q-input>
          </div>
        </q-card>
      </div>
    </div>

  </q-page>
</template>

<script>

export default {
  name: 'OpportunitiesSearchPage',
  data () {
    return {
      opportunities: [],
      filter: '',
      filterDate: ''
    }
  },
  created () {
    this.$axios.get('/api/v1/opportunities/',
      {
        headers: {
          Authorization: 'Bearer ' + this.$store.state.auth.jwt.access
        }
      })
      .then(response => {
        this.opportunities = response.data.results
      })
      .catch(e => {
        console.log(e)
      })
  },
  computed: {
    filterOpportunity: function () {
      if (!this.filter && !this.filterDate) {
        return this.opportunities
      }

      let results = this.opportunities.filter(o => {
        return o.title.toLowerCase().indexOf(this.filter.toLowerCase()) > -1
      })

      console.log()

      results = results.filter(o => {
        return o.datetime.toLowerCase().indexOf(this.filterDate.toLowerCase()) > -1
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
