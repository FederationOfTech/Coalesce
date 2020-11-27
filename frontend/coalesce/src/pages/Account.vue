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
      <div class="text-h6">Your email: {{user.organisation}}</div>
</div>

<div class="q-pa-md row items-start q-gutter-md">
        <q-card class="my-card">
          <q-card-section horizontal class="profile_info">
            <img class= "col-5" src="~assets/icon.png">
          </q-card-section>
          <q-separator/>
           <q-card-section>
              About
             <div class="text-h3">{{user.about}}</div>
          </q-card-section>
    </q-card>
     </div>
  </q-page>
</template>

 <!--
    <q-page-container>
    <div class="text-h3">Welcome {{ user.username }}!</div>
      <div>
        <img src="frontend/coalesce/src/assets/icon.png">
      </div>
      <div class="text-h6">
        Your email: {{user.email}}
      </div>
       <div class="text-h6">
        Full name: {{user.fullname}}

    </q-page-container>-->
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

export default {
  name: 'Account',
  data () {
    return {
      user: user
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

}
</style>
