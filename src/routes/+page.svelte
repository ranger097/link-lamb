<script>

  import Header from './Header.svelte';
  import { onMount } from 'svelte';
  import { supabase } from '$lib/supabaseClient';

  let repos = [];

  onMount(async () => {
    const { data } = await supabase.from('repos').select();
    repos = data ?? [];
  });
</script>

<main>
 <Header/> 
  {#each repos as repo}
    <div>
      <img src={repo.image_url} alt={repo.description} />
      <h1>{repo.project_name}</h1>
      <span>{repo.description}</span>
    </div>
  {/each}
</main>
