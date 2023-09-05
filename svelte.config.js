import adapter from '@sveltejs/adapter-static';
const dev = process.argv.includes('dev')
export default {
	kit: {
		adapter: adapter({ pages: 'docs' }),
		paths: { base: dev ? '' : process.env.BASE_PATH }
	}
}
