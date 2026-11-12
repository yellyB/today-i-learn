import { error } from '@sveltejs/kit';
import { findPost } from '$lib/posts.js';

export async function load({ params }) {
	const found = findPost(params.category, params.slug);
	if (!found) throw error(404, `Could not find ${params.category ?? ''}/${params.slug}`);

	return {
		content: found.component,
		meta: found.post
	};
}
