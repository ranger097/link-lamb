<script>
    /** @type {any[]} */
     let items = [];
     let status = 'Loading ....';
    async function fetchFeed() {
        try {
            const res = await fetch('http://127.0.0.1:5000/feed');
            const data = await res.json();
           
            if (data.items && data.items.length > 0) {
                items = data.items;
                status = 'Loaded ${item.length} items.';
            } else {
                status = 'Nothing New : ( ';
            }
          
        } catch (err) {
            console.error(err);
            status = 'Couldnt fetch feed';
        }
    }

    fetchFeed()
</script>

<div class="whole-page">
<main class="main-page">
    {#each items as item}
    <section class="main-page-section">
        {#if item.image}
        <img src="" alt="">
        {/if}
        <p class="main-page-section-title">{item.title}</p>
        <p class="main-page-section-content">{@html item.content_text || item.content_html}</p>
    </section>
    {/each}
</main>
</div>