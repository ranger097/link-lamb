<script>
  import { onMount } from 'svelte';
  import { supabase } from '$lib/supabaseClient';

  let images = [];
  let current = 0;

  onMount(async () => {
    const { data } = await supabase.from('images').select('*');
    images = data ?? [];
    const interval = setInterval(() => {
    if (images.length) {
    current = ( current + 1) % images.length;
    }
    }, 10000);

    return () => clearInterval(interval);
  });
</script>

<main>
{#each images as image,i}
<div class="image_container"
style:display={i === current ? 'block' : 'none'}
>
<img class="image" src="{image.image_url}" alt="{image.description}"/>
<div class="description_container">
<span class="title">{image.title}</span>
<span class="description">{image.image_description}</span>
</div>
</div>
{/each}
</main>

<style>
@import url('https://fonts.googleapis.com/css2?family=Sofia+Sans:ital,wght@0,1..1000;1,1..1000&display=swap');

* {
font-family: "Sofia Sans", sans-serif;
  font-optical-sizing: auto;
  font-weight: 400; 
  transition: transform 0.3s ease-in-out, opacity 0.3s ease-in-out;

}


main {
display: flex;
flex-direction: row;
gap: 0px;
margin: 0px;
padding: 0px;
}

.image {
width: 100vw;
aspect-ratio: 2/1;
object-fit: cover;
}

.image_container {
max-width: 100vw;
display: flex;
flex-direction: column;
position: relative;
}

.description_container {
display: flex;
flex-direction: column;
padding: 6vh 5vh;
margin:0px;
position: absolute;
bottom: 0vh;
left: 0vh;
width: 100vw;
background: linear-gradient(transparent, black, black);
}

.title, .description {
text-shadow: -3px 3px 4px rgba(0,0,0,0.2);
color: white;
}

.title {
font-size: clamp(2rem, 5vw, 3rem);
font-weight: 400;
}

.description {
font-size: clamp(1rem, 2vw, 2rem);
font-weight: 200;
}

</style>
