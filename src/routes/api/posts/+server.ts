import { json } from '@sveltejs/kit';
import { getPosts } from '$lib/posts.js';

export async function GET() {
  return json(getPosts());
}
