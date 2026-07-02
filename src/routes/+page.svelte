<script>
  let { data } = $props();
</script>

<main>
  {#each data.repos as repo}
  <div>
  <img src={repo.image_url} alt={repo.description}/>
  </div>
  {/each}
</main>
