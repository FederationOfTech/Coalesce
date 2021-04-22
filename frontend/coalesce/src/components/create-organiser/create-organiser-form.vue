<template>
    <q-form class="form" method="post" @submit.prevent="createOrganiser">
        <div class="grid-container">
            <div class="form-group">
                <q-input v-model="organisationName" label="Organisation name" placeholder="Your Organisation name..." />
                <p class="error" v-if="!$v.organisationName.minLength">Please enter an orgnaisation name longer than 1 character</p>
            </div>
            <div class="form-group">
                <q-input v-model="websiteUrl" label="Do you have a website?" placeholder="Enter URL here..." />
                <p class="error" v-if="!$v.websiteUrl.url">Website must be a valid URL</p>
            </div>
            <q-input
                v-model="organisationDescription"
                label="Description of organisation"
                placeholder="Brief description of your organisation..."
                type="textarea"
            />
            <div class="organisation-type">
                <p>What form of organisation do you represent?</p>
                <div v-if="organisationTypes" class="q-gutter-sm column">
                    <q-radio v-for="({label, value}) in organisationTypes" :key="label" v-model="organisationType" :val="value" :label="label" />
                </div>
            </div>
            <div class="user-password">
                <q-input v-model="username" label="Username" placeholder="Your Username..." />
                <q-input v-model="password" type="password" label="Password" placeholder="Your Password..." />
            </div>
            <div class="form-group">
                <q-input v-model="email" type="email" label="Email" placeholder="Your Email..." />
                <p class="error" v-if="!$v.email.email">Please enter a valid email address</p>
            </div>
        </div>
        <q-btn type="submit" unelevated no-caps class="submit-button q-mt-xl" padding="8px 16px" text-color="white" label="Submit Profile" />
    </q-form>
</template>

<script>
import { validationMixin } from 'vuelidate'
import { email, minLength, required, url } from 'vuelidate/lib/validators'
import { organisationTypes } from './utils/form-data'
export default {
  name: 'CreateOrganiserForm',

  data () {
    return {
      organisationName: '',
      websiteUrl: '',
      organisationDescription: '',
      username: '',
      password: '',
      email: '',
      organisationTypes: null,
      organisationType: ''
    }
  },

  mixins: [
    validationMixin
  ],

  validations: {
    organisationName: {
      required,
      minLength: minLength(2)
    },

    email: {
      required,
      email
    },

    websiteUrl: {
      url
    }
  },

  methods: {
    isFormValid () {
      this.$v.$touch()
      return !this.$v.$invalid
    },

    onFormSubmit () {
      if (this.isFormValid()) {
        this.createOrganiser()
      } else {
        // An error happened
      }
    },

    createOrganiser () {
      // POST to endpoint
    }
  },

  mounted () {
    this.organisationTypes = organisationTypes
  }
}
</script>

<style lang="scss">

.form {
    display: flex;
    flex-direction: column;
    max-width: 1280px;
    margin: 16px auto;
    .grid-container {
        display: grid;
        grid-template-columns: 2fr 1fr;
        grid-template-rows: repeat(4, 1fr);
        grid-column-gap: 16px;
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

        @media screen and (max-width: 768px) {
            display: flex;
            flex-direction: column;
        }

    }
    .submit-button {
        margin-top: 24px;
        font-weight: bold;
        color: white;
        background: $accent;
        border-radius: 8px;
        min-width: 300px;
        max-width: 300px;
        align-self: flex-end;
    }

    .organisation-type {
        border: 1px solid grey;
        border-radius: 8px;
        grid-area: 2 / 2 / 5 / 3;
        padding: 16px;
    }
}
</style>
