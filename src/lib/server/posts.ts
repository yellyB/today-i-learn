import gitDates from 'virtual:content-dates';
import { parseContentPath, type Post } from '$lib/content.js';

type Metadata = { title?: string; date?: string };

const modulesByPath = import.meta.glob<{ metadata?: Metadata }>(['/content/*.md', '/content/*/*.md'], {
	eager: true
});

const today = new Date().toISOString().slice(0, 10);

const posts: Post[] = Object.entries(modulesByPath)
	.flatMap(([path, { metadata }]) => {
		const parsed = parseContentPath(path);
		if (!parsed) return [];

		return [
			{
				title: metadata?.title ?? parsed.name,
				date: metadata?.date ?? gitDates[path] ?? today,
				category: parsed.category,
				slug: parsed.slug
			}
		];
	})
	.sort((a, b) => b.date.localeCompare(a.date));

export function getPosts() {
	return posts;
}

export function findPost(category: string | undefined, slug: string) {
	return posts.find((post) => post.category === (category ?? null) && post.slug === slug);
}
