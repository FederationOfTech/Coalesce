<template>
    <q-form>
        <div class="grid-container">
            <q-input v-model="organisationName" label="Organisation name" placeholder="Your Organisation name..." />
            <q-input v-model="websiteUrl" label="Do you have a website?" placeholder="Enter URL here..." />
            <q-input v-model="organisationDescription" label="Description of organisation" placeholder="Brief description of your organisation..." />
            <div class="organisation-type">
                <div class="q-gutter-sm">
                    <q-checkbox v-model="teal" label="Teal" color="teal" />
                    <q-checkbox v-model="orange" label="Orange" color="orange" />
                    <q-checkbox v-model="red" label="Red" color="red" />
                    <q-checkbox v-model="cyan" label="Cyan" color="cyan" />
                </div>
                <q-input v-model="organisationName" label="Description of your organisation" />
                <q-input v-model="organisationName" label="Description of your organisation" />
                <q-input v-model="organisationName" label="Description of your organisation" />
                <q-input v-model="organisationName" label="Description of your organisation" />
                <q-input v-model="organisationName" label="Description of your organisation" />
            </div>
            <div class="user-password">
                <q-input v-model="username" label="Username" placeholder="Your Username..." />
                <q-input v-model="password" type="password" label="Password" placeholder="Your Password..." />
            </div>
            <q-input v-model="email" type="email" label="Email" placeholder="Your Email..." />
        </div>
    </q-form>
</template>

<script>
export default {
  name: 'CreateOrganiserForm',
  data () {
    return {
      organisationName: '',
      websiteUrl: '',
      organisationDescription: '',
      username: '',
      password: '',
      email: ''
    }
  },
  computed: {
  },
  methods: {
  }
}
</script>

<style lang="scss">

.grid-container {
    max-width: 1280px;
    margin: auto;
    display: grid;
    grid-template-columns: 2fr 1fr;
    grid-template-rows: repeat(4, 1fr);
    grid-column-gap: 8px;
    grid-row-gap: 16px;
    padding: 16px;

    input {
        font-size: 28px;

        &::-webkit-input-placeholder {
            color: $font-primary;
            font-weight: 300;
        }
    }

    .user-password {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        grid-gap: 16px;
    }
}

.organisation-type {
    grid-area: 2 / 2 / 5 / 3;
}
</style>
