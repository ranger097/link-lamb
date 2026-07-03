<script>
import { onMount } from 'svelte';
  import { supabase } from '$lib/supabaseClient';

  let repos = []; 

  onMount(async () => {
    const { data } = await supabase.from('repos').select('*');
    repos = data ?? [];
    });
</script>

<main>
<section>
{#each repos as repo}
<a class="repo_container" href="{repo.repo_url}">
<img class="image" src="{repo.image_url}" alt="{repo.description}"/>
<div class="title_container">
<span class="title">{repo.project_name}</span>
</div>
</a>
{/each}

</section>
</main>
<style>
@import url('https://fonts.googleapis.com/css2?family=Sofia+Sans:ital,wght@0,1..1000;1,1..1000&display=swap');

* {
font-family: "Sofia Sans", sans-serif;
  font-optical-sizing: auto;
  font-weight: 300;
  font-style: normal;
  transition: transform 0.3s ease-in-out, opacity 0.3s ease-in-out;

}

section {
display: flex;
flex-wrap: wrap;
width: calc(100vw - 10px);
padding:  0px 5px;
align-items: flex-start;
justify-content: center;
background-color: black;
}

main {
background-color: black;
color: white;
}


.image {
aspect-ratio:2/1 ;
object-fit: cover;
border-radius: 10px;
}

.repo_container {
display: flex;
flex-direction: column;
flex: 1;
width: 400px;
margin: 0px 5px 10px 5px;
background-color: transparent;
border-radius: 10px;
 box-shadow: -2px 2px 10px rgba(0,0,0,0.3);
 position: relative;
 text-decoration: none;
 color: black;
}

.title {
overflow: hidden;
word-break: break-word;
background-color: rgba(0,0,0,0);
display: -webkit-box;
  -webkit-line-clamp: 2; 
  -webkit-box-orient: vertical;
  padding: 20px;
  
}

.title  {
padding: 10px 20px;
font-size: 1.3rem;
font-weight: 300;
}

.title_container {
display: flex;
align-items: center;
justify-content: center;
background-color: rgba(255,255,255,0.7);
border-radius: 0px 0px 10px 10px;
position: absolute;
bottom: 0px;
left: 0px;
width: 100%;
backdrop-filter: blur(10px);
}

</style>
