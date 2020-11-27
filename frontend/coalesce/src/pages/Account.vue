<template>
  <q-page>
<!-- Load an icon library -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

<div class="topnav">
  <a class="title" href="#home">Coalesce</a>
  <div class="topnav-right">
    <a href="#contact">Sign Out</a>
    <a href="#about"><i class="fa fa-fw fa-search"></i> Search</a>
  </div>
</div>

<div class="banner">
      <div class="text-h3">{{ user.username }}</div>
      <div class="text-h6">{{user.organisation}}</div>
</div>

<div class="q-pa-md row items-start q-gutter-md">
  <q-card class="my-card">
    <q-card-media horizontal class="profile_info">
            <img class= "col-5" src="~assets/icon.png">
    </q-card-media>

    <q-separator/>

    <q-card-title class="card-title">
       <div class="text-h5 font-weight-bold">About</div>
    </q-card-title>
    <q-card-main>
       <div >{{user.about}}</div>
    </q-card-main>
  </q-card>

   <q-card class="column" >
          <div class="text-h5 font-weight-bold">Upcoming Tasks</div>
          <div class="col-md-6 q-pa-md" v-for="o in opportunities" v-bind:key="o.id">
            <q-card class="opportunity-card">
              <q-card-section class>
                <div class="text-h5 font-weight-bold">{{ o.title }}</div>
              </q-card-section>

              <q-card-section>
                <div class="text-h7 ellipsis-2-lines">{{ o.description }}</div>
              </q-card-section>

            </q-card>
          </div>
        </q-card>
  </div>
  </q-page>
</template>
<script>
// eslint-disable-next-line no-unused-vars
const user =
  {
    username: 'username',
    email: 'email@email.com',
    fullname: 'Abcdef ghijklmn',
    photolink: 'icon.png',
    organisation: 'Federation of Sleuths',
    about: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'
  }
// eslint-disable-next-line no-unused-vars
const opportunities = [
  {
    id: 123,
    date: '2020/12/25',
    title: 'My opportunity 1',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
  },
  {
    id: 234,
    date: '2020/11/30',
    title: 'Opportunity 2',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
  },
  {
    id: 345,
    date: '2020/12/04',
    title: 'Opportunity 23',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
  },
  {
    id: 456,
    date: '2021/01/14',
    title: 'Opportunity 4',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
  }
]

export default {
  name: 'Account',
  data () {
    return {
      user: user,
      opportunities: opportunities
    }
  }
}
</script>

<style>
/* Add a black background color to the top navigation */
.topnav {
  background-color: #333;
  overflow: hidden;
}

/* Style the links inside the navigation bar */
.topnav a {
  float: left;
  color: #f2f2f2;
  text-align: right;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

/* Change the color of links on hover */
.topnav a:hover {
  background-color: #ddd;
  color: black;
}

/* Add a color to the active/current link */
.topnav a.title {
  color: white;
}
.topnav-right {
  float: right;
}
.banner{
  background-color: #26A69A;
  height: 150px;
  text-align: right;
  vertical-align: text-bottom;
}
.text-h3{
  color: #f2f2f2;
  opacity: 0.9;
}
.text-h6{
  color: #f2f2f2;
  opacity: 0.9;
}
.profile_info img{
  width:300px;
  height:300px;
}
.my-card{
  justify-self: left;
}
.opportunity-card{
  justify-self: right;
}
</style>
