# create-svelte

Everything you need to build a Svelte project, powered by [`create-svelte`](https://github.com/sveltejs/kit/tree/master/packages/create-svelte).

## Creating a project

If you're seeing this, you've probably already done this step. Congrats!

```bash
# create a new project in the current directory
npm create svelte
npm i
```

## Developing

Once you've created a project and installed dependencies with `npm i`, start a development server:

```bash
npm run dev
```

## Config to semicolon don't show

.prettierrc

```json
"semi": false,
```

## Config to build & publish

```bash
npm i -D @sveltejs/adapter-static
touch static/.nojekyll
echo "export const prerender = true;" >> ./src/routes/+layout.js
```

svelte.config.js

```js
import adapter from '@sveltejs/adapter-static';
const dev = process.argv.includes('dev')
export default {
 kit: {
  adapter: adapter({ pages: 'docs' }),
  paths: { base: dev ? '' : process.env.BASE_PATH }
 }
}
```

## Building

To create a production version of your app:

```bash
npm run build
```
