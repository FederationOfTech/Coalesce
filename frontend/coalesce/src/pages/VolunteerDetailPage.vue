<template>
  <q-page>
    <div class="row q-pt-xl">
      <div class="col-3 q-pa-lg">
        <q-card class="my-card">
          <img src="https://cdn.quasar.dev/img/mountains.jpg">
          <q-card-section>
            <div class="text-h6">About</div>
            <div class="text-body2">This is a section to describe Mike Nolan</div>
          </q-card-section>
          <q-card-section class="q-pt-none">
            {{ lorem }}
          </q-card-section>

          <q-separator />
          <q-card-actions align="left" class="text-blue">
            <q-btn flat>Open</q-btn>
          </q-card-actions>

        </q-card>
      </div>
      <div class="col-9 q-pa-lg">
        <div class="text-h3 q-pt-xl">{{ volunteer.name }}</div>
        <div class="text-h6">Organiser - Federation of Tech</div>

        <div class="text-h5 q-pt-lg">Upcoming Tasks</div>
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
                    <div class="text-subtitle2 q-pt-lg">{{ o.date }}</div>
                    <q-icon class="centre-icon large-icon" name="remove_red_eye" color="grey" />
                  </div>
                </div>
              </q-card>
            </div>
          </div>
        </q-scroll-area>
      </div>
    </div>
  </q-page>
</template>

<script>
const volunteer = {
  id: 123,
  name: 'Mike Nolan',
  description: 'Lorem ipsum',
  skills: [
    'skill1', 'skill2'
  ],
  organization: 'The volunteers employer or organization',
  organizer_comments: 'Notes from organizers about this volunteer'
}

const opportunities = [
  {
    id: 1,
    title: 'Opportunity Title',
    date: '2020/09/30',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
  },
  {
    id: 2,
    title: 'Opportunity Title',
    date: '2020/10/15',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
  },
  {
    id: 3,
    title: 'Opportunity Title',
    date: '2020/11/30',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
  }
]

export default {
  name: 'VolunteerDetailPage',
  data () {
    return {
      volunteer: volunteer,
      opportunities: opportunities
    }
  }
}
</script>
