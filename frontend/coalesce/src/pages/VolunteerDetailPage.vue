<template>
  <q-page>
    <div class="row">
      <div class="col-3">
        <div class="text-h5 q-pt-lg">{{ volunteer.name }}</div>
        <div class="text-h5 q-pt-lg">{{ volunteer.description }}</div>
        <div class="text-h5 q-pt-lg">{{ volunteer.skills }}</div>
      </div>
      <div class="col-9">
        <div class="text-h5 q-pt-lg">{{ volunteer.organization }}</div>
        <div class="text-h5 q-pt-lg">{{ volunteer.organizer_comments }}</div>
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
