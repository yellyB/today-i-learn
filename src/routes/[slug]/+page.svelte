<script lang="ts">
	export let data;
	console.log(data);
</script>

<svelte:head>
	<title>{data.meta.title}</title>
	<meta property="og:type" content="article" />
	<meta property="og:title" content={data.meta.title} />
</svelte:head>

<article>
	<div>
		<h1>{data.meta.title}</h1>
		<p>Published at {data.meta.date}</p>
	</div>

	<div>
		<svelte:component this={data.content} />
	</div>
</article>
