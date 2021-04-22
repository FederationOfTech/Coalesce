<template>
  <q-page class="q-px-xl q-mx-xl">
    <div class="text-h2 text-weight-bold q-pt-xl">Create an Opportunity</div>
    <div class="text-body1 q-py-lg">A little bit of info about creating a volunteering opportunity</div>

    <div class="q-pb-lg">
      <q-btn color="secondary" label="Submit Opportunity" />
    </div>

    <div class="text-overline">OPPORTUNITY DETAILS</div>
    <q-card class="my-card">
      <q-card-section>
        <q-input v-model="opportunity_title" label="Opportunity Title" stack-label />
        <q-input v-model="opportunity_description" label="Description" stack-label />
        <q-input v-model="opportunity_location" label="Location" stack-label />
        <div class="q-py-md">
          <q-select
            label="Personnel Needed"
            filled
            v-model="personnel_needed_model"
            :options="personnel_needed"
            style="width: 250px"
          />
        </div>
      </q-card-section>
      <q-card-section>
        <div class="row">
          <div class="col-6 q-pa-md">
            <q-card>
              <q-card-section>
                <div class="text-caption">Skillset Required</div>
                <q-scroll-area style="height: 200px">
                  <q-option-group
                    :options="skills_required"
                    label="Notifications"
                    type="checkbox"
                    v-model="skills_required_group"
                  />
                </q-scroll-area>
              </q-card-section>
              <q-card-section class="bg-primary text-white">
                <q-input v-model="skills_required_other" label="Other, please enter below" stack-label />
              </q-card-section>
            </q-card>
          </div>
          <div class="col-6 q-pa-md">
            <q-card>
              <q-card-section>
                <div class="text-caption">Background Checks Required</div>
                <q-scroll-area style="height: 200px">
                  <q-option-group
                    :options="background_check_requirements"
                    label="Notifications"
                    type="checkbox"
                    v-model="background_check_requirements_group"
                  />
                </q-scroll-area>
              </q-card-section>
              <q-card-section class="bg-primary text-white">
                <q-input v-model="background_check_requirements_other" label="Other, please enter below" stack-label />
              </q-card-section>
            </q-card>
          </div>
        </div>
        <div class="row">
          <div class="col-6 q-pa-md">
            <q-card>
              <q-card-section>
                <div class="text-caption">Clothing Required</div>
                <q-scroll-area style="height: 200px">
                  <q-option-group
                    :options="clothing_requirements"
                    label="Notifications"
                    type="checkbox"
                    v-model="clothing_requirements_group"
                  />
                </q-scroll-area>
              </q-card-section>
              <q-card-section class="bg-primary text-white">
                <q-input v-model="clothing_requirements_other" label="Other, please enter below" stack-label />
              </q-card-section>
            </q-card>
          </div>
          <div class="col-6 q-pa-md">
            <q-card>
              <q-card-section>
                <div class="text-caption">Commitment Type</div>
                <q-scroll-area style="height: 200px">
                  <q-option-group
                    :options="commitment_type"
                    label="Notifications"
                    type="checkbox"
                    v-model="commitment_type_group"
                  />
                </q-scroll-area>
              </q-card-section>
              <q-card-section class="bg-primary text-white">
                <q-input v-model="commitment_type_other" label="Other, please enter below" stack-label />
              </q-card-section>
            </q-card>
          </div>
        </div>
      </q-card-section>
    </q-card>

    <div class="text-overline q-py-md">OPPORTUNITY DATE &amp; TIME</div>
    <q-card>
      <div class="row">
        <div class="col-5 q-pa-md">
          <q-input v-model="start_date" label="Start Date" stack-label />
          <q-input v-model="end_date" label="End Date" stack-label />
        </div>
        <div class="col-7 q-pa-md">
          <q-card-section>
            <div class="row">
              <div class="q-pa-md">
                <q-date v-model="model" mask="MM-DD-YYYY" />
              </div>
              <div class="q-pa-md">
                <q-date v-model="model2" mask="MM-DD-YYYY" />
              </div>
            </div>
          </q-card-section>
        </div>
      </div>
    </q-card>
  </q-page>
</template>

<script>
const skills_required = [
  { label: 'Hospitality', value: 'hospitality' },
  { label: 'Information Technology', value: 'it' },
  { label: 'Building & Construction', value: 'buildingconstruction' },
  { label: 'Arts & Communication', value: 'arts&communication' },
  { label: 'Science & Engineering', value: 'science&engineering' }
]

const background_check_requirements = [
  { label: 'Criminal Record Check', value: 'criminalrecordcheck' },
  { label: 'Social Media Screening', value: 'socialmediascreening' },
  { label: 'Credit Checks', value: 'creditchecks' },
  { label: 'Educational Verifications', value: 'educationalverifications' },
  { label: 'Reference Checks', value: 'referencechecks' },
  { label: 'Right to Work Checks', value: 'righttoworkchecks' }
]

const commitment_type = [
  { label: 'One Time', value: 'onetime' },
  { label: 'Recurring', value: 'recurring' },
  { label: 'Fixed Ad-Hoc', value: 'fixedadhoc' },
  { label: 'Other', value: 'other' }
]

const clothing_requirements = [
  { label: 'T-shirt', value: 'tshirt' },
  { label: 'Winterwear', value: 'winterwear' },
  { label: 'Face Masks', value: 'facemasks' },
  { label: 'Waterproofs', value: 'waterproofs' },
  { label: 'Protective Footware', value: 'protectivefootware' },
  { label: 'Kitchen Apron', value: 'kitchenapron' }
]

export default {
  name: 'CreateAnOpportunityPage',
  data () {
    return {
      opportunity_title: '',
      opportunity_description: '',
      opportunity_location: '',
      skills_required_other: '',
      background_check_requirements_other: '',
      commitment_type_other: '',
      clothing_requirements_other: '',
      start_date: '',
      end_date: '',
      model: '2019-02-15',
      model2: '2019-02-15',
      skills_required: skills_required,
      skills_required_group: [],
      background_check_requirements: background_check_requirements,
      background_check_requirements_group: [],
      commitment_type: commitment_type,
      commitment_type_group: [],
      clothing_requirements: clothing_requirements,
      clothing_requirements_group: [],
      personnel_needed_model: 0,
      personnel_needed: Array.from(Array(10).keys())
    }
  }
}
</script>
