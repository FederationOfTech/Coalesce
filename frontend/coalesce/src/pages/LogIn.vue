<template>
  <q-page class="bg-primary row justify-center items-center">
    <div class="column">
      <div class="row">
        <q-card
          square
          bordered
          class="q-pa-lg shadow-1"
        >
          <q-card-section>
            <q-form class="q-gutter-md">
              <q-input
                square
                filled
                clearable
                v-model="username"
                type="username"
                label="username"
              />
              <q-input
                square
                filled
                clearable
                v-model="password"
                type="password"
                label="password"
              />
            </q-form>
          </q-card-section>
          <q-card-actions class="q-px-md">
            <q-btn
              unelevated
              color="primary"
              size="lg"
              class="full-width"
              label="Login"
              @click="auth()"
            />
          </q-card-actions>
          <q-card-section class="text-center q-pa-none">
            <p class="text-grey-6">Not registered? Create an Account</p>
          </q-card-section>
        </q-card>
      </div>
    </div>
  </q-page>
</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    auth () {
      this.$store.dispatch('auth/obtainToken', {
        username: this.username,
        password: this.password
      })
        .then(response => {
          this.$q.notify({
            type: 'positive',
            message: 'Login success!'
          })
        })
        .catch(error => {
          this.$q.notify({
            type: 'negative',
            message: 'Login credentials incorrect'
          })
          console.error(error)
        })
    }
  }
}
</script>

<style>
.q-card {
  width: 360px;
}
</style>
