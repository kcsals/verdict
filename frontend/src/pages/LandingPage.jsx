import Card from "../components/Card";
import LinksCard from "../components/LinksCard";
import { fetchTrending } from '../api/games'; 
import { useState, useEffect } from "react";

function LandingPage() {

    const [trending, setTrending] = useState([]);

    useEffect(() => {
        async function fetchData() {
            const data = await fetchTrending();
            setTrending(data);
        }

        fetchData();
    }, []);

    // Function to filter and render cards based on the column
    const renderCardsForColumn = (columnName) => {
        return mockData
            .filter(article => article.column === columnName)
            .map(article => <Card key={article.title} {...article} />);
    };

    return (
        <div className="container mx-auto grid grid-cols-12 gap-4">
            {/* Left Column */}
            <div className="col-span-2">
              <LinksCard 
                spotLight="Trending Games"
                titles={trending.map(game => game.game_title)}
              />
              <LinksCard 
                spotLight="Rankings"
              />
              <LinksCard 
                spotLight="Best Hardware"
              />
            </div>
            {/* Center Column */}
            <div className="col-span-7">
              <Card />
            </div>
            {/* Right Column */}
            <div className="col-span-3">
              <Card />
            </div>
        </div>
    );
}

export default LandingPage;
