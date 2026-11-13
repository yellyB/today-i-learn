import { getPosts } from '$lib/server/posts.js';

export function load() {
	return { posts: getPosts() };
}
