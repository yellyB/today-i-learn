<script lang="ts">
	import 'prismjs/themes/prism.css';
	import { categories, categoryLabels, type Category, type Post } from '$lib/categories.js';

	let { data } = $props();
	const posts: Post[] = data.posts;

	let filter = $state<Category | 'all'>('all');

	const filtered = $derived(filter === 'all' ? posts : posts.filter((p) => p.category === filter));
</script>

<section>
	<h1>Today I Learned</h1>

	<nav>
		<button class:active={filter === 'all'} onclick={() => (filter = 'all')}>전체</button>
		{#each categories as category}
			<button class:active={filter === category} onclick={() => (filter = category)}>
				{categoryLabels[category]}
			</button>
		{/each}
	</nav>

	<ul>
		{#each filtered as post}
			<li>
				{#if filter === 'all' && post.category}<span class="tag">[{categoryLabels[post.category]}]</span>{/if}
				<a href={post.href}>{post.title}</a>
				<span class="date">{post.date}</span>
			</li>
		{/each}
	</ul>
</section>

<style>
	nav {
		display: flex;
		gap: 8px;
		margin: 12px 0;
	}
	button.active {
		font-weight: bold;
	}
	.tag {
		color: #888;
	}
	.date {
		color: #888;
		margin-left: 8px;
	}
</style>
