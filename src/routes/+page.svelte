<script lang="ts">
	export let data;
	console.log(data);
	// import '../app.postcss';
	// import './prism.css';
	// import Header from './header.svelte';
</script>

<section>
	<div>
		<h1>Today I Learned</h1>
		<div>
			{#each data.posts as post}
				<div>
					<div>
						<a href={post.slug}>
							{post.title}
						</a>
						<span>Date: {post.date}</span>
					</div>
				</div>
			{/each}
		</div>
	</div>
</section>
