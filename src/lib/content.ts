export const categories = ['til', 'algorithms'] as const;
export type Category = (typeof categories)[number];

export const categoryLabels: Record<Category, string> = {
	til: 'TIL',
	algorithms: '알고리즘'
};

export type Post = {
	title: string;
	date: string;
	category: Category | null;
	slug: string;
};

export function postHref(post: Pick<Post, 'category' | 'slug'>) {
	return post.category ? `/${post.category}/${post.slug}` : `/${post.slug}`;
}

function isCategory(value: string): value is Category {
	return (categories as readonly string[]).includes(value);
}

function toSlug(name: string) {
	return name
		.toLowerCase()
		.replace(/[^\p{L}\p{N}]+/gu, '-')
		.replace(/^-+|-+$/g, '');
}

function splitContentPath(path: string): { category: Category | null; filename: string } | null {
	const parts = path.split('/').slice(2);
	if (parts.length === 1) return { category: null, filename: parts[0] };
	if (parts.length === 2 && isCategory(parts[0])) return { category: parts[0], filename: parts[1] };
	return null;
}

export function parseContentPath(path: string) {
	const split = splitContentPath(path);
	if (!split || !split.filename.endsWith('.md')) return null;

	const name = split.filename.replace(/\.md$/, '');
	return { category: split.category, name, slug: toSlug(name) };
}
