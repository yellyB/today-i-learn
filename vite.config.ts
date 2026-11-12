import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';
import { contentDates } from './vite-plugin-content-dates.js';

export default defineConfig({
	plugins: [contentDates(), sveltekit()],
	server: {
		fs: {
			allow: ['content']
		}
	}
});
