<script>
  import { onMount } from "svelte";

  let posx = 0;
  let posy = 0;
  let counter = 0;
  let mapcolor = null;

  const GRID_SIZE = 5;
  let ws;

  onMount(() => {
    ws = new WebSocket("ws://10.101.0.6:8000/ws");

    ws.addEventListener("open", () => {
      console.log("Connected to WebSocket");
    });

    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);

      if (data.counter != null) counter = data.counter; // only if not null/undefined
      if (data.posx != null) posx = data.posx;
      if (data.posy != null) posy = data.posy;
      if (data.mapcolor != null) mapcolor = data.mapcolor;
    };


    const handleKey = (e) => {
      if (e.key === "ArrowUp") move("north");
      if (e.key === "ArrowDown") move("south");
      if (e.key === "ArrowLeft") move("west");
      if (e.key === "ArrowRight") move("east");
    };

    window.addEventListener("keydown", handleKey);
    return () => window.removeEventListener("keydown", handleKey);
  });

  function move(direction) {
    if (ws && ws.readyState === WebSocket.OPEN) {
      ws.send(JSON.stringify({ type: "move", direction }));
    }
  }

  function setcolor(color) {
    if (ws && ws.readyState === WebSocket.OPEN) {
      ws.send(JSON.stringify({ type: "color", color }));
    }
  }

  function xyColor(cx, cy) {
    const r = ((cx * 37 + cy * 91) % 256);
    const g = ((cx * 53 + cy * 97) % 256);
    const b = ((cx * 61 + cy * 83) % 256);
    return `rgb(${r},${g},${b})`;
  }
</script>

<style>
  .grid {
    display: grid;
    grid-template-columns: repeat(5, 50px);
    grid-template-rows: repeat(5, 50px);
    gap: 5px;
    margin-bottom: 1rem;
  }
  .cell {
    width: 50px;
    height: 50px;
    border: 1px solid #333;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background-color 0.2s;
  }
  .player {
    border: 2px solid black;
    font-weight: bold;
    color: white;
  }
</style>

<h2>Grid 5×5 — Use arrow keys or buttons</h2>

<div class="grid">
  {#each Array(GRID_SIZE) as _, rowIndex}
    {#each Array(GRID_SIZE) as _, colIndex}
      <div
        class="cell {(posx + colIndex - 2 === posx && posy + (2 - rowIndex) === posy) ? 'player' : ''}"
        style="background-color: {xyColor(posx + colIndex - 2, posy + (2 - rowIndex))}"
      >
      </div>
    {/each}
  {/each}
</div>

<div>
  <button on:click={() => move("north")}>⬆</button><br/>
  <button on:click={() => move("west")}>⬅</button>
  <button on:click={() => move("east")}>➡</button><br/>
  <button on:click={() => move("south")}>⬇</button>
  <button on:click={() => setcolor("red")}>Red</button>
</div>

<h3>Position: ({posx}, {posy})</h3>
<h1>Counter: {counter}</h1>
<h1>Color: {mapcolor}</h1>