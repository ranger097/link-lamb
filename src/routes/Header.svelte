<script>

</script>

<header>
<nav>
<div class="container">
<span>link-lamb</span>

<div class="nav_container">
  <div class="option_container">
  <span class="option_span">Home</span>
  <div class="dropdown_container">
  <a href="#">Featured</a>
  <a href="#">About</a>
  <a href="#">Socials</a>
  </div>
  </div>

   <div class="option_container">
  <span class="option_span">Trending</span>
  <div class="dropdown_container">
  <a href="#">New</a>
  <a href="#">Views</a>
  <a href="#">Favorites</a>
  </div>
  </div>

   <div class="option_container">
  <span class="option_span">Collabs</span>
  <div class="dropdown_container">
  <a href="#">Free</a>
  <a href="#">Paid</a>
  <a href="#">Urgent</a>
  </div>
  </div>
</div>
</div>
<div class="login-div">
<a class="login_link" href="#">Login</a>
</div>
</nav>


</header>


<style>
@import url('https://fonts.googleapis.com/css2?family=Sofia+Sans:ital,wght@0,1..1000;1,1..1000&display=swap');

* {
font-family: "Sofia Sans", sans-serif;
  font-optical-sizing: auto;
  font-weight: 300;
  font-style: normal;
  transition: transform 0.3s ease-in-out, opacity 0.3s ease-in-out;

}

header {
position: sticky;
top: 0px;
left: 0px;
z-index: 100000000;
padding: 10px 20px;
background: linear-gradient(45deg, white, rgba(255,255,255,0.5) 80%, white);
backdrop-filter: blur(50px);
width: 100vw;
}

.container {
display: flex;
gap: 20px;
}

.login-div {
padding-right: 40px;
}

nav {
display: flex;
align-items: flex-start;
justify-content: space-between;
gap: 20px;
}

.nav_container {
display: flex;
align-items: flex-start;
justify-content: center;
flex-direction: row;
background-color: rgba(0,0,0,0);
gap: 0px;
}

.option_container {
display: flex;
flex-direction: column;
align-items: flex-start;
justify-content: flex-start;
background-color: rgba(0,0,0,0);
padding-right: 20px;
}

.option_container:hover .dropdown_container {
display: flex;
}

.dropdown_container {
display: flex;
flex-wrap: wrap;
max-width: 10px;
display:none;
background-color: rgba(0,0,0,0);
}

a {
color: black;
text-decoration: none;
}

a:hover {
text-decoration: underline;
}

.login_link {
font-style: italic;
}
</style>
