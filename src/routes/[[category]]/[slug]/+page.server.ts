import { error } from '@sveltejs/kit';
import { findPost } from '$lib/server/posts.js';

export function load({ params }) {
	const post = findPost(params.category, params.slug);
	if (!post) throw error(404, `Could not find ${params.category ?? ''}/${params.slug}`);

	return { meta: post };
}
