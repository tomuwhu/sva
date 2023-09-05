<script>
	var n = 2
	$: x = Array(31)
		.fill(0)
		.map((v, i) => [i - 15, (i - 15) ** n, Math.abs(i - 15) ** n, -(Math.abs(i - 15) ** n)])
</script>

<div>
	<input type="range" bind:value={n} min="0" max="4" step="0.1" />
	<h3>y = x<sup>{n}</sup></h3>
	<table>
		<tr>
			{#each x as o}
				<td>{o[0]}</td>
			{/each}
		</tr>
		<tr>
			{#each x as o}
				<th>{@html !isNaN(o[1]) ? o[1].toFixed(2) : `<i>${o[3].toFixed(2)}</i>`}</th>
			{/each}
		</tr>
	</table>
</div>
<svg viewBox="0 0 1000 1000" height="500px">
	{#each x as o}
		{#if !isNaN(o[1])}
			<circle cx={o[0] * 70 + 500} cy={500 - (30 * o[1]) / 15 ** (n - 1)} r="20" />
		{:else}
			<circle class="c" cx={o[0] * 70 + 500} cy={500 - (30 * o[3]) / 15 ** (n - 1)} r="20" />
		{/if}
	{/each}
</svg>

<style>
	input {
		width: 600px;
	}
	sup {
		font-size: 12px;
	}
	table,
	svg {
		width: 1120px;
		margin: auto;
		border: solid 1px rgb(80, 41, 41);
		background-color: rgb(231, 235, 213);
	}
	svg {
		display: block;
	}
	td,
	th {
		font-size: 10px;
		border: solid 1px black;
		color: rgb(91, 23, 23);
		width: 30px;
	}
	circle {
		filter: drop-shadow(1px 1px 3px black);
		fill: rgb(54, 120, 181);
	}
	circle.c {
		fill: rgb(230, 186, 177);
	}
	:global(i) {
		color: red;
	}
</style>
