<template>
  <q-page>
    <div id="container">
      <div class="q-pt-xl bg-secondary text-white" id="background">
      </div>
      <div class="row q-pt-xl">
        <div class="col-3 q-pa-lg">
          <q-card class="my-card">
            <img src="https://cdn.quasar.dev/img/mountains.jpg" >
            <q-card-section>
              <div class="text-h6">About</div>
              <div class="text-body2">{{ volunteer.description }}</div>
            </q-card-section>
            <q-card-section style="display: flow-root">
<!--              <div v-for="s in volunteer.skills" v-bind:key="s">-->
<!--                <q-chip size="md" style="float:right;">{{ s }}</q-chip>-->
<!--              </div>-->
            </q-card-section>
          </q-card>
        </div>
        <div class="col-9 q-pa-lg">
          <div class="text-h3 text-weight-bold q-pt-xl text-white">{{ user.first_name }} {{ user.last_name }}</div>
          <div class="text-h6 text-white">Organiser - {{ volunteer.organization }}</div>

          <div class="text-h5 text-weight-bold q-pt-xl q-pb-lg">Upcoming Tasks</div>
          <!-- list all opportunities -->
          <q-scroll-area style="height: 500px; max-width: 100%;">
            <div class="row">
              <div class="col-md-12 q-pa-md" v-for="o in opportunities" v-bind:key="o.id">
                <q-card class="opportunity-card card">
                  <div class="row">
                    <div class="col">
                      <q-card-section>
                        <div class="text-h6">{{ o.title }}</div>
                      </q-card-section>

                      <q-card-section>
                        <div class="text-h7 ellipsis-2-lines">{{ o.description }}</div>
                      </q-card-section>
                    </div>

                    <div class="justify-end q-pa-md">
                      <div class="text-subtitle2 q-pt-lg">{{ o.datetime }}</div>
                      <q-icon class="centre-icon large-icon" name="remove_red_eye" color="grey" />
                    </div>
                  </div>
                </q-card>
              </div>
            </div>
          </q-scroll-area>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>

export default {
  name: 'VolunteerDetailPage',
  data () {
    return {
      volunteer: {},
      user: {},
      opportunities: []
    }
  },
  created () {
    this.$axios.get('/api/v1/volunteers/' + this.$route.params.id + '/',
      {
        headers: {
          Authorization: 'Bearer ' + this.$store.state.auth.jwt.access
        }
      })
      .then(response => {
        this.volunteer = response.data

        this.$axios.get('/api/v1/users/' + this.$route.params.id + '/',
          {
            headers: {
              Authorization: 'Bearer ' + this.$store.state.auth.jwt.access
            }
          })
          .then(response => {
            this.user = response.data
          })
          .catch(e => {
            console.log(e)
          })

        this.$axios.get('/api/v1/opportunities/',
          {
            headers: {
              Authorization: 'Bearer ' + this.$store.state.auth.jwt.access
            }
          })
          .then(response => {
            console.log(response)
            this.opportunities = response.data.results
          })
          .catch(e => {
            console.log(e)
          })
      })
      .catch(e => {
        console.log(e)
      })
  }
}
</script>
