code = ''''use client';

import React, { useEffect, useRef, useState } from 'react';

export default function HeroSnakeBackground() {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const [isVisible, setIsVisible] = useState(false);
  const [score, setScore] = useState(0);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    // Configuration
    const CELL_SIZE = 18;
    const TICK_RATE = 140; // ms

    // Colors
    const COLOR_BG = '#0a0e1a';
    const COLOR_GRID = 'rgba(120,170,255,0.06)';
    const COLOR_BODY = '#4d8bff';
    const COLOR_HEAD = '#bfe0ff';
    const COLOR_FOOD = '#ff5d73';

    // State
    let cols = 0;
    let rows = 0;
    let snake: {x: number, y: number}[] = [];
    let food = {x: 0, y: 0};
    let dx = 1;
    let dy = 0;
    let nextDx = 1;
    let nextDy = 0;
    let lastTick = 0;
    let animationFrameId: number;
    let isReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    let playing = false;

    const resetSnake = () => {
      const startX = Math.floor(cols / 2);
      const startY = Math.floor(rows / 2);
      snake = [
        { x: startX, y: startY },
        { x: startX - 1, y: startY },
        { x: startX - 2, y: startY }
      ];
      dx = 1;
      dy = 0;
      nextDx = 1;
      nextDy = 0;
      setScore(0);
      spawnFood();
    };

    const spawnFood = () => {
      let valid = false;
      while (!valid) {
        food = {
          x: Math.floor(Math.random() * cols),
          y: Math.floor(Math.random() * rows)
        };
        valid = !snake.some(segment => segment.x === food.x && segment.y === food.y);
      }
    };

    const resize = () => {
      const parent = canvas.parentElement;
      if (!parent) return;
      const rect = parent.getBoundingClientRect();
      const dpr = window.devicePixelRatio || 1;
      canvas.width = rect.width * dpr;
      canvas.height = rect.height * dpr;
      ctx.scale(dpr, dpr);
      cols = Math.ceil(rect.width / CELL_SIZE);
      rows = Math.ceil(rect.height / CELL_SIZE);
      if (snake.length === 0 && cols > 0 && rows > 0) {
        resetSnake();
      }
    };

    const handleKeyDown = (e: KeyboardEvent) => {
      if (['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].includes(e.key)) {
        e.preventDefault();
        if (!playing) {
          playing = true;
          setIsVisible(true);
        }
        switch (e.key) {
          case 'ArrowUp':
            if (dy !== 1) { nextDx = 0; nextDy = -1; }
            break;
          case 'ArrowDown':
            if (dy !== -1) { nextDx = 0; nextDy = 1; }
            break;
          case 'ArrowLeft':
            if (dx !== 1) { nextDx = -1; nextDy = 0; }
            break;
          case 'ArrowRight':
            if (dx !== -1) { nextDx = 1; nextDy = 0; }
            break;
        }
      }
    };

    const update = () => {
      if (!playing) return;

      dx = nextDx;
      dy = nextDy;
      let newX = snake[0].x + dx;
      let newY = snake[0].y + dy;

      // Wrap around edges
      if (newX < 0) newX = cols - 1;
      else if (newX >= cols) newX = 0;
      if (newY < 0) newY = rows - 1;
      else if (newY >= rows) newY = 0;

      // Self collision -> Reset Game
      if (snake.some(segment => segment.x === newX && segment.y === newY)) {
        resetSnake();
        return;
      }

      const newHead = { x: newX, y: newY };
      snake.unshift(newHead);

      // Eat food
      if (newX === food.x && newY === food.y) {
        setScore(s => s + 1);
        spawnFood();
      } else {
        snake.pop();
      }
    };

    const draw = () => {
      if (!playing) return;
      
      const parent = canvas.parentElement;
      if (!parent) return;
      const rect = parent.getBoundingClientRect();

      ctx.fillStyle = COLOR_BG;
      ctx.fillRect(0, 0, rect.width, rect.height);

      ctx.strokeStyle = COLOR_GRID;
      ctx.lineWidth = 1;
      ctx.beginPath();
      for (let x = 0; x <= rect.width; x += CELL_SIZE) {
        ctx.moveTo(x, 0);
        ctx.lineTo(x, rect.height);
      }
      for (let y = 0; y <= rect.height; y += CELL_SIZE) {
        ctx.moveTo(0, y);
        ctx.lineTo(rect.width, y);
      }
      ctx.stroke();

      ctx.fillStyle = COLOR_FOOD;
      ctx.fillRect(food.x * CELL_SIZE, food.y * CELL_SIZE, CELL_SIZE, CELL_SIZE);

      snake.forEach((segment, index) => {
        ctx.fillStyle = index === 0 ? COLOR_HEAD : COLOR_BODY;
        ctx.fillRect(segment.x * CELL_SIZE, segment.y * CELL_SIZE, CELL_SIZE, CELL_SIZE);
      });
    };

    const loop = (timestamp: number) => {
      if (!lastTick) lastTick = timestamp;
      const elapsed = timestamp - lastTick;

      const parent = canvas.parentElement;
      if (parent && (canvas.width / (window.devicePixelRatio || 1) !== parent.clientWidth || canvas.height / (window.devicePixelRatio || 1) !== parent.clientHeight)) {
        resize();
      }

      if (elapsed > TICK_RATE) {
        lastTick = timestamp;
        if (!isReducedMotion) {
          update();
        }
      }

      draw();

      if (!isReducedMotion) {
        animationFrameId = requestAnimationFrame(loop);
      }
    };

    window.addEventListener('resize', resize);
    window.addEventListener('keydown', handleKeyDown);
    
    resize();
    
    if (isReducedMotion) {
      draw();
    } else {
      animationFrameId = requestAnimationFrame(loop);
    }

    return () => {
      window.removeEventListener('resize', resize);
      window.removeEventListener('keydown', handleKeyDown);
      cancelAnimationFrame(animationFrameId);
    };
  }, []);

  return (
    <div style={{ position: 'absolute', inset: 0, zIndex: 0, pointerEvents: 'none', opacity: isVisible ? 1 : 0, transition: 'opacity 0.8s ease-in-out' }}>
      <canvas
        ref={canvasRef}
        aria-hidden="true"
        style={{
          position: 'absolute',
          inset: 0,
          width: '100%',
          height: '100%',
          opacity: 0.06,
          imageRendering: 'pixelated',
        }}
      />
      <div className="absolute bottom-8 right-12 font-mono text-3xl font-bold tracking-widest transition-opacity duration-1000" style={{ color: 'rgba(255, 255, 255, 0.25)' }}>
        SCORE {score.toString().padStart(3, '0')}
      </div>
    </div>
  );
}
'''

with open('src/components/hero/HeroSnakeBackground.tsx', 'w') as f:
    f.write(code)

print("Snake rewritten with score, hidden by default, self-collision reset")
