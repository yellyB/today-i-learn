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
	href: string;
};
