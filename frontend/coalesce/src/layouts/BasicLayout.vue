<template>
  <q-layout view="lHh Lpr lFf">
    <q-banner>
      Coalesce
    </q-banner>

    <q-page-container class="body">
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
export default {
  name: 'BasicLayout',
  data () {
    return {

    }
  }
}
</script>
