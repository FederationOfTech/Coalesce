<template>
  <q-page>
    <div class="row">
      <div class="col-3">
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
      <div class="col-9">
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

export default {
  name: 'VolunteerDetailPage',
  data () {
    return {
      volunteer: volunteer
    }
  }
}
</script>
