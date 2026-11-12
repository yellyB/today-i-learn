import type { Component } from 'svelte';
import gitDates from 'virtual:content-dates';

import { categories, type Category, type Post } from './categories.js';

export { categories, categoryLabels, type Category, type Post } from './categories.js';

type PostModule = {
	default: Component;
	metadata?: { title?: string; date?: string };
};

const modules = import.meta.glob<PostModule>(['/content/*.md', '/content/*/*.md'], {
	eager: true
});

function toSlug(filename: string) {
	return filename
		.replace(/\.md$/, '')
		.toLowerCase()
		.replace(/[^\p{L}\p{N}]+/gu, '-')
		.replace(/^-+|-+$/g, '');
}

function isCategory(value: string): value is Category {
	return (categories as readonly string[]).includes(value);
}

function splitContentPath(path: string): { category: Category | null; filename: string } | null {
	const parts = path.split('/').slice(2);
	if (parts.length === 1) return { category: null, filename: parts[0] };
	if (parts.length === 2 && isCategory(parts[0])) return { category: parts[0], filename: parts[1] };
	return null;
}

const today = new Date().toISOString().slice(0, 10);

const entries = Object.entries(modules).flatMap(([path, mod]) => {
	const split = splitContentPath(path);
	if (!split) return [];

	const { category, filename } = split;

	const slug = toSlug(filename);
	const post: Post = {
		title: mod.metadata?.title ?? filename.replace(/\.md$/, ''),
		date: mod.metadata?.date ?? gitDates[path] ?? today,
		category,
		slug,
		href: category ? `/${category}/${slug}` : `/${slug}`
	};
	return [{ post, component: mod.default }];
});

entries.sort((a, b) => b.post.date.localeCompare(a.post.date));

export function getPosts(): Post[] {
	return entries.map((entry) => entry.post);
}

export function findPost(category: string | undefined, slug: string) {
	return entries.find((entry) => entry.post.category === (category ?? null) && entry.post.slug === slug);
}
