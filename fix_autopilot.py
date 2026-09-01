import re

with open('src/components/hero/HeroSnakeBackground.tsx', 'r') as f:
    code = f.read()

old_autopilot = '''    const doAutopilot = () => {
      const head = snake[0];
      const diffX = food.x - head.x;
      const diffY = food.y - head.y;

      // Wrap-around logic for autopilot - find shortest path including wraps
      // Note: Full pathfinding is complex, so we'll do simple greedy towards food
      // considering wrap-around distance.
      
      let targetDx = 0;
      let targetDy = 0;

      const distXP = diffX > 0 ? diffX : diffX + cols;
      const distXN = diffX < 0 ? -diffX : cols - diffX;
      
      const distYP = diffY > 0 ? diffY : diffY + rows;
      const distYN = diffY < 0 ? -diffY : rows - diffY;

      const goRight = distXP <= distXN;
      const goDown = distYP <= distYN;
      
      const absX = Math.min(distXP, distXN);
      const absY = Math.min(distYP, distYN);

      // Prefer moving in the direction of greatest distance
      let pref1: [number, number] = [0, 0];
      let pref2: [number, number] = [0, 0];

      if (absX > absY) {
        pref1 = [goRight ? 1 : -1, 0];
        pref2 = [0, goDown ? 1 : -1];
      } else {
        pref1 = [0, goDown ? 1 : -1];
        pref2 = [goRight ? 1 : -1, 0];
      }

      // Ensure we don't reverse
      if (pref1[0] !== -dx || pref1[1] !== -dy) {
        nextDx = pref1[0];
        nextDy = pref1[1];
      } else if (pref2[0] !== -dx || pref2[1] !== -dy) {
        nextDx = pref2[0];
        nextDy = pref2[1];
      } else {
        // Fallback if both preferences lead to reverse (rare, but possible if snake is exactly aligned)
        // Just pick a safe orthogonal direction
        if (dx !== 0) {
          nextDx = 0;
          nextDy = 1;
        } else {
          nextDx = 1;
          nextDy = 0;
        }
      }
    };'''

new_autopilot = '''    const doAutopilot = () => {
      const head = snake[0];
      const diffX = food.x - head.x;
      const diffY = food.y - head.y;
      
      const distXP = diffX > 0 ? diffX : diffX + cols;
      const distXN = diffX < 0 ? -diffX : cols - diffX;
      const distYP = diffY > 0 ? diffY : diffY + rows;
      const distYN = diffY < 0 ? -diffY : rows - diffY;

      const goRight = distXP <= distXN;
      const goDown = distYP <= distYN;
      
      const absX = Math.min(distXP, distXN);
      const absY = Math.min(distYP, distYN);

      let pref1: [number, number] = absX > absY ? [goRight ? 1 : -1, 0] : [0, goDown ? 1 : -1];
      let pref2: [number, number] = absX > absY ? [0, goDown ? 1 : -1] : [goRight ? 1 : -1, 0];
      let pref3: [number, number] = [-pref2[0], -pref2[1]];
      let pref4: [number, number] = [-pref1[0], -pref1[1]];

      const prefs = [pref1, pref2, pref3, pref4];
      
      for (const p of prefs) {
        // Don't reverse
        if (p[0] === -dx && p[1] === -dy && snake.length > 1) continue;
        
        // Predict next position
        let nx = head.x + p[0];
        let ny = head.y + p[1];
        if (nx < 0) nx = cols - 1; else if (nx >= cols) nx = 0;
        if (ny < 0) ny = rows - 1; else if (ny >= rows) ny = 0;
        
        // Check for self-collision (exclude the tail since it will move)
        let collision = false;
        for (let i = 0; i < snake.length - 1; i++) {
           if (snake[i].x === nx && snake[i].y === ny) {
               collision = true;
               break;
           }
        }
        
        if (!collision) {
           nextDx = p[0];
           nextDy = p[1];
           return;
        }
      }
    };'''

code = code.replace(old_autopilot, new_autopilot)

with open('src/components/hero/HeroSnakeBackground.tsx', 'w') as f:
    f.write(code)

print("Fixed autopilot")
