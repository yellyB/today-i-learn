import type { Post } from './api/posts/type.js';

export async function load({ fetch }: any) {
	const response = await fetch('api/posts');
	const posts: Post[] = await response.json();
    
	return { posts };
}
