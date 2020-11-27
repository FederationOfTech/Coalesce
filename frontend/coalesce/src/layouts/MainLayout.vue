<template>
  <q-layout view="lHh Lpr lFf">
    <q-header>
      <div class="q-px-lg q-pt-md q-mb-md">
        <div class="text-h3">Coalesce</div>
      </div>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>

export default {
  name: 'MainLayout',
  data () {
    return {
    }
  }
}
</script>
