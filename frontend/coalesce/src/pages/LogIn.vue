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
                v-model="email"
                type="email"
                label="email"
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
            <p class="text-grey-6">Not reigistered? Created an Account</p>
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
    console.log('asdf')

    return {
      email: '',
      password: ''
    }
  },
  methods: {
    auth () {
      debugger
    }
  }
}
</script>

<style>
.q-card {
  width: 360px;
}
</style>
