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
    <section class="spacer">
        </section>
    <section class="main-page-section">
          
        {#if item.image}
        <img src="" alt="">
        {/if}
        <p class="main-page-section-title">{item.title}</p>
        <p class="main-page-section-content">{@html item.content_text || item.content_html}</p>
             
      


    <section class="the-whole-comment-section">
<article class="the-container-to-hold-top-row">
    <section class="the-comments-section">

        <div class="reaction-glue">
             <button class="the-share-button" aria-label="share button">
                    <svg class="w-6 h-6 text-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
                            <path d="M5.027 10.9a8.729 8.729 0 0 1 6.422-3.62v-1.2A2.061 2.061 0 0 1 12.61 4.2a1.986 1.986 0 0 1 2.104.23l5.491 4.308a2.11 2.11 0 0 1 .588 2.566 2.109 2.109 0 0 1-.588.734l-5.489 4.308a1.983 1.983 0 0 1-2.104.228 2.065 2.065 0 0 1-1.16-1.876v-.942c-5.33 1.284-6.212 5.251-6.25 5.441a1 1 0 0 1-.923.806h-.06a1.003 1.003 0 0 1-.955-.7A10.221 10.221 0 0 1 5.027 10.9Z"/>
                    </svg>
            </button>

                <button class="the-share-button" aria-label="reaction button">
                   <svg class="w-6 h-6 text-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
  <path fill-rule="evenodd" d="M2 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10S2 17.523 2 12Zm5.495.93A.5.5 0 0 0 6.5 13c0 1.19.644 2.438 1.618 3.375C9.099 17.319 10.469 18 12 18c1.531 0 2.9-.681 3.882-1.625.974-.937 1.618-2.184 1.618-3.375a.5.5 0 0 0-.995-.07.764.764 0 0 1-.156.096c-.214.106-.554.208-1.006.295-.896.173-2.111.262-3.343.262-1.232 0-2.447-.09-3.343-.262-.452-.087-.792-.19-1.005-.295a.762.762 0 0 1-.157-.096ZM8.99 8a1 1 0 0 0 0 2H9a1 1 0 1 0 0-2h-.01Zm6 0a1 1 0 1 0 0 2H15a1 1 0 1 0 0-2h-.01Z" clip-rule="evenodd"/>
</svg>


                </button>

            </div>
    
        <button class="the-comments-button">
            <p>comments</p>
        </button>
        </section>
    </article>

    <section class="actual-comment-background">
    <article class="actual-comment-container">
        <p>Test Title</p>
        <p>Test Comment</p>
    </article>
   </section>


     <button class="the-share-button-open" aria-label="reaction button">
                    <svg class="w-6 h-6 text-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
                            <path fill-rule="evenodd" d="M18.425 10.271C19.499 8.967 18.57 7 16.88 7H7.12c-1.69 0-2.618 1.967-1.544 3.271l4.881 5.927a2 2 0 0 0 3.088 0l4.88-5.927Z" clip-rule="evenodd"/>
                    </svg>
                </button>
</section>












    </section>


    {/each}
</main>
</div>