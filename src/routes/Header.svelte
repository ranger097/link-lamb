<script>

</script>

<header>
<nav>
<div class="container">
<div class="logo_container">
    <svg height="20" width="30" viewBox="0 0 56 40" xmlns="http://www.w3.org/2000/svg" data-logo="logo">
        <g transform="translate(0, 0)&#xA;    rotate(0 27.5 20)" id="logogram"><path d="M23.6322 0.597911C19.9395 1.76672 16.9327 5.48248 10.9192 12.914C3.501 22.0814 -0.208097 26.665 0.00900851 30.5474C0.155095 33.1598 1.30933 35.6108 3.22485 37.3763C6.07159 40 11.9392 40 23.6745 40H24.3275C27.1975 40 29.9133 38.6992 31.7186 36.4682C37.6627 29.1224 40.6348 25.4496 44.4744 24.8957C45.4078 24.7611 46.3555 24.7611 47.2889 24.8957C49.8634 25.2671 52.048 27.0408 55 30.3839C50.2776 21.5248 41.6084 3.83856 31.37 0.597911C28.8514 -0.199304 26.1508 -0.199304 23.6322 0.597911Z" fill="#000000"/></g>
        <g transform="" id="logotype"/>
        
      </svg>
      <a href="#" class="logo_span">link-lamb</a>
</div>
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
position: fixed;
top: 0px;
left: 0px;
z-index: 100000000;
padding: 0px 0px;
background: linear-gradient(45deg, white 0%, rgba(255,255,255,0.5) 70%, white);
backdrop-filter: blur(50px);
width: 100vw;
}

.container {
display: flex;
gap: 0px;
}

.login-div {
padding: 10px 20px;
display: flex;
align-items: center;
justify-content: center;
background-color: rgba(0,0,0,0);
}

.logo_container {
display: flex;
flex-direction: row;
align-items: flex-start;
justify-content: center;
gap: 5px;
padding: 10px 10px 10px 20px;
}

nav {
display: flex;
align-items: flex-start;
justify-content: space-between;
gap: 0px;
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
background-color: transparent;
padding: 10px;
margin: 0px;
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

.logo_span {
font-weight: 500;
}

</style>
