<template>
  <q-page>
    <div class="text-h5 q-pt-lg">{{ volunteer.description }}</div>
    <div class="text-h5 q-pt-lg">{{ volunteer.skills }}</div>
    <div class="text-h5 q-pt-lg">{{ volunteer.organization }}</div>
    <div class="text-h5 q-pt-lg">{{ volunteer.organizer_comments }}</div>
  </q-page>
</template>

<script>
const volunteer = {
  id: 123,
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
