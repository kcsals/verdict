import Card from "../components/Card";

function LandingPage() {
    // Example data with added "column" property
    const mockData = [
        { column: "left", title: "Article 1", content: "Content for article 1", imageUrl: "path_to_image_1" },
        { column: "center", title: "Article 2", content: "Content for article 2", imageUrl: "path_to_image_2" },
        { column: "right", title: "Article 3", content: "Content for article 3", imageUrl: "path_to_image_3" },
        { column: "right", title: "Article 4", content: "Content for article 4", imageUrl: "path_to_image_4" },
        // ... add more mock articles
    ];

    // Function to filter and render cards based on the column
    const renderCardsForColumn = (columnName) => {
        return mockData
            .filter(article => article.column === columnName)
            .map(article => <Card key={article.title} {...article} />);
    };

    return (
        <div className="grid grid-cols-12 gap-4">
            {/* Left Column */}
            <div className="col-span-3">
                {renderCardsForColumn('left')}
            </div>
            {/* Center Column */}
            <div className="col-span-6">
                {renderCardsForColumn('center')}
            </div>
            {/* Right Column */}
            <div className="col-span-3">
                {renderCardsForColumn('right')}
            </div>
        </div>
    );
}

export default LandingPage;
