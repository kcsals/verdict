// GamePage.jsx

import React, { useState, useEffect } from 'react';
import Card from '../components/Card';
import { fetchGames } from '../api/games'; 

function GamePage() {
    const [games, setGames] = useState([]);

    useEffect(() => {
        async function fetchData() {
            const data = await fetchGames();
            setGames(data);
        }

        fetchData();
    }, []);

    return (
        <div className="container mx-auto">
          <h1 className="text-2xl font-bold mb-4">Games</h1>
          <div className="game-list">
            {games.map(game => (
              <Card 
                key={game.id}
                title={game.title}
                imageUrl={game.cover_image}
                slug={game.slug}
                genres={game.genres}
              />
            ))}
          </div>
        </div>
    );
}

export default GamePage;
