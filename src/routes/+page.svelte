<script lang="ts">
	import 'prismjs/themes/prism.css';
	export let data;
	console.log(data);
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
