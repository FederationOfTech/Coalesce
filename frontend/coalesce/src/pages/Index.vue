<template>
  <q-page class="q-pa-md">
    <!-- Above the fold, main landing page content -->
    <div>
      <div class="text-subtitle1 text-uppercase">Volunteering made easy</div>
      <div class="text-h1">Welcome to Coalesce</div>
      <div class="text-h5">A 100% open-source volunteer management platform...</div>

      <div class="row q-gutter-xl q-mt-md">
        <q-btn to="/create-organiser" label="Register as an Organisation" color="primary" padding="md xl"></q-btn>
      </div>
    </div>

    <!-- Below the fold, how it works information -->
    <div>
      <h2>How it works</h2>
      <div class="row q-gutter-lg">
        <q-card class="col-3">
          <q-card-section>
            <q-icon name="account_circle" size="xl" color="primary" />
          </q-card-section>
          <q-card-section>
            <div class="text-subtitle2">Step 1</div>
            <div class="text-h6">Register as a Volunteer or an Organisation</div>
            <div class="text-body">Culpa maiores eius consequuntur. Nostrum voluptatem qui in laboriosam.</div>
          </q-card-section>
        </q-card>
        <q-card class="col-3">
          <q-card-section>
            <q-icon name="description" size="xl" color="primary" />
          </q-card-section>
          <q-card-section>
            <div class="text-subtitle2">Step 2</div>
            <div class="text-h6">Create, manage or apply for opportunities on the dashboard</div>
            <div class="text-body">Qui non nobis aperiam corporis perferendis id cumque. Illo reprehenderit numquam quia ut doloremque aut ipsam eos.</div>
          </q-card-section>
        </q-card>
        <q-card class="col-3">
          <q-card-section>
            <q-icon name="check_circle" size="xl" color="primary" />
          </q-card-section>
          <q-card-section>
            <div class="text-subtitle2">Step 3</div>
            <div class="text-h6">Shortlist candidates and accept opportunities</div>
            <div class="text-body">Eaque quaerat nihil quidem non voluptas. Est suscipit non nihil officia aut animi.</div>
          </q-card-section>
        </q-card>
      </div>
    </div>

    <!-- About Coalesce -->
    <div>
      <h2>About Coalesce</h2>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
    </div>

    <!-- Who is using Coalesce? -->
    <div>
      <h2>Who is using Coalesce?</h2>
      <div class="row q-gutter-lg">
        <q-card class="col-2">
          <q-card-section>
            <q-icon name="face" size="xl" color="primary" />
          </q-card-section>
          <q-card-section>
            <div class="text-subtitle2">Alice</div>
          </q-card-section>
        </q-card>
        <q-card class="col-2">
          <q-card-section>
            <q-icon name="face" size="xl" color="primary" />
          </q-card-section>
          <q-card-section>
            <div class="text-subtitle2">Shreya</div>
          </q-card-section>
        </q-card>
        <q-card class="col-2">
          <q-card-section>
            <q-icon name="face" size="xl" color="primary" />
          </q-card-section>
          <q-card-section>
            <div class="text-subtitle2">Frank</div>
          </q-card-section>
        </q-card>
      </div>
    </div>

    <!-- Connect with us -->
    <div>
      <h2>Connect with us</h2>
      <div class="row q-gutter-lg">
        <q-card class="col-2">
          <q-card-section>
            <q-icon name="favorite" size="xl" color="primary" />
          </q-card-section>
          <q-card-section>
            <div class="text-subtitle2">Social post heading</div>
            <div class="text-body">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</div>
          </q-card-section>
        </q-card>
        <q-card class="col-2">
          <q-card-section>
            <q-icon name="thumb_up" size="xl" color="primary" />
          </q-card-section>
          <q-card-section>
            <div class="text-subtitle2">Social post heading</div>
            <div class="text-body">Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus.</div>
          </q-card-section>
        </q-card>
        <q-card class="col-2">
          <q-card-section>
            <q-icon name="share" size="xl" color="primary" />
          </q-card-section>
          <q-card-section>
            <div class="text-subtitle2">Social post heading</div>
            <div class="text-body">Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae.</div>
          </q-card-section>
        </q-card>
      </div>
    </div>
  </q-page>
</template>

<script>
export default {
  name: 'PageIndex'
}
</script>
