import { error } from '@sveltejs/kit';
import type { Component } from 'svelte';
import { parseContentPath } from '$lib/content.js';

const loaders = import.meta.glob<Component>(['/content/*.md', '/content/*/*.md'], { import: 'default' });

export async function load({ params, data }) {
	const path = Object.keys(loaders).find((key) => {
		const parsed = parseContentPath(key);
		return parsed?.category === (params.category ?? null) && parsed.slug === params.slug;
	});
	if (!path) throw error(404, `Could not find ${params.category ?? ''}/${params.slug}`);

	return { ...data, content: await loaders[path]() };
}
