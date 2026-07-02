<script>
  import { onMount } from 'svelte';
  import { supabase } from '$lib/supabaseClient';

  let repos = [];

  onMount(async () => {
    const { data } = await supabase.from('repos').select();
    repos = data ?? [];
  });
</script>

<main>
  {#each repos as repo}
    <div>
      <img src={repo.image_url} alt={repo.description} />
    </div>
  {/each}
</main>
