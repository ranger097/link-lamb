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
        <!--{#if item.image}
        <img src="" alt="">
        {/if}-->
        <p class="main-page-section-title">{item.title}</p>
        <p class="main-page-section-content">{@html item.content_text// || item.content_html}</p>
         }</p> 
             <div class="reaction-container">
    <section class="reaction-section">
        <div class="upvote">
           <svg class="w-6 h-6 text-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
  <path fill-rule="evenodd" d="M5.575 13.729C4.501 15.033 5.43 17 7.12 17h9.762c1.69 0 2.618-1.967 1.544-3.271l-4.881-5.927a2 2 0 0 0-3.088 0l-4.88 5.927Z" clip-rule="evenodd"/>
</svg>
        <span>push</span>
        </div>
        <div class="downvote">
            <svg class="w-6 h-6 text-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
  <path fill-rule="evenodd" d="M18.425 10.271C19.499 8.967 18.57 7 16.88 7H7.12c-1.69 0-2.618 1.967-1.544 3.271l4.881 5.927a2 2 0 0 0 3.088 0l4.88-5.927Z" clip-rule="evenodd"/>
</svg>
        <span>puts</span>
        </div>
        <div class="share">
            <svg class="w-6 h-6 text-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
  <path d="M5.027 10.9a8.729 8.729 0 0 1 6.422-3.62v-1.2A2.061 2.061 0 0 1 12.61 4.2a1.986 1.986 0 0 1 2.104.23l5.491 4.308a2.11 2.11 0 0 1 .588 2.566 2.109 2.109 0 0 1-.588.734l-5.489 4.308a1.983 1.983 0 0 1-2.104.228 2.065 2.065 0 0 1-1.16-1.876v-.942c-5.33 1.284-6.212 5.251-6.25 5.441a1 1 0 0 1-.923.806h-.06a1.003 1.003 0 0 1-.955-.7A10.221 10.221 0 0 1 5.027 10.9Z"/>
</svg>
        <span>share</span>
        </div>
        <div class="comment">
            <svg class="w-6 h-6 text-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 17h6l3 3v-3h2V9h-2M4 4h11v8H9l-3 3v-3H4V4Z"/>
</svg>
    <span>comments</span>
        </div>
    </section>
    </div>
    </section>
   
    {/each}
</main>
</div>

