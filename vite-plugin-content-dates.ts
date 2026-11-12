import { execFileSync } from 'node:child_process';
import { readdirSync } from 'node:fs';
import { join } from 'node:path';
import type { Plugin } from 'vite';

const MODULE_ID = 'virtual:content-dates';
const RESOLVED_ID = '\0' + MODULE_ID;
const CONTENT_DIR = 'content';

function git(args: string[]) {
	try {
		return execFileSync('git', args, { encoding: 'utf8' }).trim();
	} catch {
		return '';
	}
}

function listMarkdownFiles() {
	return readdirSync(CONTENT_DIR, { withFileTypes: true }).flatMap((entry) => {
		if (entry.isFile() && entry.name.endsWith('.md')) return [`${CONTENT_DIR}/${entry.name}`];
		if (!entry.isDirectory()) return [];

		return readdirSync(join(CONTENT_DIR, entry.name))
			.filter((name) => name.endsWith('.md'))
			.map((name) => `${CONTENT_DIR}/${entry.name}/${name}`);
	});
}

function firstCommitDate(file: string) {
	const dates = git(['log', '--follow', '--format=%as', '--', file]).split('\n').filter(Boolean);
	return dates.at(-1);
}

export function contentDates(): Plugin {
	return {
		name: 'content-dates',
		resolveId(id) {
			if (id === MODULE_ID) return RESOLVED_ID;
		},
		load(id) {
			if (id !== RESOLVED_ID) return;

			if (git(['rev-parse', '--is-shallow-repository']) === 'true') {
				this.warn('Shallow git clone detected. Post dates without frontmatter may be wrong.');
			}

			const dates: Record<string, string> = {};
			for (const file of listMarkdownFiles()) {
				const date = firstCommitDate(file);
				if (date) dates[`/${file}`] = date;
			}
			return `export default ${JSON.stringify(dates)};`;
		}
	};
}
